import numpy as np

def values_entering():
    try:
        values = int(input())
        return values
    except:
        print("Use integer!")
        return values_entering()

class NPV:
    def __init__(self, percentage, years):
        self.percentage = percentage
        self.years = years
    
    def NPV_rates(self):
        year = list(range(1, self.years + 1))
        rates = [round((1 / (1 + (self.percentage / 100)) ** y),5) for y in year]
        return rates
    
    def entering_values(self):
        values = [values_entering() for _ in list(range(1, self.years + 1))]
        return values
    
    def final(self):
        rates = self.NPV_rates()
        val = self.entering_values()
        added = [round((rates[x] * val[x]),5) for x in range(len(val))]
        return added
    
    def summarize(self):
        table = np.array(self.final())
        summ = np.sum(table)
        print(f"Cash flow: {tuple(np.round(table,2))}.")
        return summ