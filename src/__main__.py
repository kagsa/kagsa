#!/usr/bin/env python3
from .lexer import run as Lexer
from .syntax_checker import run as Syntax_checker
from .parser import run as Parser
from .compiler import run as Compiler
import sys,platform,requests,os,re,logging, coloredlogs
from colorama import Fore as f

def main ():
    pass

if platform.system() == 'Windows' :
    logger = logging.getLogger(f"Logger")
    coloredlogs.install(logger=logger)

version = '0.1.5'

class ErrorReader:
    def __init__ (self,theErr):
        # Get Error Text & Type
        ErrStr=str(theErr).replace('<string>','<file>').replace('.',' . ')
        ErrType=theErr.__class__.__name__.replace('error','ERR').replace('Error','ERR').replace('compiler.classes.__init__.','').replace('.',' . ')
        # Start Decoding Texts
        #
        ###########################################################################
        text=ErrStr.replace('(','').replace(')','').replace('"','').replace('\'','')
        text=text.replace('__','_C')
        for c in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'):
            text=text.replace(c,'C')
        COUNT=-1
        for i in text.split(' '):
            COUNT+=1
            i=i[1:]
            i=i.replace('_C','')
            if i =='':
                ORG=ErrStr.split(' ')[COUNT]
                Org=ErrStr.split(' ')[COUNT].replace('__','$').replace('_','').replace('$','_')
                ErrStr=ErrStr.replace(ORG,Org)
        #
        ###########################################################################
        text=ErrType.replace('(','').replace(')','').replace('"','').replace('\'','')
        text=text.replace('__','_C')
        for c in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'):
            text=text.replace(c,'C')
        COUNT=-1
        for i in text.split(' '):
            COUNT+=1
            i=i[1:]
            i=i.replace('_C','')
            if i =='':
                ORG=ErrType.split(' ')[COUNT]
                Org=ErrType.split(' ')[COUNT].replace('__','$').replace('_','').replace('$','_')
                ErrType=ErrType.replace(ORG,Org)
        ###########################################################################
        #
        # Somethings..
        ErrType=ErrType.replace(' . ','.')
        ErrStr=ErrStr.replace(' . ','.').replace('STR_SYM_TWO','\\"').replace("STR_SYM_ONE","\\'").replace("STR_SYM_THREE","\\``")
        print(f'{ErrType} : {ErrStr}',end='')


def ArgsParser ():
    argv = sys.argv[1:]
    data = {}
    if len(argv) == 0: return {}
    if not(argv[0].startswith('-')):
        if len(re.findall(r'(.*?).kg', argv[0])) < 1 :
            return {}
        data['main'] = argv[0]
        argv.pop( 0 )
    if '-m' in argv:
        try:
            if (argv[argv.index('-m')+1]).startswith('-'):
                return {}
            if len(re.findall(r'(.*?).json', argv[argv.index('-m')+1])) < 1 :
                return {}
            data['m'] = argv[argv.index('-m')+1]
            argv.pop( argv.index('-m')+1 )
            argv.pop( argv.index('-m') )
        except:
            return {}
    if '-o' in argv:
        try:
            if (argv[argv.index('-o')+1]).startswith('-'):
                return {}
            if len(re.findall(r'(.*?).kgl', argv[argv.index('-o')+1])) < 1 :
                return {}
            data['o'] = argv[argv.index('-o')+1]
            argv.pop( argv.index('-o')+1 )
            argv.pop( argv.index('-o') )
        except:
            return {}
    if '-l' in argv:
        try:
            if (argv[argv.index('-l')+1]).startswith('-'):
                return {}
            if len(re.findall(r'(.*?).kg', argv[argv.index('-l')+1])) < 1 :
                return {}
            data['l'] = argv[argv.index('-l')+1]
            argv.pop( argv.index('-l')+1 )
            argv.pop( argv.index('-l') )
        except:
            return {}
    if ('-v' in argv) or ('--version' in argv):
        data['v'] = '.'
        try:argv.pop( argv.index('-v') )
        except:argv.pop( argv.index('--version') )
    if ('-h' in argv) or ('--help' in argv):
        data['h'] = '.'
        try:argv.pop( argv.index('-h') )
        except:argv.pop( argv.index('--help') )
    if ('-u' in argv) or ('--updates' in argv):
        data['u'] = '.'
        try:argv.pop( argv.index('-u') )
        except:argv.pop( argv.index('--updates') )
    if not(argv==[]):
        return {}
    return data




args = ArgsParser()
params = args.keys()
# Run a Code
# kagsa File.kg -m import.json
if (('main' in params) and not('l' in params) and not('o' in params) and not('h' in params) and not('u' in params) and not('v' in params)):
    kg_file = args['main']
    importer = 0
    if 'm' in params :
        importer = args['m']
    ## Check main file
    try:
        open(kg_file,'r')
    except:
        sys.exit(f'\n[ - ] "{kg_file}" is not defined\n')

    # Check importer file
    if importer:
        try:
            open(importer,'r').close()
        except:
            sys.exit(f'\n[ - ] "{importer}" is not defined\n')
    ErrorIn = None # used to catch the error
    try:
        ErrorIn='Lexer'
        LEXER = Lexer(  open(kg_file,'r').read()  )
        ErrorIn='SyntaxChecker'
        SYNTAX = Syntax_checker(LEXER)
        ErrorIn='Parser'
        PARSER = Parser(LEXER)
    except Exception as theErr:
        print(f'Error Catched in "{kg_file}", Out From {ErrorIn} :')
        if ', line' in str(theErr):
            ErrLine=int(re.findall(r', line (\d+)',str(theErr))[0])
            LineStr=open(kg_file,'r').read().split('\n')[ErrLine-1].strip()
            print(f'    >> {LineStr}')
            print(f'    >> line {ErrLine}')
        else:
            print(f'    >> ????????')
            print(f'    >> unknown line')
        ErrorReader(theErr)
        raise SystemExit('')
    
    if importer:
        Compiler(PARSER,    kagsa_file=kg_file,  importer= importer)
    else:
        Compiler(PARSER,    kagsa_file=kg_file)
# Compile a Kagsa Library
# kagsa -l libFile.kg -o newFile.kgl -m import.json
elif (('l' in params) and ('o' in params) and not('main' in params) and not('h' in params) and not('u' in params) and not('v' in params)):
    kg_file = args['l']
    importer = 0
    output = args['o']
    if 'm' in params :
        importer = args['m']
    ## Check main file
    try:
        open(kg_file,'r')
    except:
        sys.exit(f'\n[ - ] "{kg_file}" is not defined\n')

    # Check importer file
    if importer:
        try:
            open(importer,'r').close()
        except:
            sys.exit(f'\n[ - ] "{importer}" is not defined\n')
    ErrorIn = None
    try:
        ErrorIn='Lexer'
        LEXER = Lexer(  open(kg_file,'r').read()  )
        ErrorIn='SyntaxChecker'
        SYNTAX = Syntax_checker(LEXER)
        ErrorIn='Parser'
        PARSER = Parser(LEXER)
    except Exception as theErr:
        print(f'Error Catched in "{kg_file}", Out From {ErrorIn} :')
        if ', line' in str(theErr):
            ErrLine=int(re.findall(r', line (\d+)',str(theErr))[0])
            LineStr=open(kg_file,'r').read().split('\n')[ErrLine-1].strip()
            print(f'    >> {LineStr}')
            print(f'    >> line {ErrLine}')
        else:
            print(f'    >> ????????')
            print(f'    >> unknown line')
            raise SystemExit('')
        ErrorReader(theErr)
    if importer:
        Compiler(PARSER,  lib=True,    lib_name=output    ,kagsa_file=kg_file,  importer= importer)
    else:
        Compiler(PARSER,  lib=True,    lib_name=output    ,kagsa_file=kg_file)
# Check Kagsa Version
# kagsa -v
elif (args == {'v':'.'}):
    print(f'\n\033[1;32mKagsa Version : {f.YELLOW}{version}{f.RESET}\n')
# Check for New Updates
# kagsa -u
elif (args == {'u':'.'}):
    try:
        version_req=requests.get('https://kagsa.github.io/kg-version.txt').text
        newVersion=version_req.replace('.','').replace(' ','')
        oldVersion=version.replace('.','').replace(' ','')
        if int(newVersion) > int(oldVersion):
            print(f'\n\033[1;32mNew Version \033[1;33m{version_req}\n\033[1;32mDownload it From Github : \033[1;37mhttps://github.com/kagsa/kagsa\n{f.RESET}')
        else:
            print(f'\n\033[1;32mThere is No Updates.\n{f.RESET}')
    except:
        print(f'\n\033[1;32mFailed To Check Updates.\n{f.RESET}')
# Any Else Parameter
else:
    w='\033[1;37m'
    g='\033[1;32m'
    #print(f'''\n{f.GREEN} _   __                      \n| | / /                      \n| |/ /  __ _  __ _ ___  __ _ \n|    \ / _` |/ _` / __|/ _` |\n| |\  \ (_| | (_| \__ \ (_| |\n\_| \_/\__,_|\__, |___/\__,_|\n              __/ |          \n             |___/           ''')
    print(f'''{g}\nKagsa Programming Language\n\nUsage :
Run Kagsa File :     kagsa {w}<file-path.kg>
                        -m <importer-path.json>{g}
Compile Library :    kagsa {w}-l <file-path.kg> -o <out-file.kgl>
                        -m <importer-path.json>{g}
Print Version :      kagsa {w}-v{g}
Print Help\\Usage :   kagsa {w}-h{g}
Search For Updates : kagsa {w}-u{g}
Full Documention at {w}https://github.com/kagsa/kagsa{f.RESET}\n''')