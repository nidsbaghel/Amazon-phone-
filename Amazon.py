#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install lxml')


# In[6]:


from bs4 import BeautifulSoup
import requests
import re


# In[7]:


Page=requests.get("https://www.amazon.in/s?k=under+20000+mobile&crid=1SZXKVA79LZXZ&sprefix=under+20000+%2Caps%2C1349&ref=nb_sb_ss_ts-doa-p_4_1s")
Page


# In[8]:


Page.content


# In[9]:


soup = BeautifulSoup(Page.content)
soup


# In[9]:


File = open("out.csv", "a")


# In[10]:


soup = BeautifulSoup(webpage.content, "lxml")


# In[12]:


title = soup.find("span", attrs={"id":'productTitle'})
title_value = title.string


# In[13]:


title_string = title_value.strip()


# In[14]:


print(type(title))
print(type(title_value))
print(type(title_string))
print()
print("Product Title = ", title_string)


# In[15]:


<class 'bs4.element.Tag'>
<class 'bs4.element.NavigableString'>
<class 'str'>
 
Product Title =  Sony PlayStation 4 Pro 1TB Console - Black (PS4 Pro)


# In[13]:


def get_title(soup):
     
    try:
           title = soup.find("span", attrs={"id":'productTitle'})
 
              title_value = title.string
 
               title_string = title_value.strip()
 
    except AttributeError:
        title_string = ""   
 
    return title_string
def get_price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
        price = ""  
 
    return price
def get_Avarage rating(soup):
 
    try:
        Avarage rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
         
    except AttributeError:
         
        try:
            Avarage rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = "" 
 
    return rating

    print("Product Name =", get_title(soup))
    print("Product Price =", get_price(soup))
    print("Product Avarage Rating =", get_rating(soup))
    print()


# In[12]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
links_list = []
for link in links:
    links_list.append(link.get('href'))
       for link in links_list:
         
        new_webpage = requests.get("https://www.amazon.in/s?k=under+20000+mobile&crid=1SZXKVA79LZXZ&sprefix=under+20000+%2Caps%2C1349&ref=nb_sb_ss_ts-doa-p_4_1s" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "lxml")
         
        print("Product Title =", get_title(new_soup))
        print("Product Price =", get_price(new_soup))
        print("Product Avarage Rating =", get_rating(new_soup))
       
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.in/s?k=under+20000+mobile&crid=1SZXKVA79LZXZ&sprefix=under+20000+%2Caps%2C1349&ref=nb_sb_ss_ts-doa-p_4_1s" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "lxml")
        print("Product Title =", get_title(new_soup))
        print("Product Price =", get_price(new_soup))
        print("Product Avarage Rating =", get_rating(new_soup))
       


# In[ ]:




