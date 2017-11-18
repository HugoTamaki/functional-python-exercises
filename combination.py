from functools import reduce
from person import Person

def total_letters(arr):
  letters_num = []

  for elem in arr:
    letters_num.append(len(elem))

  sum = 0
  for elem in letters_num:
    sum += elem

  return sum

def total_letters_x(arr, letter):
  names_with_letter = []

  for elem in arr:
    if letter in elem:
      names_with_letter.append(elem)

  letters_num = []
  for elem in names_with_letter:
    letters_num.append(len(elem))

  sum = 0
  for elem in letters_num:
    sum += elem

  return sum

def transform_objs_to_dic(arr, attributes):
  result = []

  for elem in arr:
    temp = {}
    for attr in attributes:
      temp[attr] = getattr(elem, attr)
    result.append(temp)

  return result
