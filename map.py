
def len_map(arr):
  response = []
  for elem in arr:
    response.append(len(elem))
  return response

def odd_even_map(arr):
  response = []
  for elem in arr:
    if elem % 2 == 0:
      response.append('par')
    else:
      response.append('impar')
  return response

def objects_to_dic(arr):
  response = []
  for elem in arr:
    response.append(
      {
        'name': elem.name,
        'type': elem.type
      }
    )
  return response

def dic_to_string(arr):
  response = []
  for elem in arr:
    response.append("{0} is a {1}".format(elem['name'], elem['type']))
  return response