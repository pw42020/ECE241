# -*- coding: utf-8 -*-
"""q5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KISwKnkEod7JpuSAG1LCFIeA6JEJUzKQ
"""

"""
UMass ECE 241 - Advanced Programming
Homework #2     Fall 2021
question5.py - 3 way merge sort

"""


## This is an example of code to merge two lists in a descending order
## You can directly call this function or write your own one

# The two lists "lefthalf" and "righthalf" are start from i and j
# The destination list "alist" start from the given position "pos"
# The function returns the number of comparisons during merge
def merge2List(alist, left,mid,right, i, j,k, pos):
    
    comparison = 0 # initial the comparison number as 0
    while i < len(left) and j < len(mid) and k < len(right): 
        if left[i] < mid[j] and right[k] > left[i]:#if first value of left is smallest
          alist[pos] = left[i]
          i += 1
          comparison +=1

        elif left[i] > mid[j] and right[k] > mid[j]: #if mid is the smallest value
          alist[pos] = mid[j]
          j += 1
          comparison +=1

        elif right[k] < left[i] and right[k] < mid[j]: #if right value is smallest
          alist[pos] = right[k]
          k += 1
          comparison += 1

        pos += 1

    while i<len(left) and j <len(mid): #solving down for last two lists
      if left[i]<mid[j]:
        alist[pos] = left[i]
        i+=1
      else:
        alist[pos] = mid[j]
        j+=1

      comparison += 1
      pos += 1
    
    while j<len(mid) and k <len(right): #solving down for last two lists
      if mid[j]<right[k]:
        alist[pos] = mid[j]
        j+=1
      else:
        alist[pos] = right[k]
        k+=1
      
      comparison += 1
      pos += 1
    
    while i<len(left) and k <len(right): #solving down for last two lists
      if left[i]<right[k]:
        alist[pos] = left[i]
        i+=1
      else:
        alist[pos] = right[k]
        k+=1
      
      comparison += 1
      pos += 1

    while i < len(left): # add the remained numbers in the left to alist
        alist[pos] = left[i]
        i = i + 1
        pos += 1

    while j < len(mid): # add the remained numbers in the mid to alist
        alist[pos]=mid[j]
        j=j+1
        pos += 1

    while k < len(right): # add the remained numbers in the right to alist
        alist[pos]=right[k]
        
        k=k+1
        pos += 1
        
    return comparison


## Implement 3 way merge sorting algorithm
## It takes a given list "alist" and return the number of comparison used
def mergeSort_3_way(alist):

    comparison = 0

    if len(alist)>2:
      third = len(alist)//3
      left = alist[:third]
      mid = alist[third:2*third]
      right = alist[2*third:]
      
      mergeSort_3_way(left)
      mergeSort_3_way(mid)
      mergeSort_3_way(right)

      comparison += merge2List(alist,left,mid,right,0,0,0,0)

      

    return comparison