
import random

import string
list1 = list()
present_elements = []
count2 = []
list2 = [["Jan",31], ["Feb",28],[ "Mar",31], ["Apr",30],[ "May", 31], ["June", 30], ["July",31] , ["August", 31],
 ["September", 30], ["October", 31], ["November", 30], ["December", 31]]
while True:
    try:
        number_of_dates = int(input("Number of dates: "))
        break
    except ValueError:
        print("Invalid Input ,Please try again.")

for i in range(number_of_dates):
    random_number = random.randint(0,11)
    random_number2 = random.randint(1,list2[random_number][1])

    data_precise = list2[random_number][0] + " " + str(random_number2)
    list1.append(data_precise)
count = 1
print(f"Orignal Random date list is: {list1}")


for i in range(number_of_dates):
    if list1[i]  not in present_elements:
        for j in range(i+1, number_of_dates):
               
                if list1[i] == list1[j]:
                    count+=1    
                else:    
                    pass
        present_elements.append(list1[i])
                    
       
    
    count2.append(count)
    count = 1
print(f"elements in the list without repetition : {present_elements}")  
for i in range (0,len(present_elements)):
    print(f"number of times {present_elements[i]} present in result list is : {count2[i]}")