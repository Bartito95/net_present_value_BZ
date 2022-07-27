import numpy as np
from classes import NPV
   
start = 0

while start == 0:
    per = float(input("Please input percentage of investment(%): "))
    y = int(input("Please confirm how many years would you like to invest: "))
    capital = float(input("What is beginnig capital? "))
    
    npv = NPV(percentage = per, years = y)
    cf = npv.summarize()
    
    check = cf - capital
    
    if check >= 0:
        print(f"\nNPV ({round(check,2)}) is above 0. You should invest!")
        start += 1
    else:
        print(f"\nNPV ({round(check,2)}) is below 0. Do not invest!")
        start += 1