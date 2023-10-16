class ParseError(Exception):
    pass

def __init__(value, parseMemory):
    if parseMemory[7] == 'else':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to else command')
    if parseMemory[7] == 'catch':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to catch command')
    if parseMemory[7] == 'try':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to try command')

    value = value.replace('@', 'أ').replace('$', 'ب').replace('^', 'ت').replace('~', 'ث').replace('?', 'ج')

    if len(value) > 2 or (len(value) == 2 and not value.startswith('#')):
        value = '_'.join(list(value))

    if value[0] in '1234567890':
        value = '_' + value

    if value == 'أ_c_o_n_s_t_r_u_c_t_o_r':
        value = '__init__'
    if value == 'أ_s_t_r_i_n_g':
        value = '__str__'
    if value == 'أ_r_e_p_r':
        value = '__repr__'
    if value == 'أ_t_h_i_s':
        value = 'self'

    if '|DATA_N|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA_N|', value)
    elif '|DATA-P|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA-P|', value)
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA|', value + '|DATA|')
    elif '|DATA0|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA0|', value + '|DATA0|')
    elif '|DATA1|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA1|', value + '|DATA1|')
    elif parseMemory[5] == '':
        parseMemory[5] += value + '|DATA|'
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')

    return parseMemory
