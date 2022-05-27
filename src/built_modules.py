import os,platform,subprocess,base64,sys,re,requests,json,random,time
from .methods import *

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
    class b_a_s_e_6_4 :
        def d_e_c_o_d_e (data):
            base64_byte = data.encode('ascii')
            ascii_data = base64.b64decode(base64_byte)
            return ascii_data.decode('ascii')
        def e_n_c_o_d_e (data):
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
            self.c_o_o_k_i_e_s =  data.cookies.get_dict()
            self.h_e_a_d_e_r_s =  data.headers
            self.t_e_x_t       =  data.text
            self.c_o_n_t_e_n_t =  data.content
            self.c_o_d_e       =  data.status_code
    def h_e_a_d_e_r_s (self,data):
        self.session.headers.update(data)
    def a_u_t_h (self,data):
        self.session.auth=data
    def c_o_o_k_i_e_s (self,data):
        self.session.cookies.update(data)
    def U_R_L (self,*url):
        if len(url) < 1 :
            raise self.HTTPRequestError('Enter a Url in "HTTP().URL( URL_HERE )" function')
        self.url='/'.join(url)
    def m_e_t_h_o_d (self,data):
        if data.upper().strip() in ['GET','POST']:
            self.method=data.upper().strip()
        else:
            raise self.HTTPRequestError('Unknown Method You Can Use (GET, POST)')
    def s_e_n_d (self,*data):
        try:
            if self.method=='': raise self.HTTPRequestError('Please Set H_T_T_P Request Method "HTTP().method( METHOD_HERE )"')
            if self.url=='':    raise self.HTTPRequestError('Please Set Request URL "HTTP().url( URL_HERE )"')
            if self.method == 'GET':
                if len(data) >= 1 :   req=self.session.get(self.url, data=data[0])
                else:                 req=self.session.get(self.url)
            if self.method == 'POST':
                if len(data) >= 1 :   req=self.session.post(self.url, data=data[0])
                else:                 req=self.session.post(self.url)
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
    def s_p_l_i_t (self,string,o_n=None):
        if o_n==None:
            return re.split(self.re_str,string)
        else:
            return re.split(self.re_str,string,o_n)
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
    def e_x_e_c (command,s_h_e_l_l=False):
        DEVNULL = subprocess.DEVNULL
        return subprocess.check_output(command,shell=s_h_e_l_l, stderr = DEVNULL , stdin = DEVNULL ).decode("utf-8",errors='backslashreplace')
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
        def __init__ (self,filename):
            self.F = open (filename,'r')
        def g_e_t_T_e_x_t (self):
            return self.F.read()
        def e_n_d (self):
            self.F.close()
    class W_r_i_t_e:
        def __init__ (self,filename):
            self.F = open(filename,'w')
        def w_r_i_t_e (self,*arguments):
            for arg in arguments:
                self.F.write(arg)
        def e_n_d (self):
            self.F.close()
    class A_d_d:
        def __init__ (self,filename):
            self.F = open(filename,'a')
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