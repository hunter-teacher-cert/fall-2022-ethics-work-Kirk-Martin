#Kirk Martin
#Ethics Class
#Sept 27th, 2022
# Week 4 regular expressions


import re


def find_name(line):
 
    #First Name Last Name Expression Works
    pattern=r'[A-Z]\w*\s[A-Z]\w*'
    result = re.findall(pattern,line)

     
    #Mr. Last attempt at expression
    pattern=r'Mr.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    #Dr. and Last name appear in list.
    pattern=r'Dr.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    #Mrs. Last expression
    pattern=r'Mrs.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    #Ms. F. Last expression
    pattern=r'Ms.\s[A-Z]\.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    #Mrs. F. Last name expression
    pattern=r'Mrs.\s[A-Z]\.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)
    return result

f = open("Names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
