import re
from .parse_endl import __init__ as parse_endl
from .parse_cmnt import __init__ as parse_cmnt
from .parse_keyword import __init__ as parse_keyword
from .parse_id import __init__ as parse_id
from .parse_dot_coma import __init__ as parse_dot_coma
from .parse_number import __init__ as parse_number
from .parse_assign import __init__ as parse_assign
from .parse_string import __init__ as parse_string
from .parse_math import __init__ as parse_math
from .parse_paren import __init__ as parse_paren
from .parse_cparen import __init__ as parse_cparen
from .parse_co import __init__ as parse_co

class ParseError (Exception) :pass

def main (data):
    parseMemory = [
        0,     # under_codes        : [0] : Current Codes Blocks (Tab)
        False, # under_codes_holder : [1] : Holder to get a New Block ('if' ,'else' ,'while')
        '',    # last_under_cmnd    : [2] : The Holder Value
        [],    # parsed_input       : [3] : All The Translated Python Codes (list)
        1,     # line               : [4] : The Current Line (used to print in errors)
        '',    # line_items         : [5] : The Line Items (its will be edit and add it to 'parsed_input')
        False  # variable close     : [6] : Is The Variable Assign Closed ?
    ]
    for key,value in data:          # Read All The Lexed Data ( [['key','value']..] )
        if    key == 'ENDLINE':
            parseMemory = parse_endl(value,parseMemory)
        elif  key == 'COMMENT':
            parseMemory = parse_cmnt(value,parseMemory)
        elif  key == 'KEYWORD':
            parseMemory = parse_keyword(value,parseMemory)
        elif  key == 'ID':
            parseMemory = parse_id(value,parseMemory)
        elif (key == 'COMA') or (key == 'DOT'):
            parseMemory = parse_dot_coma(value,parseMemory)
        elif (key == 'INT') or (key == 'FLOAT'):
            parseMemory = parse_number(value,parseMemory)
        elif (key == 'ASSIGN'):
            parseMemory = parse_assign(value,parseMemory)
        elif  key == 'STRING':
            parseMemory = parse_string(value,parseMemory)
        elif  key=='MATH':
            parseMemory = parse_math(value,parseMemory)
        elif (key=='RPAREN') or(key=='LPAREN'):
            parseMemory = parse_paren(value,parseMemory)
        elif (key=='RCPAREN') or(key=='LCPAREN'):
            parseMemory = parse_cparen(value,parseMemory)
        elif  key=='CO':
            parseMemory = parse_co(value,parseMemory)
    #print(parseMemory[3])
    return parseMemory[3]