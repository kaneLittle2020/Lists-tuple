def get_fruits():
  fruits = []
  for count in range (5):
    print ("please enter fruit:")
    fruits.append(input())

  print("Your fruits are: {}".format(fruits))

get_fruits ()
-----------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]

#adds to the end of the list
fruits.append("dragon fruit")
fruits.remove("dragon fruit")

# Display the first item i.e. apple
print(fruits[0])

# Update the second item i.e. replace banana with berry
fruits[1] = "berry"

# Remove the third item i.e. removes cherry
del fruits[2]

print("Your fruits are: {}".format(fruits))