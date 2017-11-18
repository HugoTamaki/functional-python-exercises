
def filter_odds(arr):
  return list(filter(lambda elem: elem % 2 == 0, arr))

def filter_dic_with(attr, arr):
  return list(filter(lambda elem: attr in elem, arr))

def filter_array_with_more_than(num, arr):
  return list(filter(lambda elem: len(elem) > num, arr))
