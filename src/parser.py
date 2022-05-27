import re

class ParseError (Exception) :
    """Parsing Error Class"""
    pass

def run (data):
    under_codes=0
    under_codes_holder=False
    last_under_cmnd=None
    #
    parsed_input=[]
    #
    line = 1
    line_items=''
    for key,value in data:
        if    key == 'ENDLINE':
            if under_codes_holder:
                under_codes+=1
            under_codes_holder=False
            if line_items.startswith('while') or line_items.startswith('if') or line_items.startswith('elseif') or line_items.startswith('else') or line_items.startswith('def') or line_items.startswith('try') or line_items.startswith('except') :
                last_under_cmnd=str(line_items)
            TheData= line_items.replace('|DATA|','').replace('|DATA1|','').replace('|DATA0|','').replace('|DATA-P|','').replace('|DATA_N|','')
            LineComment = ''
            if TheData!='': LineComment = f'    # The Line {line}'
            parsed_input.append('\t'*under_codes + TheData + LineComment)
            line_items=''
            if value!=';': line+=1
        elif  key == 'KEYWORD':
            if (value!='input') and (line_items!=''):
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nKeysword must be in the first of line')
            if value == 'global':
                line_items='global |DATA-P|'
            if value == 'delvar':
                line_items='del |DATA-P|'
            if value == 'write':
                line_items='print(|DATA|,SET_PRINT_END_AS_NONE)'
            if value == 'input':
                if (len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0) and not('elif ' in line_items) and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items) and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                    line_items=line_items.replace('|DATA1|','input(|DATA-P|)|DATA1|')
                else:
                    if line_items=='':
                        line_items+='|DATA|'
                    line_items=line_items.replace('|DATA|','input(|DATA-P|)|DATA|')
            if value == 'var':
                line_items='|DATA0| = |DATA1|'
            if value == 'try':
                line_items='try :'
            if value == 'catch':
                line_items='except Exception as ERROR :'
            if value == 'for':
                line_items='for |DATA| :'
            if value == 'if':
                line_items='if |DATA| :'
            if value == 'elseif':
                line_items='elif |DATA| :'
            if value == 'while':
                line_items='while |DATA| :'
            if value == 'func':
                line_items='def |DATA_N| |DATA| :'
            if value == 'else':
                line_items='else :'
            if value =='break':
                line_items='break'
            if value =='return':
                line_items='return |DATA|'
        elif  key == 'ID':
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            if (len(value)>2) or (len(value)==2 and not(value.startswith('#'))):
                value='_'.join(list(value))
                if '|DATA_N|' in line_items:
                    line_items=line_items.replace('|DATA_N|',value)
                elif '|DATA-P|' in line_items:
                    line_items=line_items.replace('|DATA-P|',value)
                elif '|DATA|' in line_items:
                    line_items=line_items.replace('|DATA|',f'{value}|DATA|')
                elif len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0 and not('elif ' in line_items) and not('for ' in line_items)and not('else ' in line_items) and not('if ' in line_items)and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')) :
                    if '|DATA0|' in line_items:
                        line_items=line_items.replace('|DATA0|',value)
                    elif '|DATA1|' in line_items:
                        if not(' = ' in line_items):
                            line_items=line_items.replace('|DATA1|',f'{value}|DATA1|')
                        else:
                            raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
                    else:
                        raise ParseError(f'can\'t parsing (<file>, line {line})')
                elif line_items=='':
                    line_items+=f'{value}|DATA|'
                else:
                    raise ParseError(f'can\'t parsing (<file>, line {line})')
            else:
                if value[1:]=='':
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nUse # before Variable name')
                if '|DATA_N|' in line_items:
                    line_items=line_items.replace('|DATA_N|',value[1:])
                elif '|DATA-P|' in line_items:
                    line_items=line_items.replace('|DATA-P|',value[1:])
                elif '|DATA|' in line_items:
                    line_items=line_items.replace('|DATA|',f'{value[1:]}|DATA|')
                elif len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0 and not('elif ' in line_items)and not('for ' in line_items) and not('else ' in line_items) and not('if ' in line_items)and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                        if '|DATA0|' in line_items:
                            line_items=line_items.replace('|DATA0|',value[1:])
                        elif '|DATA1|' in line_items:
                            if not(' = ' in line_items):
                                line_items=line_items.replace('|DATA1|',f'{value[1:]}|DATA1|')
                            else:
                                raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
                        else:
                            raise ParseError(f'can\'t parsing (<file>, line {line})')
                elif line_items=='':
                    line_items+=f'{value[1:]}|DATA|'
                else:
                    raise ParseError(f' can\'t parsing (<file>, line {line})')
        elif (key == 'COMA') or (key == 'DOT'):
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            if '|DATA-P|' in line_items:
                line_items=line_items.replace('|DATA-P|','')
            if '|DATA|' in line_items:
                line_items=line_items.replace('|DATA|',f'{value}|DATA|')
            elif (len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0)and not('for ' in line_items) and not('elif ' in line_items)and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                if ('|DATA0|' in line_items) or (not('|DATA1|' in line_items)):
                    raise ParseError(f'can\'t parsing (<file>, line {line})')
                else:
                    line_items=line_items.replace('|DATA1|',f'{value}|DATA1|')
            else:
                raise ParseError(f'can\'t parsing (<file>, line {line})')
        elif (key == 'INT') or (key == 'FLOAT'):
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            if '|DATA-P|' in line_items:
                line_items=line_items.replace('|DATA-P|',value)
            elif '|DATA|' in line_items:
                line_items=line_items.replace('|DATA|',f'{value}|DATA|')
            elif len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0 and not('for ' in line_items) and not('elif ' in line_items)and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                if not(' = ' in line_items):
                    if ('|DATA0|' in line_items) or (not('|DATA1|' in line_items)):
                        raise ParseError(f'can\'t parsing (<file>, line {line})')
                    else:
                        line_items=line_items.replace('|DATA1|',f'{value}|DATA1|')
                else:
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
        elif (key == 'ASSIGN'):
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            if '|DATA-P|' in line_items:
                line_items=line_items.replace('|DATA-P|','')
            elif ((len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0) and not('for ' in line_items) and not('elif ' in line_items)and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)) or ('= |DATA1|' in line_items) and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                if '= |DATA1|' in line_items :
                    line_items=line_items.replace(' = ','=')
                else:
                    line_items=line_items.replace('|DATA1|','=|DATA1|')
            elif line_items.startswith('def '):
                if '|DATA_N|' in line_items:
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete function basic :\nfunc NAME (PARAMETERS){"{"+"}"}')
                else:
                    line_items=line_items.replace('|DATA|','=|DATA|')
            else:
                if '(' in line_items:
                    line_items=line_items.replace('|DATA|','=|DATA|')
                else:
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nUnknown place of assign')
        elif  key == 'STRING':
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            if value.startswith('``'):
                value='"""'+value[2:-2]+'"""'
                line+=value.count('\n')
                #print(value.count('\n'))
            STR_PARSED=value
            FORMAT=re.findall(r'(%{([_A-Za-z][0-9a-zA-Z_]*|#[a-zA-Z_])})',STR_PARSED)
            if len(FORMAT) > 0:
                STR_PARSED='f'+STR_PARSED
                for d in FORMAT:
                    format_id = None
                    if d[1].startswith('#') and len(d[1])==2:
                        format_id= d[1][1:]
                    else:
                        format_id= '_'.join(list(d[1]))
                    NEW='{'+format_id+'}'
                    STR_PARSED=STR_PARSED.replace(d[0],NEW)
            STR_PARSED=STR_PARSED.replace('STR_SYM_ONE',"\\'").replace('STR_SYM_TWO','\\"')
            value1=STR_PARSED
            if len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0:
                if (' = ' in line_items) and not('elif ' in line_items)and not('for ' in line_items) and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
                else:
                    if '|DATA-P|' in line_items:
                        line_items=line_items.replace('|DATA-P|',value1)
                    else:
                        if not('elif ' in line_items)and not('for ' in line_items) and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                            line_items=line_items.replace('|DATA1|',f'{value1}|DATA1|')
                        else:
                            line_items=line_items.replace('|DATA|',f'{value1}|DATA|')
            else:
                if '|DATA-P|' in line_items:
                    line_items=line_items.replace('|DATA-P|',value1)
                else:
                    line_items=line_items.replace('|DATA|',f'{value1}|DATA|')
        elif  key=='MATH':
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            if '|DATA-P|' in line_items:
                line_items=line_items.replace('|DATA-P|','')
            # r'(([_A-Za-z][0-9a-zA-Z_]*|#[a-zA-Z_]*) = (.*?))'
            if len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0:
                if ((' = ' in line_items)) and not('elif ' in line_items)and not('for ' in line_items) and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
                else:
                    line_items=line_items.replace('|DATA1|',f'{value}|DATA1|')
            else:
                line_items=line_items.replace('|DATA|',f'{value}|DATA|')
        elif (key=='RPAREN') or(key=='LPAREN'):
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            if '|DATA-P|' in line_items:
                line_items=line_items.replace('|DATA-P|','')
            if '|DATA|' in line_items:
                line_items=line_items.replace('|DATA|',f'{value}|DATA|')
            elif (len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0) and not('for ' in line_items) and not('elif ' in line_items)and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)and not(line_items.startswith('def ')) and not(line_items.startswith('try ')) and not(line_items.startswith('except ')):
                if not(' = ' in line_items):
                    if ('|DATA0|' in line_items) or (not('|DATA1|' in line_items)):
                        raise ParseError(f'can\'t parsing (<file>, line {line})')
                    else:
                        line_items=line_items.replace('|DATA1|',f'{value}|DATA1|')
                else:
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
        elif (key=='RCPAREN') or(key=='LCPAREN'):
            if ('|DATA-P|' in line_items):
                line_items=line_items.replace('|DATA-P|','')
            if key=='LCPAREN': #  {
                if ('if' in line_items) or ('elif' in line_items) or ('for' in line_items) or ('while' in line_items) or ('def ' in line_items) or ('try ' in line_items):
                    if ('while |DATA| :' in line_items) :
                        raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete while command')
                    if ('for |DATA| :' in line_items) :
                        raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete for command')
                    if ('if |DATA| :' in line_items) :
                        raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete if command')
                    elif ('elseif |DATA| :' in line_items):
                        raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete elseif command')
                    elif ('def ' in line_items) and('|DATA_N|' in line_items) :#or (' |DATA|' in line_items):
                        raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete function basic')
                    under_codes_holder=True
                elif ('else' in line_items):
                    if not('else :' in line_items):
                       raise SyntaxError(f'invalid syntax (<file>, line {line})\nUnknown error in else command')
                    under_codes_holder=True
                elif ('except' in line_items):
                    if not('except Exception as ERROR :' in line_items):
                        raise SyntaxError(f'invalid syntax (<file>, line {line})\nUnknown error in catch command')
                    under_codes_holder=True
                else:
                    if last_under_cmnd.startswith('while') or last_under_cmnd.startswith('try') or last_under_cmnd.startswith('except') or last_under_cmnd.startswith('for') or last_under_cmnd.startswith('if') or last_under_cmnd.startswith('elseif') or last_under_cmnd.startswith('else') or last_under_cmnd.startswith('def'):
                        if ('while |DATA| :' in last_under_cmnd):
                            raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete while command')
                        if ('for |DATA| :' in last_under_cmnd):
                            raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete for command')
                        elif ('if |DATA| :' in last_under_cmnd):
                            raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete if command')
                        elif ('def ' in last_under_cmnd) and('|DATA_N|' in last_under_cmnd) or (' |DATA|' in last_under_cmnd):
                            raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete function basic')
                        elif ('elseif |DATA| :' in last_under_cmnd):
                            raise SyntaxError(f'invalid syntax (<file>, line {line})\nTry to complete elseif command')
                        else:
                            under_codes_holder=True
            else: #  }
                if under_codes==0:
                    #print(parsed_input)
                    raise SyntaxError('invalid syntax (<file>, line '+line+')\nUnknown place for \'}\'')
                under_codes-=1
            ##############
            if line_items.startswith('while') or line_items.startswith('try') or line_items.startswith('except') or line_items.startswith('for') or line_items.startswith('if') or line_items.startswith('elseif') or line_items.startswith('else') or line_items.startswith('def'):
                last_under_cmnd=str(line_items)
            #line+=1
            TheData= line_items.replace('|DATA|','').replace('|DATA1|','').replace('|DATA0|','').replace('|DATA-P|','').replace('|DATA_N|','')
            LineComment = ''
            if TheData!='': LineComment = f'    # The Line {line}'
            parsed_input.append('\t'*under_codes + TheData + LineComment)
            line_items=''
            if under_codes_holder:
                under_codes+=1
            under_codes_holder=False
            ##############
        elif  key=='CO':
            if 'else :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
            if 'except Exception as ERROR :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
            if 'try :' in line_items:
                raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
            value=value.replace(' ','')
            CO_DICT={
                '->':' in ',
                '<=':'<=',
                '>=':'>=',
                '==':'==',
                '<':'<',
                '>':'>',
                '!=':'!=',
                '||':' or ',
                '&&':' and ',
                'true':' True ',
                'false':' False '
            }
            if len(re.findall(r'(.*?)=(.*?)\|DATA1\|',line_items))>0 and not('for ' in line_items) and not('elif ' in line_items)and not('else ' in line_items) and not('if ' in line_items) and not('while ' in line_items)and not('def ' in line_items) and not('try ' in line_items)and not('except ' in line_items):
                if not(' = ' in line_items):
                    if ('|DATA0|' in line_items) or (not('|DATA1|' in line_items)):
                        if '(' in line_items:
                            line_items=line_items.replace('|DATA|',f'{CO_DICT[value]}|DATA|')
                        else:
                            raise ParseError(f'can\'t parsing (<file>, line {line})')
                    if (' = ' in line_items):
                        if not(line_items.startswith('def ')):
                            raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
                    else:
                        line_items=line_items.replace('|DATA1|',f'{CO_DICT[value]}|DATA1|')
                else:
                    raise SyntaxError(f'invalid syntax (<file>, line {line})\nVariable opened without assign')
            else:
                line_items=line_items.replace('|DATA|',f'{CO_DICT[value]}|DATA|')
    return parsed_input