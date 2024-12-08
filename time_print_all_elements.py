'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Measure time for printing all entrys using get entry
'''

import time
import csv
from datastructures import LinkedList

sizes = range(1000, 100001, 1000)

#Measure in seconds
def time_print_all():
	"""Measure time to print all elements in a linked list"""
	results = []

	for n in sizes:
		
		ll = LinkedList()

		for value in range(n):
			ll.insert(ll.length(), value)

		start_time = time.perf_counter()
		
		for i in range(ll.length()):
			print(ll.get_entry(i))
		end_time = time.perf_counter()    

		elapsed_time = end_time - start_time
		results.append([n, elapsed_time])

	return results

def save_data(data, file_name):
	with open(file_name, mode='w', newline="") as file:
		writer = csv.writer(file)
		writer.writerow(["Size", "Time (s)"])
		writer.writerows(data)

print_all_data = time_print_all()
save_data(print_all_data, "print_all_elements_timing.csv")
