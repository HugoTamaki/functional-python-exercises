
def filter_odds(arr):
  response = []
  for elem in arr:
    if elem % 2 == 0:
      response.append(elem)
  return response

def filter_dic_with(attr, arr):
  response = []
  for elem in arr:
    if attr in elem:
      response.append(elem)

  return response

def filter_array_with_more_than(num, arr):
  response = []
  for elem in arr:
    if len(elem) > num:
      response.append(elem)
  return response