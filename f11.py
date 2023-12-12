#!/usr/bin/env python
# coding: utf-8

# # List practice

# In[2]:


list1=[3,6,9,"i hate school",12.3]


# In[3]:


list1.append(69)


# In[4]:


list1


# In[5]:


list1.remove(9)


# In[6]:


list1


# In[7]:


list1.pop(2)


# In[8]:


list1


# # How to check if an element is in a list?

# In[9]:


6 in list1


# In[10]:


10 in list1


# In[11]:


"Fatimah" in list1


# # Can a list be nested (contain other lists)?

# In[12]:


list2=[[3,9],"hi",24.6,[3,"apple","banana"]]


# In[13]:


list2[3]


# # How to find the length of a list?

# In[15]:


len(list2)


# # How to slice elements from a list?

# # my_list[start:end:step]

# print(list2)

# In[20]:


list3=list2[1:3]


# In[21]:


list3


# In[23]:


list4=list2[3]


# #### 

# In[24]:


list4


# # Can elements in a list be changed or reassigned?

# In[25]:


list5 = [6,7,9,8,0,1]


# In[26]:


list5[1]=50


# In[27]:


list5


# In[28]:


list5[4]=10


# In[29]:


list5


# In[31]:


list5[5]="end"


# In[32]:


list5


# In[33]:


list6=[3,6,7]
list7=[2,4,6]


# # How to concatenate or combine lists?

# In[34]:


list8=list6+list7
list8


# In[35]:


list6.extend(list7)


# In[36]:


list6


# # What is the difference between append() and extend() methods

# In[37]:


list7


# In[38]:


list7.append(list6)


# In[39]:


list7


# In[40]:


list6


# # How to reverse a list?

# list6.reverse()

# In[41]:


list6.reverse()


# In[42]:


list6


# # How to sort a list?

# In[43]:


list6.sort()


# In[44]:


list6


# # Can a list have duplicate elements?

# In[46]:


list8=[8,8,6,6,9,9,0,1,7,9]


# In[47]:


list8.sort()


# In[48]:


list8


# In[50]:


list8.reverse()


# In[51]:


list8


# In[55]:


my_list = [1, 2, 3, 4, 5]
for num1 in list8:
    print("hello")


# In[ ]:




