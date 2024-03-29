#!/usr/bin/env python
# coding: utf-8

# In[18]:


# here i will import ticket and visitor classes
from Ticket import Ticket
from Visitor import Visitor

# here i am storing visitor detail in a variable visitor
visitor = Visitor(visitor_name="Mouza", visitor_age=20, visitor_category="Adult")
# here i am creating ascennerio where i have purchased ticket and stored in a variable named event_ticket
event_ticket = Ticket(ticket_id=123456, price=63.0, visitor= Visitor)

# here i am Calculating the total price including VAT (5%)
total_price_with_vat = event_ticket.get_price() * 1.05

# Display payment receipt for the purchased ticket
print("Payment Receipt:")
print("Visitor Name:", visitor.visitor_name)
print("Visitor Category:", visitor.visitor_category)
print("Ticket Price (Before VAT):", event_ticket.get_price(), "AED")
print("Total Price (Including VAT):", total_price_with_vat, "AED")


# In[ ]:




