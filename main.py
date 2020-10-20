#function with no parameters
def steps():
  likelihoods = []
  likelihoods.append (("steps 1", 50))
  likelihoods.append (("steps 2", 38))
  likelihoods.append (("steps 3", 27))
  likelihoods.append (("steps 4", 99))
  likelihoods.append (("steps 5", 4))
  return likelihoods

def run():
  likelihoods = steps()
  good_steps = []
  bad_steps = []

  for likelihood in likelihoods:
    if (likelihood[1] >=50):
      bad_steps.append(likelihood)
  else:
      good_steps.append(likelihood)

print ("Good step; {}, Bad steps: {}".format(len(good_steps), len (bad_steps)))


  

  



