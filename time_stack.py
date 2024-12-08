'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Measure time for popping single item and all items
'''

import time
import numpy as np
from buildexcel import BuildExcel
from datastructures import Stack

sizes = range(1000, 100001, 1000)

#Measure in nanoseconds
def time_stack_pop():
    """Measure time for popping 1 item"""
    results = []
    for n in sizes:
        s = Stack()
        for value in range(n):
            s.push(value)

        start_time = time.perf_counter_ns()
        s.pop()
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time

        results.append([n, elapsed_time])

    return np.array(results)

#Measure in seconds
def time_stack_pop_all():
    """Measure time to pop all elements from stack"""
    results = []

    for n in sizes:
        s = Stack()
        for value in range(n):
            s.push(value)

        start_time = time.perf_counter_ns()
        while not s.is_empty():
            s.pop()
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])

    return np.array(results)

stack_pop_data = time_stack_pop()
BuildExcel(stack_pop_data, "stack_pop_timing.xlsx", "Stack Pop Timing")

stack_pop_all_data = time_stack_pop_all()
BuildExcel(stack_pop_all_data, "stack_pop_all_timing.xlsx", "Stack Pop All Timing")