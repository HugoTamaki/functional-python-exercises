
def len_map(arr):
  return list(map(len, arr))

def odd_even_map(arr):
  return list(map(lambda elem: 'par' if elem % 2 == 0 else 'impar', arr))

def objects_to_dic(arr):
  return list(map(lambda elem: {'name': elem.name, 'type': elem.type}, arr))

def dic_to_string(arr):
  return list(map(lambda elem: "{0} is a {1}".format(elem['name'], elem['type']), arr))