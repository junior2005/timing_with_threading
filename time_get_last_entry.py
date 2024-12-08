'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Measure time for getting last entry
'''
import time
import numpy as np
from buildexcel import BuildExcel
from datastructures import LinkedList
from tqdm import tqdm

sizes = range(1000, 100001, 1000)

#Measure in seconds
def time_get_last_entry():
    """Measure time to get last entry in linked list"""
    results = []
 
    for n in tqdm(sizes, desc='Data sizes', total=len(sizes)):
        ll = LinkedList()
        for value in range(n):
            ll.insert(ll.length(), value)

        start_time = time.perf_counter()
        ll.get_entry(ll.length() - 1)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])
    return np.array(results)

get_last_entry_data = time_get_last_entry()
BuildExcel(get_last_entry_data, "get_last_entry_timing.xlsx", "Get Last Entry Timing", time_unit='s')


