class ParseError (Exception):pass

def __init__ (value,parseMemory):

    # if any keyword (except 'input') did not writted in line start
    if (value!='input') and (parseMemory[5]!=''):
        print(parseMemory[5])
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nKeywords must be in the first of line')
    if value == 'jump':
        parseMemory[5]='JUMP(|DATA-P|)'
        parseMemory[7]='jump'
    if value == 'include':
        parseMemory[5]='INCLUDE(|DATA-P|)'
        parseMemory[7]='include'
    # Add The Keyword To The Line
    if value == 'global':
        parseMemory[5]='global |DATA-P|'
        parseMemory[7]='global'
    if value == 'delvar':
        parseMemory[5]='del |DATA-P|'
        parseMemory[7]='delvar'
    if value == 'write':
        parseMemory[5]='print(|DATA|,end="")'
        parseMemory[7]='write'
    if value == 'input':
        # if it writted in var : add it and complete after it (|DATA1|)
        if ('|DATA1|' in parseMemory[5]):
            parseMemory[5]=parseMemory[5].replace('|DATA1|','input(|DATA-P|)|DATA1|')
        else:
            # if the line is empty add |DATA| to start write codes
            if parseMemory[5]=='':
                parseMemory[5]+='|DATA|'
            # if it didn't writted in var : add it and complete after it (|DATA|)
            if '|DATA|' in parseMemory[5]:
                parseMemory[5]=parseMemory[5].replace('|DATA|','input(|DATA-P|)|DATA|')
            else:
                raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')
    if value == 'var':
        # |DATA0|  :  Variable Name
        # |DATA1|  :  Variable items
        parseMemory[5]='|DATA0| = |DATA1|'
        parseMemory[7]='var'
    if value == 'string':
        parseMemory[5]='|DATA0| = str(|DATA1|)'
        parseMemory[7]='string'
    if value == 'int':
        parseMemory[5]='|DATA0| = int(|DATA1|)'
        parseMemory[7]='int'
    if value == 'float':
        parseMemory[5]='|DATA0| = float(|DATA1|)'
        parseMemory[7]='float'
    if value == 'dict':
        parseMemory[5]='|DATA0| = json.loads(|DATA1|)'
        parseMemory[7]='dict'
    if value == 'list':
        parseMemory[5]='|DATA0| = list(|DATA1|)'
        parseMemory[7]='list'
    
    if value == 'try':
        parseMemory[5]='try :'
        parseMemory[7]='try'
    if value == 'catch':
        # Get Error Out as 'ERROR'
        parseMemory[5]='except Exception as ERROR :'
        parseMemory[7]='catch'
    if value == 'for':
        parseMemory[5]='for |DATA| :'
        parseMemory[7]='for'
    if value == 'if':
        parseMemory[5]='if |DATA| :'
        parseMemory[7]='if'
    if value == 'elseif':
        parseMemory[5]='elif |DATA| :'
        parseMemory[7]='elseif'
    if value == 'while':
        parseMemory[5]='while |DATA| :'
        parseMemory[7]='while'
    if value == 'func':
        # |DATA_N|  :  Function Name
        parseMemory[5]='def |DATA_N| |DATA| :'
        parseMemory[7]='func'
    if value == 'class':
        parseMemory[5]='class |DATA-P| :'
        parseMemory[7]='class'
    if value == 'else':
        parseMemory[5]='else :'
        parseMemory[7]='else'
    if value =='break':
        parseMemory[5]='break'
        parseMemory[7]='break'
    if value =='continue':
        parseMemory[5]='continue'
        parseMemory[7]='continue'
    if value =='return':
        parseMemory[5]='return |DATA|'
        parseMemory[7]='return'
    
    return parseMemory