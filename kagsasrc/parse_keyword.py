class ParseError (Exception):pass

def __init__ (value,parseMemory):
    # if any keyword (except 'input') did not writted in line start
    if (value!='input') and (parseMemory[5]!=''):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nKeywords must be in the first of line')
    if value == 'jump':
        parseMemory[5]='JUMP(|DATA-P|)'
    if value == 'include':
        parseMemory[5]='INCLUDE(|DATA-P|)'
    # Add The Keyword To The Line
    if value == 'global':
        parseMemory[5]='global |DATA-P|'
    if value == 'delvar':
        parseMemory[5]='del |DATA-P|'
    if value == 'write':
        parseMemory[5]='print(|DATA|,end="")'
    if value == 'input':
        # if it writted in var : add it and complete after it (|DATA1|)
        if ('|DATA1|' in parseMemory[5]):
            parseMemory[5]=parseMemory[5].replace('|DATA1|','input(|DATA-P|)|DATA1|')
        else:
            # if the line is empty add |DATA| to start write codes
            if parseMemory[5]=='':
                parseMemory[5]+='|DATA|'
            # if it didn't writted in var : add it and complete after it (|DATA|)
            if '|DATA|' in parseMemory:
                parseMemory[5]=parseMemory[5].replace('|DATA|','input(|DATA-P|)|DATA|')
            else:
                raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')
    if value == 'var':
        # |DATA0|  :  Variable Name
        # |DATA1|  :  Variable items
        parseMemory[5]='|DATA0| = |DATA1|'
    if value == 'string':
        parseMemory[5]='|DATA0| = str(|DATA1|)'
    if value == 'int':
        parseMemory[5]='|DATA0| = int(|DATA1|)'
    if value == 'float':
        parseMemory[5]='|DATA0| = float(|DATA1|)'
    if value == 'dict':
        parseMemory[5]='|DATA0| = json.loads(|DATA1|)'
    if value == 'list':
        parseMemory[5]='|DATA0| = list(|DATA1|)'
    
    if value == 'try':
        parseMemory[5]='try :'
    if value == 'catch':
        # Get Error Out as 'ERROR'
        parseMemory[5]='except Exception as ERROR :'
    if value == 'for':
        parseMemory[5]='for |DATA| :'
    if value == 'if':
        parseMemory[5]='if |DATA| :'
    if value == 'elseif':
        parseMemory[5]='elif |DATA| :'
    if value == 'while':
        parseMemory[5]='while |DATA| :'
    if value == 'func':
        # |DATA_N|  :  Function Name
        parseMemory[5]='def |DATA_N| |DATA| :'
    if value == 'class':
        parseMemory[5]='class |DATA-P| :'
    if value == 'else':
        parseMemory[5]='else :'
    if value =='break':
        parseMemory[5]='break'
    if value =='continue':
        parseMemory[5]='continue'
    if value =='return':
        parseMemory[5]='return |DATA|'
    
    return parseMemory