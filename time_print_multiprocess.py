'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Measure time for printing all entrys using get entry
'''

import time
from buildexcel import BuildExcel
from datastructures import LinkedList
from tqdm import tqdm
from multiprocessing import Pool, set_start_method

def process_dataset(n):
	ll = LinkedList()

	for value in range(n):
		ll.insert(ll.length(), value)

	entries = []
	start_time = time.perf_counter()
	for i in range(ll.length()):
		entries.append(f"Element {i}: {ll.get_entry(i)}")
	end_time = time.perf_counter()

	elapsed_time = end_time - start_time
	return n, elapsed_time, entries

if __name__ == "__main__":
	set_start_method("spawn", force=True)
	sizes = range(1000, 100001, 1000)

	with Pool() as pool:
		results = list(tqdm(pool.imap(process_dataset, sizes), total=len(sizes), desc='Processing datasets'))

	timing_results = [(size, time_elapsed) for size, time_elapsed, _ in results]

	BuildExcel(timing_results, "print_all_elements_timing.xlsx", "Print All Elements", time_unit='s')

	for size, time_elapsed, entries in results:
		for entry in entries:
			print(entry)

	#return results
