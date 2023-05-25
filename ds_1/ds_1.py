#!/usr/bin/env python
# coding: utf-8

# # Data Science
# ## Home task 1

# In[1]:


#import module numpy
import numpy as np


# #### 1. Create a one-dimensional array (vector) with the first 10 positive integers and print its value.

# In[2]:


np.arange(10)


# In[3]:


a = np.arange(1, 10)
print(a)


# #### 2. Create a two-dimensional array (matrix) of size 3x3, fill it with zeros and print its value. 

# In[4]:


np.zeros((3, 3), dtype=int)


# In[5]:


a = np.zeros((3, 3), dtype=int)
print(a)


# #### 3. Create an array of size 5x5, fill it with random integers in the range from 1 to 10 and print its value.

# In[6]:


np.random.randint(1, 11, size=(5, 5))


# In[7]:


a = np.random.randint(1, 11, size=(5, 5))
print(a)


# #### 4. Create an array of size 4x4, fill it with random real numbers in the range from 0 to 1 and print its value.

# In[8]:


a = np.random.uniform(low=0.0, high=1.0, size=(4, 4))
print(a)


# #### 5. Create two one-dimensional arrays of size 5, fill them with random integers in the range from 1 to 10, and perform elementwise addition, subtraction, and multiplication operations on them.

# In[9]:


a = np.random.randint(1, 11, size=(5))
b = np.random.randint(1, 11, size=(5))


# In[10]:


print(a+b)


# In[11]:


print(a-b)


# In[12]:


print(a/b)


# #### 6. Create two vectors of size 7, fill them with random numbers and find their scalar product.

# In[13]:


a = np.random.random(7)
b = np.random.random(7)
print(np.dot(a, b))


# #### 7. Create two matrices of size 2x2 and 2x3, fill them with random integers in the range from 1 to 10, and multiply them.

# In[14]:


a = np.random.randint(1, 11, size=(2, 2))
b = np.random.randint(1, 11, size=(2, 3))
print(np.dot(a, b))


# #### 8. Create a 3x3 matrix, fill it with random integers in the range from 1 to 10, and find its inverse.

# In[15]:


a = np.random.randint(1, 11, size=(3, 3))
a_inv = np.linalg.inv(a)


# In[16]:


print(a)


# In[17]:


print(a_inv)


# #### 9. Create a 4x4 matrix, fill it with random real numbers in the range from 0 to 1 and transpose it.

# In[18]:


a = np.random.uniform(0, 1, size=(4, 4))


# In[19]:


print(a)


# In[20]:


print(a.T)


# #### 10. Create a 3x4 matrix and a 4-dimensional vector, fill them with random integers in the range 1 to 10, and multiply the matrix by the vector.

# In[21]:


a = np.random.randint(1, 11, size=(3, 4))
b = np.random.randint(1, 11, size=(4))


# In[22]:


print(a)


# In[23]:


print(b)


# In[24]:


print(a * b)


# #### 11. Create a 2x3 matrix and a vector of size 3, fill them with random real numbers in the range 0 to 1, and multiply the matrix by the vector.

# In[25]:


a = np.random.uniform(low=0.0, high=1.0, size=(2, 3))
b = np.random.uniform(low=0.0, high=1.0, size=(3))


# In[26]:


print(a)


# In[27]:


print(b)


# In[28]:


print(a * b)


# #### 12. Create two matrices of size 2x2, fill them with random integers in the range from 1 to 10, and perform their elementwise multiplication.

# In[29]:


a = np.random.randint(1, 11, size=(2, 2))
b = np.random.randint(1, 11, size=(2, 2))


# In[30]:


print(a)


# In[31]:


print(b)


# In[32]:


print(a * b)


# #### 13. Create two matrices of size 2x2, fill them with random integers in the range from 1 to 10 and find their product.

# In[33]:


a = np.random.randint(1, 11, size=(2, 2))
b = np.random.randint(1, 11, size=(2, 2))


# In[34]:


print(a)


# In[35]:


print(b)


# In[36]:


print(np.dot(a, b))


# #### 14. Create a 5x5 matrix, fill it with random integers in the range from 1 to 100 and find the sum of the matrix elements.

# In[37]:


a = np.random.randint(1, 101, size=(5, 5))


# In[38]:


print(a)


# In[39]:


print(a.sum())


# #### 15. Create two matrices of size 4x4, fill them with random integers in the range from 1 to 10 and find their difference.

# In[40]:


a = np.random.randint(1, 11, size=(4, 4))
b = np.random.randint(1, 11, size=(4, 4))


# In[41]:


print(a)


# In[42]:


print(b)


# In[43]:


print(a - b)


# #### 16. Create a 3x3 matrix, fill it with random real numbers in the range from 0 to 1, and find the column vector containing the sum of the elements of each row of the matrix.

# In[44]:


a = np.random.uniform(low=0.0, high=1.0, size=(3, 3))
b = np.array([sum(a[0, :3]), sum(a[1, :3]), sum(a[2, :3])])


# In[45]:


print(a)


# In[46]:


print(b.reshape((3, 1)))


# #### 17. Create a 3x4 matrix with any integers and create a matrix with the squares of these numbers.

# In[47]:


a = np.random.randint(-11, 11, size=(3, 4))


# In[48]:


print(a)


# In[49]:


print(np.square(a))


# #### 18. Create a vector of size 4, fill it with random integers in the range from 1 to 50, and find the vector with the square roots of these numbers.

# In[50]:


a = np.random.randint(1, 51, size=(4))


# In[51]:


print(a)


# In[52]:


print(np.sqrt(a))

