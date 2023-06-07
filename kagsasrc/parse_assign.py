import re

def __init__ (value,parseMemory):

    # catch errors
    if (parseMemory[7] == 'else'):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to else command')
    if (parseMemory[7] == 'catch'):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to catch command')
    if (parseMemory[7] == 'try'):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to try command')
    
    # if |DATA-P| is empty : close it
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|','')
    # this mean the var is opened with assign
    if ('|DATA1|' in parseMemory[5]) and (parseMemory[6] == False):
        parseMemory[6] = True
        parseMemory[5] = parseMemory[5].replace('|DATA0|','')
    # if creat/call function in the line
    elif (parseMemory[5].startswith('def ') or len(re.findall(r'[a-zA-Z0-9]* *\(|[a-zA-Z0-9] *\(',parseMemory[5]))>0) and (parseMemory[5].count('(') > parseMemory[5].count(')')) :
        #print(parseMemory[5])
        if '|DATA1|' in parseMemory[5]:
            parseMemory[5]=parseMemory[5].replace('|DATA1|','=|DATA1|')
        else:
            parseMemory[5]=parseMemory[5].replace('|DATA|','=|DATA|')
    elif (parseMemory[5].count('(') == parseMemory[5].count(')')):
        parseMemory[6] = True
        parseMemory[5] = parseMemory[5].replace('|DATA|','= |DATA1|')
    else:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown place of assign')

    return parseMemory