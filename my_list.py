# 1. Create an empty list
my_list = []
 
# 2. Append elements 
my_list.append(10)
my_list.append(20)
my_list.append(30) 
my_list.append(40)

# 3. Insert 15 at index 1
my_list.insert(1, 15)  

# 4. Extend with another list
my_list.extend([50, 60, 70])  

# 5. Remove last element
my_list.pop(-1)  

# 6. Sort list  
my_list.sort()

# 7. Print index of 30
print(my_list.index(30))