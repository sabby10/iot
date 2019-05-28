
# Python code to demonstrate naive method 
# to compute factorial 
val = 10      #user-defined value whose factorial is to be found
fact = 1    #Initializing fact value to 1
  
for i in range(1,val+1): 
    fact = fact * i 
      
print ("The factorial of 10 is : ",fact,end="")
print()
