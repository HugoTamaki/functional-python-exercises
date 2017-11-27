
def callback(status, success, failure):
  if status == 200:
    return success()
  else:
    return failure()
