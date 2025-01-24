import random

# create list of 100 random numbers from 0 to 1000
list_random = [random.randrange(0, 1000) for i in range(100)]
print(list_random)

# sort list from min to max (without using sort())
def sort_list_items(list_random):
    n = len(list_random)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_random[j] > list_random[j + 1]:
                list_random[j], list_random[j + 1] = list_random[j + 1], list_random[j]
    return list_random


list_sorted = sort_list_items(list_random)
print(list_sorted)

# calculate average for even and odd numbers
list_sorted_even = [i for i in list_sorted if i % 2 == 0]
list_sorted_odd = [i for i in list_sorted if i % 2 != 0]
average_even = sum(list_sorted_even) / len(list_sorted_even)
average_odd = sum(list_sorted_odd) / len(list_sorted_odd)

print(f'Average for even numbers: {average_even}')

print(f'Average for odd numbers: {average_odd}')




