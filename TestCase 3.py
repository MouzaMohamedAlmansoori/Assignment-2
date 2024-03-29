#!/usr/bin/env python
# coding: utf-8

# In[22]:


#here i will import classes
from Ticket import Ticket
from Visitor import Visitor
from Exhibitions import Exhibition  # Import Exhibition class

# here i will Instantiate an instance of the Visitor class
visitor = Visitor(visitor_name="Mouza", visitor_age=20, visitor_category="Adult")

# here i will Instantiate an instance of the Exhibition class
new_exhibition = Exhibition(title="Cartier, Islamic Inspiration and Modern Design", duration="2023-11-16 to 2024-03-24", location="Permanent Galleries")
# Instantiate an instance of the Ticket class for the event
event_ticket = Ticket(ticket_id=123456, price=63.0, visitor=visitor)

# here i will Verify that the ticket has been successfully purchased
print("Ticket purchased successfully by", visitor.get_visitor_name())
print("Ticket price:", event_ticket.get_price())
print("Visitor category:", visitor.get_visitor_category())
print("Exhibition details:")
print("Title:", new_exhibition.get_title())
print("Duration:", new_exhibition.get_duration())
print("Location:", new_exhibition.get_location())


# In[ ]:





# In[ ]:




