
bands = [{'name': 'Hell Riders', 'country': 'UK', 'active': False},
         {'name': 'Dragons Crown', 'country': 'Germany', 'active': False},
         {'name': 'Crystal Illusion', 'country': 'Spain', 'active': True}]

def format_bands(bands):
  for band in bands:
    band['country'] = 'Canada'
    band['active'] = True
    band['name_length'] = len(band['name'])

format_bands(bands)

print bands