import pandas as pd
from country_module import Country_Processor
from state_module import State_Processor
from county_module import County_Processor

print("Please choose the datasets that you want to display")
print("Type in 'us', 'state' or 'county' ")
input1 = input()

if input1 != "us" and input1 != "state" and input1 != "county":
    print("cannot read input")
else:
    if input1 == "us":
        processor =  Country_Processor('data/us.csv')
        processor.printing()
    elif input1 == "state":
        processor =  State_Processor('data/us-states.csv')
        processor.printing()
    else: 
        processor =  County_Processor('data/us-counties.csv')
        processor.printing()
