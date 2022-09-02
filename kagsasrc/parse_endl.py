def __init__ (value,parseMemory,addline=True):
    # catch some error
    if ('while |DATA| :' in parseMemory[5]) :
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete while sentence')
    if ('for |DATA| :' in parseMemory[5]) :
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete for sentence')
    if ('if |DATA| :' in parseMemory[5]) :
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete if sentence')
    if ('elif |DATA| :' in parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete elseif sentence')
    if ('class |DATA-P| :' in parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete class sentence')
    if ('def ' in parseMemory[5]) and('|DATA_N|' in parseMemory[5]) :
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete function sentence')
    if  ('else' in parseMemory[5]) and not('else :' == parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown error in else sentence')
    if ('except' in parseMemory[5]) and not('except Exception as ERROR :' == parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown error in catch sentence')
    if ('try' in parseMemory[5]) and not('try :' == parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown error in try sentence')
    if ('break' in parseMemory[5]) and not('break' == parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown error in break')
    if ('continue' in parseMemory[5]) and not('continue' == parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown error in continue')
    if ('|DATA0|' in parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete var sentence')
    if ('= |DATA1|' in parseMemory[5]) or ((parseMemory[6] == False) and ('|DATA1|' in parseMemory[5])):
        #print(parseMemory)
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete var sentence')
    if ('print(|DATA|,end=None)' in parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete write sentence')
    if ('global |DATA-P|' in parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete global sentence')
    if ('del |DATA-P|' in parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete delvar sentence')
    

    if parseMemory[1]:  # if There a Holder Add a new Block
        parseMemory[0]+=1
    parseMemory[1]=False
    parseMemory[6]=False
    # if There a Keyword Use a Code Block :
    # Add Line items to 'last_under_cmnd'
    if parseMemory[5].startswith('while') or parseMemory[5].startswith('for') or parseMemory[5].startswith('if') or parseMemory[5].startswith('elseif') or parseMemory[5].startswith('else') or parseMemory[5].startswith('def') or parseMemory[5].startswith('class') or parseMemory[5].startswith('try') or parseMemory[5].startswith('except') :
        parseMemory[2]=str(parseMemory[5])
    # Delete Somthings
    TheData= parseMemory[5].replace('|DATA|','').replace('|DATA1|','').replace('|DATA0|','').replace('|DATA-P|','').replace('|DATA_N|','')
    # Create Comment of The Kagsa Line in Python (this help to get the error from the compiler)
    if TheData.replace('\t','') !='':
        parseMemory[3].append('\t'*parseMemory[0] + TheData + f'    # line {parseMemory[4]}')
    parseMemory[5]='' # Clean Line items
    if addline:
        if value!=';':
            parseMemory[4]+=1 # Add New Line

    return parseMemory