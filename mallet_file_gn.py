from __future__ import unicode_literals
from hazm import *
import filtering as fl
import openpyxl
def mallet(file_name1, file_name2):
    words = []
    words_count =[]
    delete_list = ["ViviGirl",':',"?" ,"؟" ,"ک","ها","از","در","Mr_Mean","mehraveh_tma","MAminHP","!","ب","ی","یه","FWD","Photo","]","{","[","هاش",".","اگ","اگه","اگر","۱","۲","۳","۴","۵"
                   ,"۶","۷","۸", "۹","…","نه", "ن" ,"و" ,"را" ,"که","این","در","برای","تو","من","او" ,"به","با","تا","یک","چی", "هر" ,"چون" ,"باشه","ولی","بعد","هم","یا","کلا",
                   "ای" ,"ن" ,"چ"]

    o = open("mallet.txt" ,"w")
    f1 = open(file_name1.__str__()+"_cleaned.txt")
    f2 = open(file_name2.__str__()+"_cleaned.txt")

    normalizer = Normalizer()
    lemmatizer = Lemmatizer()

    counter = 0
    count = 0
    feature = ''
    for i in range(8032):
        line1 = f1.readline()
        line2 = f2.readline()
        s1 = normalizer.normalize(line1.__str__())
        t1 = word_tokenize(s1.__str__())
        s2 = normalizer.normalize(line2.__str__())
        t2 = word_tokenize(s2.__str__())
        for word in t1:
            word = lemmatizer.lemmatize(word.__str__())
            if word not in delete_list:
                feature += 'f'+ (count + 1).__str__()+' '+word+' '
                count += 1
            if count >= 5:
                    break

        label = 'l' + (counter % 2 + 1).__str__()
        o.writelines((counter+1).__str__() + ' ' + label.__str__()+ ' '+ feature.__str__()+'\n')
        counter += 1
        count = 0
        feature = ''

        for word in t2:
            word = lemmatizer.lemmatize(word.__str__())
            if word not in delete_list:
                feature += 'f' + (count + 1).__str__() + ' ' + word + ' '
                count += 1
            if count >= 5:
                break

        label = 'l' + (counter % 2 + 1).__str__()
        o.writelines((counter+1).__str__() + ' ' + label.__str__() + ' ' + feature.__str__()+'\n')
        counter += 1
        count = 0
        feature = ''
        print(i)


