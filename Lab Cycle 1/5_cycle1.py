# -*- coding: utf-8 -*-
"""5_cycle1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QX3dJxp9PeuuJiSwz-0yK9_T8Mat5gdR
"""

#Develop a program to read a string and perform the following operations:
#  • Print all possible substrings.
#  • Print all possible substrings of length K.
#  • Print all possible substrings of length K with N distinct characters.
#  • Print substring(s) of maximum length with N distinct characters.
#  • Print all palindrome substrings.


strg=str(input("Enter a string : "))  # reading a string

def substring():                      # function to print substrings
  for i in range(0,len(strg)+1):
    for j in range(i+1,len(strg)+1):
      sub=strg[i:j]
      print(sub)



def sub_length():                     # function to print substring with specific length
  length=int(input("Enter the length substring : "))
  for i in range(0,len(strg)+1):
    for j in range(i+1,len(strg)+1):
      sub=strg[i:j]
      if(len(sub)==length):
        print(sub)


def sub_length_distinct():                             # function to print substring with specific length and 
  length=int(input("Enter the length substring : "))   # specific distinct charector
  distinct=int(input("Enter the number of distinct characters : "))
  for i in range(0,len(strg)+1):
    for j in range(i+1,len(strg)+1):
      sub=strg[i:j]
      if(len(sub)==length and len(set(sub))==distinct):
        print(sub)



def sub_max_distinct():                                # function to print substring with specific distinct charector
  ls=[]                                                # with maximum length
  distinct=int(input("Enter the number of distinct characters : "))
  for i in range(0,len(strg)+1):
    for j in range(i+1,len(strg)+1):
      sub=strg[i:j]
      if(len(set(sub))==distinct):
        ls.append(sub)
  print(ls)      
  max_leng=len(max(ls, key=len))
  for k in range(len(ls)):
    if(len(ls[k])==max_leng):
      print(ls[k])

def sub_pallian():                                     # function to print palliandrome sub strings 
  for i in range(0,len(strg)+1):
    for j in range(i+1,len(strg)+1):
      sub=strg[i:j]
      rev=sub[::-1]
      if(sub==rev):
        print(sub)


substring()
sub_length()
sub_length_distinct()
sub_max_distinct()
sub_pallian()