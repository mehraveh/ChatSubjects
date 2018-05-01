# chatSubjects

This project will compare 2 telegram chats based on subject

### Getting Started
we use txt files of telegram chats. we can have if from "save telegram chat history". Its google chrome extension.
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
in new phease we are using vowpal wabbit app 
you can install it by:
sudo apt-get install vowpal-wabbit
**this command are in ubuntu because hazm module install on ubuntu easily**




### Running project
word map :
you just need to set file name in main.py to find word maps.
then for comparing number of words in chats and drow word map run word_map.py
**in total doc I use this web site fore generating wordmap: https://worditout.com/word-cloud/create**
in new phease we have naviie bayes code with smoothing and without it
also calculate precision and recall.
**our precision withtout smoothing was : 0.61
our recall  withtout smoothing was : 0.006
our precision with smoothing was : 0.68
our recall  witht smoothing was : 0.007**

then we have vowpal wabbit commands.
At first we must train our data by this command:
vw -d movie_reviews_train.vw --loss_function logistic -f movie_reviews_model.vw
movie_reviews_train.vw : our input file
movie_reviews_model.vw : our trained file
 **input file should be like this : " 1 | hi 
                                      -1 | hellow
                                       1 | how are u" **
                                       
 then we create test file like input file format and run it by this command:
 vw -i movie_reviews_model.vw -t -d movie_reviews_valid.vw -p movie_valid_pred.txt
 movie_reviews_model.vw : our trained file
 movie_reviews_valid.vw : our test file
 movie_valid_pred.txt : our out put file with predictions .thats like this:
 -0.067254
1.778347
-0.250602
-0.262202
-2.076922
-0.067254
-0.234892
1.817633
-0.332480
3.940919
 also we test it by different ngrams:
 for example we test n = 1 ,2 ,3 ,4 ,5 ,6 
 and calculate accurecy. the result is that:
 **1:0.6936842105263158
 2: 0.6978947368421052
 3: 0.6989473684210527
 4: 0.7021052631578948
 5: 0.7042105263157895
 6: 0.6989473684210527**
 you see that 5-gram is the best for our data.
 
 
 
                                    
###  code
when you get telegram chats txt file from that extension , it has authers name id and dates.
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



