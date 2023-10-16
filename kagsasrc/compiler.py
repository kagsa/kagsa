import os
import json
import re
import zipfile
import traceback
import requests
import copy
from .methods import *
from .built_modules import *
from .errors import __init__ as errors
from .parse_id import __init__ as parse_id
from .paths import Paths as Paths

def main(data, kagsa_file, lib=False, lib_name=None, memory=None):
    # Join data lines into a single string
    data = '\n'.join(data)

    # Replace symbol codes with actual symbols
    data = data.replace('STR_SYM_TWO', '\\"').replace('STR_SYM_ONE', "\\'").replace('STR_SYM_THREE', "``")

    MEMORY = {
        'errors': errors,
        're': re,
        'os': os,
        'zipfile': zipfile,
        'sys': sys,
        'traceback': traceback,
        'parse_id': parse_id,
        'requests': requests,
        'Paths': Paths,
        'copy': copy
    }

    KAGSALINES = data
    kagsa_file = kagsa_file.replace('\\', '\\\\')
    exec_data = Paths.getFile('exec_data.py', 'r').read().replace('[KAGSA-FILE]', kagsa_file)
    data = exec_data + data

    if lib:
        nl = '\n'
        kgl_text = (
            Paths.getFile('libtemplate.py', 'r').read() + '\n'
            + f'KAGSA_FILE=Paths.__path__() + os.sep + "temp" + os.sep + "{kagsa_file}" \n'
            + f'KAGSA_FILE2 = "{kagsa_file}"\n'
            + 'try: KAGSA_CODES=open(KAGSA_FILE).read() \n'
            + 'except: KAGSA_CODES=open(KAGSA_FILE2).read() \n'
            + data
        )
        kgl = zipfile.ZipFile(lib_name, 'w')
        kgl.writestr(kagsa_file, open(kagsa_file).read())
        kgl.writestr('main.py', kgl_text)
        kgl.close()
    else:
        MEMORY = dict(globals(), **locals(), **MEMORY)
        if memory is not None:
            for i, j in memory.items():
                MEMORY[i] = j
        MEMORY['KAGSA_CODES'] = KAGSALINES
        MEMORY['KAGSA_FILE'] = kagsa_file

        try:
            exec(data, MEMORY)
            return MEMORY
        except Exception as ERR:
            the_tb = traceback.extract_tb(sys.exc_info()[2])
            tb_filename, tb_lineno, tb_func, _ = the_tb[-1]
            tb_filetype = ''

            if tb_lineno == '':
                if ', line' in str(ERR):
                    tb_lineno = int(re.findall(r', line (\d+)', str(ERR))[0])

            if (tb_filename == '<string>') and (tb_func == '<module>'):
                tb_filename_print = kagsa_file
                tb_filetype = 'kg'
            elif 'kgtmp' in tb_filename:
                tb_filename_print = tb_filename.split(os.sep)[-1].replace('_main.py', '')
                tb_filename_print = tb_filename_print.replace('__', 'ة').replace('_', '').replace('ة', '_')
                tb_filetype = 'py'
            else:
                data_founded = False
                for ttb in the_tb:
                    tb_fn, tb_lno, tb_f, _ = ttb
                    if (tb_fn == '<string>'):
                        tb_filename, tb_lineno, tb_func, _ = ttb
                        data_founded = True
                        break
                if not (data_founded):
                    tb_lineno = int(re.findall(r', line (\d+)', str(ERR))[0])
                tb_filename_print = kagsa_file
                tb_filetype = 'kg'

            try:
                if tb_filetype == 'kg':
                    tb_lineno = data.split('\n')[tb_lineno - 1]
                    tb_lineno = int(re.findall(r'    # line (\d+)', tb_lineno)[-1])
                    file_lines = open(kagsa_file, 'r').read().split('\n')
                    file_lines_no = len(file_lines)
                else:
                    file_lines = open(tb_filename, 'r').read().split('\n')
                    file_lines_no = len(file_lines)

                if (tb_lineno == file_lines_no) or (tb_lineno < file_lines_no):
                    line_text = file_lines[tb_lineno - 1].strip()
                else:
                    line_text = '?'
                    tb_lineno = '?'
            except:
                line_text = '?'
                tb_lineno = '?'

            tb_type, tb_text, _ = errors(ERR, lineno=str(tb_lineno), get_value_back=1)

            def Red(t): return f'\x1b[1;31m{t}\x1b[0m'
            def Cyan(t): return f'\x1b[0;36m{t}\x1b[0m'
            def Yellow(t): return f'\x1b[0;33m{t}\x1b[0m'

            if tb_filetype == 'py':
                print(f'{Red("error catched [")} {tb_filename_print}.kgl/main.py/{tb_type}{Red(" ]")}')
            else:
                print(f'{Red("error catched [")} {tb_filename_print}/{tb_type}{Red(" ]")}')
            print(' ' + (' ' * len(str(tb_lineno))) + ' |')
            print(f' {Cyan(tb_lineno)} | {Cyan(line_text)}')
            print(' ' + (' ' * len(str(tb_lineno))) + ' |')

            if '\n' in tb_text:
                print(f'{Red("error")}:', tb_text.split('\n')[0])
                print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:]))
            else:
                print(f'{Red("error")}:', tb_text)

        except KeyboardInterrupt:
            print('\n\nCTRL + C')

