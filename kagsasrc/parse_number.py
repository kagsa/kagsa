def __init__ (value,parseMemory):
    # catch errors
    if 'else :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to try command')

    if value.replace('0','') != '':
        while True:
            if value.startswith('0'):
                value = value[1:]
            else:
                break
        if value=='':
            raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nNumber Can\'t be zero')

    if ('|DATA0|' in parseMemory[5]):
        #print(parseMemory[5])
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nVariable not named yet')
    # if |DATA-P| not set yet    
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|',value)
    # if |DATA| in line
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')
    # var item bar found
    elif '|DATA1|' in parseMemory[5]:
        if parseMemory[6]:
            parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
        else:
            raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nVariable opened without assign')
                
    elif parseMemory[5]=='':
        parseMemory[5]+=f'{value}|DATA|'
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')
    return parseMemory