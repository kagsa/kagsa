from .methods import *
from .built_modules import *
import re,base64,json,sys,traceback
from colorama import Fore as f


def encodeString (string):
    data = ''
    for char in string:
        data += chr(ord(char)+2)
    return data

def decodeString (string):
    data = ''
    for char in string:
        data += chr(ord(char)-2)
    return data
# 
# This Class is Used To Edit Python Error
# 
class ErrorWriter:
    def __init__ (self,theErr,get_value_back=False, rep_line=None):
        # Get Error Text & Type
        ErrStr=str(theErr).replace('<string>','<file>').replace('.',' . ')
        ErrType=theErr.__class__.__name__.replace('error','ERR').replace('Error','ERR').replace('compiler.classes.__init__.','').replace('.',' . ')
        Somethings_need_to_replace = {
            'expected an indented block after function definition' : 'empty codes block'
        }
        for i in Somethings_need_to_replace.items():
            ErrStr=ErrStr.replace(i[0],i[1])
        if rep_line!=None:
            lll = re.findall(r'line \d+',ErrStr)
            for i in lll:
                ErrStr=ErrStr.replace(i , 'line '+rep_line)
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
        # Return a Values or Print it
        if get_value_back:
            self.type=ErrType
            self.value=f'{ErrType} : {ErrStr}'
        else:
            print(f'{ErrType} : {ErrStr}',end='')


# Get Out Librarys From (.kgl) File And Return it
class Library_importer:
    def __init__(self,importer):
        self.codes=''
        self.importer=importer
    def get (self):
        # Open Importer File & Decrypt JSON
        x = open(self.importer,'r')
        d = json.loads(x.read())
        x.close()
        # Start Reading Librarys and Add Codes to (self.codes)
        for i in d.keys():
            try:
                lib_file = open(d[i],'r')
            except:
                sys.exit(f'\n  "{d[i]}" library file is not defined\n')
            # Decrypt
            PyCodes = decodeString(lib_file.read())
            # Edit Functions
            funcStartName="_".join(list(i))
            for line in PyCodes.split('\n'):
                if len(re.findall(r'def (.*?) :',line)) > 0 :
                    funcName=re.findall(r'def (.*?) :',line)[0]
                    if not('_____' in funcName):
                        line=line.replace(funcName,f'{funcStartName}_____{funcName}')
                self.codes=self.codes+line+'\n'
        # Return Everything
        return self.codes


def run (data,lib=False,lib_name=None,importer=5,kagsa_file=''):
    hidden_items={
        'SET_PRINT_END_AS_NONE':'end=""',
        'STR_SYM_TWO':'\\"',
        'STR_SYM_ONE':"\\'",
        'STR_SYM_THREE':"``"
    }
    # Add Lines to an Array
    CODES=[]
    for d in data:
        if not(d.strip()==''):
            CODES.append(d)
    CODES='\n'.join(CODES)
    # Replace Somethings
    for d in hidden_items.items():
        CODES=CODES.replace(d[0],d[1])
    # Read The Importer
    if importer!=5:
        X = Library_importer(importer).get()
        CODES=X+'\n\n'+CODES
    # For Compiling a Library
    if lib:
        x = open(lib_name,'w')
        x.write( encodeString(CODES) )
        x.close()
        print(f'\n  \033[1;32mDone Compile Lib : {lib_name}{f.RESET}\n')
    # For Run a Code
    else:
        # 
        # Create a Memory for Run Python Codes
        #
        data_is_need_to_add_to_exec=f'''
class g_e_t_E_r_r_o_r ():
    def __init__ (self) :
        self.t_e_x_t = ''
        self.l_i_n_e = ''
        self.t_y_p_e = ''
        self.f_i_l_e = "{kagsa_file}"
        if 'ERROR' in globals().keys():
            trace = []
            tb = globals()['ERROR'].__traceback__
            while tb!=None:
                filename = tb.tb_frame.f_code.co_filename
                name = tb.tb_frame.f_code.co_name
                lineno = tb.tb_lineno
                if (filename == '<string>') and (name == '<module>'):
                    FullCodes2 = FullCodes.split(n_l)[lineno-1]
                    Comment = REGEX(r'    # The Line (\d+)' , FullCodes2)[-1]
                    self.l_i_n_e = Comment
                    break
                tb = tb.tb_next
            E = ErrorWriter(globals()['ERROR'], get_value_back=True)
            self.t_e_x_t = E.value
            if E.type=='main':
                self.t_y_p_e = str(E.value).split(':')[1].strip()
            else:
                self.t_y_p_e = E.type
        else:
            return ''
'''
        #print(CODES)
        MEMORY = {
            'ErrorWriter':ErrorWriter,
            'FullCodes':data_is_need_to_add_to_exec + CODES,
            'REGEX':re.findall
        }
        for i in dict(globals() , **locals()).keys():
            i2 = i
            for j in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'):
                i2=i2.replace(j,'C')
            if not('CC' in i2):
                MEMORY[i]=dict(globals() , **locals())[i]
        try:
            exec(data_is_need_to_add_to_exec+CODES,MEMORY)
        #
        # The Exception of Compiler Error
        #  How This Work ?
        #    1- Search For Traceback Thats Happened in The exec() String
        #    2- Get The Line Thats Writed in The Translated Python Codes 
        #       ( The Line of Kagsa is Written in Pythhon Codes as a Comment )
        #    3- Read Kagsa File and Get The Line
        #    4- Write Error
        #
        except Exception as ERR:
            trace = []
            tb = ERR.__traceback__
            tb_lineno=''
            while tb!=None:
                filename = tb.tb_frame.f_code.co_filename
                name = tb.tb_frame.f_code.co_name
                lineno = tb.tb_lineno
                if (filename == '<string>') and (name == '<module>'):
                    tb_lineno=lineno
                    break
                tb = tb.tb_next
            if tb_lineno=='':
                if ', line' in str(ERR):
                    tb_lineno = int(re.findall(r', line (\d+)',str(ERR))[0])
            #
            print(f'Error Catched in "{kagsa_file}", Out From Compiler :')
            try:
                if tb_lineno=='': raise SyntaxError('')
                thecodes=data_is_need_to_add_to_exec+CODES
                the_python_line = thecodes.split('\n')[tb_lineno-1]
                PythonLineComment=int(re.findall(r'    # The Line (\d+)',the_python_line)[-1])
                KagsaLines={}
                KagsaLinesNO=0
                the_line_of_kagsa_error = ''
                for j in open(kagsa_file,'r').read().split('\n'):
                    KagsaLinesNO+=1
                    KagsaLines[ KagsaLinesNO ] = j
                if PythonLineComment in KagsaLines.keys():
                    the_line_of_kagsa_error = PythonLineComment
                    print(f'    >> {KagsaLines[PythonLineComment].strip()}')
                    print(f'    >> line {PythonLineComment}')
                elif (PythonLineComment-1) in KagsaLines.keys():
                    the_line_of_kagsa_error = PythonLineComment-1
                    print(f'    >> {KagsaLines[PythonLineComment-1].strip()}')
                    print(f'    >> line {PythonLineComment-1}')
                else:
                    the_line_of_kagsa_error = "?"
                    print(f'    >> ????????')
                    print(f'    >> unknown line')
            except:
                the_line_of_kagsa_error = "?"
                print(f'    >> ????????')
                print(f'    >> unknown line')
            ErrorWriter(ERR, rep_line=str(the_line_of_kagsa_error))
        except KeyboardInterrupt:
            print('\n\nCTRL + C')