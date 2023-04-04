#Answer for Question 2 (5 points) in the Spring23 MidTerm Review question 




def csv_reader_with_generator(file):
    result = []
    for line in file:
        result.append(line)
        yield result




















# def csv_reader_with_generator(file):
#     result = []
#     for row in file:
#         result.append(row)
#        yield result


import time

file = open("LargeCSVFile.csv", "r")
csv_gen = csv_reader_with_generator(file)
row_count = 0
start_time = time.perf_counter_ns()
for row in csv_gen:
    row_count += 1
total_time = time.perf_counter_ns() - start_time
print(f"Row count is {row_count}")
print(total_time / 1e9)
file.close()

import psutil

# Getting % usage of virtual_memory ( 3rd field)
print('Total RAM memory used:', psutil.virtual_memory()[3])
