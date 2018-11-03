import mysql.connector
import sys
from gtts import gTTS
from PIL import Image
from pytesseract import image_to_string
from pytesseract import image_to_boxes
from pytesseract import image_to_osd
from pytesseract import image_to_data
from pytesseract import image_to_pdf_or_hocr
#from pytesseract import osd_to_dict
#from pytesseract import run_tesseract
#from pytesseract import run_and_get_output


img=Image.open("/home/san/aaa/example_03.png")
text=image_to_data(img)
print text

text=image_to_boxes(img)
print text







#======================================

# db= mysql.connector.connect(user="root",password="asdfghjkl;",host="localhost",database="dsaa")

# mycursor = db.cursor()

# print """ 
# 	+=========================================+
# 	|    Please select  page no. of Book	  |
# 	+=========================================+
# 	  """
# mycursor.execute("select address,id from test")

# data = mycursor.fetchall()
# a=[]
# for i in data:
# 	a.append(i[0])
# 	#print i

# for i in range(len(a)):
# 	print i,".",a[i]

# mycursor.close()
# #=====================================
	
# page_no=int(input("Enter a page number which you want to read and listen:\n\n"))
	
# for i in range(len(a)):
# 	if page_no==i:
# 		path=a[i]
	
# print ("\t\t\t<<<========================Book Page=======================================>>>\n\n")

# #============Image to text=============

# img=Image.open(path)
# text=image_to_string(img)
# print text
# img.show()

# #==========Text to Speech===============

# blabla = (text)
# tts = gTTS(text=blabla, lang='en')
# tts.save("/home/san/aaa/audio1.mp3")

# #==========Playing sound==================
# from playsound import playsound
# playsound("/home/san/aaa/audio1.mp3")


# db.close()
# sys.exit()