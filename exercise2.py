from copy import deepcopy

bands = [{'name': 'Hell Riders', 'country': 'UK', 'active': False},
         {'name': 'Dragons Crown', 'country': 'Germany', 'active': False},
         {'name': 'Crystal Illusion', 'country': 'Spain', 'active': True}]

def change_country(elem):
  elem['country'] = 'Canada'

def set_active(elem):
  elem['active'] = True

def set_name_length(elem):
  elem['name_length'] = len(elem['name'])

def pipeline_formatter(functions, items):
  def execute(functions, elem):
    list(map(lambda x: x(elem), functions))

  data = deepcopy(items)
  list(map(lambda x: execute(functions, x), data))
  return data

formatted = pipeline_formatter(
  [
    change_country,
    set_active,
    set_name_length
  ],
  bands
)

print(formatted)

