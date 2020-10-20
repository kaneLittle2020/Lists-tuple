def movement():
  movement = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return movement

def run():
  print(movement())

run()
--------------------------------------------------------------------------------
def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
   print("Moving...")
   direction = movements()
   print ("{} for {} steps".format(direction[0], direction[1]))
   print ("{} for {} steps".format(direction[2], direction[3]))
   print ("{} for {} steps".format(direction[4], direction[5]))
   print ("{} for {} steps".format(direction[6], direction[7]))

  
run()
---------------------------
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
-------------------------------
def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path



def run():
   print("Moving...")
   path = movements()
   for index in range(0, len(path),2):
    print("{} for {} steps".format(path [index] , path [index + 1 ]))





run()
-----------------------------------
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
-------------------?
def movements():
  path = ["Move Forward",  "Move Backward",  "Move Left", "Move Right"]
  return path

def menu():
  print ("please select a direction:")
  path = movements()

  for index in range (len(path)):
    print("{} : {}". format(index, path [index]))
    path_index = int (input())

    return path [path_index]

def run():
  route = []
  print ("Working out escape route...")
  for count in range (5):
    path = menu ()
    route.append(path)
    print ("escape route: {}".format (route))
    menu()





run()