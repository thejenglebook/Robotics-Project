#!/usr/bin/python

# Demo of some programming concepts in Python
# Initial code written by: Jason Ziglar <jpz@vt.edu>
# Extended and modified by: Thomas Schluszas <tms2874@vt.edu>


# Define a function which computes the harmonic series
def harmonic_series(num_terms):
  '''Function which computes some number of terms from the harmonic series.
  num_terms: the number of terms to add together.
  returns: The value computed'''
  #Create variable to store result, set to some initial value
  value = 0
  #Only runs program if num_terms is not 0 or negative. It it is, value will remain 0.
  if num_terms > 0:
    #range produces a sequence of numbers, [0, num_terms), and executes the loop
    # with ii set to each value
    for ii in range(num_terms):
      #Set value to the value plus the next term
      # Note: Computers start counting at 0, so we have to add 1 to be safe
      value = value + (1.0 / (ii + 1))

  # Return the value to whomever called this function
  return value

# Define a function that estimates pi
def pi_estimate(num_terms):
  '''Function estimates pi using a specified number of terms.
  num_terms: the number of terms used during the estimation.
  returns: The value computed'''
  #Create variable to store result, set to some initial value
  value = 0
  #Only runs program if num_terms is not 0 or negative. It it is, value will remain 0.
  if num_terms > 0:
    #range produces a sequence of numbers, [0, num_terms), and executes the loop
    # with ii set to each value
    for ii in range(num_terms):
      #Set value to the value plus the next term
      # Note: Computers start counting at 0, so we have to add 1 to be safe
      value = value + (1.0 / ((ii + 1)**2))
    #function yields pi^2/6, so we need to adjust our value to get actual estimation of pi
    value = (value * 6)**0.5

  # Return the value to whomever called this function
  return value

def harmonic_series_while(num_terms):
  '''Function which computes some number of terms from the harmonic series, using a while loop.
  num_terms: the number of terms to add together.
  returns: The sum of the first n terms of the series'''

  #Create variable to store summation
  value = 0
  #A counter to keep track of how many terms have been computed
  counter = 0
  #Only runs program if num_terms is not 0 or negative. It it is, value will remain 0.
  if num_terms > 0:
    # This will run until "counter <= num_terms" returns a false statement
    while counter < num_terms:
      value = value + (1.0 / (counter + 1))
      # Very important - while runs until it sees false, so we have to make sure
      # the test will eventually fail
      counter = counter + 1

  # Return value
  return value
#this statement allows file to be used as module without running the main code below
if __name__ == "__main__":
  #Starting here, the program begins execution, since the previous statements were describing functions, but not actually calling them
  # Print a welcome
  print "Welcome to a simple harmonic series approximation program."

  #establish an arbitrary variable to start a while loop on
  request = 4.0
  #while loop ensures that entry is a valid value
  while request != 0.0 and request != 1.0 and request !=2.0 and request !=3.0:
    #Ask the user to select a function or enter 0 to end program
    request = float(raw_input("Enter 0 to exit program. Enter 3 to estimate pi. Otherwise, select which function to use: 1) For loop 2) While loop: "))
    #chastises user if input is not valid
    if request != 0.0 and request != 1.0 and request != 2.0 and request !=3.0:
      print "That's not a valid input! Do it right!"

  #Convert that input to an integer
  request = int(request)
  #ignores last part of program if 0 is entered
  if request != 0:
    #takes next input as a float, so it can be converted to an integer
    iterations = float(raw_input("How many terms should I use? "))
    #converts iterations float into an integer
    iterations = int(iterations)

  # Test input
  if request == 1:
    # Get value form function
    result = harmonic_series(iterations)
    # Print using a technique known as string interpolation. %s means "take the next value after the string and insert as a string"
    # So it will look at the list of values after the % and grab the next (only) one
    # For more details, look here: https://docs.python.org/2/library/stdtypes.html#string-formatting
    print "For loop produces: %s" % result
  if request == 2:
    # Same as previous statement, but notice you don't have to store a value in a variable before using it, if it makes sense.
    print "While loop produces %s" % harmonic_series_while(iterations)
  if request == 3:
    #outputs value from pi_estimate
    print "Pi estimation function produces %s" % pi_estimate(iterations)

