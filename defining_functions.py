


# # Define function
# def my_function():
#     print("Hello")
#     num_char = len("Hello")
#     print("Bye")
#     return num_char
    

# # Execute Function
# my_function()

# print(my_function())



# Pass a function to an argument

def wage(w_hours):
    return w_hours * 25

def with_bonus(w_hours):
    return wage(w_hours) + 50


print(wage(8))
print(with_bonus(8))




def greet_all(people):
    for person in people:
        print("Hello" + person)


friends = ["Bob", "Josh", "Austin"]

greet_all(friends)