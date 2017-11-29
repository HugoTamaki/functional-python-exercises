
def my_map(func, list):
  result = []

  for item in list:
    result.append(func(item))

  return result