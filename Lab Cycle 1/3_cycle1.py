# -*- coding: utf-8 -*-
"""3_cycle1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BmjBPJ1rtwGSEXbm3SKrlSOZWeELeB4T
"""

# Develop a program to read the employee's name, code, and basic pay
# and calculate the gross salary, deduction, and net salary according to
# the following conditions. Define a function to find each of the
# components. Finally, generate a payslip.

# Gross Salary (GS) : BP + DA + HRA + MA
# Deduction (D): PT + PF + IT
# Net Salary = GS – D



name=str(input("Enter employee's name : "))        # reading employees name
code=str(input("Enter employee's code : "))        # reading employees code
bp=float(input("Enter employee's basic pay :"))    # reading employees basic pay
  
def salary():                                      # function to calculate net salary
  if(bp>50000):
    gs=bp+(0.25*bp)+(0.11*bp)+7000                 # using else if 
    d=80+(0.12*bp)+(0.20*bp)                       # for calculating net salary in different range
    net_slry=gs-d                                  
  elif(30000<bp<50000):
    gs=bp+(bp*0.11)+(bp*0.075)+5000
    d=60+(0.11*bp)(0.11*bp)
    net_slry=gs-d
  elif(10000<bp<30000):
    gs=bp+(0.075*bp)+(0.05*bp)+2500
    d=60+(0.08*bp)+0
    net_slry=gs-d
  else:
    gs=bp+(0.05*bp)+(0.025*bp)+500
    d=20+(0.08*bp)+0
    net_slry=gs-d

  return net_slry  

print("Eployee's name : ",name)                  # printing payslip
print("Employee's code : ",code)
print("Employee's basic pay : ",bp)
print("Employee's Net Salary : ",salary())

