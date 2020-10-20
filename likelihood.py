def likelihood():
  #tuple
  likelihoods = (50, 38,27, 99, 4)
  return min(likelihoods)

def run():
  min_likelihood = likelihood ()
  print ("minimum lilelihood of falling: {} % ".format (min_likelihood) )


run ()
----------------