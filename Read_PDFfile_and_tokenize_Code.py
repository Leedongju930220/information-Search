import PyPDF2       
import mysql.connector
from PyPDF2 import PdfFileReader
import nltk
from nltk.tokenize.regexp import RegexpTokenizer
#PDF파일을 읽기 위해 pip install PyPDF2로 설치한다. MySQL을 사용하기 위해 mysql.connector도 설치해서 import한다.

file = open("short_stories.pdf","rb")
#PDF파일은 다운로드후 경로파일에 저장해야 불러서 읽을수 있다.

pdf_reader = PyPDF2.PdfFileReader(file)

print(pdf_reader.getNumPages())
#print를 해서 PDF로부터 총 몇개의 Page를 불러왔는지 확인해본다.

pageObj = pdf_reader.getPage(0)
text1 = pageObj.extractText()
print(text1)
#잘 불러왔다 text1을 하나 출력해본다.  pdf_reader.getPage(0)으로 첫번째 pdf페이지를 가져왔다.

pdf_page_num = pdf_reader.getNumPages()

directory = ["doc1","doc2", "doc3", "doc4", "doc5", "doc6", "doc7", "doc8", "doc9", "doc10", "doc11","doc12", "doc13","doc14"]
tokened_text = ["tokened1","tokened2","tokened3","tokened4","tokened5","tokened6","tokened7","tokened8","tokened9","tokened10","tokened11","tokened12","tokened13","tokened14",]
frequency_list = ["fre1","fre2","fre3","fre4","fre5","fre6","fre7","fre8","fre9","fre10","fre11","fre12","fre13","fre14",]
for i in range(pdf_page_num):
    pageObj = pdf_reader.getPage(i)
    directory[i] = pageObj.extractText()
    print("-----------------------new page: %d------------------" % i)
    print(directory[i])
    print("-----------------------page %d token-----------------" % i)
    tokenizer = RegexpTokenizer(r'\b[a-z]{3,15}\b')
    tokened_text[i] = tokenizer.tokenize(directory[i])
    print(tokened_text[i])

#directory는 내가 총 14개의 페이지를 불러왔기 때문에 doc1~doc14까지 저장했다
#tokened_text는 doc1~doc14까지 각 doc을 토큰화한 단어들을 doc마다 구별해서 저장하기위해 tokened1~14까지 저장했다
#frequency_list느 tokened_text에 있는 단어들을 '같은 기호들을 빼고 순수히 단어들만 저장하기 위해 지정하였다.
#아직 파이썬 실력이 좋지않아서 저렇게 지정했지만, 커스텀해서 사용해야한다, 더 실력이 되면 바꾸어 볼 예정이다(7월안에)


cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='Leedongju_midexam',
                              port='3306')
######################################################################

# CREATE cursor

cursor = cnx.cursor()

# delete all data ...

#cursor.executev=("DELETE FROM word_location")
cursor.execute("DELETE FROM words")
cursor.execute("ALTER TABLE words AUTO_INCREMENT=1")
cursor.execute("DELETE FROM word_location")
cursor.execute("ALTER TABLE word_location AUTO_INCREMENT=1")
#cursor.executev=("ALTER TABLE pages AUTO_INCREMENT=1")


    

        
frequency = {}
for i in range(14):
    
    for word in tokened_text[i]:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        
    total= frequency.keys()

total_count =0
for p in total:    
    cursor.execute(("INSERT INTO words (word) VALUES ('%s')"% (p)))
    total_count +=1
    
    
for i in range(14):
    frequency = {}
    for word in tokened_text[i]:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        
    frequency_list[i]= frequency.keys()

word_id =1
    
for i in range(14):
    word_id =1
    for t in total:        
        stopw = {t}
        for word in frequency_list[i]:
            if word in stopw:
                cursor.execute(("INSERT INTO word_location VALUES ('%s','%s')"% (word_id,i+1)))
        word_id+=1
    
        



cnx.commit()
cursor.close()
cnx.close()
file.close()
