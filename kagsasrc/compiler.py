from .methods import *
from .built_modules import *
from .errors import __init__ as errors
from .parse_id import __init__ as parse_id
from .paths import Paths as Paths
import sys,re,zipfile,traceback,os,requests,copy




def main (data,kagsa_file,lib=False,lib_name=None,memory=None):
    data = '\n'.join(data)
    # Replace ( Some Symbols Codes ) to ( Backslash + str sybmbols )
    data = data.replace('STR_SYM_TWO','\\"' ).replace('STR_SYM_ONE',"\\'" ).replace('STR_SYM_THREE',"``")
    #print(data)
    MEMORY = {
        'errors':errors,
        're':re,
        'os':os,
        'zipfile':zipfile,
        'sys':sys,
        'traceback':traceback,
        'parse_id':parse_id,
        'requests':requests,
        'Paths':Paths,
        'copy':copy
    }
    KAGSALINES=data
    kagsa_file = kagsa_file.replace('\\','\\\\')
    exec_data = Paths.getFile('exec_data.py','r').read().replace('[KAGSA-FILE]', kagsa_file)    
    data = exec_data + data
    if lib:
        nl='\n'
        kgl_text = Paths.getFile('libtemplate.py','r').read() + '\n' + f'KAGSA_FILE=Paths.__path__() + os.sep + "temp" + os.sep + "{kagsa_file}" \nKAGSA_FILE2 = "{kagsa_file}"\ntry: KAGSA_CODES=open(KAGSA_FILE).read() \nexcept: KAGSA_CODES=open(KAGSA_FILE2).read() \n' + data
        kgl = zipfile.ZipFile(lib_name,'w')
        kgl.writestr( kagsa_file , open(kagsa_file).read())
        kgl.writestr('main.py', kgl_text)
        kgl.close()
    # For Run a Code
    else:
        # 
        # Create a Memory for Run Python Codes
        #
        MEMORY = dict(globals() , **locals(), **MEMORY)
        if memory != None:
            for i,j in memory.items():
                MEMORY[i]=j
        MEMORY['KAGSA_CODES'] = KAGSALINES
        MEMORY['KAGSA_FILE']  = kagsa_file
        try:
            #print(KAGSALINES)
            exec(data,MEMORY)
            return MEMORY
        #
        # The Exception of Compiler Error
        #  How This Work ?
        #    1- Search For The Last Traceback
        #    2- Get The Line Thats Writed in The Translated Python Codes 
        #       ( The Line of Kagsa is Written in Pythhon Codes as a Comment )
        #    3- Read The File File and Get The Line
        #    4- Write Error
        #
        except Exception as ERR:
            #tb = ERR.__traceback__
            the_tb = traceback.extract_tb(sys.exc_info()[2])
            tb_filename, tb_lineno, tb_func, _ = the_tb[-1]
            tb_filetype = ''
            # if no lineno in the error frame
            #     go and get it from error text
            if tb_lineno=='':
                if ', line' in str(ERR):
                    tb_lineno = int(re.findall(r', line (\d+)',str(ERR))[0])
            
            # parse the error filename
            # error came from kagsa code
            if (tb_filename == '<string>') and (tb_func == '<module>'):
                tb_filename_print = kagsa_file
                tb_filetype = 'kg'
            # form a library
            elif 'kgtmp' in tb_filename:
                tb_filename_print = tb_filename.split(os.sep)[-1].replace('_main.py','')
                tb_filename_print = tb_filename_print.replace('__','ة').replace('_','').replace('ة','_')
                tb_filetype = 'py'
            # something else
            else:
                data_founded = False
                for ttb in the_tb:
                    tb_fn, tb_lno, tb_f, _ = ttb
                    if (tb_fn == '<string>') :
                        tb_filename, tb_lineno, tb_func, _ = ttb
                        data_founded = True
                        break
                if not(data_founded):
                    tb_lineno = int(re.findall(r', line (\d+)',str(ERR))[0])
                tb_filename_print = kagsa_file
                tb_filetype = 'kg'
            


            
            try:                
                if tb_filetype == 'kg':
                    tb_lineno = data.split('\n')[tb_lineno-1]
                    tb_lineno = int(re.findall(r'    # line (\d+)',tb_lineno)[-1])
                    file_lines = open(kagsa_file,'r').read().split('\n')
                    file_lines_no = len( file_lines )
                else:
                    file_lines = open(tb_filename, 'r').read().split('\n')
                    file_lines_no = len( file_lines )
                
                ########

                if (tb_lineno == file_lines_no) or (tb_lineno < file_lines_no):
                    line_text = file_lines[tb_lineno-1].strip()
                    #tb_lineno   = tb_lineno
                else:
                    line_text = '?'
                    tb_lineno   ='?'
            except:
                line_text = '?'
                tb_lineno   ='?'
            
            tb_type, tb_text, _ = errors(ERR, lineno=str(tb_lineno),get_value_back=1)

            # tb_filetype
            # line_text
            # tb_lineno
            # tb_filename_print
            # tb_type
            # tb_text

            # Colors :
            def Red (t) : return f'\x1b[1;31m{t}\x1b[0m'
            def Cyan (t) : return f'\x1b[0;36m{t}\x1b[0m'
            def Yellow (t) : return f'\x1b[0;33m{t}\x1b[0m'

            # Start Print The Error
            # print first line : error catched [ .. ]
            if tb_filetype == 'py':
                print(f'{Red("error catched [")} {tb_filename_print}.kgl/main.py/{tb_type}{Red(" ]")}')
            else:
                print(f'{Red("error catched [")} {tb_filename_print}/{tb_type}{Red(" ]")}')
            # print the line text/no of error
            print(' ' + (' '* len(str(tb_lineno))) + ' |')
            print(f' {Cyan(tb_lineno)} | {Cyan(line_text)}')
            print(' ' + (' '* len(str(tb_lineno))) + ' |')
            # print err string with the details
            if '\n' in tb_text:
                print(f'{Red("error")}:', tb_text.split('\n')[0]) # error
                print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:])) # details
            else:
                print(f'{Red("error")}:', tb_text) # error

        except KeyboardInterrupt:
            print('\n\nCTRL + C')