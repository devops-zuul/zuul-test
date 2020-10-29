import sys 
def add(first_term, second_term):
    return first_term + second_term

 
def subtract(first_term, second_term):
    return first_term - second_term


def print_to_stdout(*a): 
    # Here a is the array holding the objects 
    # passed as the arguement of the function 
    print(*a, file = sys.stdout) 

 


print_to_stdout("calling add...")
print_to_stdout("result of addition 1 and 2  is =")
print_to_stdout(add(1,2))

print_to_stdout("\n calling substract....")
print_to_stdout("result of subtraction 4 and 2  is =")
print_to_stdout(subtract(4,2))

