
def cleaning(file_name):
    file = open(file_name.__str__()+".txt", encoding="utf8")
    file1 = open(file_name.__str__()+"_cleaned.txt" ,'w', encoding="utf8" )
    s = []
    sender_tmp = ''
    pm = []
    pmf = ''
    pmf1 = ''
    for i in range(32475):
        s.append(file.readline())
        s[i] = s[i].__str__()
        if '@' in s[i]:
            sender = s[i][s[i].find("@") + 1:s[i].find("]")]
            sender_tmp = sender
        else:
            sender = sender_tmp
        pm = s[i].split(':')
        if "[" in s[i] and "@" in s[i]:
           pmf = pm[3].__str__().split("\n")
        else:
            pmf = pm
        pmf1 = pmf[0]
        if len(pmf1) > 2:
            print(sender + " : " + pmf1)
            print(len(pmf1))
            file1.write(sender + " : " + pmf1+ '\n')



