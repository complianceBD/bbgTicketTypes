
# coding: utf-8

# In[7]:

from bbgTickets.ticketTypes import ticketTypes
import pandas as pd


# In[77]:

class bbgTicketTypes(object):

    
    
    
    def __init__(self, ticketDict):
        self.dict = ticketDict
        #self.frame = pd.DataFrame.from_dict(ticketDict).transpose().
        self.frame = self.frame()

    
    def frame(self):
        frame = pd.DataFrame.from_dict(self.dict)
        frame = frame.transpose().reset_index()
        frame.columns = ['ticketCode', 'ticketDescription', 'ticketType']
        return frame
        
    


# In[78]:

tickets = bbgTicketTypes(ticketTypes)


# In[ ]:




# In[ ]:




# In[23]:




# In[ ]:




# In[ ]:



