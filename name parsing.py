#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests
from bs4 import BeautifulSoup
URL = "https://www.pulsarsecurity.com/team"
page = requests.get(URL)

print(page.text)


# In[22]:


soup = BeautifulSoup(page.content, "html.parser")


# In[23]:


results = soup.find(id="block-team")


# In[24]:


print(results.prettify())


# In[25]:


name_elements = results.find_all("h3", class_="block-team-name")


# In[26]:


for name_element in name_elements:
    print(name_element, end="\n"*2)


# In[27]:


for name_element in name_elements:
    print(name_element.text)
    print()


# In[ ]:





# In[ ]:




