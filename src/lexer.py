from sly import Lexer
import re

class Lexer(Lexer):
    # Tokens Names
    tokens = { COMMENT, KEYWORD, CO, ID, DOT, FLOAT, INT, STRING, MATH, ASSIGN, 
        LPAREN, RPAREN, LCPAREN, RCPAREN, ENDLINE, COMA}

    # Ignored Characters Between Tokens
    ignore = ' \t'

    # Regex Rules
    COMMENT    = r'//..*|/\*(.*?|\n)*\*/'
    KEYWORD    = r'input|write|var|if|elseif|else|while|func|break|return|global|for|try|catch|delvar'
    CO         = r'true|false|->|==|>|<|<=|>=|!=|\|\||&&|= *=|>|<|< *=|> *=|! *=|\| *\||& *&|- *>'
    ID         = r'[_A-Za-z][0-9a-zA-Z_]*|#[a-zA-Z_]*'
    DOT        = r'\.'
    FLOAT      = r'\d+\.\d+'
    INT        = r'\d+|\-\d+'
    MATH       = r'\+=|\-=|/=|\*=|\+ *=|\- *=|/ *=|\* *=|\*\*|\* *\*|\+|\-|%|/|\*'
    ASSIGN     = r'='
    LPAREN     = r'\('
    RPAREN     = r'\)'
    LCPAREN    = r'\{'
    RCPAREN    = r'\}'
    STRING     = r'\'(.*?)\'|"(.*?)"|``(.*?|\n)*``'
    ENDLINE    = r'\n|;'
    COMA       = r','


def run (context) :
    context=context.replace('\\"','STR_SYM_TWO')
    context=context.replace("\\'",'STR_SYM_ONE')
    context=context.replace("\\``",'STR_SYM_THREE')
    lexer = Lexer()
    try:
        end=[]
        # Start Lexeing Loop and Get Outout
        for tok in lexer.tokenize(context):
            # myfile = File.write('f.txt');
            # Write Fuunc     ^
            # Will Be Lexed as ID
            if (tok.type=='KEYWORD') and (len(end) > 2):
                if (end[-1][0] == 'DOT') and (end[-2][0] == 'ID'):
                    end.append(['ID',tok.value])
                    continue
            # if true {
            #   write 'ok\n';  }else{
            #   write 'err\n';
            # }
            if tok.type=='RCPAREN':
                end.append(['ENDLINE',';'])
                end.append(['RCPAREN','}'])
                end.append(['ENDLINE',';'])
                continue
            end.append([tok.type,tok.value])
        # End Loop
        end.append(['ENDLINE','\n'])
        #print(end)
        return end
    except Exception as err:
        # Return a Illegal Character Error
        if 'Illegal character' in str(err):
            ERR=str(err)
            try:
                char=re.findall(r"'(.*?)'",ERR)[0]
            except:
                char=re.findall(r'"(.*?)"',ERR)[0]
            index=ERR[ERR.find('index '):].replace('index ','')
            line=context.count('\n')+1
            raise SyntaxError(f'Iillegal Char "{char}" in Index {index}, line {line}')
        # Return a Unknown Error
        else:
            raise SyntaxError('Maybe a Lexing Error')