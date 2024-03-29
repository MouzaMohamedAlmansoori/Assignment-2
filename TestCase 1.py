#!/usr/bin/env python
# coding: utf-8

# In[2]:


# first i will import artwork class
from Artwork import Artwork

# Here i will Instantiate an instance of the Artwork class
new_art = Artwork(title="Reliquary in the Form of a Stupa, and its Contents", artist="unnown", date_of_creation="1303-1306", historical_significance="Buddhist reliquary", exhibition_location="Permanent Galleries")

# here i will Add the new art piece to the museum's collection (assuming museum is a collection or database)
museum_collection = []  # Example list to store artworks in the museum's collection
museum_collection.append(new_art)

# here i will Verify that the art piece has been successfully added to the museum's collection
if new_art in museum_collection:
    print("New art piece successfully added to the museum's collection!")
    print("Information of the newly added artwork:")
    print("Title:", new_art.get_title())
    print("Artist:", new_art.get_artist())
    print("Date of Creation:", new_art.get_date_of_creation())
    print("Historical Significance:", new_art.get_historical_significance())
    print("Exhibition Location:", new_art.get_exhibition_location())
else:
    print("Failed to add new art piece to the museum's collection.")


# In[ ]:




