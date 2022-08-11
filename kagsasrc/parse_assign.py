import re

def __init__ (value,parseMemory):
    # catch errors
    if 'else :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to try command')
    
    # if |DATA-P| is empty : close it
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|','')
    # this mean the var is opened with assign
    if ('|DATA1|' in parseMemory[5]) and (('= |DATA1|' in parseMemory[5]) or ('= str(|DATA1|)' in parseMemory[5]) or ('= int(|DATA1|)' in parseMemory[5]) or ('= float(|DATA1|)' in parseMemory[5]) or ('= list(|DATA1|)' in parseMemory[5]) or ('= json.loads(|DATA1|)' in parseMemory[5])):
        parseMemory[5]=parseMemory[5].replace(' = ','=').replace('|DATA0|','')

    # if creat/call function in the line
    elif parseMemory[5].startswith('def ') or len(re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*\(',parseMemory[5]))>0 :
        #print(parseMemory[5])
        if '|DATA1|' in parseMemory[5]:
            parseMemory[5]=parseMemory[5].replace('|DATA1|','=|DATA1|')
        else:
            parseMemory[5]=parseMemory[5].replace('|DATA|','=|DATA|')

    else:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown place of assign')

    return parseMemory