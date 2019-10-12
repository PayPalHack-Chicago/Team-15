#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas
import json
import csv
lst=[ 'All Majors', 'Accounting and Actuarial Science', 'Advertising and Public Relations', 'Aerospace Engineering', 'Agricultural Economics', 'Animal Sciences', 'Anthropology and Archeology', 'Architecture', 'Area, Ethnic, and Civilization Studies', 'Art and Music Education', 'Art History and Criticism', 'Associates Degree', 'Biochemistry and Molecular Biology', 'Biological, Biomedical, and Environmental Engineering', 'Biology', 'Botany, Ecology, and Zoology', 'Business Management and Administration', 'Chemical Engineering', 'Chemistry', 'Civil Engineering', 'Commercial Art and Graphic Design', 'Communication Technologies', 'Communications', 'Composition and Speech', 'Computer Engineering', 'Computer Science', 'Construction Services', 'Criminology and Criminal Justice', 'Drama and Theater Arts', 'Early Childhood Education', 'Earth and Other Physical Sciences', 'Economics', 'Electrical Engineering', 'Elementary Education', 'Energy and Extraction Engineering', 'Engineering Technologies', 'English Language and Literature', 'Environment and Natural Resources', 'Family and Consumer Sciences', 'Film, Video and Photographic Arts', 'Finance', 'Fine and Studio Arts', 'General Agriculture', 'General Education', 'General Engineering', 'Geography', 'Health and Medical Administration', 'High School Degree or GED', 'History', 'Hospitality Management', 'Human Resources and Personnel Management', 'Industrial and Manufacturing Engineering', 'International Business and Business Economics', 'International Relations', 'Journalism', 'Language and Drama Education', 'Liberal Arts', 'Linguistics and Foreign Languages', 'Marketing and Marketing Research', 'Mass Media', 'Math and Science Teacher Education', 'Mathematics and Statistics', 'Mechanical Engineering', 'Medical Technologies and Assistance', 'Microbiology, Physiology, Genetics, and Neuroscience', 'Multidisciplinary Science', 'Music', 'Nursing', 'Operations and Logistics', 'Philosophy and Religious Studies', 'Physical and Health Education Teaching', 'Physical Fitness, Nutrition, and Sports Studies', 'Physics', 'Political Science and Government', 'Production and Transportation Technologies', 'Psychology', 'Public Administration and Policy', 'Secondary Teacher Education', 'Social Science or History Teacher Education', 'Social Work', 'Sociology', 'Some College, No Degree', 'Some High School', 'Special Needs Education', 'Theology and Religious Vocations', 'Treatment Therapy Professions']
a='salary data.csv'
b='median_.csv'
c='output-v1.csv'

f = open(b)
reader = pandas.read_csv(b) 
reader


# In[79]:


lst=[ 'All Majors', 'Accounting and Actuarial Science', 'Advertising and Public Relations', 'Aerospace Engineering', 'Agricultural Economics', 'Animal Sciences', 'Anthropology and Archeology', 'Architecture', 'Area, Ethnic, and Civilization Studies', 'Art and Music Education', 'Art History and Criticism', 'Associates Degree', 'Biochemistry and Molecular Biology', 'Biological, Biomedical, and Environmental Engineering', 'Biology', 'Botany, Ecology, and Zoology', 'Business Management and Administration', 'Chemical Engineering', 'Chemistry', 'Civil Engineering', 'Commercial Art and Graphic Design', 'Communication Technologies', 'Communications', 'Composition and Speech', 'Computer Engineering', 'Computer Science', 'Construction Services', 'Criminology and Criminal Justice', 'Drama and Theater Arts', 'Early Childhood Education', 'Earth and Other Physical Sciences', 'Economics', 'Electrical Engineering', 'Elementary Education', 'Energy and Extraction Engineering', 'Engineering Technologies', 'English Language and Literature', 'Environment and Natural Resources', 'Family and Consumer Sciences', 'Film, Video and Photographic Arts', 'Finance', 'Fine and Studio Arts', 'General Agriculture', 'General Education', 'General Engineering', 'Geography', 'Health and Medical Administration', 'High School Degree or GED', 'History', 'Hospitality Management', 'Human Resources and Personnel Management', 'Industrial and Manufacturing Engineering', 'International Business and Business Economics', 'International Relations', 'Journalism', 'Language and Drama Education', 'Liberal Arts', 'Linguistics and Foreign Languages', 'Marketing and Marketing Research', 'Mass Media', 'Math and Science Teacher Education', 'Mathematics and Statistics', 'Mechanical Engineering', 'Medical Technologies and Assistance', 'Microbiology, Physiology, Genetics, and Neuroscience', 'Multidisciplinary Science', 'Music', 'Nursing', 'Operations and Logistics', 'Philosophy and Religious Studies', 'Physical and Health Education Teaching', 'Physical Fitness, Nutrition, and Sports Studies', 'Physics', 'Political Science and Government', 'Production and Transportation Technologies', 'Psychology', 'Public Administration and Policy', 'Secondary Teacher Education', 'Social Science or History Teacher Education', 'Social Work', 'Sociology', 'Some College, No Degree', 'Some High School', 'Special Needs Education', 'Theology and Religious Vocations', 'Treatment Therapy Professions']
import matplotlib.pyplot as plt
for i in lst:
    plt.plot(reader[i])
#plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
plt.ylabel('some numbers')
plt.show()


# In[58]:


fig=plt.figure()
fig.set_size_inches(30, 30)
sp2 = fig.add_subplot(2,2,1)
for i in lst:
    sp2.scatter(reader['Year'],reader[i])
sp2


# In[80]:


import pandas
import json
import csv

a='salary data.csv'
b='median_.csv'
c='output-v1.1.csv'

f = open(c)
reader = pandas.read_csv(c) 
reader


# In[60]:


fig=plt.figure()
fig.set_size_inches(30, 30)
sp2 = fig.add_subplot(2,2,1)
for i in lst:
    sp2.scatter(reader['Year'],reader[i])
sp2


# In[96]:



import matplotlib.pyplot as plt
plt.figure(figsize=(16,9))
for i in lst:
    plt.plot(reader[i],label=i)
#plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
plt.xlabel('Year')
plt.ylabel('some numbers')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0.)
plt.show()







