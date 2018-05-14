import csv
import sys
import io
import re
import string
import os
import codecs
import nltk                             
#nltk는 영어텍스트를 다룰 때 좋고, 한국어는 KoNLPy를 이용하시면 됩니다(pip install nltk)


frequency = {}
filename1 = open('doc1.txt', 'r')
text1= filename1.read()
filename2 = open('doc2.txt', 'r')
text2= filename2.read()
filename3 = open('doc3.txt', 'r')
text3= filename3.read()
filename4 = open('doc4.txt', 'r')
text4= filename4.read()
filename5 = open('doc5.txt', 'r')
text5= filename5.read()
filename6 = open('doc6.txt', 'r')
text6= filename6.read()
filename7 = open('doc7.txt', 'r')
text7= filename7.read()
#파이썬 경로에 먼저 doc1~doc7까지 텍스트파일을 저장시킵니다.

print(text1)
# text1을 열어서 저장된 doc1.txt파일을 잘 읽어왔나 print해봅니다.



filenames = ['doc1.txt', 'doc2.txt','doc3.txt','doc4.txt','doc5.txt','doc6.txt','doc7.txt']
with open('doc8.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
#doc1~doc7까지의 각각 다른 txt파일들을 하나의 txt파일로 합치는 과정입니다. token화를 한번에 하기 위해서.

filename1.close()
filename2.close()
filename3.close()
filename4.close()
filename5.close()
filename6.close()
filename7.close()
#열었던 파일들을 모두 닫아줍니다

filename8 = open('doc8.txt' , 'r')
text_string = filename8.read().lower()
#doc8.txt를 소문자로 읽어옵니다

match_pattern = re.findall(r'\b[a-z]{3,15}\b',text_string)
#단어읽는 방법입니다 '\b[a-z]{3,15}\b 이부분은 다른 코드도 많으니 검색 후 사용해보시기 바랍니다

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
#단어들을 count하는 코드입니다.

frequency_list = frequency.keys()
print("-------------------------------------------")

print ("word       count")
for x in frequency_list:
    print(x ,"   ",frequency[x])
#doc8을 읽어와 token화한 단어들과 count를 출력합니다
    
    
