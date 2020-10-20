def movements():
  path = ["Move Forward",  "Move Backward",  "Move Left", "Move Right"]
  return path

def menu():
  print ("please select a direction:")
  path = movements()

  for index in range (len(path)):
    print("{} : {}". format(index, path [index]))

def run():
   menu()





run()