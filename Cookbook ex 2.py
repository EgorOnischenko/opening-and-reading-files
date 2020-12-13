#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

keys = ['ingredient_name', 'quantity', 'measure', ]
cook_book_dict = {}

with open('cookbook.txt') as text:
   
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


new_dict = {}
dishes = input().split()
person_count = int(input())
for i in dishes:
  recipe = cook_book_dict[i]
  for k in recipe:
    ingredient = k.get("ingredient_name")
    if ingredient in new_dict:
      dic = new_dict[ingredient] 
      dic["measure"] = k.get("measure")
      dic["quantity"] += int(k.get("quantity")) * person_count
    else: 
      new_dict[ingredient] = {}
      new_dict[ingredient]["measure"] = k.get("measure")
      new_dict[ingredient]["quantity"] = int(k.get("quantity")) * person_count

