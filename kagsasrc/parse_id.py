class ParseError (Exception):pass

def __init__ (value,parseMemory):
    # Catch Error
    if 'else :' in parseMemory[5]: # else can't take ID after
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]: # catch can't take ID after
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]: # try can't take ID after
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to try command')
    
    # Replace All The Symbols in The Var Name : @$^~:?
    value = value.replace('@','أ').replace('$','ب').replace('^','ت').replace('~','ث').replace('?','ج')
    
    # Variables that more than 1 Length :
    # my_name   or   my_age
    if (len(value)>2) or (len(value)==2 and not(value.startswith('#'))):
        # Replace From This         To This
        # my_var                    m_y___v_a_r
        value='_'.join(list(value))
    
    # 4h5  =  ID
    # #4  =  ID
    if value[0] in '1234567890' :
        value='_'+value
    
    # catch the words that used in class
    if (value == 'أ_c_o_n_s_t_r_u_c_t_o_r')    : value='__init__' 
    if (value == 'أ_s_t_r_i_n_g')    : value='__str__' 
    if (value == 'أ_r_e_p_r')    : value='__repr__' 
    if (value == 'أ_t_h_i_s')    : value='self' 

    # if function name not set yet
    if '|DATA_N|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA_N|',value)
    # if |DATA-P| not set yet
    elif '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|',value)
    # if |DATA| in line
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')
    # if var name not set yet
    elif '|DATA0|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA0|',value+'|DATA0|')
    # if this is var & is named
    elif '|DATA1|' in parseMemory[5]:
        if parseMemory[6]:
            parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
        else:
            #print(parseMemory)
            raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nVariable opened without assign')
        # line is empty
    elif parseMemory[5]=='':
        parseMemory[5]+=f'{value}|DATA|'
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')

    return parseMemory