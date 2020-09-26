import time

start_time = time.time()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        def fn(value, curr):
            if value >= curr.value: #if same value, go right per test?
                #if right child is None
                if curr.right is None:
                    curr.right = BSTNode(value)
                    return
                else:
                    fn(value, curr.right)
            elif value < curr.value:
                # if left child is None
                if curr.left is None:
                    curr.left = BSTNode(value)
                    return
                else:
                    fn(value, curr.left)
        fn(value, self) # recursive call

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def fn(value, curr):
            #check if self.value is target
            if value == curr.value:
                #if yes, return True 
                return True
            elif value > curr.value:
                # go right
                if curr.right is None:
                    return False
                else:
                    return fn(value, curr.right)
            elif value < curr.value:
                # go left
                if curr.left is None:
                    return False
                else:
                    return fn(value, curr.left)
        return fn(target, self)   


duplicates = []  # Return the list of duplicates in this data structure

f = open('names_1.txt', 'r')
first = f.readline()
#create first node branch
name_tree1 = BSTNode(first)
for name in f: #read each line in the file
    if name is first: #skip first line
        pass
    else:
        name_tree1.insert(name) #add each line to the tree

f.close()

f = open('names_2.txt', 'r')
for name in f:
    #if in the tree, add it to list
    if name_tree1.contains(name): 
        duplicates.append(name)

f.close()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# original code
# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime complexity of original code is: O(n^2) Quadratic due to the nested loops
# runtime complexity of BST is O(n) Linear as it grows in direct proportion to n

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  
# Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# best time 0.13s


# if can only store names in array:

f = open('names_1.txt', 'r')
first = f.readline()
array1 = []
for name in f: #read each line in the file
        array1.append(name) #add each line to the array
f.close()

f = open('names_2.txt', 'r')
array2 = []
for name in f: #read each line in the file
        array2.append(name) #add each line to the array
f.close()

#built in methods only - set and len
first_list = set(array1)
second_list = set(array2)
len(first_list & second_list) #sets the intersection which is the common names


end_time = time.time()
print (len(first_list & second_list))
print (f"runtime: {end_time - start_time} seconds")



