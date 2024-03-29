#!/usr/bin/env python
# coding: utf-8

# In[6]:


# This is class Visitor
class Visitor:
    #i have made constructor of class Visitor
    def __init__(self, visitor_name, visitor_age, visitor_category):
         # i have Initialize attributes
        self.visitor_name = visitor_name  # Name of the visitor
        self.visitor_age = visitor_age  # Age of the visitor
        self.ticket = None  # Ticket purchased by the visitor
        self.visitor_category = visitor_category  # Category of the visitor
    
 # i have made method to get the name of the visitor
    def get_visitor_name(self):
        return self.visitor_name

     # i have made method to get the age of the visitor
    def get_visitor_age(self):
        return self.visitor_age

    # i have made method to get the category of the visitor
    def get_visitor_category(self):
        return self.visitor_category
    
     # i have made method to buy ticket online
    def buy_ticket_online(self, event_type):
        self.ticket = Ticket(event_type, self.visitor_category)
    
     # i have made method to buy ticket in person
    def buy_ticket_in_person(self, event_type):
        # Assuming Ticket class is already defined
        # Create a new ticket for the visitor
        self.ticket = Ticket(event_type, self.visitor_category)

    # i have made method to Set the name of the visitor
    def set_visitor_name(self, visitor_name):
        self.visitor_name = visitor_name
    
     # i have made method to Set the age of the visitor
    def set_visitor_age(self, visitor_age):
        self.visitor_age = visitor_age
    
    # i have made method to Set the category of the visitor
    def set_visitor_category(self, visitor_category):
        self.visitor_category = visitor_category



# In[ ]:




