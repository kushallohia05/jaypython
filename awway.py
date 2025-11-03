import array as arr
array_nun=arr.array('i', [1,3,5,3,7,9,3])
print("Original array:"+str(array_nun))
print("How many times three appears in the array:",array_nun.count(3))
array_nun.reverse()
print("Reverse the order of the array:")
print(str(array_nun))