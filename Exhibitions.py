#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This is class Exhibition
class Exhibition:
   #i have made constructor of Exhibition class
    def __init__(self, title, duration, location):
        # i have Initialize attributes
        self.title = title  # Title of the exhibition
        self.duration = duration  # Duration of the exhibition (datetime object)
        self.location = location  # Location where the exhibition takes place

 # i have made method to get the title of the exhibition
    def get_title(self):
        return self.title

     # i have made method to get the duration of the exhibition
    def get_duration(self):
        return self.duration

     # i have made method to get the location of the exhibition
    def get_location(self):
        return self.location

   # i have made method to set the title of the exhibition
    def set_title(self, title):
        self.title = title

     # i have made method to set the duration of the exhibition
    def set_duration(self, duration):
        self.duration = duration

     # i have made method to set the location of the exhibition
    def set_location(self, location):
        self.location = location


# In[ ]:




