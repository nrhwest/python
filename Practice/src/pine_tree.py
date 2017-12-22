'''
Create a pine tree

    #
   ###
  #####
 #######
#########
    #
'''

tree_height = input('How tall is the tree?  ') # ask user for tree height
tree_height = int(tree_height) # converts input to int
spaces = tree_height - 1 # gets the starting spaces for top of tree
hashes = 1 # one hash to start
stump_spaces = tree_height - 1 # save stump spaces for later

while tree_height != 0: # make sure right number of rows are printed
    for i in range(spaces): # print the spaces
        print(' ', end="")

    for i in range(hashes): #print the hashes, end="" stops the printing
            print('#', end="")
    print()  # Prints a new line

    spaces -= 1 # decrement spaces by 1
    hashes += 2 # increment hashes by 2
    tree_height -= 1 # decrement tree_height by 1

# print last stump
for i in range(stump_spaces):
    print(' ', end="")
print('#')
