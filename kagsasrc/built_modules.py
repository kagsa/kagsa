import os,platform,subprocess,base64,sys,re,requests,json,random,time,datetime,keyboard
from .methods import *

#

P_A_T_H = sys.path

class W_e_b:
    class HTMLError (Exception):pass
    def s_c_r_i_p_t (data):
        return f'<script>{data}</script>'
    def b_o_x (data):
        data = data.replace('"','\\"')
        print(f'<script>alert("{data}")</script>')
    class H_T_M_L_E_l_e_m_e_n_t:
        def __init__ (self,inner,outer):
            self.i_n_n_e_r_H_T_M_L = C_o_d_e.b_a_s_e_6_4.d_e_c_o_d_e(inner)
            self.o_u_t_e_r_H_T_M_L = C_o_d_e.b_a_s_e_6_4.d_e_c_o_d_e(outer)
    class E_l_e_m_e_n_t:
        def __init__ (self,tagName,n,innerHTML,**attrs):
            self.t_a_g_N_a_m_e = tagName
            if not(n in [1,2,'1','2']):
                raise W_e_b.HTMLError('Element(tagName, n, innerHTML, **attrs) n must be 1 or 2')
            self.n = n
            self.a_t_t_r_s = attrs
            self.i_n_n_e_r_H_T_M_L = innerHTML
        def __str__ (self):
            d = ''
            if self.n == 1:
                d = f'<{self.t_a_g_N_a_m_e} _DATA_>'
            else:
                d = f'<{self.t_a_g_N_a_m_e} _DATA_>{self.i_n_n_e_r_H_T_M_L}</{self.t_a_g_N_a_m_e}>'
            for i,j in self.a_t_t_r_s.items():
                j =j.replace('"','\\"')
                i=i.replace('__','ة').replace('_','').replace('ة','_')
                d=d.replace('_DATA_',f'{i}="{j}" _DATA_')
            d=d.replace(' _DATA_','')
            return d
    class i_n_p_u_t_s:
        inp = {}
        def s_e_t (selector,htmlclass):
            W_e_b.i_n_p_u_t_s.inp[selector] = htmlclass
        def g_e_t (selector):
            if selector in W_e_b.i_n_p_u_t_s.inp.keys():
                return W_e_b.i_n_p_u_t_s.inp[selector]
            else:
                raise W_e_b.HTMLError(f"{selector} is not denfined")
        def e_d_i_t (selector,**data):
            o = "<script>_DATA_</script>"
            for i,j in data.items():
                i=i.replace('__','ة').replace('_','').replace('ة','_')
                j = j.replace('"','\\"')
                o = o.replace('_DATA_', f'document.querySelector("{selector}").{i} = "{j}";_DATA_')
            o = o.replace('_DATA_','')
            print(o)
        


class K_e_y_b_o_a_r_d:
    class KeyboardError (Exception) :pass
    def w_a_i_t (text):
        try:
            keyboard.wait(text)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
    def w_r_i_t_e (text):
        try:
            keyboard.write(text)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
    def n_e_w_H_o_t_k_e_y (text, func):
        try:
            keyboard.add_hotkey(text, func)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
    class r_e_c_o_r_d:
        def __init__ (self,u_n_t_i_l=''):
            try:
                self.record = keyboard.record(until= u_n_t_i_l)
                self.g_e_t = []
                for i in self.record:
                    self.g_e_t.append(str(i).replace('KeyboardEvent(','')[0:-1])
            except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
        def p_l_a_y_A_l_l (self,s_p_e_e_d=0.5):
            keyboard.play(self.record, speed_factor = s_p_e_e_d)
    def p_r_e_s_s (text):
        try:
            keyboard.press_and_release(text)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))


class M_a_t_h:
    def a_c_o_s (*arg) :
        return math.acos(*arg)
    def a_c_o_s_h (*arg) :
        return math.acosh(*arg)
    def a_s_i_n (*arg) :
        return math.asin(*arg)
    def a_s_i_n_h (*arg) :
        return math.asinh(*arg)
    def a_t_a_n (*arg) :
        return math.atan(*arg)
    def a_t_a_n_2 (*arg) :
        return math.atan2(*arg)
    def a_t_a_n_h (*arg) :
        return math.atanh(*arg)
    def c_e_i_l (*arg) :
        return math.ceil(*arg)
    def c_o_m_b (*arg) :
        return math.comb(*arg)
    def c_o_p_y_s_i_g_n (*arg) :
        return math.copysign(*arg)
    def c_o_s (*arg) :
        return math.cos(*arg)
    def c_o_s_h (*arg) :
        return math.cosh(*arg)
    def d_e_g_r_e_e_s (*arg) :
        return math.degrees(*arg)
    def d_i_s_t (*arg) :
        return math.dist(*arg)
    def e (*arg) :
        return math.e(*arg)
    def e_r_f (*arg) :
        return math.erf(*arg)
    def e_r_f_c (*arg) :
        return math.erfc(*arg)
    def e_x_p (*arg) :
        return math.exp(*arg)
    def e_x_p_m_1 (*arg) :
        return math.expm1(*arg)
    def f_a_b_s (*arg) :
        return math.fabs(*arg)
    def f_a_c_t_o_r_i_a_l (*arg) :
        return math.factorial(*arg)
    def f_l_o_o_r (*arg) :
        return math.floor(*arg)
    def f_m_o_d (*arg) :
        return math.fmod(*arg)
    def f_r_e_x_p (*arg) :
        return math.frexp(*arg)
    def f_s_u_m (*arg) :
        return math.fsum(*arg)
    def g_a_m_m_a (*arg) :
        return math.gamma(*arg)
    def g_c_d (*arg) :
        return math.gcd(*arg)
    def h_y_p_o_t (*arg) :
        return math.hypot(*arg)
    def i_n_f (*arg) :
        return math.inf(*arg)
    def i_s_c_l_o_s_e (*arg) :
        return math.isclose(*arg)
    def i_s_f_i_n_i_t_e (*arg) :
        return math.isfinite(*arg)
    def i_s_i_n_f (*arg) :
        return math.isinf(*arg)
    def i_s_n_a_n (*arg) :
        return math.isnan(*arg)
    def i_s_q_r_t (*arg) :
        return math.isqrt(*arg)
    def l_c_m (*arg) :
        return math.lcm(*arg)
    def l_d_e_x_p (*arg) :
        return math.ldexp(*arg)
    def l_g_a_m_m_a (*arg) :
        return math.lgamma(*arg)
    def l_o_g (*arg) :
        return math.log(*arg)
    def l_o_g_1_0 (*arg) :
        return math.log10(*arg)
    def l_o_g_1_p (*arg) :
        return math.log1p(*arg)
    def l_o_g_2 (*arg) :
        return math.log2(*arg)
    def m_o_d_f (*arg) :
        return math.modf(*arg)
    def n_a_n (*arg) :
        return math.nan(*arg)
    def n_e_x_t_a_f_t_e_r (*arg) :
        return math.nextafter(*arg)
    def p_e_r_m (*arg) :
        return math.perm(*arg)
    def p_i (*arg) :
        return math.pi(*arg)
    def p_o_w (*arg) :
        return math.pow(*arg)
    def p_r_o_d (*arg) :
        return math.prod(*arg)
    def r_a_d_i_a_n_s (*arg) :
        return math.radians(*arg)
    def r_e_m_a_i_n_d_e_r (*arg) :
        return math.remainder(*arg)
    def s_i_n (*arg) :
        return math.sin(*arg)
    def s_i_n_h (*arg) :
        return math.sinh(*arg)
    def s_q_r_t (*arg) :
        return math.sqrt(*arg)
    def t_a_n (*arg) :
        return math.tan(*arg)
    def t_a_n_h (*arg) :
        return math.tanh(*arg)
    def t_a_u (*arg) :
        return math.tau(*arg)
    def t_r_u_n_c (*arg) :
        return math.trunc(*arg)
    def u_l_p (*arg) :
        return math.ulp(*arg)


class R_a_n_d_o_m:
    def s_t_r (length, a_b_c=True, c_a_p=True, n_u_m=True, a_d_d=''):
        chars = ''
        if a_b_c:
            chars+='qwertyuioplkjhgfdsazxcvbnm'
            if c_a_p:
                chars+='QWERTYUIOPLKJHGFDSAZXCVBNM'
        if n_u_m:
            chars+='0123456789'
        chars+=a_d_d
        chars = chars * 2
        return ''.join(random.sample(chars,length))
    def i_n_t (s,e):
        return random.randint(s,e)
    def o_n_e_O_f (data):
        return random.choice(data)


class C_o_d_e:
    class CodeError (Exception):
        pass
    class u_t_f___8 :
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'bytes':
                raise C_o_d_e.CodeError('utf-8 input data must be bytes')
            return data.decode('utf-8')
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('utf-8 input data must be string')
            return data.encode('utf-8')
    class b_a_s_e_6_4 :
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('base64 input data must be string')
            base64_byte = data.encode('ascii')
            ascii_data = base64.b64decode(base64_byte)
            return ascii_data.decode('ascii')
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('base64 input data must be string')
            encoded_ascii = data.encode('ascii')
            base64_byte = base64.b64encode(encoded_ascii)
            return base64_byte.decode('ascii')
    class h_e_x :
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('hex input data must be string')
            data=data.encode('utf-8')
            data2 = data.hex()
            return data2
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('hex input data must be string')
            data2 = bytes.fromhex(data)
            data2 = data2.decode('ascii')
            return data2
    class b_i_n_a_r_y :
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('binary input data must be string')
            return "".join(format(ord(i),'08b')for i in data)
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('binary input data must be string')
            out=''
            d2=list(data)
            end=[]
            while len(d2)!=0:
                end.append(''.join(d2[0:8]))
                d2=d2[8:]
            for value in end:
                an_integer = int(value,2)
                ascii_char = chr(an_integer)
                out+=ascii_char
            return out


class J_S_O_N:
    class JsonError (Exception):
        pass
    class p_a_r_s_e :
        def __init__(self,data):
            if data.__class__.__name__ == 'str' :
                data = J_S_O_N.t_o_D_i_c_t( data )
            if data.__class__.__name__ == 'dict' :
                pass
            else:
                raise J_S_O_N.JsonError('JSON.pasre() take only str/dict value')

            for i in data.keys():
                if data[i].__class__.__name__ == 'dict':
                    try :     exec(f'self.{"_".join(list(i))} = J_S_O_N.p_a_r_s_e({data[i]})')
                    except:  raise J_S_O_N.JsonError(f'value error : "{i}"')
                else:
                    if data[i].__class__.__name__ == 'str':
                        data[i] = f'"{data[i]}"'
                    try :     exec(f'self.{"_".join(list(i))} = {data[i]}')
                    except:  raise J_S_O_N.JsonError(f'value error : "{i}"')
    def u_n_P_a_r_s_e (data):
        if not('p_a_r_s_e' in data.__class__.__name__):
            raise J_S_O_N.JsonError('JSON.unPasre() take only "JSON.parse()" value')
        outdict = {}
        for i in dir(data):
            if len(re.findall(r'__[a-zA-Z0-9_]*__',i)) > 0 :
                continue
            i2 = i.replace('__','ة').replace('_','').replace('ة','_')
            exec(f'''if J_S_O_N.p_a_r_s_e == data.{i}.__class__:\n\toutdict["{i2}"] = J_S_O_N.u_n_P_a_r_s_e(data.{i})\nelse:\n\texec(f'outdict["{i2}"] = data.{i}')''')
        return outdict
    def t_o_J_s_o_n (data):
        try:
            return json.dumps(data)
        except Exception as e:
            raise J_S_O_N.JsonError(str(e))
    def t_o_D_i_c_t (data):
        try:
            return json.loads(data)
        except Exception as e:
            raise J_S_O_N.JsonError(str(e))


class H_T_T_P:
    def __init__ (self):
        self.session=requests.Session()
        self.url=''
        self.method=''
    class HTTPRequestError (Exception):
        'For Any Request Error'
        pass
    class response:
        def __init__ (self,data):
            self.u_r_l            =  data.url
            self.r_e_d_i_r_e_c_t  =  data.is_redirect
            self.c_o_o_k_i_e_s    =  data.cookies.get_dict()
            self.h_e_a_d_e_r_s    =  data.headers
            self.t_e_x_t          =  data.text
            self.c_o_n_t_e_n_t    =  data.content
            self.c_o_d_e          =  data.status_code
    def h_e_a_d_e_r_s (self,data):
        self.session.headers.update(data)
    def e_n_c_o_d_i_n_g (self,data):
        self.session.encoding = data
    def a_u_t_h (self,data):
        self.session.auth=data
    def c_o_o_k_i_e_s (self,data):
        self.session.cookies.update(data)
    def U_R_L (self,*url):
        if len(url) < 1 :
            raise self.HTTPRequestError('Enter a Url in "HTTP().URL( URL_HERE )" function')
        self.url='/'.join(url)
    def m_e_t_h_o_d (self,data):
        if data.upper().strip() in ['GET','POST','PUT','DELETE','HEAD','PATCH','OPTIONS']:
            self.method=data.upper().strip()
        else:
            raise self.HTTPRequestError('Unknown Method You Can Use (GET, POST)')
    def s_e_n_d (self,*data):
        try:
            if self.method=='': raise self.HTTPRequestError('Please Set HTTP Request Method "HTTP().method( METHOD_HERE )"')
            if self.url=='':    raise self.HTTPRequestError('Please Set Request URL "HTTP().url( URL_HERE )"')
            
            if self.method == 'GET':
                if len(data) >= 1 :   req=self.session.get(self.url, data=data[0])
                else:                 req=self.session.get(self.url)
            if self.method == 'POST':
                if len(data) >= 1 :   req=self.session.post(self.url, data=data[0])
                else:                 req=self.session.post(self.url)
            if self.method == 'PUT':
                if len(data) >= 1 :   req=self.session.put(self.url, data=data[0])
                else:                 req=self.session.put(self.url)
            if self.method == 'DELETE':
                if len(data) >= 1 :   req=self.session.delete(self.url, data=data[0])
                else:                 req=self.session.delete(self.url)
            if self.method == 'HEAD':
                if len(data) >= 1 :   req=self.session.head(self.url, data=data[0])
                else:                 req=self.session.head(self.url)
            if self.method == 'PATCH':
                if len(data) >= 1 :   req=self.session.patch(self.url, data=data[0])
                else:                 req=self.session.patch(self.url)
            if self.method == 'OPTIONS':
                if len(data) >= 1 :   req=self.session.options(self.url, data=data[0])
                else:                 req=self.session.options(self.url)
            
            return self.response(req)
        except Exception as e:
            raise self.HTTPRequestError(str(e))


class R_e_g_e_x :
    def __init__ (self,reStr):
        self.re_str=fr'{reStr}'
    def i_s_M_a_t_c_h (self,string):
        if re.search(self.re_str,string):
            return True
        else:
            return False
    def f_i_n_d_A_l_l (self,string):
        return re.findall(self.re_str,string)
    def i_n_d_e_x_S_t_a_r_t (self,string):
        try:
            return re.search(self.re_str,string).start()
        except:
            return -1
    def i_n_d_e_x_E_n_d (self,string):
        try:
            return re.search(self.re_str,string).end()
        except:
            return -1
    def s_p_l_i_t (self,string,t_i_l_l=None):
        if t_i_l_l==None:
            return re.split(self.re_str,string)
        else:
            return re.split(self.re_str,string,t_i_l_l)
    def r_e_p_l_a_c_e(self,string,join):
        return re.sub(self.re_str, join, string)
    

class S_y_s_t_e_m:
    a_r_g_v = sys.argv[1:]
    def i_n_p_u_t():
        return sys.stdin.readline()
    class w_r_i_t_e :
        def o_u_t (*text):
            for i in text : sys.stdout.write(i)
            return 1
        def e_r_r (*text):
            print(*text, file = sys.stderr)
            return 1
    def e_x_i_t (text):
        sys.exit(text)
    def c_m_d (command):
        os.system(command)
        return 0
    def e_x_e_c (command):
        popen = os.popen(command)
        return o.read()
    def p_a_t_h ():
        return os.getcwd()
    def i_n_f_o_r_m_a_t_i_o_n_s ():
        UNAME = platform.uname()
        out = {
            'system':UNAME.system,
            'node':UNAME.node,
            'release':UNAME.release,
            'version':UNAME.version,
            'machine':UNAME.machine,
            'processor':UNAME.processor,
        }
        return out


class F_i_l_e:
    class R_e_a_d:
        def __init__ (self,filename,u_t_f___8=0):
            if u_t_f___8:
                self.F = open (filename,'r',encoding='utf-8')
            else:
                self.F = open (filename,'r')
        def g_e_t_T_e_x_t (self):
            return self.F.read()
        def e_n_d (self):
            self.F.close()
    class R_e_a_d_B_y_t_e_s:
        def __init__ (self,filename):
            self.F = open (filename,'rb')
        def g_e_t (self):
            return self.F.read()
        def e_n_d (self):
            self.F.close()
    class W_r_i_t_e:
        def __init__ (self,filename,u_t_f___8=0):
            if u_t_f___8:
                self.F = open (filename,'w',encoding='utf-8')
            else:
                self.F = open (filename,'w')
        def w_r_i_t_e (self,*arguments):
            for arg in arguments:
                self.F.write(arg)
        def e_n_d (self):
            self.F.close()
    class A_d_d:
        def __init__ (self,filename,u_t_f___8=0):
            if u_t_f___8:
                self.F = open (filename,'a',encoding='utf-8')
            else:
                self.F = open (filename,'a')
        def w_r_i_t_e (self,*arguments):
            for arg in arguments:
                self.F.write(arg)
        def e_n_d (self):
            self.F.close()


class T_i_m_e:
    class get_time_data :
        def __init__ (self,obj):
            self.y_e_a_r  = obj.tm_year
            self.m_o_n  = obj.tm_mon
            self.m_d_a_y  = obj.tm_mday
            self.h_o_u_r  = obj.tm_hour
            self.m_i_n  = obj.tm_min
            self.s_e_c  = obj.tm_sec
            self.w_d_a_y  = obj.tm_wday
            self.y_d_a_y  = obj.tm_yday
            self.i_s_d_s_t  = obj.tm_isdst
    def e_p_o_c_h () :
        return time.time()
    def a_E_p_o_c_h (num, o_b_j = False) :
        if o_b_j:
            return T_i_m_e.get_time_data( time.localtime(num) )
        else:
            return time.ctime(num)
    def s_l_e_e_p (num) :
        time.sleep(num)
    def n_o_w (o_b_j = False) :
        if o_b_j:
            return T_i_m_e.get_time_data( time.localtime( time.time() ) )
        else:
            return time.ctime( time.time() )
    class c_o_u_n_t:
        def __init__ (self,o_b_j=False):
            pass
            self.obj = o_b_j
            self.time = 0
        def s_t_a_r_t (self):
            self.time =  datetime.datetime.now()
        def e_n_d (self):
            if self.obj:
                obj = datetime.datetime.now() - self.time
                self.d_a_y_s = obj.days
                self.m_i_n = obj.min
                self.s_e_c_o_n_d_s = obj.seconds
                self.m_i_c_r_o_s_e_c_o_n_d_s = obj.microseconds
                self.t_o_t_a_l___s_e_c_o_n_d_s = obj.total_seconds()
            else:
                self.g_e_t = str(datetime.datetime.now() - self.time)