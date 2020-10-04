from processor_module import Processor
import pandas as pd

class Country_Processor (Processor):
    df = pd.DataFrame()
    
    def __init__(self, url):
        self.df = pd.read_csv(url)
        
    def printing(self):
        print("Total number of cases in the US:")
        print(self.df['cases'].sum())
        print("Total number of deaths in the US:")
        print(self.df['deaths'].sum())
