from lark import Lark, Transformer, v_args
from pathlib import Path

given_path = "~/BlueCopper/Python_Bp/grammar.lark"
p = Path(given_path).expanduser()
full_path = p.resolve()

@v_args(inline=True) 
class ParserBlTree(Transformer):
    from all_functions.base_function import create_print
    create_print = staticmethod(create_print)
    vars = {}
    
    def int_decl(self, name, value):
        self.vars[str(name)] = int(value)
        return int(value)
        
    def str_decl(self, name, value):
        self.vars[str(name)] = str(value)[1:-1]
        return str(value)[1:-1]
        
    def expr(self, token):
        t = str(token)
        if t in self.vars:
            return self.vars[t]
        return t
        
bl_parser = Lark.open(full_path, parser="lalr", transformer=ParserBlTree())
        
path = "/Users/wolfi/BlueCopper/tests/test0.bp"
with open(path, 'r') as file:
    code = file.read()

bl_parser.parse(code)

