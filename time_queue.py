'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Measure time for enqueue
'''

import time
import numpy as np
from buildexcel import BuildExcel
from datastructures import LinkedQueue

sizes = range(1000, 100001, 1000)

#Measure in nanoseconds
def time_queue_enqueue():
    """Measure time to enqueue"""
    results = []

    for n in sizes:
        q = LinkedQueue()

        for value in range(n):
            q.enqueue(value)

        start_time = time.perf_counter_ns()
        q.enqueue(n)
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])

    return np.array(results)

queue_enqueue_data = time_queue_enqueue()
BuildExcel(queue_enqueue_data, "queue_enqueue_timing.xlsx", "Queue Enqueue Timing")