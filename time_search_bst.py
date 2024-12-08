'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Measure time to search for value in bst
'''
import random
import time
import numpy as np
from buildexcel import BuildExcel
from datastructures import BinarySearchTree

sizes = range(1000, 100001, 1000)

#Time in nanoseconds
def time_seach_bst():
	"""Measure time to search an element in the bst"""
	results = []

	for n in sizes:
		bst = BinarySearchTree()

		random_vals = random.sample(range(1_000_000), n)
		for value in random_vals:
			bst.add(value)

		target = random.choice(random_vals)

		start_time = time.perf_counter_ns()
		bst.search(target)
		end_time = time.perf_counter_ns()

		elapsed_time = end_time - start_time
		results.append([n, elapsed_time])

	return np.array(results)

search_bst_data = time_seach_bst()
BuildExcel(search_bst_data, "search_bst_timing.xlsx", "Search BST Timing", time_unit='s')

