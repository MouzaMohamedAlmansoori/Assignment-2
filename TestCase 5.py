#!/usr/bin/env python
# coding: utf-8

# In[12]:


#here i will import datetime
from datetime import datetime
# here i will import class EducationalProgram
from EducationalProgram import EducationalProgram

# here i will Create an instance of EducationalProgram
new_program = EducationalProgram(
    program_id=1,
    title="Mindful Art Moments",
    duration=45,
    time=datetime(2024, 4, 15, 10, 0),  # April 15, 2024, 10:00 AM
    fee=600.0,
    max_capacity=25
)


# here i will Display program details
print("Program ID:", new_program.get_program_id())
print("Title:", new_program.get_title())
print("Duration:", new_program.get_duration(), "minutes")
print("Scheduled Time:", new_program.get_time().strftime("%Y-%m-%d %H:%M"))
print("Fee:", new_program.get_fee(), "AED")
print("Max Capacity:", new_program.get_max_capacity(), "participants")


# In[ ]:




