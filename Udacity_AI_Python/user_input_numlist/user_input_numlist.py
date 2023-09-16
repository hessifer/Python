# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers
for _ in range(10):
    try:
        userInput = int(input("Enter any 2-digit number: "))
    except ValueError:
        # print incorrect value warning  when ValueError exception occurs
        print("Incorrect value. That's not an int!")
    else:
        # check to see if number is even and if yes, add to list_sum
        if userInput % 2 == 0:
            list_sum += userInput
        user_list.append(userInput)

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))
