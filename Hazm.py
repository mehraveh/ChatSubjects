from __future__ import unicode_literals
from hazm import *
import filtering as fl
import openpyxl
def hazm(file_name):
    words = []
    words_count =[]
    delete_list = [':',"?" ,"؟" ,"ک","ها","از","در","mehraveh_tma","bangtansv","MAminHP","!","ب","ی","یه","FWD","Photo","]","{","[","هاش",".","اگ","اگه","اگر","۱","۲","۳","۴","۵"
                   ,"۶","۷","۸", "۹","…","نه", "ن" ,"و" ,"را"]

    book = openpyxl.load_workbook('PersianWords.xlsx')
    sheet = book.active
    words_dict = []
    for i in range(32640):
        s = "B" + (i + 5).__str__()
        words_dict.append(sheet[s].value)

    o = open(file_name.__str__()+"_tokenized.txt" ,"w")
    f = open(file_name.__str__()+"_cleaned.txt")
    normalizer = Normalizer()
    lemmatizer = Lemmatizer()
    for i in range(8032):
        print(i)
        line = f.readline()
        s = normalizer.normalize(line.__str__())
        t = word_tokenize(s.__str__())
        for word in t:
            word = fl.filtering(word,words_dict)
            word = lemmatizer.lemmatize(word.__str__())
            # print(word.__str__())
            if word not in words and not word in delete_list:
                words.append(word.__str__())
                words_count.append(1)
                #o.writelines(word.__str__()+""+"\n")
            elif  word  in words:
                words_count[words.index(word.__str__())] +=1
    print(words)
    print(words_count)
    for i in range(len(words)):
        o.writelines(words[i].__str__() + " :" +words_count[i].__str__()+ "\n")
    return words ,words_count
