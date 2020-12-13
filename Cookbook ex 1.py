#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json

keys = ['ingredient_name', 'quantity', 'measure', ]
cook_book_dict = {}

with open('Cookbook.txt') as text:
   
    lines = []
    for line in text:
        line = line.strip()
        if line:
            lines.append(line)
        continue
    lines = iter(lines)  

    
    for name in lines:  
        cook_book_dict[name] = []
        num = next(lines)  

        for _ in range(int(num)):  
            make_line = next(lines)  
            ingrid = make_line.split(' | ')  
            z = zip(keys, ingrid)  
            make_dict = {k: v for (k, v) in z}  
            cook_book_dict[name].append(make_dict)
            continue

        
        continue

print(json.dumps(cook_book_dict, indent=1, ensure_ascii=False))


# In[ ]:





# In[ ]:





# In[ ]:




