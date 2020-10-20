def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def menu():
  print ("please select a direction:")
  route = movements()
  for index in range (len(route)):
    print("{} : {}". format(index, route [index]))

def run():
   print("Moving...")
   path = movements()
   print ("{} for {} steps".format(path[0], path[1]))
   print ("{} for {} steps".format(path[2], path[3]))
   print ("{} for {} steps".format(path[4], path[5]))
   print ("{} for {} steps".format(path[6], path[7]))




menu()
run()