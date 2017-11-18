from functools import reduce

def sum_of_integers(arr):
  return reduce(
    lambda sum, elem: sum + elem,
    arr,
    0
  )

def dic_from_double_array(arr):
  def assign(hash, elem):
    hash[elem[0]] = elem[1]
    return hash

  return reduce(
    lambda sum, elem: assign(sum, elem),
    arr,
    {}
  )
