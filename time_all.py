import stack
import linkedqueue
import linkedlist
import maxheap
import bst

import random
import numpy as np
import pandas as pd
import time

#Must install pandas, numpy, and openpyxl (for writing excel files)
total_start = time.perf_counter()

sizes = range(1000, 100001, 1000)

#Measure in nanoseconds
def time_stack_pop():
    """Measure time for popping 1 item"""
    results = []

    for n in sizes:
        s = stack.Stack()
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
        s = stack.Stack()
        for value in range(n):
            s.push(value)

        start_time = time.perf_counter()
        while not s.is_empty():
            s.pop()
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])

    return np.array(results)

#Measure in nanoseconds
def time_queue_enqueue():
    """Measure time to enqueue"""
    results = []

    for n in sizes:
        q = linkedqueue.LinkedQueue()

        for value in range(n):
            q.enqueue(value)

        start_time = time.perf_counter_ns()
        q.enqueue(n)
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])

    return np.array(results)

#Measure in seconds
def time_get_last_entry():
    """Measure time to get last entry in linked list"""
    results = []

    for n in sizes:
        ll = linkedlist.LinkedList()
        for value in range(n):
            ll.insert(ll.length(), value)

        start_time = time.perf_counter()
        ll.get_entry(ll.length() - 1)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])
    return np.array(results)

#Measure in seconds
def time_print_all():
    """Measure time to print all elements in a linked list"""
    results = []

    for n in sizes:
        ll = linkedlist.LinkedList()
        for value in range(n):
            ll.insert(ll.length(), value)

        start_time = time.perf_counter()
        for i in range(ll.length()):
            print(ll.get_entry(i))
        end_time = time.perf_counter()    

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])

    return np.array(results)

#Measure in nanoseconds
def time_add_max_heap():
    """Measure time to add to max heap"""
    results = []

    for n in sizes:
        heap = maxheap.MaxHeap()

        for value in range(n):
            heap.add(value)

        start_time = time.perf_counter_ns()
        heap.add(n + 1)
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])
    return np.array(results)

#Time in seconds
def time_seach_bst():
    """Measure time to search an element in the bst"""
    results = []

    for n in sizes:
        tree = bst.BinarySearchTree()

        random_vals = random.sample(range(1_000_000), n)
        for value in random_vals:
            tree.add(value)

        target = random.choice(random_vals)

        start_time = time.perf_counter()
        tree.search(target)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        results.append([n, elapsed_time])

    return np.array(results)

def make_excel(data, file, sheet_name, time_unit='ns'):
    df = pd.DataFrame(data, columns=["Size", f"Time ({time_unit})"])
    df.to_excel(file, index=False, sheet_name=sheet_name)

stack_pop_data = time_stack_pop()
make_excel(stack_pop_data, "stack_pop_timing.xlsx", "Stack Pop Timing")

stack_pop_all_data = time_stack_pop_all()
make_excel(stack_pop_all_data, "stack_pop_all_timing.xlsx", "Stack Pop All Timing", time_unit='s')

queue_enqueue_data = time_queue_enqueue()
make_excel(queue_enqueue_data, "queue_enqueue_timing.xlsx", "Queue Enqueue Timing")

get_last_entry_data = time_get_last_entry()
make_excel(get_last_entry_data, "get_last_entry_timing.xlsx", "Get Last Entry Timing", time_unit='s')

print_all_data = time_print_all()
make_excel(print_all_data, "print_all_elements_timing.xlsx", "Print All Elements", time_unit='s')

max_heap_add_data = time_add_max_heap()
make_excel(max_heap_add_data, "heap_add_timing.xlsx", "Heap Add timing")

search_bst_data = time_seach_bst()
make_excel(search_bst_data, "search_bst_timing.xlsx", "Search BST Timing", time_unit='s')


final_end = time.perf_counter()

totaltime = final_end - total_start
print(f"Total time: {totaltime}")