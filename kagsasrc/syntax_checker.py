import re

def main(data):
    opened_paren = 0
    KEYS = ""
    current_line = 1

    for d in data:
        if d[0] == 'ENDLINE':
            if d[1] != ';':
                KEYS += '.ENDLINE\n'
            else:
                KEYS += '.SEMICOLON'
            if opened_paren != 0:
                raise SyntaxError(
                    f'invalid syntax (<file>, line {current_line})\nLine ended without closing the parenthesis')
            continue

        if d[0] == 'COMMENT':
            lines = d[1].count('\n')
            data = '.ENDLINE\n' * lines
            KEYS += data

        if d[0] == 'LPAREN':
            opened_paren += 1
            KEYS += '.' + d[0]
            continue

        if d[0] == 'RPAREN':
            if opened_paren == 0:
                raise SyntaxError(
                    f'invalid syntax (<file>, line {current_line})\nLine ended without closing the parenthesis')
            opened_paren -= 1
            KEYS += '.' + d[0]
            continue

        KEYS += '.' + d[0]

        if d[0] == 'ENDLINE':
            current_line += 1

    WrongsSyntax = [
        r'KEYWORD.KEYWORD',
        r'MATH.KEYWORD',
        r'ASSIGN.KEYWORD',
        r'INT.KEYWORD',
        r'STRING.KEYWORD',
        r'FLOAT.KEYWORD',
        r'CO.KEYWORD',
        r'COMA.KEYWORD',
        r'KEYWORD.ASSIGN',
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

    for w in WrongsSyntax:
        search_for_error = re.findall(w, KEYS)
        if len(search_for_error) > 0:
            line = KEYS[:KEYS.find(search_for_error[0])].count('\n') + 1
            raise SyntaxError(
                f'invalid syntax (<file>, line {line})\nError code: {w.lower()}')

    return 1
