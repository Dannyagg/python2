list_of_numbers = [1,2,3]

#print(sum(list_of_numbers))

total = 0
for number in list_of_numbers:
    print( 'The number is now:' + str(number))    
    total = total +number
    print('The total is now: ' + str(total))
    
print( '------------- add and print only total--------------------')
    
total = 0
for number in list_of_numbers:
#    print('The number is now:' + str(number))
    total = total + number
    
print('The total is now: ' + str(total))
