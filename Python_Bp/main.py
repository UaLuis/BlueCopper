import parser as pr
import sys

#script_name = sys.argv(1)

code = []

code = pr.read_file("/Users/wolfi/BlueCopper/tests/test0.bp")
print(code)
pr.check_base_structure(code)