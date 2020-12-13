#!/usr/bin/env python
# coding: utf-8

# In[ ]:


p = 0
b = 0
c = 0
with open('txt.1') as f1:
    for line in f1:
        p += 1

with open('txt.2') as f2:
    for line in f2:
        b += 1

with open('txt.3') as f3:
    for line in f3:
        c += 1

f1.close()
f2.close()
f3.close()
f1 = open('txt.1', 'r')
f2 = open('txt.2', 'r')
f3 = open('txt.3', 'r')

d = open('answer.txt','w')

arr = [[p, f1, "txt.1"], [b, f2, "txt.2"],[c, f3, "txt.3"]]
arr.sort()
for i in arr:
  d.write(i[2] + "\n")
  d.write(str(i[0]) + "\n")
  for k in i[1]:
    d.write(k)

d.close()
f1.close()
f2.close()
f3.close()

