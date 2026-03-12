import edit_variables

def print_(DATA):
    print(DATA)

def plus_(num1, num2, outVar):
    value = int(num1) + int(num2)
    create_var(outVar, value, 'int')

def minus_(num1, num2, outVar):
    value = int(num1) - int(num2)
    create_var(outVar, value, 'int')
    
def asterisk_(num1, num2, outVar):
    value = int(num1) * int(num2)
    create_var(outVar, value, 'int')

def slash_(num1, num2, outVar):
    value = int(num1) / int(num2)
    create_var(outVar, value, 'int')

def if_(logick, block):
    pass