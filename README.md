# chatSubjects

This project will compare 2 telegram chats based on subject

### Getting Started
we use txt files of telegram chats. we can have if from "save telegram chat history". Its google chrome extention.
https://chrome.google.com/webstore/detail/save-telegram-chat-histor/kgldnbjoeinkkgpphaaljlfhfdbndfjc?hl=en

### Installing

you just need to install python 3 for this project.
and install pip3 in ubuntu :
sudo apt install python3-pip


then you need to install openpyxl module by this command:
pip3 install openpyxl
Then we need hazm module.install it by 
pip3 install hazm
for generating wordmap you need to install wordcloud module bt commands bellow:
sudo apt-get install python3-dev
sudo yum install -y python34-devel
but you must install python tkinter first:
sudo apt-get install python-tk
**this command are in ubuntu because hazm module install on ubuntu easily**




### Running project
word map :
you just need to set file name in main.py to find word maps.
then for comparing number of words in chats and drow word map run word_map.py
**in total doc I use this web site fore generating wordmap: https://worditout.com/word-cloud/create**


###  code
when you get telegram chats txt file from that extention , it has authers name id and dates.
we remove them by cleaning function.
this function writes cleaned chats in new file. its name is auther_cleaned.txt
Then we have hazm function that at first modify spaces between words.
also tokenize word and delete unnecessary words and delete plural signs and etc by filtering function.
then writes them to auther_tokenized. this file have words and their number of repeatation
we have wordmap  file that has wordmap_genarator function that generaets graphical word map of the file.
**this chats are just example and maybe find better chats next.**

### to do
write edit distance function for words in word map.
text clasiffication
####### Authors

* **by Mehraveh Ahmadi** 



