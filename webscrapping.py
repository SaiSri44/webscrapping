# Web scraping can be done in two ways
# 1.Using the API
# 2.Using bs4  to web scrapp with python

# Steps invovled in web scrapping
# step 0 : installing the requirments
# step 1 : getting the HTML text
# step 2 : parasing the HTML text
# step 3 :HTML tree taversal

# STEP 0 : INSTALLING REQUIRED PACKAGES
# pip install bs4
# pip install requests
# pip install html5lib
from bs4 import BeautifulSoup
import html5lib
import requests


# STEP 1 getting the HTML content

url = "https://en.wikipedia.org/wiki/Elon_Musk"
r = requests.get(url)  # requesting the server for index.html file
html_content = r.content  # reading the content of the index.html file in html mode
# print(html_content)

# STEP 2 PARASING THE HTML FILE

# Beautifuolsoup will convert the string type html_content to in the format of HTML code
soup = BeautifulSoup(html_content, "html.parser")
# print(soup) #we will get the code in ther html format rather than the text format


# STEP 3 html tree traversal


title = soup.title
# print(title) It will give the whole tittle tag,if we wan tonly the title then we would need title.string
print(title.string)  # this will give the title of the html file

# Getting all the respective tags  from html file
paras = soup.find_all('p')  # getting all the paragraph's in the html file
# print(paras) we will get the list of all the paragraphs using findall function
para1 = soup.find("p") #this will give the first paragraph
# print(para1)
# 'a' is used for anchor ,'div' for divisions.'select' for select etc are used to find all the respective tags
anchors = soup.find_all('a') #getting all the anchor tags
# print(anchors)

#GETTING THE CLASSES 

div_classses = soup.find('div')['class'] #by soup.find('div) we get the first div tag,we can get the classes inside it by using soup.find('tag')['class']
# if there are multiple classes in the tag ,we get the list containg all the classes in tag. we can abstract them by list indexing,in above example ther is only one class
# print(div_classses)

#OBTAINING ALL THE ELEMENTS WITH SPECIFIED CLASS

# print(soup.find_all("p",class_="noprint"))
#here we had given two arguments,one tag,other is class, we get the all the tag elements containg the given classes,if there is no tag element containing given class
# then it will retiurn empty list..in above example there is no paragrah tags containing the class noprint

# print(soup.find_all("div",class_="noprint")) ,this is not an empty list,ther are some div tag elements which has class noprint
#tag may not other classes too,if the given classes is present in that tag it would  be considered

#GETTING TEXT FROM THE ELEMENTS


# print(soup.find('p').get_text())
# for para in soup.find_all('p') :
#     print(para.get_text()) 


#get_text() function is used to get the text from tag, soup.find('p') .get_text() mean we are trying to get text from the first paragraph
# As soup.find_all('p') is list ,so we should iterate through the list inorder to get text from the each paragraph tag

 ## Finding all the links in the web page

# for link in soup.find_all('a') :
#      print(link.get('href'))           #get function is used toget the attributes of the  tag like href,id,class,name,value
#      print(link.get('id'))             #here anchor tags has no id and name so the output is none
#      print(link.get('name')) 
    
# for para in soup.find_all('p') :
#     print(para.get('id'))     #In this page there are no id's because it doesn't use backend 
#     print(para.get('name'))   # In this page there are no name because it doesn't use backend
#     
print()
