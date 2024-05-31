'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.
'''

def stack(input):
    stack = []
    
    for digit in input:
        if digit.isdigit():
            stack.append(int(digit))
        else:
            b = stack.pop()
            a = stack.pop()

            if digit == '+':
                result = a + b
            elif digit == '-':
                result = a - b
            elif digit == '*':
                result = a * b
            elif digit == '/':
                result = a / b

            stack.append(result)
    return stack[0]

input1 = ["1", "2", "+", "5", "*"]
input2 = ["10", "2", "3", "+","-", "5", "*"]
result = stack(input1)
result1 = stack(input2)
print(result)
print(result1)