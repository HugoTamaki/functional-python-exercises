
def callback(status, success, failure):
  if status == 200:
    return "Success!"
  else:
    return "Failure!"
