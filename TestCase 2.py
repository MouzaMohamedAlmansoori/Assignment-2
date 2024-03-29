#!/usr/bin/env python
# coding: utf-8

# In[4]:


# here i will import exhibition class
from Exhibitions import Exhibition

# here i will Instantiate an instance of the Exhibition class
new_exhibition = Exhibition(title="Cartier, Islamic Inspiration and Modern Design", duration="2023-11-16 to 2024-03-24", location="Permanent Galleries")

# here i will Add the new exhibition to the museum's list of exhibitions
museum_exhibitions = []  # Example list to store exhibitions in the museum
museum_exhibitions.append(new_exhibition)

# here i will Verify that the new exhibition has been successfully added to the list of exhibitions
if new_exhibition in museum_exhibitions:
    print("New exhibition successfully opened at the museum!")
    # Display the details of the newly opened exhibition
    print("Details of the newly opened exhibition:")
    print("Title:", new_exhibition.get_title())
    print("Duration:", new_exhibition.get_duration())
    print("Location:", new_exhibition.get_location())
else:
    print("Failed to open new exhibition at the museum.")


# In[ ]:




