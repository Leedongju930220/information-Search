import csv
import sys
import io
import re
import string
import os
import codecs
import nltk

page_no = 1
#간단한 코드를 위해 page_no를 1로 지정했습니다. 여러가지로 응용하시기 바랍니다.

bookwords = {'i','korea','love','lost','love','is','run'}
#단어들을 저장하는 공간입니다.

check_word= 'run'
#run이란 단어가 있는지 보기 위해 check_word에  run을 지정합니다.

stopw = {check_word}

tokens ={}
for word in bookwords:
    if word  in stopw:
        if word not in tokens:
            tokens["%s" %word] = []
        if page_no not in tokens["%s" % word]:
            tokens["%s" %word].append(page_no)

            print(tokens)
            #run이 bookwords에 있다면 page_no인 1을 출력합니다.
