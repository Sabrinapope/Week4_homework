i = 1 
while(i<=10):
    print(i)
    i += 1 
   #
  
n = int(input("10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"))
i = numbers
print ("The reversed numbers from {0} to 1 in reverse order: ". format(numbers))
while (i >= 1):
    print (1, end = ' ')
    i = i -1
    
    #
    
print("Uppercase Alphabets are:")
for i in range(65,91): 
        ''' to print alphabets with seperation of space.'''still
        print(chr(i),end=' ') 
        
   #
   
max = 100
num = 1

while num <= max:
    if(num % 2 == 0):
        print("{0}" .format(num))
    num = num + 1

    #
    
print(" Multiplication Table ")

for i in range(5):
    for j in range(1, 11):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    print('==============')
    
    #
    
    maximum = int(input(" Please Enter any Maximum Value : "))

for number in range(1, maximum + 1):
    if(number % 2 != 0):
        print("{0}".format(number))
