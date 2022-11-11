#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil # high level file operations
import re # regular expressions
import os # misc operating system interfaces
import fnmatch # file name matching
import pandas as pd
import numpy as np
import copy # generic copying operations (deep and shallow)
import nltk
from nltk.tokenize import WordPunctTokenizer
nltk.download('stopwords')
from nltk.corpus import stopwords


# In[2]:


# Enter the directory name where your images are 
# this should be a subdirectory of where 
# you are running the script from
default_dir = "images"

my_photo_dir = input('Enter your image folder name or blank to use default name "images":') or default_dir

print(my_photo_dir)

# create the full path to the photos
photo_dir = (os.path.join(os.getcwd(), my_photo_dir))


# In[3]:


photos = [] # create an empty list called photos (full paths)
photos_base = [] # this will be just the photo base names

# walk through the photo directory and append to the lists
for root, dirs, files in os.walk(photo_dir, topdown=True):
   for name in files:
    if fnmatch.fnmatch(name, '*.png'):
      #print(os.path.join(root, name))
      photopath = (os.path.join(root, name))
    photos.append(photopath)
    photos_base.append(name)


# In[5]:


# create string - join elements of the list with a space
keyword_tokens = ' '.join(photos_base)


# In[6]:


# returns tokens from a string
word_punct_keywords = WordPunctTokenizer().tokenize(keyword_tokens)


# In[7]:


# this is sourced from KahEm Chu (2021): https://towardsdatascience.com/text-processing-in-python-29e86ea4114c
# cleans up the tokens
clean_token=[]
for token in word_punct_keywords:
    token = token.lower()
    # remove any value that are not alphabetical
    new_token = re.sub(r'[^a-zA-Z]+', '', token) 
    # remove empty value and single character value
    if new_token != "" and len(new_token) >= 2: 
        vowels=len([v for v in new_token if v in "aeiou"])
        if vowels != 0: # remove line that only contains consonants
            clean_token.append(new_token)


# In[8]:


# get the list of stop words
stop_words = stopwords.words('english')

# add new stopwords to the list including dall e stop words
stop_words.extend(["lots","many","much", "dsstore", "imgsortr", "ipynb"])
stop_words.extend(["eating", "wearing", "holding", "style", "checkpoint", "variation", "huge", "wide", "angle"])

# remove the stopwords from the list of tokens
tokens = [x for x in clean_token if x not in stop_words]


# In[9]:


# numpy and pandas
# wrap the list into a numpy array
# call value_counts() method of pd 
dataframe = pd.value_counts(np.array(tokens))


# In[10]:


keywords = []
for i in dataframe.index:
    word = i
    keywords.append(word)


# In[11]:


# check for matches and move files
photos_rep = copy.deepcopy(photos)
for key in keywords:
    for file in photos_rep.copy():
        if not re.search(key, file):
            pass
        else: 
            photos_rep.remove(file)
            if os.path.exists(os.path.join(photo_dir, key)):
                shutil.copy2(file, os.path.join(photo_dir, key))
            else:
                os.mkdir(os.path.join(photo_dir, key))
                shutil.copy2(file, os.path.join(photo_dir, key))


# In[ ]:




