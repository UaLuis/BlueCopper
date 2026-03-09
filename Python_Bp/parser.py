from all_functions import base_function as bsf
import shlex

variables = {}

def create_var(name, value, type):
    if type == 'int':
        variables[name] = int(value)
    elif type == 'string': 
        variables[name] = str(value)
    elif type == 'float':
        variables[name] = float(value)
    elif type == 'bool':
        variables[name] = bool(value)
    else:
        print(f'Помилка! Не існує типу {type}!')
        
def resolve_args(args):
    return [variables.get(a, a) for a in args]
    
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
    index_start = None
    index_start_end = None
    
    for i, line in enumerate(code):
        if line[0] == '.data:' and index_data is None:
            index_data = i
        if line[0] == '.data_end' and index_data_end is None:
            index_data_end = i
        if line[0] == '.start:' and index_start is None:
            index_start = i
        if line[0] == '.start_end' and index_start_end is None:
            index_start_end = i

    if code[0][0] == '.start:' and code[index_data-1][0] == '.start_end':
        if code[index_data][0] == '.data:' and code[index_data_end][0] == '.data_end':
            print("OK")
        else:
            print("ERROR in .data section!")
    else:
        print("ERROR in .start section!")
    
    return index_data, index_data_end, index_start, index_start_end
    
def check_structure(code, type_structure):
    pass
    
def parser(code, index_start, index_data, index_data_end, index_start_end):
    #Читання блоку .data та створення змінних
    for i in range(index_data + 1, index_data_end):
        name, value, type = code[i][1], code[i][2], code[i][0]
        create_var(name, value, type)
   
   #Читання блоку .start та запуск коду 
    for i in range(index_start + 1, index_start_end):
        command, args = code[i][0], code[i][1:]
        args = resolve_args(args)
        fun_run = getattr(bsf, f"{command}_", None)
        
        if fun_run:
            fun_run(*args)
        else:
            print(f"ERROR! {command} невідома команда!")


        
    