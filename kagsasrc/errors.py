import re

def __init__(theErr, get_value_back=False, lineno=None):
    """
    Error Handling and Transformation Module

    This module provides functions for handling and transforming error messages.

    Args:
        theErr (Exception): The exception object to process.
        get_value_back (bool, optional): If True, return the processed error message as a list containing
            the error type, error message, and combined message. If False, print the combined message. Default is False.
        lineno (str, optional): The line number to replace in the error message. Default is None.

    Returns:
        list or None: If `get_value_back` is True, returns a list containing the error type, error message,
            and combined message. If False, returns None.

    Examples:
        >>> try:
        ...     x = 1 / 0
        ... except Exception as e:
        ...     errors.__init__(e)
        ZeroDivisionError : division by zero
    """
    ErrStr = str(theErr).replace('<string>', '<file>')
    ErrStr = ErrStr.replace('expected an indented block after function definition', 'empty code block')
    ErrStr = ErrStr.replace('print()', 'write')
    ErrStr = ErrStr.replace('str()', 'string variable')
    ErrStr = ErrStr.replace('float()', 'float variable')
    ErrStr = ErrStr.replace('int()', 'int variable')
    ErrStr = ErrStr.replace('JSONDecoder.__init__()', 'json variable')
    ErrStr = ErrStr.replace('list()', 'list variable')
    ErrStr = ErrStr.replace('input()', 'input')
    ErrStr = ErrStr.replace('INCLUDE()', 'include')
    ErrStr = ErrStr.replace('JUMP()', 'jump')
    ErrStr = ErrStr.replace('STR_SYM_TWO', '\\"').replace("STR_SYM_ONE", "\\'").replace("STR_SYM_THREE", "\\``")
    ErrType = theErr.__class__.__name__.replace('error', 'ERR').replace('Error', 'ERR').replace('compiler.classes.__init__.', '')
    
    if lineno is not None:
        lll = re.findall(r'line \d+', ErrStr)
        for i in lll:
            ErrStr = ErrStr.replace(i, 'line ' + lineno)
    
    Symbols = {
        'أ': '@',
        'ب': '$',
        'ت': '^',
        'ث': '~',
        'ج': '?'
    }
    
    for symbol, replacement in Symbols.items():
        ErrStr = ErrStr.replace(symbol, replacement)
        ErrType = ErrType.replace(symbol, replacement)
    
    ErrStr_tmp = ErrStr.replace('(', '').replace(')', '').replace('\'', '').replace('"', '').replace('.', ' . ')
    ErrType_tmp = ErrType.replace('.', ' . ')
    
    try:
        for word in [word for word in ErrStr_tmp.split(' ') if not(word[0].isdigit() or word[0] == '_' and not word[1].isdigit() or any([len(char) > 1 for char in word.split('_')]))]:
            new_word = ''.join(word.replace('__', 'ظ').split('_')).replace('ظ', '_')
            ErrStr = ErrStr.replace(word, new_word)
        
        for word in [word for word in ErrType_tmp.split(' ') if not(word[0].isdigit() or word[0] == '_' and not word[1].isdigit() or any([len(char) > 1 for char in word.split('_')]))]:
            new_word = ''.join(word.replace('__', 'ظ').split('_')).replace('ظ', '_')
            ErrStr = ErrStr.replace(word, new_word)
    except:
        None
    
    if get_value_back:
        return [ErrType, ErrStr, f'{ErrType} : {ErrStr}']
    else:
        print(f'{ErrType} : {ErrStr}', end='')
