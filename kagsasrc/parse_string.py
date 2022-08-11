from .parse_id import __init__ as parse_id
import re

def __init__ (value,parseMemory):
    if 'else :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to try command')
    
    # parse the string that have more than 1 line
    if value.startswith('``'):
        value='"""'+value[2:-2]+'"""'
        parseMemory[4]+=value.count('\n')
    
    # Check Formats
    FORMAT=re.findall(r'(%{([0-9a-zA-Z_@$^~?][0-9a-zA-Z_@$^~?]*|#[0-9a-zA-Z_@$^~?])})',value)
    if len(FORMAT) > 0:
        value='f'+value
        for d in FORMAT:
            format_id = parse_id(d[1],[0,False,'',[],1,''])[5].replace('|DATA|','')
            NEW='{'+format_id+'}'
            value=value.replace(d[0],NEW)
    
    value=value.replace('STR_SYM_ONE',"\\'").replace('STR_SYM_TWO','\\"')

    if ('|DATA0|' in parseMemory[5]):
        #print(parseMemory[5])
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nVariable not named yet')
    elif ('|DATA1|' in parseMemory[5] and ' = ' in parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nVariable opened without assign')
    
    elif '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|',value)
    elif ('|DATA1|' in parseMemory[5]):
        parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')

    elif parseMemory[5]=='':
        parseMemory[5]+=f'{value}|DATA|'
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')
    return parseMemory