import builtins

variables = {}
type_list = ["int", "string", "float", "bool"]


def create_var(name, value, type):
    if type in type_list:
        convert_value = getattr(builtins, type)
        variables[name] = convert_value(value)

    else:
        print(f"Помилка! Не існує типу {type}!")
