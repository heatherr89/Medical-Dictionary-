#!/usr/bin/env python
# coding: utf-8

# ## Import dependencies

# In[1]:


import requests
from bs4 import BeautifulSoup


# ## Get links

# In[176]:


def get_links():
    URL = 'https://www.health.harvard.edu/a-through-c'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(id="main")
    letter_links = [link.get('href') for link in main.find_all('a')]
    letter_links = letter_links[0:26]
    return letter_links


# ## Get words from sites
# 

# In[178]:


def word_collection(letter_links):
    word_list = []
    for link in letter_links:
        letter_page = requests.get(link)
        soup = BeautifulSoup(letter_page.content, 'html.parser')
        main = soup.find(id="main")
        for word in main.find_all('strong'):
            word_list.append(word.get_text().replace(": ",''))
        word_list = word_list[0:len(word_list)-1]
    return word_list


# # Create a file

# In[179]:


links = get_links()
word_list = word_collection(links)


# In[180]:


newfile = open("medical_dictionary.txt", "w+")


# In[181]:


for word in word_list:
    newfile.write(word + "\n")


# In[ ]:




