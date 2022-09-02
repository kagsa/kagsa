#!/usr/bin/env python3
from .lexer import main as Lexer
from .syntax_checker import main as Syntax_checker
from .parser import main as Parser
from .compiler import main as Compiler
from .errors import __init__ as errors
import sys,platform,requests,os,re,logging, coloredlogs,re
from colorama import Fore as f


def main ():
    pass

if platform.system() == 'Windows' :
    logger = logging.getLogger(f"Logger")
    coloredlogs.install(logger=logger)

version = '1.1.0'

# Colors :
def Red (t) : return f'\x1b[1;31m{t}\x1b[0m'
def Cyan (t) : return f'\x1b[0;36m{t}\x1b[0m'
def Yellow (t) : return f'\x1b[0;33m{t}\x1b[0m'

def ArgsParser ():
    argv = ' '.join(sys.argv[1:])
    data = {'do':''}
    if   re.search(r'-v|--version',argv):
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
    elif re.search(r'-l .*? -o .*',argv):
        if re.findall(r'-l .*? -o .*',argv)[0] != argv:
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

    ErrorIn = None # used to catch the error
    try:
        ErrorIn='Lexer'
        LEXER = Lexer(  open(kg_file,'r').read()  )
        ErrorIn='SyntaxChecker'
        SYNTAX = Syntax_checker(LEXER)
        ErrorIn='Parser'
        PARSER = Parser(LEXER)
        ErrorIn=None
    except Exception as theErr:
        if ', line' in str(theErr):
            line_no=int(re.findall(r', line (\d+)',str(theErr))[0])
            line_text=open(kg_file,'r').read().split('\n')[line_no-1].strip()
        else:
            line_no = '?'
            line_text = '?'
        tb_type, tb_text, _ = errors(theErr, lineno=str(line_no),get_value_back=1)

        print(f'{Red("error catched [")} {ErrorIn}/{kg_file}/{tb_type} {Red("]")}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        print(f' {Cyan(line_no)} | {Cyan(line_text)}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        if '\n' in tb_text:
            print(f'{Red("error")}:', tb_text.split('\n')[0]) # error
            print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:])) # details
        else:
            print(f'{Red("error")}:', tb_text) # error


    if ErrorIn==None:
        Compiler(PARSER,kg_file)
# Run Kagsa without any Command
# Start Kagsa Console
elif (args['do'] == 'shell'):
    memory= {}
    first = 0
    print(f'KAGSA Programming Language {version}\nMIT License: Copyright (c) 2022 Kagsa',end='')
    while True:
        try:
            command = input('\n[KAGSA]->')
            ErrorIn = None # used to catch the error
            try:
                ErrorIn='Lexer'
                LEXER = Lexer(  command  )
                ErrorIn='SyntaxChecker'
                SYNTAX = Syntax_checker(LEXER)
                ErrorIn='Parser'
                PARSER = Parser(LEXER)
                ErrorIn=None
            except Exception as theErr:
                line_no = '1'
                line_text = command
                tb_type, tb_text, _ = errors(theErr, lineno=str(line_no),get_value_back=1)

                print(f'{Red("error catched [")} {ErrorIn}/[stdin]/{tb_type} {Red("]")}')
                print(' ' + (' '* len(str(line_no))) + ' |')
                print(f' {Cyan(line_no)} | {Cyan(line_text)}')
                print(' ' + (' '* len(str(line_no))) + ' |')
                if '\n' in tb_text:
                    print(f'{Red("error")}:', tb_text.split('\n')[0]) # error
                    print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:])) # details
                else:
                    print(f'{Red("error")}:', tb_text) # error


            if ErrorIn==None:
                first+=1
                if first==1:
                    memory=Compiler(PARSER,'[stdin]')
                else:
                    memory=Compiler(PARSER,'[stdin]',memory=memory)
        except KeyboardInterrupt:
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

    ErrorIn = None
    try:
        ErrorIn='Lexer'
        LEXER = Lexer(  open(kg_file,'r').read()  )
        ErrorIn='SyntaxChecker'
        SYNTAX = Syntax_checker(LEXER)
        ErrorIn='Parser'
        PARSER = Parser(LEXER)
        ErrorIn=None
    except Exception as theErr:
        print(f'Error Catched in "{kg_file}", Out From {ErrorIn} :')
        if ', line' in str(theErr):
            line_no = int(re.findall(r', line (\d+)',str(theErr))[0])
            line_text = open(kg_file,'r').read().split('\n')[line_no-1].strip()
        else:
            line_no = '?'
            line_text = '?'
        tb_type, tb_text, _ = errors(theErr, lineno=str(line_no),get_value_back=1)

        
        print(f'{Red("error catched [")} {ErrorIn}/{kg_file}/{tb_type} {Red("]")}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        print(f' {Cyan(line_no)} | {Cyan(line_text)}')
        print(' ' + (' '* len(str(line_no))) + ' |')
        if '\n' in tb_text:
            print(f'{Red("error")}:', tb_text.split('\n')[0]) # error
            print(f'{Yellow("details")}:', '\n'.join(tb_text.split('\n')[1:])) # details
        else:
            print(f'{Red("error")}:', tb_text) # error
    
    if ErrorIn==None:
        Compiler(PARSER,kg_file,  lib=True,    lib_name=output)
# Check Kagsa Version
# kagsa -v
elif (args['do'] == 'check_version'):
    print(f'Kagsa version : {version}')
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
Kagsa Programming Language

Usage : kagsa <command>
Commands :
   Run file :       kagsa <file.kg>
   Compile lib :    kagsa -l <file.kg> -o <output.kgl>
   Check version :  kagsa -v
                    kagsa --version
   Help :           kagsa -h
                    kagsa --help
   Check updates :  kagsa -u
                    kagsa --updates

Read more at https://github.com/kagsa/kagsa
''')
else:
    print('error : unknown command, use "-h"')