from sly import Lexer
import re

class Lexer(Lexer):
    # Tokens Names
    tokens = { COMMENT, KEYWORD, CO, ID, DOT, FLOAT, INT, STRING, MATH, ASSIGN, 
        LPAREN, RPAREN, LCPAREN, RCPAREN, ENDLINE, COMA}

    # Ignored Characters Between Tokens
    ignore = ' \t'

    # Regex Rules
    COMMENT    = r'//..*|/\*(.*?|\n)*\*/|//|/\**\*'
    CO         = r'true|false|->|==|>|<|<=|>=|!=|\|\||&&|= *=|>|<|< *=|> *=|! *=|\| *\||& *&|- *>'
    ID         = r'[0-9a-zA-Z_@$^~?][0-9a-zA-Z_@$^~?]*|[0-9a-zA-Z_@$^~?]'
    DOT        = r'\.'
    FLOAT      = r'\d+\.\d+'
    INT        = r'\d+|\-\d+'
    MATH       = r'\*\*=|\+=|\-=|/=|\*=|%=|\* *\* *=|\+ *=|\- *=|/ *=|\* *=|% *=|\*\*|\* *\*|\+|\-|%|/|\*'
    ASSIGN     = r'='
    LPAREN     = r'\('
    RPAREN     = r'\)'
    LCPAREN    = r'\{'
    RCPAREN    = r'\}'
    STRING     = r'\'(.*?)\'|"(.*?)"|``(.*?|\n)*``'
    ENDLINE    = r'\n|;'
    COMA       = r','

def main(context):
    context = context.replace('\\"', 'STR_SYM_TWO')
    context = context.replace("\\'", 'STR_SYM_ONE')
    context = context.replace("\\``", 'STR_SYM_THREE')
    lexer = Lexer()
    try:
        end = []
        for tok in lexer.tokenize(context):
            if tok.type == 'ID' and tok.value in ['jump', 'include', 'input', 'write', 'var', 'if', 'elseif', 'else', 'while', 'func', 'break', 'return', 'global', 'for', 'try', 'catch', 'delvar', 'continue', 'class']:
                tok.type = 'KEYWORD'
            if (tok.type == 'ID') and (tok.value in ['string', 'int', 'float', 'list', 'dict']):
                if len(end) > 1:
                    if (end[-1][0] == 'ENDLINE'):
                        tok.type = 'KEYWORD'
                else:
                    tok.type = 'KEYWORD'
            if (tok.type == 'KEYWORD') and (len(end) > 2):
                if (end[-1][0] == 'DOT') or (end[-1][0] == 'LPAREN') or (end[-1][0] == 'COMA'):
                    if tok.value != 'input':
                        tok.type = 'ID'
            if tok.type == 'RCPAREN':
                end.append(['ENDLINE', ';'])
                end.append(['RCPAREN', '}'])
                end.append(['ENDLINE', ';'])
            if tok.type == 'LCPAREN':
                end.append(['ENDLINE', ';'])
                end.append(['LCPAREN', '{'])
                end.append(['ENDLINE', ';'])
            if tok.type == 'ID':
                if re.sub(r'[0-9]*', '', tok.value) == '':
                    end.append(['INT', tok.value])
                else:
                    end.append([tok.type, tok.value])
            else:
                end.append([tok.type, tok.value])
        end.append(['ENDLINE', '\n'])
        return end
    except Exception as err:
        if 'Illegal character' in str(err):
            ERR = str(err)
            try:
                char = re.findall(r"'(.*?)'", ERR)[0]
            except:
                char = re.findall(r'"(.*?)"', ERR)[0]
            index = int(ERR[ERR.find('index '):].replace('index ', ''))
            line = context[0:index].count('\n') + 1
            raise SyntaxError(f'illegal char "{char}" in index {index}, line {line}')
        else:
            raise SyntaxError(str(err))
