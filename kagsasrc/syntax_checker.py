import re
def main (data):
    opened_paren=0
    KEYS = ""
    for d in data:
        current_line = KEYS.count("\n")
        # if The TYPE is End Line -> Close The Current Line & Open New One
        # And Check if The Opened Paren == 0
        if d[0] == 'ENDLINE':
            if d[1]!=';' :
                KEYS+='.ENDLINE\n'
            else:
                KEYS+='.SEMICOLON'
            if opened_paren != 0:
                raise SyntaxError(f'invalid syntax (<file>, line {current_line})\nLine ended without close the paren')
            continue
        
        if d[0] == 'COMMENT':
            lines=d[1].count('\n')
            data = '.ENDLINE\n' * lines
            KEYS+=data
        # if There a Open Paren Add 1 to ( opened_paren )
        if d[0]=='LPAREN': # (
            opened_paren+=1
            KEYS+='.'+d[0]
            continue
        
        # if There a Open Paren Minus 1 From ( opened_paren )
        if d[0]=='RPAREN': # )
            if opened_paren == 0:
                raise SyntaxError(f'invalid syntax (<file>, line {current_line})\nLine ended without close the paren')
            opened_paren-=1
            KEYS+='.'+d[0]
            continue
        
        # Add TYPE to a String With (.) Between Them
        if (d[0]=='PLUS') or (d[0]=='MINUS') or (d[0]=='TIMES') or (d[0]=='DIVIDE') :
            KEYS+='.MATH'
        if (d[0]=='KEYWORD' and d[1]=='input'):
            KEYS+='.INPUT'
        if (d[0]=='STRING' and d[1].startswith('``')):
            KEYS+='.'+d[0]
            #current_line+=(d[1].count('\n'))
            #for i in range(1,d[1].count('\n')+1):
            #    lines[str(1)]=''
            lines=d[1].count('\n')
            data = '.ENDLINE\n' * lines
            KEYS+='.'+data
        else:
            KEYS+='.'+d[0]
    
    WrongsSyntax=[
        r'KEYWORD.KEYWORD',
        r'MATH.KEYWORD',
        r'ASSING.KEYWORD',
        r'INT.KEYWORD',
        r'STRING.KEYWORD',
        r'FLOAT.KEYWORD',
        r'CO.KEYWORD',
        r'COMA.KEYWORD',
        r'KEYWORD.ASSING',
        r'KEYWORD.MATH',
        r'STRING.MATH.INT',
        r'INT.MATH.STRING',
        r'STRING.MATH.FLOAT',
        r'FLOAT.MATH.STRING',
        r'STRING.INT',
        r'STRING.FLOAT',
        r'INT.STRING',
        r'FLOAT.STRING',
        r'INT.FLOAT',
        r'FLOAT.INT',
        r'INT.INT',
        r'STRING.STRING',
        r'FLOAT.FLOAT',
        r'DOT.DOT',
        r'MATH.MATH',
        r'COMA.COMA',
        r'STRING.ID',
        r'ID.ID',
        r'INT.ID',
        r'FLOAT.ID',
        r'ASSIGN.COMA',
        r'MATH.COMA',
        r'COMA.ASSIGN',
        r'COMMA.MATH',
        r'LCPAREN.[\n-\.ENDLINE-ENDLINE]*.RCPAREN',
        r'LCPAREN.ENDLINE.RCPAREN'
    ]
    # Checking The Wrong Syntax
    #print(KEYS)
    for w in WrongsSyntax:
        searchForError=re.findall(w,KEYS)
        if len(searchForError) > 0:
            #print(w)
            line = KEYS[  0 :  KEYS.find(searchForError[0])   ].count('\n') + 1
            raise SyntaxError(f'invalid syntax (<file>, line {line})\nError code : {w.lower()}')

    return 1