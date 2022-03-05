# -*- coding: utf-8 -*-
"""4_cycle1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YnfMG3HHRYHF0wp5JGivPeapo9tm6qr8
"""

# Develop a program to perform the following task:
#  a. Define a function to check whether a number is happy or not.
#  b. Define a function to print all happy numbers within a range.
#  c. Define a function to print first N happy numbers.


num=int(input("Enter a positive integer : "))  # reading a positive integer

def hppy_not(num):                             # function to check the number happy or not
  is_happy = False
  n=0
  cnt=0
  while(n<=100):
    temp=num
    sum=0
    while(temp>0):
     temp=temp//10
     cnt=cnt+1
    for i in range(1, cnt+1):
      x=num%10
      sum=sum+(x**2)
      num=num//10
    if(sum==1):
      is_happy = True
      break
    else:
     n=n+1
     num=sum
     
     
  return is_happy
if hppy_not(num)==True:        # printing happy number or not by checking returned boolian value
  print("Happy number")
else:
  print("Not a Happy Number")         


def hppy_range():             # function to print happy number with in a range
  lower_range=int(input("Enter lower range : "))
  upper_range=int(input("Enter higher range : "))
  for i in range(lower_range, upper_range+1):
    if hppy_not(i)==True:
      print(i)

hppy_range()                  # calling function 

def hppy_n():                 # function to print first n happy number
  no_off=int(input("Enter N : "))
  count=1
  i=0
  while(count<=no_off):
    if hppy_not(i)==True:
      print(i)
      count=count+1
    i=i+1    

hppy_n()                      # calling function