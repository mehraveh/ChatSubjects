from __future__ import unicode_literals
from hazm import *


def test(filename1, filename2):

    f1 = open(filename1.__str__() + '_cleaned.txt' , encoding="utf8")
    f2 = open(filename2.__str__() + '_cleaned.txt' , encoding="utf8")
    o1 = open('train_t.txt' , 'w' ,  encoding="utf8")
    o2 = open('test_t.txt', 'w', encoding="utf8")
    line1 = f1.readline()
    line2 = f2.readline()
    count = 0
    normalizer = Normalizer()
    while line1 and line2 :
        line1 = normalizer.normalize(line1.__str__())
        line2 = normalizer.normalize(line2.__str__())
        if count%2 == 0 :
            s1 = line1.__str__()
            if count%9 != 0:
                o1.writelines(s1)
            else:
                o2.writelines(s1)
        else:
            s2 = line2.__str__()
            if count% 9!= 0:
                o1.writelines(s2)
            else:
                o2.writelines(s2)

        line1 = f1.readline()
        line2 = f2.readline()
        count+=1
        print(count)
