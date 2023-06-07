
def __init__ (value,parseMemory,addline=True):

    # catch some error
    # ( "|DATA|" , " |DATA|" ) Space before |..| means there is nothing added to data

    # while + for + if + elseif
    co_in_end = ('True ' in parseMemory[5]) or ('False ' in parseMemory[5]) or ('or ' in parseMemory[5]) or ('and ' in parseMemory[5]) or ('in ' in parseMemory[5])
    if (' |DATA|' in parseMemory[5]) and not(co_in_end) and (parseMemory[7] in ['while','for','if','elseif']) :
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\n{parseMemory[7]} sentence is not completed')
    
    # class + global + delvar
    if ('|DATA-P|' in parseMemory[5]) and (parseMemory[7] in ['class','global','delvar']):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\n{parseMemory[7]} sentence is not completed')
    
    # func name
    if (parseMemory[7] == 'func') and('|DATA_N|' in parseMemory[5]) :
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nfunction sentence is not completed')
    
    # else + try + catch
    if  (parseMemory[7] in ['else','try','catch']) and not(f'{parseMemory[7]} :'.replace('catch','except Exception as ERROR') == parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nunknown error in {parseMemory[7]} sentence')
    
    # break + continue
    if (parseMemory[5] in ['break','continue']) and not(parseMemory[7] == parseMemory[5]):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nunknown error in {parseMemory[7]}')
    
    # variable sentence
    var_has_not_items = ('= |DATA1|' in parseMemory[5]) or ('= str(|DATA1|' in parseMemory[5]) or ('= int(|DATA1|' in parseMemory[5]) or ('= float(|DATA1|' in parseMemory[5]) or ('= json.loads(|DATA1|' in parseMemory[5]) or ('= list(|DATA1|' in parseMemory[5])
       # variable didn't named yet                   # is var has an items     # var assign didn't writted
    if (parseMemory[5].startswith('|DATA0|')) or      var_has_not_items     or (not(parseMemory[6]) and ('|DATA1|' in parseMemory[5])):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nvariable sentence is not completed')
    

    if ('print(|DATA|,end=None)' in parseMemory[5]):
        parseMemory[5] = parseMemory[5].replace('|DATA|','\n')
    
    

    if parseMemory[1]:  # if There a Holder Add a new Block
        parseMemory[0]+=1
    parseMemory[1]=False
    parseMemory[6]=False
    # if There a Keyword Use a Code Block :
    # Add Line items to 'last_under_cmnd'
    if (parseMemory[7]==('while')) or parseMemory[7]==('for') or parseMemory[7]==('if') or parseMemory[7]==('elseif') or parseMemory[7]==('else') or parseMemory[7]==('def') or parseMemory[7]==('class') or parseMemory[7]==('try') or parseMemory[7]==('except') :
        parseMemory[2]=str(parseMemory[5])
    # Delete Somthings
    TheData= parseMemory[5].replace('|DATA|','').replace('|DATA1|','').replace('|DATA0|','').replace('|DATA-P|','').replace('|DATA_N|','')
    n=0
    for i in parseMemory[8]:
        TheData=TheData.replace(f'"[{n}]"',i)
        n+=1
    # Create Comment of The Kagsa Line in Python (this help to get the error from the compiler)
    if TheData.replace('\t','') !='':
        parseMemory[3].append('\t'*parseMemory[0] + TheData + f'    # line {parseMemory[4]}')
    parseMemory[5]='' # Clean Line items
    parseMemory[7]='' # Clean Command Type
    parseMemory[8]=[] # Clean Line Strings
    if addline:
        if value!=';':
            parseMemory[4]+=1 # Add New Line

    return parseMemory