
from typing import List

"""
Function rolling_average calculates the rolling (or moving) average of a
list of numerical values over a specified period.
"""
def rolling_average(values: List, period:int)-> List:
    rolling_averages = []
    
    for i in range(period, len(values)+1):
        average = sum(values[i-period:i]) / period
        rolling_averages.append(average)
    
    return rolling_averages