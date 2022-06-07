
lst = []
 

n = int(input("Enter number of elements : "))
 

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele) 
     
print(lst)

arr = lst;    
temp = 0;    
     
  
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
     
   
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
 
   
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ")



import statistics
lst = []
 

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele)
     
print(lst)
x = statistics.mean(lst)
print("Mean is :", x)



import statistics
lst = []
 

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele)
     
print(lst)
x = statistics.median(lst)
print("Median is :", x)


import statistics
lst = []
 

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele)
     
print(lst)
x = statistics.stdev(lst)
print("Standard Deviation is :", x)




