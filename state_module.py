from country_module import  Country_Processor
import pandas as pd

class State_Processor (Country_Processor):
 
    def printing(self):
        summary = self.df.groupby(['state']).sum()
        print(summary)
