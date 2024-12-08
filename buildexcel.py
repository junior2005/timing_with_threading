'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Use pandas to put data in excel
'''

import pandas as pd

def BuildExcel(data, file, sheet_name, time_unit='ns'):
    df = pd.DataFrame(data, columns=["Size", f"Time ({time_unit})"])
    df.to_excel(file, index=False, sheet_name=sheet_name)