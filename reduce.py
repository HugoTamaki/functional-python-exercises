from functools import reduce
import operator

def sum_of_integers(arr):
  sum = 0
  for elem in arr:
    sum += elem

  return sum

def dic_from_double_array(arr):
  response = {}
  for elem in arr:
    response[elem[0]] = elem[1]
  return response