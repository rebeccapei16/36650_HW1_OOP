from state_module import State_Processor
import pandas as pd

class County_Processor (State_Processor):
 
    def printing(self):
        summary = self.df.groupby(['county']).sum()
        print(summary)