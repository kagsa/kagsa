from .parse_endl import __init__ as parse_endl

def __init__ (value,parseMemory):
    parseMemory[5] = parseMemory[5].replace('|DATA-P|','')
    if value=='{':
        parseMemory[1]=True
    else:
        parseMemory[1] = False
        if parseMemory[0]==0:
            #print(parsed_input)
            raise SyntaxError('invalid syntax (<file>, line '+str(line)+')\nUnknown place for }')
        parseMemory[0]-=1
    
    parseMemory = parse_endl('\n',parseMemory,addline=False)
    return parseMemory