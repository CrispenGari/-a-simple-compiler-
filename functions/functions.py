try:
    import os, subprocess, commands
    from errors.errors import PythonError as e
except ImportError as e:
    print(e)

class Function:
    def __init__(self):
        pass
    def run_program(self, sorce_code):
        code_1 = str(sorce_code).replace("\n", "1001001")
        code_2 = code_1.replace("1001001", '\n')
        return exec(str(code_2))
    def line_of_codes(self, sorce_code, keysym):
        lines_list = sorce_code.split('\n')
        if keysym == "BackSpace":
            return len(lines_list) -1
        else:

            return len(lines_list)