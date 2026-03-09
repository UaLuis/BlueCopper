import parser as pr
import sys

# script_name = sys.argv(1)

code = []

code = pr.read_file("/Users/wolfi/BlueCopper/tests/test0.bp")

index_data, index_data_end, index_start, index_start_end = pr.check_base_structure(code)
pr.parser(code, index_start, index_data, index_data_end, index_start_end)
