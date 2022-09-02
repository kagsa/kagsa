import re



def __init__ (theErr,get_value_back=False, lineno=None):
    # Get Error Text & Type
    ErrStr=str(theErr).replace('<string>','<file>').replace('.',' . ')
    ErrStr=ErrStr.replace('expected an indented block after function definition' , 'empty code block')
    ErrStr=ErrStr.replace('print()' , 'write')
    ErrStr=ErrStr.replace('str()' , 'string variable')
    ErrStr=ErrStr.replace('float()' , 'float variable')
    ErrStr=ErrStr.replace('int()' , 'int variable')
    ErrStr=ErrStr.replace('JSONDecoder.__init__()' , 'json variable')
    ErrStr=ErrStr.replace('list()' , 'list variable')
    ErrStr=ErrStr.replace('input()' , 'input')
    ErrStr=ErrStr.replace('INCLUDE()' , 'include')
    ErrStr=ErrStr.replace('JUMP()' , 'jump')
    ErrType=theErr.__class__.__name__.replace('error','ERR').replace('Error','ERR').replace('compiler.classes.__init__.','').replace('.',' . ')

    if lineno!=None:
        lll = re.findall(r'line \d+',ErrStr)
        for i in lll: ErrStr=ErrStr.replace(i , 'line '+lineno)
    # Start Decoding Texts
    #
    ###########################################################################
    text=ErrStr.replace('(','').replace(')','').replace('"','').replace('\'','')
    text=text.replace('__','_C')
    for c in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNMأبتثج'):
        text=text.replace(c,'C')
    COUNT=-1
    for i in text.split(' '):
        COUNT+=1
        i=i[1:]
        i=i.replace('_C','')
        if i =='':
            ORG=ErrStr.split(' ')[COUNT]
            Org=ErrStr.split(' ')[COUNT].replace('__','ة').replace('_','').replace('ة','_')
            ErrStr=ErrStr.replace(ORG,Org)
    #
    ###########################################################################
    text=ErrType.replace('(','').replace(')','').replace('"','').replace('\'','')
    text=text.replace('__','_C')
    for c in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNMأبتثج'):
        text=text.replace(c,'C')
    COUNT=-1
    for i in text.split(' '):
        COUNT+=1
        i=i[1:]
        i=i.replace('_C','')
        if i =='':
            ORG=ErrType.split(' ')[COUNT]
            Org=ErrType.split(' ')[COUNT].replace('__','ة').replace('_','').replace('ة','_')
            ErrType=ErrType.replace(ORG,Org)
    ###########################################################################
    #
    # Somethings..
    Symbols = {
        'أ' : '@',
        'ب' : '$',
        'ت' : '^',
        'ث' : '~',
        'ج' : '?'
    }
    for i in Symbols.items():
        ErrStr = ErrStr.replace(i[0], i[1])
        ErrType = ErrType.replace(i[0], i[1])
    ErrType=ErrType.replace(' . ','.')
    ErrStr=ErrStr.replace(' . ','.').replace('STR_SYM_TWO','\\"').replace("STR_SYM_ONE","\\'").replace("STR_SYM_THREE","\\``")
    # Return a Values or Print it
    if get_value_back:
        return [ErrType, ErrStr, f'{ErrType} : {ErrStr}']
    else:
        print(f'{ErrType} : {ErrStr}',end='')