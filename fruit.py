def get_fruits():
  fruits = []
  for count in range (5):
    print ("please enter fruit:")
    fruits.append(input())

  print("Your fruits are: {}".format(fruits))

get_fruits ()