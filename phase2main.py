import Hazm as h
import naviie_bayes as nb
words1 ,words_count1 = h.hazm("barzi")
words2 ,words_count2 = h.hazm("Amin")
w = open("test_t.txt")
s = w.readline()
ftrue = 0
ffalse = 0
strue = 0
sfalse = 0
ftrues = 0
ffalses = 0
strues = 0
sfalses = 0
count = 0
while s:
    p1nsmoot , p2nsmoot = nb.naviie_bayes_nsmoot(words1, words_count1, words2, words_count2,s)
    p1smoot , p2smoot = nb.naviie_bayes_smoot(words1, words_count1, words2, words_count2,s)
    print("p1 without smooting:")
    print(p1nsmoot)
    print("p2 without smooting:")
    print(p2nsmoot)
    if p2nsmoot >= p1nsmoot and count % 2 == 1:
        strue += 1
    elif p2nsmoot > p1nsmoot and count % 2 == 0:
        ffalse +=1
    if p2nsmoot <= p1nsmoot and count % 2 == 1:
        sfalse += 1
    elif p2nsmoot < p1nsmoot and count % 2 == 0:
        ftrue+=1
    print("p1 with smooting:")
    print(p1smoot)
    print("p2 with smooting:")
    print(p2smoot)
    if p2smoot >= p1smoot and count % 2 == 1:
        strues += 1
    elif p2smoot > p1smoot and count % 2 == 0:
        ffalses += 1
    if p2smoot <= p1smoot and count % 2 == 1:
        sfalses += 1
    elif p2smoot < p1smoot and count % 2 == 0:
        ftrues += 1
    s = w.readline()
    count += 1

print('r_n')
strue/(ftrue+strue)
print('p_n')
strue/(strue+sfalse)
print('r_s')
strues/(ftrues+strues)
print('p_s')
strues/(strues+sfalses)