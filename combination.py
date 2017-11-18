from functools import reduce
from person import Person

def total_letters(arr):
  return reduce(
    lambda sum, elem: sum + elem,
    list(map(len, arr)),
    0
  )

def total_letters_x(arr, letter):
  return reduce(
    lambda sum, elem: sum + elem,
    list(
      map(
        len,
        filter(lambda elem: letter in elem, arr)
      )
    )
  )

def transform_objs_to_dic(arr, attributes):
  def assign(hash, attribute, obj):
    hash[attribute] = getattr(obj, attribute)
    return hash

  def transform_to_dic(obj, attributes):
    return reduce(
      lambda hash, attribute: assign(hash, attribute, obj),
      attributes,
      {}
    )

  return list(map(lambda elem: transform_to_dic(elem, attributes), arr))
