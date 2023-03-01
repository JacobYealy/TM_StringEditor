import sys

##############################################################
#  Turing Machine String Computation in Python               #
#  Jacob Yealy                                               #
#                                                            #
# The purpose of this program is to take an input TM.txt     #
# file and run it against a user input string.               #
##############################################################
###
# Reads the TM.txt file and stores neccessary variables.
###
def main():
  print("Please input a text file Turing Machine.")
  try:
      file = open("TM.txt", "r") # Open the Turing Machine file
  except:
      sys.exit("You must enter a TM.txt file")


# Line 1 of TM.txt: Number of states
  global states
  states = int(file.readline())
  print("Your Turing Machine has " + str(states) + " states")

# Line 2: Halting states
  global halt
  halt = int(file.readline())
  if halt == 0 :
    sys.exit("Halting on state 0 will produce no change.")
  print("Your halting state is " + str(halt))

# Line 3+ : Transitions (2d array)
  global transitions
  transitions = list()
  for line in file: # Goes through the rest of the file
      transitions.append(line.split()) # splits for list
      transitions[-1][0] = int(transitions[-1][0]) # State transition
      transitions[-1][4] = int(transitions[-1][4]) # State transition
      print("Transition: " + line, end = '')
  print()

  # Allows you to rerun code
  run = 1
  while(int (run) == 1) :
    stringComputation()
    run = input("Type 1 to go again or 0 to quit: ")



###
# Performs the steps of the turing machine and prints the resulting string.
###
def stringComputation():
      # Get user input as string and converts to list
  global tape
  tape = input("Please input the tape you would like to process through the TM: ")
  tape = [char for char in tape]

  global head
  global currentState
  global currentTrans
  global nextState
  head = 0
  currentState = 0
  currentTrans = -1
  while(currentState != halt) :
    printMachineState()
    
    i = 0
    #Figure out where to go
    while(i < len(transitions)) : # value to read
      if(transitions[i][0] ==  currentState and transitions[i][1] == tape[head]) :
        currentTrans = i
      i+= 1
    if(currentTrans == -1) :
      sys.exit("We're stuck")
    else :
      tape[head] = transitions[currentTrans][2] #currentTrans[2] is what we want to write
    
      
      shift = transitions[currentTrans][3] # direction shift
      if (shift == 'R') :
        head += 1
      elif (shift == 'L') :
        head -= 1
      else :
        print(shift)
        sys.exit("You can only shift right or left (R or L)")
    
      nextState = transitions[currentTrans][4]
      currentState = nextState
      if(head >= len(tape)) :
        tape.append('_')
      elif(head <= -1) :
        tape.insert(0, '_')
        head = 0;
  print("Halt state reached.")
  printMachineState()

def printMachineState():
  print("Your current state is " + str(currentState) + " the tape is ", end = '')
  for i in range(0, len(tape)) :
    if(i == head) :
      print(">", end = '')
    print(tape[i], end = '') # Magical no new line
  print()
  
main()
