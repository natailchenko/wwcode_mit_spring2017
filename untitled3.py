# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:28:56 2017

@author: Nataliia
"""
annual_salary= float (input("What is your annual salary?"))
portion_saved=float(input("How much are you going to save from your salary   (decimal)?"))
total_cost= float(input("What is the price of your dream house?"))

portion_down_payment= total_cost*0.25
current_savings=0 
portion_saved2= annual_salary*portion_saved 

months=0
while current_savings < portion_down_payment:
      current_savings+=(portion_saved2+current_savings *0.04)/12 
      months= months + 1


print (months)
