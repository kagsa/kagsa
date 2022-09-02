class أ_K_A_G_S_A:
    f_i_l_e = '[KAGSA-FILE]'
    if f_i_l_e!='[stdin]':
        x = open(f_i_l_e,'r')
        c_o_d_e = x.read()
        x.close()
    else: c_o_d_e = ''
    v_e_r_s_i_o_n = '1.1.0'
    def latest () :
        try:
            req = requests.get('https://github.com/kagsa/kagsa/releases/latest').text
            req = re.findall(r'<title>(.*?)</title>',req)[0]
            return re.findall(r'\d+\.\d+\.\d+',req)[0]
        except:
            return ''

    

class g_e_t_E_r_r_o_r ():
    def __init__ (self) :
        self.t_e_x_t     = ''
        self.l_i_n_e_n_o = ''
        self.l_i_n_e     = ''
        self.t_y_p_e     = ''
        self.f_i_l_e     = '[KAGSA-FILE]'

        if self.f_i_l_e == '[stdin]':
            self.l_i_n_e_n_o = 1
            E = errors(globals()['ERROR'], get_value_back=True)
            self.t_e_x_t = E[1]
            self.t_y_p_e = E[0]
            self.l_i_n_e = ''
            return
        the_tb = traceback.extract_tb(sys.exc_info()[2])
        tb_filename, tb_lineno, tb_func, tb_line = the_tb[-1]
        tb_filetype = 'py'
        # parse the error filename
        # error came from kagsa code
        if tb_filename == '<string>':
            self.f_i_l_e = kagsa_file
            tb_filetype = 'kg'
        # form a library
        elif 'kgtmp' in tb_filename:
            self.f_i_l_e = tb_filename.split(os.sep)[-1].replace('_main.py','')
            self.f_i_l_e = self.f_i_l_e.replace('__','ة').replace('_','').replace('ة','_')
            self.f_i_l_e+= '.kgl'
        # something else
        else:
            data_founded = False
            for ttb in the_tb:
                tb_fn, tb_lno, tb_f, _ = ttb
                if (tb_fn == '<string>'):
                    tb_filename, tb_lineno, tb_func, _ = ttb
                    data_founded =True
                    break
            if not(data_founded):
                tb_lineno = int(re.findall(r', line (\d+)',str(globals()['ERROR']))[0])
            self.f_i_l_e = kagsa_file
            tb_filetype = 'kg'
        
        try:
            if tb_filetype == 'kg':
                tb_lineno = FullCodes.split('\n')[tb_lineno-1]
                tb_lineno = int(re.findall(r'    # line (\d+)',tb_lineno)[-1])
                x = open(kagsa_file,'r')
                file_lines = x.read().split('\n')
                x.close()
                file_lines_no = len( file_lines )
            else:
                x = open(tb_filename, 'r')
                file_lines = x.read().split('\n')
                x.close()
                file_lines_no = len( file_lines )
            #
            #
            #
            if (tb_lineno == file_lines_no) or (tb_lineno < file_lines_no):
                self.l_i_n_e = file_lines[tb_lineno-1].strip()
                self.l_i_n_e_n_o   = tb_lineno
            else:
                self.l_i_n_e       = '?'
                self.l_i_n_e_n_o   ='?'
        except:
            self.l_i_n_e       = '?'
            self.l_i_n_e_n_o   = '?'
        

        E = errors(globals()['ERROR'], get_value_back=True)
        self.t_e_x_t = E[1]
        self.t_y_p_e = E[0]






class IncludeError (Exception):
    pass

def INCLUDE (lib):
    try:
        # check if input is string
        if not(lib.__class__.__name__ == 'str') :
            raise IncludeError('libarary must be string')
        # check if input is .kgl file
        if not(lib.endswith('.kgl')):
            raise IncludeError('libarary must be ".kgl" file')
        if len(re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl', lib)) < 1 :
            raise IncludeError('filename must be writted as this syntax "[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl"')
        if not(re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl', lib)[0] == lib):
            raise IncludeError('filename must be writted as this syntax "[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl"')
        # try open file
        open(lib,'r')
        if os.sep in lib:
            lib_name = lib.split(os.sep)[-1]
        lib_name = lib.replace('.kgl','')
        # parse lib_name
        if (len(lib_name)>2) or (len(lib_name)==2):
            lib_name='_'.join(list(lib_name))
        if lib_name[0] in '1234567890' :
            lib_name='_'+lib_name
        # end parse
        # read it :
        # create "kgtmp"
        try:os.mkdir('kgtmp')
        except:pass
        # get "main.py"
        archive = zipfile.ZipFile(lib,'r')
        py_file = open(f'kgtmp{os.sep}{lib_name}_main.py','wb')
        py_file.write(archive.read('main.py'))
        py_file.close()
        # get "__memory__.py"
        archive.extract('__memory__.py', 'kgtmp')
        # import it
        global exec_scope
        exec_scope = {}
        sys.path.insert(1, 'kgtmp')
        try:
            exec(f'import {lib_name}_main',exec_scope)
            exec(f'def send_to_globals () :\n\tglobal {lib_name}\n\t{lib_name} = exec_scope["{lib_name}_main"]',globals())
            send_to_globals()
        except:
            raise IncludeError(f'syntaxes error in "{lib}"')
    except FileNotFoundError:
        raise IncludeError(f'"{lib}" is not defined')

def to_list (data):
    d = []
    for i in data:
        d.append(i)
    return d

class JumpingError (Exception):
    pass

def JUMP (lineno):
    lines = kagsa_lines
    lines_dict = {}
    data_founded = 0
    data = ''
    
    # Create a dict with all lines -> {'2','print("hi")    # line 2'}
    last=''
    for j in lines.split('\n'):
        no = re.findall(r'    # line (\d+)',j)[0]
        if no == last.replace('_',''):
            lines_dict[last+'_'] = j
            last = last+'_'
        else:
            lines_dict[no] = j
            last = no
        #print(last)

    if str(lineno) in lines_dict.keys():
        k,v = to_list(lines_dict.keys()), to_list(lines_dict.values())
        data_founded=1
        data = v[ k.index(str(lineno)) : ]
    else:
        up_ = int(lineno)
        down_ = int(lineno)
        while True:
            up_+=1
            down_-=1
            if str(up_) in lines_dict:
                k,v = to_list(lines_dict.keys()), to_list(lines_dict.values())
                data_founded=1
                data = v[ k.index(str(up_)) : ]
                break
            if down_ > 0:
                if str(down_) in lines_dict:
                    k,v = to_list(lines_dict.keys()), to_list(lines_dict.values())
                    data_founded=1
                    data = v[ k.index(str(down_))+1 : ]
                    break


    if data[0].startswith('\t'):
        tabs = re.findall(r'(\t+).*?',data[0])[0].count('\t')
        x=0
        for j in range(1, tabs+1):
            data.insert(x , ("\t" * x) + 'for _jump_ in [1]:')
            x+=1

    #print('\n'.join(data))
    #input()
    exec('\n'.join(data),globals())
    sys.exit(0)

