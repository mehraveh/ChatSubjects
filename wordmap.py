from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display


def wordmap_genartor(file_name):
    d = path.dirname(__file__)
    text= open(path.join(d,file_name.__str__() + '_wordmap_file.txt')).read()
    #reshaped_text = arabic_reshaper.reshape(text)
    #artext = get_display(reshaped_text)
    wordcloud = WordCloud(font_path="DroidSansMono.ttf",max_font_size=40).generate(text)
    wordcloud.to_image()
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

