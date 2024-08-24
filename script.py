from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = [left_stack, middle_stack, right_stack]


#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
for i in range(num_disks, 0, -1):
  #the loop will iterate from num_disks down to 1 and push each value onto left_stack
  left_stack.push(i) 
num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))
#Get User Input
def get_input():
  #create a choices variable and set it to equal to a list of first letters of the names of the stacks
    #[0] gets the first letter of the stack's name
  choices = [stacks.get_name()[0] for first_letter in stacks]
  while True:
    continue
        
#Play the Game
