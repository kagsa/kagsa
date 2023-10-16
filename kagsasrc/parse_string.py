from .parse_id import __init__ as parse_id
from .parse_sformat import __init__ as parse_sformat
import re

class ParseError(Exception):
    pass

def __init__(value, parseMemory):
    if parseMemory[7] == 'else':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to else command')

    if parseMemory[7] == 'catch':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to catch command')

    if parseMemory[7] == 'try':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to try command')

    if value.startswith('``'):
        value = '"""' + value[2:-2] + '"""'
        parseMemory[4] += value.count('\n')

    FORMAT = re.findall(r'(%{(.*?)})', value)
    if len(FORMAT) > 0:
        value = 'f' + value
        for d in FORMAT:
            format_id = parse_sformat(d[1])
            NEW = '{' + format_id + '}'
            value = value.replace(d[0], NEW)

    value = value.replace("\\'", "''").replace('\\"', '\\"')

    string_idx = len(parseMemory[8])
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA-P|', f'"[{string_idx}]"')

    elif '|DATA|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace(
            '|DATA|', f'"[{string_idx}]"|DATA|')

    elif '|DATA0|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace(
            '|DATA0|', f'"[{string_idx}]"|DATA0|')

    elif '|DATA1|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace(
            '|DATA1|', f'"[{string_idx}]"|DATA1|')

    elif parseMemory[5] == '':
        parseMemory[5] += f'"[{string_idx}]"|DATA|'

    parseMemory[8].append(value)
    return parseMemory
