def recursion():
  print("Hello world")
  try:
    recursion()
  except RecursionError:
    print("Recursion limit reached")
    pass
  # Python has a default recursion limit of 1000
  # Base case is where you want to stop calling the recursive function

recursion()

def recursion_with_limit(count):
  print("Hello world")
  count += 1
  if count < 500:
    recursion_with_limit(count)
  else:
    print("Recursion limit reached")
    pass

count = 0 
recursion_with_limit(count)