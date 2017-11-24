from functools import reduce
from person import Person

def average_height(people):
  heights = list(map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people)))

  if len(heights) > 0:
    average_height = reduce(lambda acc, x: acc + x, heights, 0) / len(heights)
    return average_height

  return 0

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
