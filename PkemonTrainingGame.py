number_of_pokemon=int(input("Enter how many pokemon are there :   "))  # It will take number of pokemon
list_of_pockemonPower=[]         # It is taking empty list for power of pokemon 
for count in range(number_of_pokemon):  # This loop will take that much power how many number user entered in number of pokemon
    power_of_pokemon=int(input("Enter power of pokemon :   "))  # User input will take input of power
    list_of_pockemonPower.append(power_of_pokemon)    # This will append in list 
minimum_power=min(list_of_pockemonPower)     # This mothod will find max power  
maximum_power=max(list_of_pockemonPower)    # This mothod will find minimum power  
print("\n\nMinimum power :  ",minimum_power)  # For printing minimum power 
print("Maximum power :  ",maximum_power)    # For printing maximum power 

left_power=number_of_pokemon-2  # Left power( variable ) will save the number of pair, because 1st and last pair is decided so apart of that we are deciding left number of pair
powerList=[]        # This list is for pair of power


i=0     # This is for append pair in list according to the nagative indexing 
linear=0     # This will help for sbtract linearly
while True:
    
    next_power=maximum_power-linear     # Here we are subtracting linearly
    if next_power in list_of_pockemonPower:    # This condition will check that the power ( which we found by subtraction ) is in the power list or not
        pair=[minimum_power,next_power]     # If last condition is true then it will make pair 
        powerList.insert(-i,pair)       # We are appending the pair by nagative indexing
        i=i+1       # Nagative indexing will increase because next pair we have to append before the last, pair not after
    linear+=1      # linear will incease continuesly
    if i==left_power:   # if needed pair appended then loop will break
        break
    
powerList.insert(0,[minimum_power,minimum_power])    # The pair of minimum & minimum will append in 0 indexing
powerList.insert(-1,[minimum_power,maximum_power])      # The pair of minimum & maximum will append in last indexing
print("List of power :   ",powerList)   # This will display list of power
for i in powerList:     # This will print pair of power
    print(i[0],i[1])