'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Measure time adding to max heap
'''

import time
import numpy as np
from buildexcel import BuildExcel
from datastructures import MaxHeap

sizes = range(1000, 100001, 1000)

#Measure in nanoseconds
def time_add_max_heap():
	"""Measure time to add to max heap"""
	results = []

	for n in sizes:
		heap = MaxHeap()

		for value in range(n):
			heap.add(value)

		start_time = time.perf_counter_ns()
		heap.add(n + 1)
		end_time = time.perf_counter_ns()

		elapsed_time = end_time - start_time
		results.append([n, elapsed_time])
	return np.array(results)

max_heap_add_data = time_add_max_heap()
BuildExcel(max_heap_add_data, "heap_add_timing.xlsx", "Heap Add timing")