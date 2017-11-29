
def make_pretty(func):
  def inner():
    print("I got decorated!")
    func()

  return inner

def ordinary():
  print("I am ordinary!")

ordinary = make_pretty(ordinary)

ordinary()

call_count = 0

def count(func):
  def inner():
    global call_count
    call_count += 1
    func()

  return inner

@count
def message():
  print("Hello")

message()
message()
message()
message()
message()

print(call_count)
