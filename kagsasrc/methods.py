import forbiddenfruit,threading



def SetMethod (datatypes, name, func):
    for datatype in datatypes:
        forbiddenfruit.curse(datatype,name,func)

def t_o_I_n_t (value):
    try:    return int(value)
    except: raise ValueError(f'can\'t change ({value}) to int')
def t_o_S_t_r (value):
    try :  return str(value)
    except: raise ValueError(f'can\'t change ({value}) to str')
def t_o_F_l_o_a_t (value):
    try:  return float(value)
    except: raise ValueError(f'can\'t change ({value}) to float')
def i_s_I_n_t (value):
    if value.__class__.__name__ == 'int':
        return 1
    else:
        return 0
def i_s_S_t_r (value):
    if value.__class__.__name__ == 'str':
        return 1
    else:
        return 0
def i_s_F_l_o_a_t (value):
    if value.__class__.__name__ == 'float':
        return 1
    else:
        return 0

def i_s_L_i_s_t (value):
    if value.__class__.__name__ == 'list':
        return 1
    else:
        return 0

def i_s_D_i_c_t (value):
    if value.__class__.__name__ == 'dict':
        return 1
    else:
        return 0

def n_l_i_s_t (num, z_e_r_o=True):
    d = []
    if z_e_r_o:
        for i in range(0,num+1): d.append(i)
    else:
        for i in range(1,num+1): d.append(i)
    return d

def d_i_r (data):
    lst = []
    #print(dir(data))
    for value in dir(data):
        text=value.replace('__','_C')
        for c in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNMأبتثج'):
            text=text.replace(c,'C')
        text=text[1:]
        text=text.replace('_C','')
        #
        if text == '':
            value = value.replace('أ','@').replace('ب','$').replace('ت','^').replace('ث','~').replace('ج','?')
            if (value[0]=='_') and (value[1] in '1234567890') :
                value = value[1:]
            value = value.replace('__','ة').replace('_','').replace('ة','_')
            #
            lst.append(value)
        elif value in ['__init__','__str__','__repr__','self']:
            dct = {'__init__':'@constructor','__str__':'@string','__repr__':'@repr','self':'@this'}
            lst.append(dct[value])
    return lst


n_l = '\n'
n_o_n_e = None
n_o_t = lambda co:not(co)

# Methods Starts from Here...
def r_e_p_l_a_c_e (DATA,v1,v2):
    if 'str' in DATA.__class__.__name__:
        return DATA.replace(v1,v2)
    else:
        raise ValueError('"replace()" function take only (str) value')
def s_p_l_i_t (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.split(value)
    else:
        raise ValueError('"split()" function take only (str) value')
def e_n_d (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.endswith(value)
    else:
        raise ValueError('"end()" function take only (str) value')
def s_t_a_r_t (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.startswith(value)
    else:
        raise ValueError('"start()" function take only (str) value')
def s_e_a_r_c_h (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.find(value)
    else:
        raise ValueError('"search()" function take only (str) value')
def u_p_c_a_s_e (DATA):
    if ('str' in DATA.__class__.__name__):
        return DATA.upper()
    else:
        raise ValueError('"upcase()" function take only (str) value')
def d_o_w_n_c_a_s_e (DATA):
    if ('str' in DATA.__class__.__name__):
        return DATA.lower()
    else:
        raise ValueError('"downcase()" function take only (str) value')
def s_t_r_i_p (DATA):
    if ('str' in DATA.__class__.__name__):
        return DATA.strip()
    else:
        raise ValueError('"delspace()" function take only (str) value')



# List Function
def l_i_s_t (*arg):
    d = []
    for i in arg: d.append(i)
    return d
# LIST, DICT, STR
def l_e_n_g_t_h (DATA):
    if ('dict' in DATA.__class__.__name__) or ('list' in DATA.__class__.__name__) or ('str' in DATA.__class__.__name__):
        return len(DATA)
    else:
        raise ValueError('"length(DATA)" function take only (dict, list, str) value')
# LIST, DICT, STR
def g_e_t (DATA,*value):
    if (('list' in DATA.__class__.__name__)) or (('dict' in DATA.__class__.__name__)) or ('str' in DATA.__class__.__name__) :
        if len(value)>1:
            if 'dict' in DATA.__class__.__name__: raise ValueError('"get(VAR , value)" function take only (list, str) value')
            return DATA[value[0]:value[1]]
        else:
            return DATA[value[0]]
    else:
        raise ValueError('"get(VAR , *value)" function take only (dict, list, str) value')
# LIST, DICT
def a_p_p_e_n_d (DATA,*arguments):
    if 'list' in DATA.__class__.__name__:
        for i in arguments :
            DATA.append(i)
    elif 'dict' in DATA.__class__.__name__:
        DATA[arguments[0]]=arguments[1]
    else:
        raise ValueError('"append(VAR , value)" function take only (list, dict) value')
# LIST, DICT
def c_l_e_a_r (DATA):
    if (('list' in DATA.__class__.__name__)) or (('dict' in DATA.__class__.__name__)):
        DATA.clear()
        return 1
    else:
        raise ValueError('"clear(VAR)" function take only (list, dict) value')
# LIST, DICT
def d_e_l_e_t_e (DATA,value,i_d_x=False):
    if ('list' in DATA.__class__.__name__):
        if i_d_x and (i_s_I_n_t(value)):
            DATA.pop(value)
        elif i_d_x==False:
            DATA.remove(value)
        else:
            raise ValueError('"dalete(VAR, value, idx=BOOL)" if "idx" = true -> value must be int')
    elif (('dict' in DATA.__class__.__name__)):
        DATA.pop(value)
    else:
        raise ValueError('"delete(VAR , value, idx=BOOL)" function take only (list, dict) value')
    return 1
# LIST, DICT
def a_d_d (DATA,pos,value):
    if (('list' in DATA.__class__.__name__)):
        if not(i_s_I_n_t(pos)):
            raise ValueError('"add(VAR, pos, val)" pos must be int')
        DATA.insert(pos,value)
    elif (('dict' in DATA.__class__.__name__)):
        DATA[pos]=value
    else:
        raise ValueError('"add()" function take only (list, dict) value')
    return 1
# LIST
def i_n_d_e_x (DATA,value):
    if (('list' in DATA.__class__.__name__)):
        return DATA.index(value)
    else:
        raise ValueError('"index(VAR , value)" function take only (list) value')
# LIST
def a_p_p_l_i_s_t (DATA,value):
    if ('list' in DATA.__class__.__name__) and ('list' in value.__class__.__name__):
        DATA.extend(value)
    else:
        raise ValueError('"applist(VAR , value)" function take only (list) values')
    return 1
# LIST, STR
def c_o_u_n_t (DATA,value):
    if (('list' in DATA.__class__.__name__)) or (('str' in DATA.__class__.__name__)):
        return DATA.count(value)
    else:
        raise ValueError('"count(VAR , value)" function take only (list) value')
# LIST
def j_o_i_n (DATA,value):
    if (('list' in DATA.__class__.__name__)):
        return value.join(DATA)
    else:
        raise ValueError('"join(VAR , value)" function take only (list) value')



# Dict Function
def d_i_c_t (**arg):
    dct={}
    for i in arg:
        text=i.replace('__','$').replace('_','').replace('$','_')
        dct[text]=arg[i]
    return dct
# DICT
def k_e_y_s (DATA):
    if (('dict' in DATA.__class__.__name__)):
        return DATA.keys()
    else:
       raise ValueError('"keys(VAR)" function take only (dict) values')
# DICT
def v_a_l_u_e_s (DATA):
    if (('dict' in DATA.__class__.__name__)):
        return DATA.values()
    else:
        raise ValueError('"values(VAR)" function take only (dict) values')

def buildMethods ():
    SetMethod([str],'r_e_p_l_a_c_e',r_e_p_l_a_c_e)
    SetMethod([str],'s_p_l_i_t',s_p_l_i_t)
    SetMethod([str],'e_n_d',e_n_d)
    SetMethod([str],'s_t_a_r_t',s_t_a_r_t)
    SetMethod([str],'s_e_a_r_c_h',s_e_a_r_c_h)
    SetMethod([str],'u_p_c_a_s_e',u_p_c_a_s_e)
    SetMethod([str],'d_o_w_n_c_a_s_e',d_o_w_n_c_a_s_e)
    SetMethod([str],'s_t_r_i_p',s_t_r_i_p)
    SetMethod([str,list,dict],'l_e_n_g_t_h',l_e_n_g_t_h)
    SetMethod([str,list,dict],'g_e_t',g_e_t)
    SetMethod([list,dict],'a_p_p_e_n_d',a_p_p_e_n_d)
    SetMethod([list,dict],'c_l_e_a_r',c_l_e_a_r)
    SetMethod([list,dict],'d_e_l_e_t_e',d_e_l_e_t_e)
    SetMethod([list,dict],'a_d_d',a_d_d)
    SetMethod([list],'i_n_d_e_x',i_n_d_e_x)
    SetMethod([list],'a_p_p_l_i_s_t',a_p_p_l_i_s_t)
    SetMethod([list],'j_o_i_n',j_o_i_n)
    SetMethod([str,list],'c_o_u_n_t',c_o_u_n_t)
    SetMethod([dict],'k_e_y_s',k_e_y_s)
    SetMethod([dict],'v_a_l_u_e_s',v_a_l_u_e_s)
    #SetMethod([str],'',)
threading.Thread(target=buildMethods).start()


def A_s_s_e_r_t_i_o_n_E_R_R (text):
    raise AssertionError(text)
def A_t_t_r_i_b_u_t_e_E_R_R (text):
    raise AttributeError(text)
def E_O_F_E_R_R (text):
    raise EOFError(text)
def F_l_o_a_t_i_n_g_P_o_i_n_t_E_R_R (text):
    raise FloatingPointError(text)
def G_e_n_e_r_a_t_o_r_E_x_i_t (text):
    raise GeneratorExit(text)
def I_m_p_o_r_t_E_R_R (text):
    raise ImportError(text)
def I_n_d_e_x_E_R_R (text):
    raise IndexError(text)
def K_e_y_E_R_R (text):
    raise KeyError(text)
def K_e_y_b_o_a_r_d_I_n_t_e_r_r_u_p_t (text):
    raise KeyboardInterrupt(text)
def M_e_m_o_r_y_E_R_R (text):
    raise MemoryError(text)
def N_a_m_e_E_R_R (text):
    raise NameError(text)
def N_o_t_I_m_p_l_e_m_e_n_t_e_d_E_R_R (text):
    raise NotImplementedError(text)
def O_S_E_R_R (text):
    raise OSError(text)
def O_v_e_r_f_l_o_w_E_R_R (text):
    raise OverflowError(text)
def R_e_f_e_r_e_n_c_e_E_R_R (text):
    raise ReferenceError(text)
def R_u_n_t_i_m_e_E_R_R (text):
    raise RuntimeError(text)
def S_t_o_p_I_t_e_r_a_t_i_o_n (text):
    raise StopIteration(text)
def S_y_n_t_a_x_E_R_R (text):
    raise SyntaxError(text)
def I_n_d_e_n_t_a_t_i_o_n_E_R_R (text):
    raise IndentationError(text)
def T_a_b_E_R_R (text):
    raise TabError(text)
def S_y_s_t_e_m_E_R_R (text):
    raise SystemError(text)
def S_y_s_t_e_m_E_x_i_t (text):
    raise SystemExit(text)
def T_y_p_e_E_R_R (text):
    raise TypeError(text)
def U_n_b_o_u_n_d_L_o_c_a_l_E_R_R (text):
    raise UnboundLocalError(text)
def U_n_i_c_o_d_e_E_R_R (text):
    raise UnicodeError(text)
def U_n_i_c_o_d_e_E_n_c_o_d_e_E_R_R (text):
    raise UnicodeEncodeError(text)
def U_n_i_c_o_d_e_D_e_c_o_d_e_E_R_R (text):
    raise UnicodeDecodeError(text)
def U_n_i_c_o_d_e_T_r_a_n_s_l_a_t_e_E_R_R (text):
    raise UnicodeTranslateError(text)
def V_a_l_u_e_E_R_R (text):
    raise ValueError(text)
def Z_e_r_o_D_i_v_i_s_i_o_n_E_R_R (text):
    raise ZeroDivisionError(text)
def N_e_w_E_R_R (name):
    ss={}
    exec(f'class {name} (Exception):\n\tpass\ndef rrr (text):\n\traise {name}(text)',ss)
    return ss['rrr']