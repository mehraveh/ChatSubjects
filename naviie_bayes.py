from hazm import Lemmatizer, Normalizer
from hazm import *
import math


def naviie_bayes_nsmoot(wordsin1,wordscountin1,wordsin2,wordscountin2,inputStr):
    """

    :param wordsin1:
    :param wordscountin1:
    :param wordsin2:
    :param wordscountin2:
    :param inputStr:
    :return:
    """
    pNB1 = 1
    pNB2 = 1
    words = []
    wordsCount1 = 0
    wordsCount2 = 0
    normalizer = Normalizer()
    lemmatizer = Lemmatizer()
    s = normalizer.normalize(inputStr.__str__())
    t = word_tokenize(s.__str__())
    for word in t:
        words.append(lemmatizer.lemmatize(word.__str__()))

    for i in range(len(wordsin1)):
        wordsCount1 += wordscountin1[i]

    for i in range(len(wordsin2)):
        wordsCount2 += wordscountin2[i]

    for word in words:
        if word in wordsin1:
            pNB1 += math.log10(wordscountin1[wordsin1.index(word.__str__())]/wordsCount1)
        else:
            pNB1 = 0

    for word in words:
        if word in wordsin2:
            pNB2 += math.log10(wordscountin2[wordsin2.index(word.__str__())] / wordsCount2)
        else:
            pNB2 = 0

    return pNB1, pNB2

def naviie_bayes_smoot(wordsin1,wordscountin1,wordsin2,wordscountin2,inputStr):
    """

    :param wordsin1:
    :param wordscountin1:
    :param wordsin2:
    :param wordscountin2:
    :param inputStr:
    :return:
    """
    pNB1 = 1
    pNB2 = 1
    words = []
    wordsCount1 = 0
    wordsCount2 = 0
    normalizer = Normalizer()
    lemmatizer = Lemmatizer()
    s = normalizer.normalize(inputStr.__str__())
    t = word_tokenize(s.__str__())
    for word in t:
        words.append(lemmatizer.lemmatize(word.__str__()))

    for i in range(len(wordsin1)):
        wordsCount1 += (wordscountin1[i]+1)

    #print('count1')
    #print(wordsCount1)
    for i in range(len(wordsin2)):
        wordsCount2 += (wordscountin2[i]+1)

    for word in words:
        if word in wordsin1:
            pNB1 += math.log10((wordscountin1[wordsin1.index(word.__str__())]+1)/wordsCount1)
        else:
            pNB1 = 1/wordsCount1
    for word in words:
        if word in wordsin2:
            pNB2 += math.log10((wordscountin2[wordsin2.index(word.__str__())]+1) / wordsCount2)
        else:
            pNB2 = 1 / wordsCount2
    return pNB1, pNB2
