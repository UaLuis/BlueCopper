from all_functions import base_function as bsf
from all_functions import math_function as mhf
import shlex

vars = {}

def create_var(name, value, type):
    if type == 'int':
        vars[name] = int(value)
    elif type == 'string': 
        vars[name] == str(value)
    elif type == 'float':
        vars[name] == float(value)
    elif type == 'bool':
        vars[name] == bool(value)
    else:
        print(f'Помилка! Не існує типу {type}!')
    

def read_file(script_name):
    code = []
    
    with open(script_name, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            parts = shlex.split(line)
            code.append(parts)
    
    return code
    
def check_base_structure(code):
    index_data = None
    index_data_end = None 

    for i, line in enumerate(code):
        if line[0] == '.data:' and index_data is None:
            index_data = i
        if line[0] == '.data_end' and index_data_end is None:
            index_data_end = i

    if code[0][0] == '.start:' and code[index_data-1][0] == '.start_end':
        if code[index_data][0] == '.data:' and code[index_data_end][0] == '.data_end':
            print("OK")
        else:
            print("ERROR in .data section!")
    else:
        print("ERROR in .start section!")
        
    index_start = code[0][0]
    index_start_end = code[index_data-1][0]
    
    return index_data, index_data_end, index_start, index_start_end
    
def check_structure(code, type_structure):
    pass
    
def parser(code, index_start, index_data, index_data_end, index_start_end):
    #Читання блоку .data та створення змінних
    for i in range(1, index_start_end):
        name, value, type = code[i][1], code[i][2], code[i][0]
        create_var(
    