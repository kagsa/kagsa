#!/usr/bin/env python3
import sys,os
from .paths import Paths as Paths

Paths.init()
if not('temp' in os.listdir(Paths.__path__())):
    os.mkdir(Paths.__path__()+os.sep+'temp')
if not('libs' in os.listdir(Paths.__path__())):
    os.mkdir(Paths.__path__()+os.sep+'libs')
sys.path.insert(0,Paths.__path__() + os.sep + 'libs')
sys.path.insert(0,Paths.__path__() + os.sep + 'temp')

from .lexer import main as Lexer
from .syntax_checker import main as Syntax_checker
from .parser import main as Parser
from .compiler import main as Compiler
from .errors import __init__ as errors
import platform,requests,re,logging,coloredlogs,shutil


def main ():
    pass

if platform.system() == 'Windows' :
    logger = logging.getLogger(f"Logger")
    coloredlogs.install(logger=logger)

version = '1.2.0'

# Colors :
def Red (t) : return f'\x1b[1;31m{t}\x1b[0m'
def Cyan (t) : return f'\x1b[0;36m{t}\x1b[0m'
def Yellow (t) : return f'\x1b[0;33m{t}\x1b[0m'

def ArgsParser ():
    argv = ' '.join(sys.argv[1:])
    data = {'do':''}
    if re.search(r"(-us *\S+)|(--unsetup *\S+)",argv):
        if not(argv in re.findall(r"(-us *\S+)|(--unsetup *\S+)",argv)[0]):
            return {'do':''}
        data['do'] = 'unsetup_kgl'
        data['state'] = 'ok'
        data['message'] = ''
        if not(sys.argv[2].endswith('.kgl')):
            data['state'] = 'err'
            data['message'] = 'error : unsetup_kgl : input file must be .kgl'
            return data
        data['input'] = [sys.argv[2]]
        return data
    elif   re.search(r'-v|--version',argv):
        if re.findall(r'-v|--version',argv)[0] != argv:
            return {'do':''}
        data['do'] = 'check_version'
    elif re.search(r'-u|--updates',argv):
        if re.findall(r'-u|--updates',argv)[0] != argv:
            return {'do':''}
        data['do'] = 'check_updates'
    elif re.search(r'-h|--help',argv):
        if re.findall(r'-h|--help',argv)[0] != argv:
            return {'do':''}
        data['do'] = 'help'
    elif argv=='':
        data['do'] = 'shell'
    elif re.search(r"(-l *\S+ *-o *\S+)|(--lib *\S+ *--out *\S+)",argv):
        if not(argv in re.findall(r"(-l *\S+ *-o *\S+)|(--lib *\S+ *--out *\S+)",argv)[0]):
            return {'do':''}
        data['do'] = 'compile_lib'
        data['state'] = 'ok'
        data['message'] = ''
        if not(sys.argv[2].endswith('.kg')) or not(sys.argv[4].endswith('.kgl')):
            data['state'] = 'err'
            data['message'] = 'error : compile_lib : input file must be .kg, output file must be .kgl'
            return data
        data['input'] = [sys.argv[2], sys.argv[4]]
        return data
    elif re.search(r"(-s *\S+)|(--setup *\S+)",argv):
        if not(argv in re.findall(r"(-s *\S+)|(--setup *\S+)",argv)[0]):
            return {'do':''}
        data['do'] = 'setup_kgl'
        data['state'] = 'ok'
        data['message'] = ''
        if not(sys.argv[2].endswith('.kgl')):
            data['state'] = 'err'
            data['message'] = 'error : setup_kgl : input file must be .kgl'
            return data
        data['input'] = [sys.argv[2]]
        return data
    elif re.search(r'-ct|--cleartmp',argv):
        if re.findall(r'-ct|--cleartmp',argv)[0] != argv:
            return {'do':''}
        data['do'] = 'cleartmp'
    else:
        if argv.endswith('.kg'):
            data['do'] = 'run_file'
            data['state'] = 'ok'
            data['message'] = ''
            if len(sys.argv[1:]) != 1:
                data['state'] = 'err'
                data['message'] = 'error : run_file : run file command must be like "kagsa file.kg"'
                return data
            data['input'] = [argv]
            return data
    return data


args = ArgsParser()
# Run a Code
# kagsa File.kg
if (args['do'] == 'run_file'):
    if args['state'] != 'ok':
        sys.exit(args['message'])
    
    kg_file = args['input'][0]
    ## Check main file
    try:
        open(kg_file,'r')
    except:
        sys.exit(f'error : run_file : "{kg_file}" is not defined')

    error_in = None # used to catch the error
    try:
        error_in='Lexer'
        LEXER = Lexer(  open(kg_file,'r').read()  )
        error_in='SyntaxChecker'
        SYNTAX = Syntax_checker(LEXER)
        error_in='Parser'
        PARSER = Parser(LEXER)
        error_in=None
    except Exception as ee:
        if ', line' in str(ee):
            line_no=int(re.findall(r', line (\d+)',str(ee))[0])
            line_text=open(kg_file,'r').read().split('\n')[line_no-1].strip()
        else:
            line_no = '?'
            line_text = '?'
        tb_type, tb_text, _ = errors(ee, lineno=str(line_no),get_value_back=1)

        print(f'{Red("error catched [")} {error_in}/{kg_file}/{tb_type} {Red("]")}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        print(f' {Cyan(line_no)} | {Cyan(line_text)}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        if '\n' in tb_text:
            print(f'{Red("error")}:', tb_text.split('\n')[0]) # error
            print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:])) # details
        else:
            print(f'{Red("error")}:', tb_text) # error


    if error_in==None:
        Compiler(PARSER,kg_file)
# Run Kagsa without any Command
# Start Kagsa Console
elif (args['do'] == 'shell'):
    memory= {}
    first_time_run_command = True
    print(f'KAGSA PROGRAMMING LANGUAGE {version}\nMIT License: Copyright (c) 2022 Kagsa',end='')
    while True:
        try:
            command = input('\n>>>')
            error_in = None # used to catch the error
            try:
                error_in='Lexer'
                LEXER = Lexer(  command  )
                error_in='SyntaxChecker'
                SYNTAX = Syntax_checker(LEXER)
                error_in='Parser'
                PARSER = Parser(LEXER)
                error_in=None
            except Exception as ee:
                line_no = '1'
                line_text = command
                tb_type, tb_text, _ = errors(ee, lineno=str(line_no),get_value_back=1)

                print(f'{Red("error catched [")} {error_in}/[stdin]/{tb_type} {Red("]")}')
                print(' ' + (' '* len(str(line_no))) + ' |')
                print(f' {Cyan(line_no)} | {Cyan(line_text)}')
                print(' ' + (' '* len(str(line_no))) + ' |')
                if '\n' in tb_text:
                    print(f'{Red("error")}:', tb_text.split('\n')[0]) # error
                    print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:])) # details
                else:
                    print(f'{Red("error")}:', tb_text) # error


            if error_in==None:
                if first_time_run_command:
                    memory=Compiler(PARSER,'[stdin]')
                    first_time_run_command = False
                else:
                    memory=Compiler(PARSER,'[stdin]',memory=memory)
        except KeyboardInterrupt:
            sys.exit(1)
        except EOFError:
            sys.exit(1)
# Compile a Kagsa Library
# kagsa -l libFile.kg -o newFile.kgl
elif (args['do'] == 'compile_lib'):
    if args['state'] != 'ok':
        sys.exit(args['message'])
    
    kg_file = args['input'][0]
    output  = args['input'][1]
    
    ## Check main file
    try:
        open(kg_file,'r')
    except:
        sys.exit(f'error : compile_lib : "{kg_file}" is not defined')

    error_in = None
    try:
        error_in='Lexer'
        LEXER = Lexer(  open(kg_file,'r').read()  )
        error_in='SyntaxChecker'
        SYNTAX = Syntax_checker(LEXER)
        error_in='Parser'
        PARSER = Parser(LEXER)
        error_in=None
    except Exception as ee:
        print(f'Error Catched in "{kg_file}", Out From {error_in} :')
        if ', line' in str(ee):
            line_no = int(re.findall(r', line (\d+)',str(ee))[0])
            line_text = open(kg_file,'r').read().split('\n')[line_no-1].strip()
        else:
            line_no = '?'
            line_text = '?'
        tb_type, tb_text, _ = errors(ee, lineno=str(line_no),get_value_back=1)

        
        print(f'{Red("error catched [")} {error_in}/{kg_file}/{tb_type} {Red("]")}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        print(f' {Cyan(line_no)} | {Cyan(line_text)}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        if '\n' in tb_text:
            print(f'{Red("error")}:', tb_text.split('\n')[0]) # error
            print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:])) # details
        else:
            print(f'{Red("error")}:', tb_text) # error
    
    if error_in==None:
        Compiler(PARSER,kg_file,  lib=True,    lib_name=output)
# Setup a KGL File
# kagsa --setup file.kgl
elif (args['do'] == 'setup_kgl'):
    shutil.copy(args['input'][0],Paths.__path__() + os.sep + 'libs')
    print(f'COPIED : {args["input"][0]} -> {Paths.__path__() + os.sep + "libs"}')
# UnSetup a KGL File
# kagsa --unsetup file.kgl
elif (args['do'] == 'unsetup_kgl'):
    try:
        os.remove(Paths.__path__() + os.sep + 'libs' + os.sep + args['input'][0])
        print('DELETED : ' + Paths.__path__() + os.sep + 'libs' + os.sep + args['input'][0])
    except:
        sys.exit(f'error : unsetup_kgl : "{args["input"][0]}" is not defined')
# Clear KAGSA Temps
# kagsa --cleartmp
elif (args['do'] == 'cleartmp'):
    for i in os.listdir(Paths.__path__() + os.sep + 'temp'):
        try:
            os.remove(Paths.__path__() + os.sep + 'temp' + os.sep + i)
            print(F'DELETED : {Paths.__path__() + os.sep + "temp" + os.sep + i}')
        except:None
# Check Kagsa Version
# kagsa -v
elif (args['do'] == 'check_version'):
    print(f'KAGSA version : {version}')
# Check for New Updates
# kagsa -u
# kagsa --updates
elif (args['do'] == 'check_updates'):
    try:
        version_req = requests.get('https://github.com/kagsa/kagsa/releases/latest').text
        version_req = re.findall(r'<title>(.*?)</title>',version_req)[0]
        version_req = re.findall(r'\d+\.\d+\.\d+',version_req)[0]
        newVersion=version_req.replace('.','').replace(' ','')
        oldVersion=version.replace('.','').replace(' ','')
        if int(newVersion) > int(oldVersion):
            print(f'new version {version_req}\ndownload it from Github : https://github.com/kagsa/kagsa')
        else:
            print('there is no new updates')
    except:
        print('error : check_updates : failed to check updates')
# help message
# kagsa -h
# kagsa --help
elif (args['do'] == 'help'):
    print(f'''
KAGSA PROGRAMMING LANGUAGE

kagsa [run:<filename>] [library:-l <filename> -o <output>] [version:-v, --version] [updates:-u, --updates] [help:-h, --help]
options:
    -l <filename> -o <output>  : build kgl library
    -v, --version              : check version
    -u, --updates              : check for new updates
    -h, --help                 : view this message

Read more at https://www.kagsa.org/docs/
''')
else:
    print('error : unknown command, use "-h"')