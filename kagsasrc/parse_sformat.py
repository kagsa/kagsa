from .lexer import main as Lexer
from .paths import Paths as Paths
import re

Paths.init()

def __init__ (value):
    parse_string = Paths.getFile('parse_string.py','r').read().replace('from .parse_sformat import __init__ as parse_sformat','')
    space = dict(
        parse_sformat=globals()['__init__'],
        **globals()
    )
    exec(parse_string,space)
    parse_string = space['__init__']
    space = dict(
        parse_sformat=globals()['__init__'],
        parse_string=parse_string,
        **globals()
    )
    parser = Paths.getFile('parser.py','r').read().decode('utf-8').replace('from .parse_string import __init__ as parse_string','')
    exec(parser,space)
    lex   = Lexer(value)
    parse = space['main'](lex)
    parse = '\n'.join(parse)
    parse = parse.replace('STR_SYM_TWO','\\"' ).replace('STR_SYM_ONE',"\\'" ).replace('STR_SYM_THREE',"``")
    parse = parse.replace(re.findall(r'    # line \d+',parse)[0],'')
    return parse.replace('\n','')