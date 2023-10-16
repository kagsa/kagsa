import sys
import platform
import base64
import os
import requests
import re
import json
import random
import time
import datetime
import keyboard
import math

try:
    from .methods import *
except:
    from methods import *

P_A_T_H = sys.path


class W_e_b:
    class HTMLError(Exception):
        pass

    @staticmethod
    def s_c_r_i_p_t(data):
        return f'<script>{data}</script>'

    @staticmethod
    def b_o_x(data):
        data = data.replace('"', '\\"')
        print(f'<script>alert("{data}")</script>')

    class E_l_e_m_e_n_t:
        def __init__(self, tagName, n, innerHTML, **attrs):
            self.t_a_g_N_a_m_e = tagName
            if not (n in [1, 2, '1', '2']):
                raise W_e_b.HTMLError('Element(tagName, n, innerHTML, **attrs) n must be 1 or 2')
            self.n = n
            self.a_t_t_r_s = attrs
            self.i_n_n_e_r_H_T_M_L = innerHTML

        def __str__(self):
            d = ''
            if self.n == 1:
                d = f'<{self.t_a_g_N_a_m_e} _DATA_>'
            else:
                d = f'<{self.t_a_g_N_a_m_e} _DATA_>{self.i_n_n_e_r_H_T_M_L}</{self.t_a_g_N_a_m_e}>'
            for i, j in self.a_t_t_r_s.items():
                j = j.replace('"', '\\"')
                i = i.replace('__', 'ة').replace('_', '').replace('ة', '_')
                d = d.replace('_DATA_', f'{i}="{j}" _DATA_')
            d = d.replace(' _DATA_', '')
            return d


class i_n_p_u_t_s:
    inp = {}

    @staticmethod
    def s_e_t(selector, htmlclass):
        i_n_p_u_t_s.inp[selector] = htmlclass

    @staticmethod
    def g_e_t(selector):
        if selector in i_n_p_u_t_s.inp.keys():
            return i_n_p_u_t_s.inp[selector]
        else:
            raise W_e_b.HTMLError(f"{selector} is not defined")

    @staticmethod
    def e_d_i_t(selector, **data):
        o = "<script>_DATA_</script>"
        for i, j in data.items():
            i = i.replace('__', 'ة').replace('_', '').replace('ة', '_')
            j = j.replace('"', '\\"')
            o = o.replace('_DATA_', f'document.querySelector("{selector}").{i} = "{j}";_DATA_')
        o = o.replace('_DATA_', '')
        print(o)


class K_e_y_b_o_a_r_d:
    class KeyboardError(Exception):
        pass

    @staticmethod
    def w_a_i_t(text):
        try:
            keyboard.wait(text)
        except Exception as ee:
            raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))

    @staticmethod
    def w_r_i_t_e(text):
        try:
            keyboard.write(text)
        except Exception as ee:
            raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))

    @staticmethod
    def n_e_w_H_o_t_k_e_y(text, func):
        try:
            keyboard.add_hotkey(text, func)
        except Exception as ee:
            raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))

    class r_e_c_o_r_d:
        def __init__(self, u_n_t_i_l=''):
            try:
                self.g_e_t = []
                self.recorded = []
                keyboard.hook(self.recorded.append)
                keyboard.wait(u_n_t_i_l)
                keyboard.unhook(self.recorded.append)
                for i in self.recorded:
                    self.g_e_t.append(str(i).replace('KeyboardEvent(', '')[0:-1])
            except Exception as ee:
                raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))

        def p_l_a_y_A_l_l(self, s_p_e_e_d=0.5):
            keyboard.play(self.recorded, speed_factor=s_p_e_e_d)

    @staticmethod
    def p_r_e_s_s(text):
        try:
            keyboard.press_and_release(text)
        except Exception as ee:
            raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))


class M_a_t_h:
    @staticmethod
    def a_c_o_s(*arg):
        return math.acos(*arg)

    @staticmethod
    def a_c_o_s_h(*arg):
        return math.acosh(*arg)

    @staticmethod
    def a_s_i_n(*arg):
        return math.asin(*arg)

    @staticmethod
    def a_s_i_n_h(*arg):
        return math.asinh(*arg)

    @staticmethod
    def a_t_a_n(*arg):
        return math.atan(*arg)

    @staticmethod
    def a_t_a_n_2(*arg):
        return math.atan2(*arg)

    @staticmethod
    def a_t_a_n_h(*arg):
        return math.atanh(*arg)

    @staticmethod
    def c_e_i_l(*arg):
        return math.ceil(*arg)

    @staticmethod
    def c_o_m_b(*arg):
        return math.comb(*arg)

    @staticmethod
    def c_o_p_y_s_i_g_n(*arg):
        return math.copysign(*arg)

    @staticmethod
    def c_o_s(*arg):
        return math.cos(*arg)

    @staticmethod
    def c_o_s_h(*arg):
        return math.cosh(*arg)

    @staticmethod
    def d_e_g_r_e_e_s(*arg):
        return math.degrees(*arg)

    @staticmethod
    def d_i_s_t(*arg):
        return math.dist(*arg)

    @staticmethod
    def e(*arg):
        return math.e(*arg)

    @staticmethod
    def e_r_f(*arg):
        return math.erf(*arg)

    @staticmethod
    def e_r_f_c(*arg):
        return math.erfc(*arg)

    @staticmethod
    def e_x_p(*arg):
        return math.exp(*arg)

    @staticmethod
    def e_x_p_m_1(*arg):
        return math.expm1(*arg)

    @staticmethod
    def f_a_b_s(*arg):
        return math.fabs(*arg)

    @staticmethod
    def f_a_c_t_o_r_i_a_l(*arg):
        return math.factorial(*arg)

    @staticmethod
    def f_l_o_o_r(*arg):
        return math.floor(*arg)

    @staticmethod
    def f_m_o_d(*arg):
        return math.fmod(*arg)

    @staticmethod
    def f_r_e_x_p(*arg):
        return math.frexp(*arg)

    @staticmethod
    def f_s_c_a_l_b(*arg):
        return math.fscale(*arg)

    @staticmethod
    def i_s_c_l_o_s_e(*arg):
        return math.isclose(*arg)

    @staticmethod
    def i_s_f_i_n_i_t_e(*arg):
        return math.isfinite(*arg)

    @staticmethod
    def i_s_i_n_f(*arg):
        return math.isinf(*arg)

    @staticmethod
    def i_s_n_a_n(*arg):
        return math.isnan(*arg)

    @staticmethod
    def l_d_e_e_p_c_o_p_y(*arg):
        return math.ldexp(*arg)

    @staticmethod
    def l_o_g(*arg):
        return math.log(*arg)

    @staticmethod
    def l_o_g_1_0(*arg):
        return math.log10(*arg)

    @staticmethod
    def l_o_g_1_p(*arg):
        return math.log1p(*arg)

    @staticmethod
    def l_o_g_2(*arg):
        return math.log2(*arg)

    @staticmethod
    def m_o_d_f(*arg):
        return math.modf(*arg)

    @staticmethod
    def p_o_w(*arg):
        return math.pow(*arg)

    @staticmethod
    def r_a_d_i_a_n_s(*arg):
        return math.radians(*arg)

    @staticmethod
    def s_i_n(*arg):
        return math.sin(*arg)

    @staticmethod
    def s_i_n_h(*arg):
        return math.sinh(*arg)

    @staticmethod
    def s_q_r_t(*arg):
        return math.sqrt(*arg)

    @staticmethod
    def t_a_n(*arg):
        return math.tan(*arg)

    @staticmethod
    def t_a_n_h(*arg):
        return math.tanh(*arg)

    @staticmethod
    def t_r_u_n_c(*arg):
        return math.trunc(*arg)


class J_s_o_n:
    @staticmethod
    def d_u_m_p(*args):
        try:
            return json.dump(*args)
        except Exception as ee:
            raise J_s_o_n.JSONError(str(ee))

    @staticmethod
    def d_u_m_p_s(*args):
        try:
            return json.dumps(*args)
        except Exception as ee:
            raise J_s_o_n.JSONError(str(ee))

    @staticmethod
    def l_o_a_d(*args):
        try:
            return json.load(*args)
        except Exception as ee:
            raise J_s_o_n.JSONError(str(ee))

    @staticmethod
    def l_o_a_d_s(*args):
        try:
            return json.loads(*args)
        except Exception as ee:
            raise J_s_o_n.JSONError(str(ee))

    class JSONError(Exception):
        pass


class B_o_x:
    @staticmethod
    def s_h_o_w(text):
        text = text.replace('"', '\\"')
        print(f'<script>alert("{text}")</script>')


class T_i_m_e:
    @staticmethod
    def s_l_e_e_p(seconds):
        time.sleep(seconds)

    @staticmethod
    def s_t_r_f_t_i_m_e(string):
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')

    @staticmethod
    def t_i_m_e():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


class R_e_q_u_e_s_t:
    class RequestError(Exception):
        pass

    @staticmethod
    def g_e_t(*args, **kwargs):
        try:
            return requests.get(*args, **kwargs)
        except Exception as ee:
            raise R_e_q_u_e_s_t.RequestError(str(ee))

    @staticmethod
    def p_o_s_t(*args, **kwargs):
        try:
            return requests.post(*args, **kwargs)
        except Exception as ee:
            raise R_e_q_u_e_s_t.RequestError(str(ee))


class S_y_s_t_e_m:
    @staticmethod
    def e_x_i_t():
        sys.exit()

    @staticmethod
    def e_x_i_t_code(code):
        sys.exit(code)

    @staticmethod
    def g_e_t_a_r_g_v():
        return sys.argv

    @staticmethod
    def g_e_t_p_l_a_t_f_o_r_m():
        return platform.system()

    @staticmethod
    def g_e_t_p_l_a_t_f_o_r_m_v_e_r_s_i_o_n():
        return platform.version()


class R_a_n_d_o_m:
    @staticmethod
    def g_e_t_r_a_n_d_i_n_t():
        return random.randint(0, 1000000000)

    @staticmethod
    def s_h_u_f_f_l_e(*args):
        return random.shuffle(*args)


class E_n_v_i_r_o_n_m_e_n_t:
    @staticmethod
    def g_e_t_e_n_v(variable):
        try:
            return os.environ[variable]
        except Exception as ee:
            raise E_n_v_i_r_o_n_m_e_n_t.EnvironmentError(str(ee))


class S_e_l_e_c_t:
    class SelectError(Exception):
        pass

    class E_l_e_m_e_n_t:
        def __init__(self, selector):
            try:
                self.selector = selector
                self.element = document.querySelector(selector)
            except Exception as ee:
                raise S_e_l_e_c_t.SelectError(str(ee))

        def h_t_m_l(self):
            return self.element.innerHTML

        def s_e_t_h_t_m_l(self, html):
            self.element.innerHTML = html

        def t_e_x_t(self):
            return self.element.textContent

        def s_e_t_t_e_x_t(self, text):
            self.element.textContent = text

        def v_a_l_u_e(self):
            return self.element.value

        def s_e_t_v_a_l_u_e(self, value):
            self.element.value = value

        def a_t_t_r_i_b_u_t_e(self, attribute):
            return self.element.getAttribute(attribute)

        def s_e_t_a_t_t_r_i_b_u_t_e(self, attribute, value):
            self.element.setAttribute(attribute, value)

        def s_t_y_l_e(self):
            return self.element.style

        def c_l_i_c_k(self):
            self.element.click()

        def a_d_d_c_l_a_s_s(self, class_name):
            self.element.classList.add(class_name)

        def r_e_m_o_v_e_c_l_a_s_s(self, class_name):
            self.element.classList.remove(class_name)

        def h_a_s_c_l_a_s_s(self, class_name):
            return self.element.classList.contains(class_name)

    @staticmethod
    def s_e_l_e_c_t(selector):
        return S_e_l_e_c_t.E_l_e_m_e_n_t(selector)


class M_a_t_h:
    @staticmethod
    def r_a_n_d_o_m():
        return random.random()


class A_l_e_r_t:
    @staticmethod
    def a_l_e_r_t(text):
        text = text.replace('"', '\\"')
        print(f'<script>alert("{text}")</script>')


class E_v_e_n_t:
    @staticmethod
    def d_i_s_p_a_t_c_h(event):
        try:
            return document.dispatchEvent(event)
        except Exception as ee:
            raise E_v_e_n_t.EventError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_v_e_n_t(event_type):
        try:
            return document.createEvent(event_type)
        except Exception as ee:
            raise E_v_e_n_t.EventError(str(ee))

    class EventError(Exception):
        pass


class G_e_o_l_o_c_a_t_i_o_n:
    class LocationError(Exception):
        pass

    @staticmethod
    def g_e_t_c_u_r_r_e_n_t_p_o_s_i_t_i_o_n():
        try:
            return navigator.geolocation.getCurrentPosition()
        except Exception as ee:
            raise G_e_o_l_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def w_a_t_c_h_p_o_s_i_t_i_o_n():
        try:
            return navigator.geolocation.watchPosition()
        except Exception as ee:
            raise G_e_o_l_o_c_a_t_i_o_n.LocationError(str(ee))


class F_o_r_m:
    class FormError(Exception):
        pass

    class E_l_e_m_e_n_t:
        def __init__(self, selector):
            try:
                self.selector = selector
                self.element = document.querySelector(selector)
            except Exception as ee:
                raise F_o_r_m.FormError(str(ee))

        def r_e_s_e_t(self):
            self.element.reset()

        def s_u_b_m_i_t(self):
            self.element.submit()

    @staticmethod
    def f_o_r_m(selector):
        return F_o_r_m.E_l_e_m_e_n_t(selector)


class C_o_o_k_i_e:
    @staticmethod
    def g_e_t_c_o_o_k_i_e(name):
        try:
            return document.cookie.get(name)
        except Exception as ee:
            raise C_o_o_k_i_e.CookieError(str(ee))

    @staticmethod
    def s_e_t_c_o_o_k_i_e(name, value, **kwargs):
        try:
            document.cookie.set(name, value, **kwargs)
        except Exception as ee:
            raise C_o_o_k_i_e.CookieError(str(ee))

    @staticmethod
    def r_e_m_o_v_e_c_o_o_k_i_e(name):
        try:
            document.cookie.remove(name)
        except Exception as ee:
            raise C_o_o_k_i_e.CookieError(str(ee))

    class CookieError(Exception):
        pass


class L_o_c_a_l_S_t_o_r_a_g_e:
    @staticmethod
    def g_e_t_i_t_e_m(key):
        try:
            return localStorage.getItem(key)
        except Exception as ee:
            raise L_o_c_a_l_S_t_o_r_a_g_e.StorageError(str(ee))

    @staticmethod
    def s_e_t_i_t_e_m(key, value):
        try:
            localStorage.setItem(key, value)
        except Exception as ee:
            raise L_o_c_a_l_S_t_o_r_a_g_e.StorageError(str(ee))

    @staticmethod
    def r_e_m_o_v_e_i_t_e_m(key):
        try:
            localStorage.removeItem(key)
        except Exception as ee:
            raise L_o_c_a_l_S_t_o_r_a_g_e.StorageError(str(ee))

    @staticmethod
    def c_l_e_a_r():
        try:
            localStorage.clear()
        except Exception as ee:
            raise L_o_c_a_l_S_t_o_r_a_g_e.StorageError(str(ee))

    class StorageError(Exception):
        pass


class S_e_s_s_i_o_n_S_t_o_r_a_g_e:
    @staticmethod
    def g_e_t_i_t_e_m(key):
        try:
            return sessionStorage.getItem(key)
        except Exception as ee:
            raise S_e_s_s_i_o_n_S_t_o_r_a_g_e.StorageError(str(ee))

    @staticmethod
    def s_e_t_i_t_e_m(key, value):
        try:
            sessionStorage.setItem(key, value)
        except Exception as ee:
            raise S_e_s_s_i_o_n_S_t_o_r_a_g_e.StorageError(str(ee))

    @staticmethod
    def r_e_m_o_v_e_i_t_e_m(key):
        try:
            sessionStorage.removeItem(key)
        except Exception as ee:
            raise S_e_s_s_i_o_n_S_t_o_r_a_g_e.StorageError(str(ee))

    @staticmethod
    def c_l_e_a_r():
        try:
            sessionStorage.clear()
        except Exception as ee:
            raise S_e_s_s_i_o_n_S_t_o_r_a_g_e.StorageError(str(ee))

    class StorageError(Exception):
        pass


class H_i_s_t_o_r_y:
    @staticmethod
    def g_o():
        try:
            history.go()
        except Exception as ee:
            raise H_i_s_t_o_r_y.HistoryError(str(ee))

    @staticmethod
    def b_a_c_k():
        try:
            history.back()
        except Exception as ee:
            raise H_i_s_t_o_r_y.HistoryError(str(ee))

    @staticmethod
    def f_o_r_w_a_r_d():
        try:
            history.forward()
        except Exception as ee:
            raise H_i_s_t_o_r_y.HistoryError(str(ee))

    class HistoryError(Exception):
        pass


class L_o_c_a_t_i_o_n:
    @staticmethod
    def a_s_s_i_g_n(url):
        try:
            location.assign(url)
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_p_l_a_c_e(url):
        try:
            location.replace(url)
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_l_o_a_d():
        try:
            location.reload()
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_l_o_a_d_f_o_r_c_e():
        try:
            location.reload(True)
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def h_a_s_h():
        return location.hash

    @staticmethod
    def h_o_s_t():
        return location.host

    @staticmethod
    def h_o_s_t_n_a_m_e():
        return location.hostname

    @staticmethod
    def h_r_e_f():
        return location.href

    @staticmethod
    def o_r_i_g_i_n():
        return location.origin

    @staticmethod
    def p_a_t_h_n_a_m_e():
        return location.pathname

    @staticmethod
    def p_o_r_t():
        return location.port

    @staticmethod
    def p_r_o_t_o_c_o_l():
        return location.protocol

    @staticmethod
    def s_e_a_r_c_h():
        return location.search

    @staticmethod
    def r_e_l_o_a_d_p_o_r_t():
        try:
            location.reload()
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_l_o_a_d_h_o_s_t():
        try:
            location.reload()
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_l_o_a_d_p_a_t_h_n_a_m_e():
        try:
            location.reload()
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_l_o_a_d_p_r_o_t_o_c_o_l():
        try:
            location.reload()
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_l_o_a_d_h_a_s_h():
        try:
            location.reload()
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    @staticmethod
    def r_e_l_o_a_d_s_e_a_r_c_h():
        try:
            location.reload()
        except Exception as ee:
            raise L_o_c_a_t_i_o_n.LocationError(str(ee))

    class LocationError(Exception):
        pass


class P_o_p_u_p:
    @staticmethod
    def a_l_e_r_t(text):
        try:
            window.alert(text)
        except Exception as ee:
            raise P_o_p_u_p.PopupError(str(ee))

    @staticmethod
    def c_o_n_f_i_r_m(text):
        try:
            return window.confirm(text)
        except Exception as ee:
            raise P_o_p_u_p.PopupError(str(ee))

    @staticmethod
    def p_r_o_m_p_t(text):
        try:
            return window.prompt(text)
        except Exception as ee:
            raise P_o_p_u_p.PopupError(str(ee))

    class PopupError(Exception):
        pass


class W_o_r_k_e_r:
    class WorkerError(Exception):
        pass

    @staticmethod
    def s_e_n_d(data):
        try:
            worker.postMessage(data)
        except Exception as ee:
            raise W_o_r_k_e_r.WorkerError(str(ee))

    @staticmethod
    def o_n_m_e_s_s_a_g_e(func):
        try:
            worker.onmessage = func
        except Exception as ee:
            raise W_o_r_k_e_r.WorkerError(str(ee))

    @staticmethod
    def t_e_r_m_i_n_a_t_e():
        try:
            worker.terminate()
        except Exception as ee:
            raise W_o_r_k_e_r.WorkerError(str(ee))


class D_o_m:
    class DomError(Exception):
        pass

    @staticmethod
    def g_e_t_d_o_m():
        try:
            return document
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_b_o_d_y():
        try:
            return document.body
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_h_e_a_d():
        try:
            return document.head
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_r_l():
        try:
            return document.URL
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_d_o_m_a_i_n():
        try:
            return document.domain
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_r_e_f_e_r_r_e_r():
        try:
            return document.referrer
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_n_n_e_r_h_t_m_l():
        try:
            return document.documentElement.innerHTML
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_o_u_t_e_r_h_t_m_l():
        try:
            return document.outerHTML
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_n_n_e_r_h_t_m_l(inner):
        try:
            document.documentElement.innerHTML = inner
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_o_u_t_e_r_h_t_m_l(outer):
        try:
            document.outerHTML = outer
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_n_n_e_r_t_e_x_t():
        try:
            return document.documentElement.innerText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_o_u_t_e_r_t_e_x_t():
        try:
            return document.outerText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_n_n_e_r_t_e_x_t(inner):
        try:
            document.documentElement.innerText = inner
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_o_u_t_e_r_t_e_x_t(outer):
        try:
            document.outerText = outer
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_l_i_n_k_s():
        try:
            return document.links
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_s():
        try:
            return document.uls
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_s():
        try:
            return document.forms
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_a_g_e_s():
        try:
            return document.images
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_s_c_r_i_p_t_s():
        try:
            return document.scripts
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s():
        try:
            return document.formelements
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_d_o_m_i_m_p_l_e_m_e_n_t_s():
        try:
            return document.DOMImplementation
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_l_e_m_e_n_t(tag):
        try:
            return document.createElement(tag)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_t_e_x_t_n_o_d_e(text):
        try:
            return document.createTextNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_c_d_a_t_a_n_o_d_e(text):
        try:
            return document.createCDATASection(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_c_o_m_m_e_n_t(text):
        try:
            return document.createComment(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_d_a_t_a_l_i_s_t(text):
        try:
            return document.createDatalist(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_d_o_c_u_m_e_n_t():
        try:
            return document.createDocument()
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_d_o_c_u_m_e_n_t_f_r_a_g_m_e_n_t():
        try:
            return document.createDocumentFragment()
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_d_o_c_u_m_e_n_t_t_y_p_e():
        try:
            return document.createDocumentType()
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_l_e_m_e_n_t_n_o_d_e(text):
        try:
            return document.createElementNS(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_v_e_n_t(text):
        try:
            return document.createEvent(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_v_e_n_t_t_e_x_t(text):
        try:
            return document.createEventText(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_r_a_n_g_e(text):
        try:
            return document.createRange(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_t_e_x_t_n_o_d_e(text):
        try:
            return document.createTextNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_c_o_m_m_e_n_t_t_e_x_t_n_o_d_e(text):
        try:
            return document.createCommentTextNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_c_d_a_t_a_s_e_c_t_i_o_n(text):
        try:
            return document.createCDATASection(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_d_o_c_u_m_e_n_t_f_r_a_g_m_e_n_t_t_e_x_t_n_o_d_e(text):
        try:
            return document.createDocumentFragmentTextNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_d_o_c_u_m_e_n_t_t_y_p_e_n_o_d_e(text):
        try:
            return document.createDocumentTypeNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_l_e_m_e_n_t_n_o_d_e_n_o_d_e(text):
        try:
            return document.createElementNSNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_v_e_n_t_n_o_d_e(text):
        try:
            return document.createEventNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_e_v_e_n_t_t_e_x_t_n_o_d_e_n_o_d_e(text):
        try:
            return document.createEventTextNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def c_r_e_a_t_e_r_a_n_g_e_n_o_d_e(text):
        try:
            return document.createRangeNode(text)
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_l_i_n_k_h_r_e_f(linl):
        try:
            return linl.href
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_l_i_n_k_t_a_r_g_e_t(linl):
        try:
            return linl.target
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_l_i_n_k_r_e_l(linl):
        try:
            return linl.rel
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_l_i_n_k_r_e_v(linl):
        try:
            return linl.rev
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_l_i_n_k_u_r_i(linl):
        try:
            return linl.uri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_l_i_n_k_h_r_e_f(linl, value):
        try:
            linl.href = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_l_i_n_k_t_a_r_g_e_t(linl, value):
        try:
            linl.target = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_l_i_n_k_r_e_l(linl, value):
        try:
            linl.rel = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_l_i_n_k_r_e_v(linl, value):
        try:
            linl.rev = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_l_i_n_k_u_r_i(linl, value):
        try:
            linl.uri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_t_y_p_e(u_l):
        try:
            return u_l.type
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_t_y_p_e(u_l, value):
        try:
            u_l.type = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_l_i_s_t(u_l):
        try:
            return u_l.list
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_l_i_s_t(u_l, value):
        try:
            u_l.list = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_v_a_l_u_e(u_l):
        try:
            return u_l.value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_v_a_l_u_e(u_l, value):
        try:
            u_l.value = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_s_i_z_e(u_l):
        try:
            return u_l.size
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_s_i_z_e(u_l, value):
        try:
            u_l.size = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_a_c_t_i_o_n(u_l):
        try:
            return u_l.action
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_a_c_t_i_o_n(u_l, value):
        try:
            u_l.action = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_m_e_t_h_o_d(u_l):
        try:
            return u_l.method
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_m_e_t_h_o_d(u_l, value):
        try:
            u_l.method = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_e_n_c_t_y_t_p_e(u_l):
        try:
            return u_l.enctype
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_e_n_c_t_y_t_p_e(u_l, value):
        try:
            u_l.enctype = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_n_a_m_e(u_l):
        try:
            return u_l.name
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_n_a_m_e(u_l, value):
        try:
            u_l.name = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_t_a_r_g_e_t(u_l):
        try:
            return u_l.target
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_t_a_r_g_e_t(u_l, value):
        try:
            u_l.target = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_m_e_d_i_a(u_l):
        try:
            return u_l.media
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_m_e_d_i_a(u_l, value):
        try:
            u_l.media = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_c_s_s_t_e_x_t(u_l):
        try:
            return u_l.cssText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_u_l_c_s_s_t_e_x_t(u_l, value):
        try:
            u_l.cssText = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_l_i_n_k_s(u_l):
        try:
            return u_l.links
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_l_i_s_t(u_l):
        try:
            return u_l.list
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_v_a_l_u_e(u_l):
        try:
            return u_l.value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_s_i_z_e(u_l):
        try:
            return u_l.size
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_a_c_t_i_o_n(u_l):
        try:
            return u_l.action
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_m_e_t_h_o_d(u_l):
        try:
            return u_l.method
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_e_n_c_t_y_t_p_e(u_l):
        try:
            return u_l.enctype
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_n_a_m_e(u_l):
        try:
            return u_l.name
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_t_a_r_g_e_t(u_l):
        try:
            return u_l.target
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_m_e_d_i_a(u_l):
        try:
            return u_l.media
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_u_l_c_s_s_t_e_x_t(u_l):
        try:
            return u_l.cssText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_a_c_t_i_o_n(f_o):
        try:
            return f_o.action
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_m_e_t_h_o_d(f_o):
        try:
            return f_o.method
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_n_c_t_y_t_p_e(f_o):
        try:
            return f_o.enctype
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_n_a_m_e(f_o):
        try:
            return f_o.name
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_t_a_r_g_e_t(f_o):
        try:
            return f_o.target
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s(f_o):
        try:
            return f_o.formelements
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_a_l_t(i_m):
        try:
            return i_m.alt
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_b_o_r_d_e_r(i_m):
        try:
            return i_m.border
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_h_e_i_g_h_t(i_m):
        try:
            return i_m.height
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_h_s_p_a_c_e(i_m):
        try:
            return i_m.hspace
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_i_s_m_a_p(i_m):
        try:
            return i_m.ismap
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_l_o_n_g_d_e_s_c(i_m):
        try:
            return i_m.longdesc
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_l_o_w_n_u_r_l(i_m):
        try:
            return i_m.lowsrc
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_n_a_m_e(i_m):
        try:
            return i_m.name
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_s_r_c(i_m):
        try:
            return i_m.src
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_u_s_e_m_a_p(i_m):
        try:
            return i_m.usemap
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_i_m_g_v_s_p_a_c_e(i_m):
        try:
            return i_m.vspace
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_a_l_t(i_m, value):
        try:
            i_m.alt = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_b_o_r_d_e_r(i_m, value):
        try:
            i_m.border = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_h_e_i_g_h_t(i_m, value):
        try:
            i_m.height = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_h_s_p_a_c_e(i_m, value):
        try:
            i_m.hspace = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_i_s_m_a_p(i_m, value):
        try:
            i_m.ismap = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_l_o_n_g_d_e_s_c(i_m, value):
        try:
            i_m.longdesc = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_l_o_w_n_u_r_l(i_m, value):
        try:
            i_m.lowsrc = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_n_a_m_e(i_m, value):
        try:
            i_m.name = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_s_r_c(i_m, value):
        try:
            i_m.src = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_u_s_e_m_a_p(i_m, value):
        try:
            i_m.usemap = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_i_m_g_v_s_p_a_c_e(i_m, value):
        try:
            i_m.vspace = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_s_c_r_i_p_t_c_h_a_r_s(c_s):
        try:
            return c_s.charset
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_s_c_r_i_p_t_c_h_a_r_s(c_s, value):
        try:
            c_s.charset = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_s_c_r_i_p_t_s_r_c(c_s):
        try:
            return c_s.src
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_s_c_r_i_p_t_s_r_c(c_s, value):
        try:
            c_s.src = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_s_c_r_i_p_t_t_y_p_e(c_s):
        try:
            return c_s.type
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_s_c_r_i_p_t_t_y_p_e(c_s, value):
        try:
            c_s.type = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_s_c_r_i_p_t_d_e_f_e_r(c_s):
        try:
            return c_s.defer
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_s_c_r_i_p_t_d_e_f_e_r(c_s, value):
        try:
            c_s.defer = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_s_c_r_i_p_t_t_e_x_t(c_s):
        try:
            return c_s.text
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_s_c_r_i_p_t_t_e_x_t(c_s, value):
        try:
            c_s.text = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_t_y_l_e(e_l):
        try:
            return e_l.style
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_l_a_s_s_n_a_m_e(e_l):
        try:
            return e_l.className
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_l_a_s_s_n_a_m_e(e_l, value):
        try:
            e_l.className = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_l_a_s_s_l_i_s_t(e_l):
        try:
            return e_l.classList
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_t_y_l_e_m_e_d_i_a(e_l):
        try:
            return e_l.styleMedia
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_s_s_t_e_x_t(e_l):
        try:
            return e_l.style.cssText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_s_s_t_e_x_t(e_l, value):
        try:
            e_l.style.cssText = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_s_s_r_u_l_e_s(e_l):
        try:
            return e_l.style.cssRules
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_s_s_d_e_c_l_a_r_a_t_i_o_n(e_l):
        try:
            return e_l.style.cssDeclaration
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_i_p_t(e_l):
        try:
            return e_l.script
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_i_p_t(e_l, value):
        try:
            e_l.script = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_a_d_i_o_g_r_o_u_p(e_l):
        try:
            return e_l.radioGroup
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_a_d_i_o_g_r_o_u_p(e_l, value):
        try:
            e_l.radioGroup = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_k_e_y(e_l):
        try:
            return e_l.accessKey
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_k_e_y(e_l, value):
        try:
            e_l.accessKey = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_b_i_n_d_e_x(e_l):
        try:
            return e_l.tabIndex
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_b_i_n_d_e_x(e_l, value):
        try:
            e_l.tabIndex = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_b_l_u_r(e_l):
        try:
            return e_l.onblur
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_b_l_u_r(e_l, value):
        try:
            e_l.onblur = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_c_h_a_n_g_e(e_l):
        try:
            return e_l.onchange
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_c_h_a_n_g_e(e_l, value):
        try:
            e_l.onchange = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_c_l_i_c_k(e_l):
        try:
            return e_l.onclick
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_c_l_i_c_k(e_l, value):
        try:
            e_l.onclick = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_d_b_l_c_l_i_c_k(e_l):
        try:
            return e_l.ondblclick
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_d_b_l_c_l_i_c_k(e_l, value):
        try:
            e_l.ondblclick = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_f_o_c_u_s(e_l):
        try:
            return e_l.onfocus
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_f_o_c_u_s(e_l, value):
        try:
            e_l.onfocus = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_d_o_w_n(e_l):
        try:
            return e_l.onkeydown
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_d_o_w_n(e_l, value):
        try:
            e_l.onkeydown = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_p_r_e_s_s(e_l):
        try:
            return e_l.onkeypress
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_p_r_e_s_s(e_l, value):
        try:
            e_l.onkeypress = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_u_p(e_l):
        try:
            return e_l.onkeyup
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_u_p(e_l, value):
        try:
            e_l.onkeyup = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_d_o_w_n(e_l):
        try:
            return e_l.onmousedown
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_d_o_w_n(e_l, value):
        try:
            e_l.onmousedown = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_m_o_v_e(e_l):
        try:
            return e_l.onmousemove
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_m_o_v_e(e_l, value):
        try:
            e_l.onmousemove = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_u_t(e_l):
        try:
            return e_l.onmouseout
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_u_t(e_l, value):
        try:
            e_l.onmouseout = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_v_e_r(e_l):
        try:
            return e_l.onmouseover
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_v_e_r(e_l, value):
        try:
            e_l.onmouseover = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_u_p(e_l):
        try:
            return e_l.onmouseup
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_u_p(e_l, value):
        try:
            e_l.onmouseup = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_r_e_s_i_z_e(e_l):
        try:
            return e_l.onresize
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_r_e_s_i_z_e(e_l, value):
        try:
            e_l.onresize = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_s_e_l_e_c_t(e_l):
        try:
            return e_l.onselect
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_s_e_l_e_c_t(e_l, value):
        try:
            e_l.onselect = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_u_n_l_o_a_d(e_l):
        try:
            return e_l.onunload
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_u_n_l_o_a_d(e_l, value):
        try:
            e_l.onunload = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_i_g_n(e_l):
        try:
            return e_l.align
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_i_g_n(e_l, value):
        try:
            e_l.align = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_d_e_x(e_l):
        try:
            return e_l.index
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_p_a_n(e_l):
        try:
            return e_l.span
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(e_l):
        try:
            return e_l.cellPadding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(e_l, value):
        try:
            e_l.cellPadding = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(e_l):
        try:
            return e_l.cellSpacing
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(e_l, value):
        try:
            e_l.cellSpacing = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_g_n(e_l):
        try:
            return e_l.vAlign
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_g_n(e_l, value):
        try:
            e_l.vAlign = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_o_w_i_n_d_e_x(e_l):
        try:
            return e_l.rowIndex
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_i_n_d_e_x(e_l):
        try:
            return e_l.cellIndex
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_c_k_g_r_o_u_n_d(c_e):
        try:
            return c_e.background
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_c_k_g_r_o_u_n_d(c_e, value):
        try:
            c_e.background = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_g_c_o_l_o_r(c_e):
        try:
            return c_e.bgColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_g_c_o_l_o_r(c_e, value):
        try:
            c_e.bgColor = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(c_e):
        try:
            return c_e.cellPadding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(c_e, value):
        try:
            c_e.cellPadding = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(c_e):
        try:
            return c_e.cellSpacing
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(c_e, value):
        try:
            c_e.cellSpacing = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_l_s(c_e):
        try:
            return c_e.cols
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_l_s(c_e, value):
        try:
            c_e.cols = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_o_w_s(c_e):
        try:
            return c_e.rows
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_o_w_s(c_e, value):
        try:
            c_e.rows = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_b_o_r_d_e_r(c_e):
        try:
            return c_e.frameBorder
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_b_o_r_d_e_r(c_e, value):
        try:
            c_e.frameBorder = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_s_p_a_c_i_n_g(c_e):
        try:
            return c_e.frameSpacing
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_s_p_a_c_i_n_g(c_e, value):
        try:
            c_e.frameSpacing = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_o_r_e_s_i_z_e(c_e):
        try:
            return c_e.noResize
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_o_r_e_s_i_z_e(c_e, value):
        try:
            c_e.noResize = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_o_l_l_i_n_g(c_e):
        try:
            return c_e.scrolling
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_o_l_l_i_n_g(c_e, value):
        try:
            c_e.scrolling = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e(c_e):
        try:
            return c_e.name
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e(c_e, value):
        try:
            c_e.name = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_l_o_w_f_u_l_l_s_c_r_e_e_n(c_e):
        try:
            return c_e.allowFullScreen
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_l_o_w_f_u_l_l_s_c_r_e_e_n(c_e, value):
        try:
            c_e.allowFullScreen = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_b_o_r_d_e_r(c_e):
        try:
            return c_e.frameBorder
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_b_o_r_d_e_r(c_e, value):
        try:
            c_e.frameBorder = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(c_e):
        try:
            return c_e.cellPadding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(c_e, value):
        try:
            c_e.cellPadding = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(c_e):
        try:
            return c_e.cellSpacing
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(c_e, value):
        try:
            c_e.cellSpacing = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_e_r(r_a):
        try:
            return r_a.href
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_e_r(r_a, value):
        try:
            r_a.href = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_i_n_g(r_a):
        try:
            return r_a.ping
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_i_n_g(r_a, value):
        try:
            r_a.ping = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_r_g_e_t(r_a):
        try:
            return r_a.target
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_r_g_e_t(r_a, value):
        try:
            r_a.target = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_l(r_a):
        try:
            return r_a.rel
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_l(r_a, value):
        try:
            r_a.rel = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_v(r_a):
        try:
            return r_a.rev
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_v(r_a, value):
        try:
            r_a.rev = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_l_a_s_s_n_a_m_e(r_a):
        try:
            return r_a.className
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_l_a_s_s_n_a_m_e(r_a, value):
        try:
            r_a.className = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_l_a_s_s_l_i_s_t(r_a):
        try:
            return r_a.classList
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_t_y_l_e(r_a):
        try:
            return r_a.style
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_i_p_t(r_a):
        try:
            return r_a.script
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_i_p_t(r_a, value):
        try:
            r_a.script = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_b_l_u_r(r_a):
        try:
            return r_a.onblur
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_b_l_u_r(r_a, value):
        try:
            r_a.onblur = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_f_o_c_u_s(r_a):
        try:
            return r_a.onfocus
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_f_o_c_u_s(r_a, value):
        try:
            r_a.onfocus = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_c_l_i_c_k(r_a):
        try:
            return r_a.onclick
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_c_l_i_c_k(r_a, value):
        try:
            r_a.onclick = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_d_b_l_c_l_i_c_k(r_a):
        try:
            return r_a.ondblclick
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_d_b_l_c_l_i_c_k(r_a, value):
        try:
            r_a.ondblclick = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_d_o_w_n(r_a):
        try:
            return r_a.onkeydown
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_d_o_w_n(r_a, value):
        try:
            r_a.onkeydown = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_p_r_e_s_s(r_a):
        try:
            return r_a.onkeypress
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_p_r_e_s_s(r_a, value):
        try:
            r_a.onkeypress = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_u_p(r_a):
        try:
            return r_a.onkeyup
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_k_e_y_u_p(r_a, value):
        try:
            r_a.onkeyup = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_d_o_w_n(r_a):
        try:
            return r_a.onmousedown
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_d_o_w_n(r_a, value):
        try:
            r_a.onmousedown = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_m_o_v_e(r_a):
        try:
            return r_a.onmousemove
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_m_o_v_e(r_a, value):
        try:
            r_a.onmousemove = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_u_t(r_a):
        try:
            return r_a.onmouseout
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_u_t(r_a, value):
        try:
            r_a.onmouseout = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_v_e_r(r_a):
        try:
            return r_a.onmouseover
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_o_v_e_r(r_a, value):
        try:
            r_a.onmouseover = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_u_p(r_a):
        try:
            return r_a.onmouseup
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_m_o_u_s_e_u_p(r_a, value):
        try:
            r_a.onmouseup = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_i_g_n(r_a):
        try:
            return r_a.align
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_i_g_n(r_a, value):
        try:
            r_a.align = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_d_e_x(r_a):
        try:
            return r_a.index
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(r_a):
        try:
            return r_a.cellPadding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_p_a_d_d_i_n_g(r_a, value):
        try:
            r_a.cellPadding = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(r_a):
        try:
            return r_a.cellSpacing
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_s_p_a_c_i_n_g(r_a, value):
        try:
            r_a.cellSpacing = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_g_n(r_a):
        try:
            return r_a.vAlign
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_g_n(r_a, value):
        try:
            r_a.vAlign = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_o_w_i_n_d_e_x(r_a):
        try:
            return r_a.rowIndex
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_e_l_l_i_n_d_e_x(r_a):
        try:
            return r_a.cellIndex
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_c_k_g_r_o_u_n_d(i_m_g):
        try:
            return i_m_g.background
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_c_k_g_r_o_u_n_d(i_m_g, value):
        try:
            i_m_g.background = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_g_c_o_l_o_r(i_m_g):
        try:
            return i_m_g.bgColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_g_c_o_l_o_r(i_m_g, value):
        try:
            i_m_g.bgColor = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_o_r_d_e_r(i_m_g):
        try:
            return i_m_g.border
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_o_r_d_e_r(i_m_g, value):
        try:
            i_m_g.border = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_e_i_g_h_t(i_m_g):
        try:
            return i_m_g.height
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_e_i_g_h_t(i_m_g, value):
        try:
            i_m_g.height = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_s_p_a_c_e(i_m_g):
        try:
            return i_m_g.hspace
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_s_p_a_c_e(i_m_g, value):
        try:
            i_m_g.hspace = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_a_p(i_m_g):
        try:
            return i_m_g.isMap
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_a_p(i_m_g, value):
        try:
            i_m_g.isMap = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_n_g_d_e_s_c(i_m_g):
        try:
            return i_m_g.longDesc
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_n_g_d_e_s_c(i_m_g, value):
        try:
            i_m_g.longDesc = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_w_s_o_u_r_c(e_l):
        try:
            return e_l.lowsrc
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_w_s_o_u_r_c(e_l, value):
        try:
            e_l.lowsrc = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_a_r_g_i_n_h_e_i_g_h_t(e_l):
        try:
            return e_l.marginHeight
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_a_r_g_i_n_h_e_i_g_h_t(e_l, value):
        try:
            e_l.marginHeight = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_a_r_g_i_n_w_i_d_t_h(e_l):
        try:
            return e_l.marginWidth
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_a_r_g_i_n_w_i_d_t_h(e_l, value):
        try:
            e_l.marginWidth = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e_p_l_a_i_n(e_l):
        try:
            return e_l.name
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e_p_l_a_i_n(e_l, value):
        try:
            e_l.name = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_l_o_w_f_u_l_l_s_c_r_e_e_n(e_l):
        try:
            return e_l.allowFullScreen
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_l_l_o_w_f_u_l_l_s_c_r_e_e_n(e_l, value):
        try:
            e_l.allowFullScreen = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_b_o_r_d_e_r(e_l):
        try:
            return e_l.frameBorder
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_b_o_r_d_e_r(e_l, value):
        try:
            e_l.frameBorder = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_s_p_a_c_i_n_g(e_l):
        try:
            return e_l.frameSpacing
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_r_a_m_e_s_p_a_c_i_n_g(e_l, value):
        try:
            e_l.frameSpacing = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_o_r_e_s_i_z_e(e_l):
        try:
            return e_l.noResize
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_o_r_e_s_i_z_e(e_l, value):
        try:
            e_l.noResize = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_o_l_l_i_n_g(e_l):
        try:
            return e_l.scrolling
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_o_l_l_i_n_g(e_l, value):
        try:
            e_l.scrolling = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_r_g_e_t(i_m_g):
        try:
            return i_m_g.target
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_r_g_e_t(i_m_g, value):
        try:
            i_m_g.target = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_h_a_p_e(i_m_g):
        try:
            return i_m_g.shape
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_h_a_p_e(i_m_g, value):
        try:
            i_m_g.shape = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_e_r(i_m_g):
        try:
            return i_m_g.href
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_e_r(i_m_g, value):
        try:
            i_m_g.href = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_i_s(i_m_g):
        try:
            return i_m_g.host
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_o_s_t(i_m_g):
        try:
            return i_m_g.host
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_o_s_t_n_a_m_e(i_m_g):
        try:
            return i_m_g.hostname
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_p_a_r_t(i_m_g):
        try:
            return i_m_g.hrefpart
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_p_a_r_t(i_m_g, value):
        try:
            i_m_g.hrefpart = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_o_t_o_c_o_l(i_m_g):
        try:
            return i_m_g.protocol
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_o_t_o_c_o_l(i_m_g, value):
        try:
            i_m_g.protocol = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_a_r_c_h(i_m_g):
        try:
            return i_m_g.search
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_a_r_c_h(i_m_g, value):
        try:
            i_m_g.search = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_r_t(i_m_g):
        try:
            return i_m_g.port
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_r_t(i_m_g, value):
        try:
            i_m_g.port = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_a_r_e_n_t(e_l):
        try:
            return e_l.parent
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f(n_o):
        try:
            return n_o.href
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f(n_o, value):
        try:
            n_o.href = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_o_r_d_S_t_e_e_l_i_n_g(n_o):
        try:
            return n_o.coordSteling
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_o_r_d_S_t_e_e_l_i_n_g(n_o, value):
        try:
            n_o.coordSteling = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_r_g_e_t(n_o):
        try:
            return n_o.target
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_r_g_e_t(n_o, value):
        try:
            n_o.target = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_h_a_p_e(n_o):
        try:
            return n_o.shape
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_h_a_p_e(n_o, value):
        try:
            n_o.shape = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_l(n_o):
        try:
            return n_o.rel
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_l(n_o, value):
        try:
            n_o.rel = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_v(o_l):
        try:
            return o_l.rev
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_v(o_l, value):
        try:
            o_l.rev = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_s_c_e_t(t):
        try:
            return t.hrefSet
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_s_c_e_t(t, value):
        try:
            t.hrefSet = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_b_i_n_d_e_x(t):
        try:
            return t.tabIndex
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_a_b_i_n_d_e_x(t, value):
        try:
            t.tabIndex = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_s_k_e_y_t_r_a_p(t):
        try:
            return t.accessKeyTrap
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_s_k_e_y_t_r_a_p(t, value):
        try:
            t.accessKeyTrap = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_a_v_e_k_e_y(t):
        try:
            return t.saveKey
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_a_v_e_k_e_y(t, value):
        try:
            t.saveKey = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_k_i_p_i_n_k_e_y(t):
        try:
            return t.skipInKey
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_k_i_p_i_n_k_e_y(t, value):
        try:
            t.skipInKey = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_h_i_f_t(t):
        try:
            return t.shift
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_h_i_f_t(t, value):
        try:
            t.shift = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_u_b(l_i):
        try:
            return l_i.pub
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_u_b(l_i, value):
        try:
            l_i.pub = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_i_v(l_i):
        try:
            return l_i.priv
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_i_v(l_i, value):
        try:
            l_i.priv = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_r_e_s_i_z_e(t):
        try:
            return t.onResize
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_r_e_s_i_z_e(t, value):
        try:
            t.onResize = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_z_o_o_m(i_m_g):
        try:
            return i_m_g.onZoom
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_n_z_o_o_m(i_m_g, value):
        try:
            i_m_g.onZoom = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_r_e_a_t_e_t_e_x_t_n_o_d_e(n_o):
        try:
            return n_o.createTextRange
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_a_d_j_a_c_e_n_t_t_e_x_t(r_a):
        try:
            return r_a.selectAdjacentText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_p_u_t_e_l(e_l):
        try:
            return e_l.isInput
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_p_u_t_e_l(e_l, value):
        try:
            e_l.isInput = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_t_e_x_t_a_r_e_a(e_l):
        try:
            return e_l.isText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_t_e_x_t_a_r_e_a(e_l, value):
        try:
            e_l.isText = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_a_c_t_i_v_e(e_l):
        try:
            return e_l.isActive
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_a_c_t_i_v_e(e_l, value):
        try:
            e_l.isActive = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_g(e_l):
        try:
            return e_l.big
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_l_i_n_k(e_l):
        try:
            return e_l.blink
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_l_i_n_k_i_n_g(e_l):
        try:
            return e_l.blinking
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_o_n_t_c_o_l_o_r(e_l):
        try:
            return e_l.fontColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_C_o_l_o_r(e_l):
        try:
            return e_l.linkColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_t_e_d_l_i_n_k_c_o_l_o_r(e_l):
        try:
            return e_l.visitedLinkColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_t_e_d_t_e_x_t_c_o_l_o_r(e_l):
        try:
            return e_l.visitedTextColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_t_i_v_e_l_i_n_k_c_o_l_o_r(e_l):
        try:
            return e_l.activeLinkColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_t_i_v_e_l_i_n_k_c_o_l_o_r_f_o_l_l_o_w_i(n_o):
        try:
            return n_o.activeLinkColorFollowed
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_r_i_a_s_o_f_f(e_l):
        try:
            return e_l.ariaSoe
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_o_n_e_l_i_n_e_r(a):
        try:
            return a.noHref
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_o_p_i_n_g(e_l):
        try:
            return e_l.loop
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_o_p_i_n_g(e_l, value):
        try:
            e_l.loop = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_t_a_r_t(e_l):
        try:
            return e_l.start
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_t_a_r_t(e_l, value):
        try:
            e_l.start = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_o_l_u_m_e(i_m_g):
        try:
            return i_m_g.volume
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_o_l_u_m_e(i_m_g, value):
        try:
            i_m_g.volume = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_y(e_l):
        try:
            return e_l.play
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_a_u_s_e(e_l):
        try:
            return e_l.pause
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_v_o_l_u_m_e_b_a_r(a):
        try:
            return a.isVolumeBar
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_e_g_i_n(a):
        try:
            return a.begin
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_e_g_i_n(a, value):
        try:
            a.begin = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_o_o_t_s_t_r_a_p_C_o_u_r_s_e(n_o):
        try:
            return n_o.bootstrapCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_o_o_t_s_t_r_a_p_C_o_u_r_s_e(n_o, value):
        try:
            n_o.bootstrapCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_p_e_n(e_l):
        try:
            return e_l.open
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_p_e_n(e_l, value):
        try:
            e_l.open = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_n_t_e_n_t_C_o_u_r_s_e(n_o):
        try:
            return n_o.contentCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_n_t_e_n_t_C_o_u_r_s_e(n_o, value):
        try:
            n_o.contentCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_C_o_u_r_s_e(n_o):
        try:
            return n_o.linkCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_C_o_u_r_s_e(n_o, value):
        try:
            n_o.linkCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_o_o_l_b_a_r(n_o):
        try:
            return n_o.toolBar
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_o_o_l_b_a_r(n_o, value):
        try:
            n_o.toolBar = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_e_n_u_b_a_r(n_o):
        try:
            return n_o.menuBar
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_e_n_u_b_a_r(n_o, value):
        try:
            n_o.menuBar = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_o_o_l_b_a_r_C_o_u_r_s_e(n_o):
        try:
            return n_o.toolBarCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_o_o_l_b_a_r_C_o_u_r_s_e(n_o, value):
        try:
            n_o.toolBarCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_o_l_l_i_n_g_C_o_u_r_s_e(n_o):
        try:
            return n_o.scrollingCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_o_l_l_i_n_g_C_o_u_r_s_e(n_o, value):
        try:
            n_o.scrollingCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_t_a_t_u_s_b_a_r(n_o):
        try:
            return n_o.statusBar
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_t_a_t_u_s_b_a_r(n_o, value):
        try:
            n_o.statusBar = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_c_k_C_o_u_r_s_e(n_o):
        try:
            return n_o.backCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_c_k_C_o_u_r_s_e(n_o, value):
        try:
            n_o.backCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y(n_o):
        try:
            return n_o.validity
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y(n_o, value):
        try:
            n_o.validity = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_w_i_l_l_S_u_b_m_i_t(n_o):
        try:
            return n_o.willSubmit
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_u_t_o_C_o_m_p_l_e_t_e(n_o):
        try:
            return n_o.autoComplete
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_u_t_o_C_o_m_p_l_e_t_e(n_o, value):
        try:
            n_o.autoComplete = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_a_p_p_l_i_c_a_t_i_o_n(n_o):
        try:
            return n_o.mozApplication
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_a_p_p_l_i_c_a_t_i_o_n(n_o, value):
        try:
            n_o.mozApplication = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_b_r_o_w_s_e_r_o_p_e_n(n_o):
        try:
            return n_o.mozBrowserOpen
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_b_r_o_w_s_e_r_o_p_e_n(n_o, value):
        try:
            n_o.mozBrowserOpen = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_a_p_p_l_i_c_a_t_i_o_n_n_a_m_e(n_o):
        try:
            return n_o.mozApplicationName
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_a_p_p_l_i_c_a_t_i_o_n_v_e_r_s_i_o(n_o):
        try:
            return n_o.mozApplicationVersion
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_f_i_n_d(n_o):
        try:
            return n_o.mozFind
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_b_r_o_w_s_e_r(n_o):
        try:
            return n_o.mozBrowser
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_i_d(n_o):
        try:
            return n_o.isId
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_r_o_w_s_e_r_o_p_e_n(n_o):
        try:
            return n_o.browserOpen
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_r_o_w_s_e_r_o_p_e_n(n_o, value):
        try:
            n_o.browserOpen = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_r_o_m_e_o_p_e_n(n_o):
        try:
            return n_o.chromeOpen
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_r_o_m_e_o_p_e_n(n_o, value):
        try:
            n_o.chromeOpen = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_o_u_r_c_e(n_o):
        try:
            return n_o.source
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_o_u_r_c_e(n_o, value):
        try:
            n_o.source = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_y_o_n_l_o_a_d(n_o):
        try:
            return n_o.playOnLoad
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_y_o_n_l_o_a_d(n_o, value):
        try:
            n_o.playOnLoad = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_o_p_e_n_i_n_g_t_a_b_s(i_m_g):
        try:
            return i_m_g.isOpeningTabs
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_a_d_i_n_g_t_i_m_e_o_u_t(n_o):
        try:
            return n_o.loadingTimeout
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_a_d_i_n_g_t_i_m_e_o_u_t(n_o, value):
        try:
            n_o.loadingTimeout = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_u_p_d_a_t_e_i_n_t_e_r_v_a_l(n_o):
        try:
            return n_o.updateInterval
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_u_p_d_a_t_e_i_n_t_e_r_v_a_l(n_o, value):
        try:
            n_o.updateInterval = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_c_o_r_d(n_o):
        try:
            return n_o.record
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_p_l_a_y(n_o):
        try:
            return n_o.replay
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_c_o_r_d_i_n_g_C_o_u_r_s_e(n_o):
        try:
            return n_o.recordingCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_a_n_g(u_l):
        try:
            return u_l.lang
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_a_n_g(u_l, value):
        try:
            u_l.lang = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_t_e_d_h_r_e_f_l_i_n_k_C_o_l_o_r(u_l):
        try:
            return u_l.visitedHrefLinkColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_t_e_d_l_i_n_k_S_t_y_l_e(u_l):
        try:
            return u_l.visitedLinkStyle
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_i_s_t_o_r_y(n_o):
        try:
            return n_o.history
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_u_s_e_s_t_a_m_p(n_o):
        try:
            return n_o.useStamp
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_u_s_e_s_t_a_m_p(n_o, value):
        try:
            n_o.useStamp = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_u_p_p_r_e_s_s_o_p_e_n_i_n_g_b_r_o_w_s_e_r(n_o):
        try:
            return n_o.suppressOpeningBrowser
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_u_p_p_r_e_s_s_o_p_e_n_i_n_g_b_r_o_w_s_e_r(n_o, value):
        try:
            n_o.suppressOpeningBrowser = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_i_n_t_e_r(n_o):
        try:
            return n_o.pointer
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_s_h_a_s_h(e_l):
        try:
            return e_l.hasHash
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_s_c_i_i(a):
        try:
            return a.ascii
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_i_s_t_o_r_y_p_u_s_h_S_t_a_t_e(t):
        try:
            return t.historyPushState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_p_s_t_a_t_e(t):
        try:
            return t.popState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_u_s_h_S_t_a_t_e(t):
        try:
            return t.pushState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_p_l_a_c_e_S_t_a_t_e(t):
        try:
            return t.replaceState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_p_S_t_a_t_e(t):
        try:
            return t.popState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_s_t_r_u_c_t(u_l):
        try:
            return u_l.destruct
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_s_t_r_u_c_t(u_l, value):
        try:
            u_l.destruct = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_i_s_t_o_r_y_l_i_s_t(n_o):
        try:
            return n_o.historyList
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_e_v_i_o_u_s(u_l):
        try:
            return u_l.previous
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_e_x_t(u_l):
        try:
            return u_l.next
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_s_e_t_b_u_t_t_o_n(u_l):
        try:
            return u_l.resetButton
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_s_e_t_t_b(u_l):
        try:
            return u_l.resetTb
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_y_t_h_e_m_e(s):
        try:
            return s.playTheme
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_a_u_s_e_t_h_e_m_e(s):
        try:
            return s.pauseTheme
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_i_n_s(u_l):
        try:
            return u_l.mins
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_u_r_r(e_l):
        try:
            return e_l.curr
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_t_m_l_r_e_m(o_l):
        try:
            return o_l.htmlRem
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_t_m_l_r_e_m(o_l, value):
        try:
            o_l.htmlRem = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_o_d_y_r_e_m(u_l):
        try:
            return u_l.bodyRem
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_o_d_y_r_e_m(u_l, value):
        try:
            u_l.bodyRem = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_u_s_h_T_a_r_g_e_t(n_o):
        try:
            return n_o.pushTarget
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_u_s_h_T_a_r_g_e_t(n_o, value):
        try:
            n_o.pushTarget = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_a_m_e_S_i_t_e(u_l):
        try:
            return u_l.sameSite
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_a_m_e_S_i_t_e(u_l, value):
        try:
            u_l.sameSite = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_r_o_w_s_e_r_S_t_y_l_e(u_l):
        try:
            return u_l.browserStyle
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_r_o_w_s_e_r_S_t_y_l_e(u_l, value):
        try:
            u_l.browserStyle = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_f_e_r_e_r(u_l):
        try:
            return u_l.referrer
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_f_e_r_e_r(u_l, value):
        try:
            u_l.referrer = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_u_s_e_s_t_a_m_p(n_o):
        try:
            return n_o.mozUseStamp
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_u_s_e_s_t_a_m_p(n_o, value):
        try:
            n_o.mozUseStamp = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_u_b_m_i_t_t_e_d(s):
        try:
            return s.submitted
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_r_e_p_o_r_t_s_v_a_l_i_d(i_m_g):
        try:
            return i_m_g.validityReportsValid
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_c_u_s_t_o_m_e_r_m(e_l):
        try:
            return e_l.validityCustomerM
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_t_y_p_e_m_i_s_m_a_t_c_h(u_l):
        try:
            return u_l.validityTypeMismatch
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_r_a_n_g_e_o_u_t_o_f_b_o_u_n_d(i_m_g):
        try:
            return i_m_g.validityRangeOob
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_r_a_n_g_e_u_n_d_e_r_f_l_o_w(i_m_g):
        try:
            return i_m_g.validityRangeUnderflow
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_n_t_r_o_l(l):
        try:
            return l.control
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_l_o_r(i_m_g):
        try:
            return i_m_g.color
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_o_d_y_c_o_l_o_r(i_m_g):
        try:
            return i_m_g.bodyColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_r(e_l):
        try:
            return e_l.dir
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_r(e_l, value):
        try:
            e_l.dir = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.link
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.link = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_v_i_s_i_t_e_d_l_i_n_k_C_o_l_o_r(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.mozVisitedLinkColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_v_i_s_i_t_e_d_l_i_n_k_C_o_l_o_r(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.mozVisitedLinkColor = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_g_C_o_u_r_s_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.bgCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_g_C_o_u_r_s_e(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.bgCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_g_C_o_u_r_s_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.fgCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_g_C_o_u_r_s_e(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.fgCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_e_x_t_C_o_u_r_s_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.textCourse
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_e_x_t_C_o_u_r_s_e(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.textCourse = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_t_i_o_n(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.action
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_t_i_o_n(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.action = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_r_e_s_i_z_e_b_g(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.isMozResizeBg
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_r_e_s_i_z_e_b_g(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.isMozResizeBg = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_b_i_l_i_t_y(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.visibility
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_b_i_l_i_t_y(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.visibility = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_p_e_a_t(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.repeat
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_p_e_a_t(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.repeat = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_o_r_m_e_l_e_m(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.formElement
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_o_r_m_e_l_e_m(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.formElement = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_e_r_f_o_r_m_a_n_c_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.performance
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_S_t_y_l_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.linkStyle
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_S_t_y_l_e(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.linkStyle = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_o_r_m_s(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.forms
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_t_i_v_e_e_l_e_m_e_n_t(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.activeElement
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_C_o_l_o_r(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.linkColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_u_l(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.ul
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.name
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_o_o_t_s(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.roots
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_p_u_p_M_e_n_u(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.popupMenu
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_s_e_u_r_l(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.baseURL
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_o_r_m_a_n_c_e_u_r_l(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.formanceURL
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_l_u_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.blue
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_a_r_c_h_m_o_z_a_p_p_l_i_c_a_t_i_o_n(n_o):
        try:
            return n_o.searchMozApplication
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_i_n_s_t_a_l_l(n_o):
        try:
            return n_o.isMozInstall
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_u_r_s_o_r(t):
        try:
            return t.cursor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_H_t_m_l(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.innerHtml
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_H_t_m_l(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.innerHtml = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_e_r_H_t_m_l(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.outerHtml
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_e_r_H_t_m_l(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.outerHtml = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_T_e_x_t(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.innerText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_T_e_x_t(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.innerText = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_e_r_T_e_x_t(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.outerText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_e_r_T_e_x_t(C_o_u_r_s_e, value):
        try:
            C_o_u_r_s_e.outerText = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_s_i_b_i_l_i_t_y_n_o_d_e(C_o_u_r_s_e):
        try:
            return C_o_u_r_s_e.accessibilityNode
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_a_n_i_p_u_l_a_t_e_l_e_m_e_n_t(l):
        try:
            return l.manipulateElement
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_l_l_a_p_s_e_S_e_l_e_c_t_i_o_n(t):
        try:
            return t.collapseSelection
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_e_v_i_o_u_s_E_l_e_m_e_n_t(t):
        try:
            return t.previousElement
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_e_x_t_E_l_e_m_e_n_t(t):
        try:
            return t.nextElement
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_t_S_e_l_e_c_t_i_o_n_R_a_n_g_e(t):
        try:
            return t.setSelectionRange
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_l_e_t_e_t_e_x_t(t):
        try:
            return t.deleteText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_s_e_r_t_t_e_x_t(t):
        try:
            return t.insertText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_a_l_l(t):
        try:
            return t.selectAll
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_e_x_t_C_o_n_t_e_n_t(t):
        try:
            return t.textContent
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_e_x_t_C_o_n_t_e_n_t(t, value):
        try:
            t.textContent = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_T_e_x_t_C_o_n_t_e_n_t(t):
        try:
            return t.innerTextContent
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_T_e_x_t_C_o_n_t_e_n_t(t, value):
        try:
            t.innerTextContent = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_t_m_l_C_o_n_t_e_n_t(t):
        try:
            return t.htmlContent
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_t_m_l_C_o_n_t_e_n_t(t, value):
        try:
            t.htmlContent = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_e_r_T_e_x_t_C_o_n_t_e_n_t(t):
        try:
            return t.outerTextContent
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_e_r_T_e_x_t_C_o_n_t_e_n_t(t, value):
        try:
            t.outerTextContent = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_o_c_u_s_i_n_g(t):
        try:
            return t.focusing
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_l_u_r(t):
        try:
            return t.blur
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_t_i_n_g(t):
        try:
            return t.inputting
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t(t):
        try:
            return t.input
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t(t, value):
        try:
            t.input = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_l_i_c_k_i_n_g(t):
        try:
            return t.clicking
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_u_b_m_i_t(t):
        try:
            return t.submit
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_s_e_t(t):
        try:
            return t.reset
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_u_t_t_o_n_p_u_s_h(t):
        try:
            return t.buttonPush
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_u_t_t_o_n(t):
        try:
            return t.button
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_e_n_a_b_l_e_d(t):
        try:
            return t.isMozEnabled
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_e_n_a_b_l_e_d(t, value):
        try:
            t.isMozEnabled = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_c_h_e_c_k_e_d(t):
        try:
            return t.isMozChecked
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_c_h_e_c_k_e_d(t, value):
        try:
            t.isMozChecked = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_c_h_e_c_k_i_n_d_e_t_e_r_m_i_n_e_d(t):
        try:
            return t.isMozCheckIndetermined
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_c_h_e_c_k_i_n_d_e_t_e_r_m_i_n_e_d(t, value):
        try:
            t.isMozCheckIndetermined = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_r_a_d_i_o_g_r_o_u_p(t):
        try:
            return t.isMozRadioGroup
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_r_a_d_i_o_g_r_o_u_p(t, value):
        try:
            t.isMozRadioGroup = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_s_e_r_v_e_r_p_u_s_h_t_r_i_g_g_e_r(t):
        try:
            return t.isMozServerPushTrigger
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_s_e_r_v_e_r_p_u_s_h_t_r_i_g_g_e_r(t, value):
        try:
            t.isMozServerPushTrigger = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_v_i_s_i_b_i_l_i_t_y(c):
        try:
            return c.isMozVisibility
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_v_i_s_i_b_i_l_i_t_y(c, value):
        try:
            c.isMozVisibility = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_r_a_d_i_o(t):
        try:
            return t.isMozRadio
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_m_o_z_r_a_d_i_o(t, value):
        try:
            t.isMozRadio = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_t_o_o_l_t_i_p(t):
        try:
            return t.tooltip
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_t_o_o_l_t_i_p(t, value):
        try:
            t.tooltip = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_u_r_i(t):
        try:
            return t.uri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_u_r_i(t, value):
        try:
            t.uri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_t_e_d(t):
        try:
            return t.visited
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_i_s_i_t_e_d(t, value):
        try:
            t.visited = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_a_r_s_e_t(t):
        try:
            return t.charset
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_a_r_s_e_t(t, value):
        try:
            t.charset = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_p_o_r_t_U_r_i(t):
        try:
            return t.reportUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_p_o_r_t_U_r_i(t, value):
        try:
            t.reportUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_s_k_e_y(t):
        try:
            return t.accessKey
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_s_k_e_y(t, value):
        try:
            t.accessKey = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_r_a_g_c_o_l_o_r(t):
        try:
            return t.dragColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_r_a_g_c_o_l_o_r(t, value):
        try:
            t.dragColor = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_l_i_n_k_U_r_i(t):
        try:
            return t.hrefLinkUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_r_e_f_l_i_n_k_U_r_i(t, value):
        try:
            t.hrefLinkUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e_s_p_a_c_e(t):
        try:
            return t.namespace
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e_s_p_a_c_e(t, value):
        try:
            t.namespace = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_t_i_v_e_U_r_i(t):
        try:
            return t.activeUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_t_i_v_e_U_r_i(t, value):
        try:
            t.activeUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_f_e_r_r_e_r(t):
        try:
            return t.referrer
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_f_e_r_r_e_r(t, value):
        try:
            t.referrer = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_o_c_u_m_e_n_t_U_r_i(t):
        try:
            return t.documentUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_o_c_u_m_e_n_t_U_r_i(t, value):
        try:
            t.documentUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_o_m_C_o_l_o_r(t):
        try:
            return t.domColor
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_o_m_C_o_l_o_r(t, value):
        try:
            t.domColor = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_U_r_i(t):
        try:
            return t.linkUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_k_U_r_i(t, value):
        try:
            t.linkUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_f_e_r_e_r_P_o_l_i_c_y_U_r_i(t):
        try:
            return t.referrerPolicyUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_f_e_r_e_r_P_o_l_i_c_y_U_r_i(t, value):
        try:
            t.referrerPolicyUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_l_o_r_U_r_i(t):
        try:
            return t.colorUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_o_l_o_r_U_r_i(t, value):
        try:
            t.colorUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_R_e_f_l_o_w_E_n_c_o_d_i_n_g(t):
        try:
            return t.firefoxReflowEncoding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_R_e_f_l_o_w_E_n_c_o_d_i_n_g(t, value):
        try:
            t.firefoxReflowEncoding = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_i_s(t):
        try:
            return t.this
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_T_e_l_e_m_e_t_r_y(t):
        try:
            return t.firefoxTelemetry
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_T_e_l_e_m_e_t_r_y(t, value):
        try:
            t.firefoxTelemetry = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_e_d_T_e_x_t(t):
        try:
            return t.selectedText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_B_l_o_c_k_I_n_p_u_t(t):
        try:
            return t.firefoxBlockInput
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_B_l_o_c_k_I_n_p_u_t(t, value):
        try:
            t.firefoxBlockInput = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_S_h_o_u_l_d_C_o_n_t_i_n_u_e(t):
        try:
            return t.firefoxShouldContinue
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_S_h_o_u_l_d_C_o_n_t_i_n_u_e(t, value):
        try:
            t.firefoxShouldContinue = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_F_o_r_c_e_R_e_r_e_a_d(t):
        try:
            return t.firefoxForceReread
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_F_o_r_c_e_R_e_r_e_a_d(t, value):
        try:
            t.firefoxForceReread = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_H_t_m_l_U_r_i(t):
        try:
            return t.firefoxHtmlUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_H_t_m_l_U_r_i(t, value):
        try:
            t.firefoxHtmlUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_e_n_u_m_b_e_r_U_r_i(t):
        try:
            return t.lineNumberUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_n_e_n_u_m_b_e_r_U_r_i(t, value):
        try:
            t.lineNumberUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_p_l_a_y_U_r_i(t):
        try:
            return t.displayUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_p_l_a_y_U_r_i(t, value):
        try:
            t.displayUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_p_l_a_y_F_o_r_m_s(t):
        try:
            return t.displayForms
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_p_l_a_y_F_o_r_m_s(t, value):
        try:
            t.displayForms = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_E_n_a_b_l_e_I_m_g_A_u_t_o_L_o_a_d(t):
        try:
            return t.firefoxEnableImgAutoLoad
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_E_n_a_b_l_e_I_m_g_A_u_t_o_L_o_a_d(t, value):
        try:
            t.firefoxEnableImgAutoLoad = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_s_e_T_a_r_g_e_t(t):
        try:
            return t.baseTarget
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_s_e_T_a_r_g_e_t(t, value):
        try:
            t.baseTarget = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_o_m_U_r_i(t):
        try:
            return t.domUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_o_m_U_r_i(t, value):
        try:
            t.domUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_e_e_n_X(t):
        try:
            return t.screenX
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_e_e_n_X(t, value):
        try:
            t.screenX = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_e_e_n_Y(t):
        try:
            return t.screenY
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_c_r_e_e_n_Y(t, value):
        try:
            t.screenY = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_H_t_m_l(t):
        try:
            return t.innerHtml
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_n_e_r_H_t_m_l(t, value):
        try:
            t.innerHtml = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_a_r_e_n_t_D_o_c_u_m_e_n_t(t):
        try:
            return t.parentDocument
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_a_r_e_n_t_N_o_d_e(t):
        try:
            return t.parentNode
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_o_o_t_N_o_d_e(t):
        try:
            return t.rootNode
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_U_r_i(t):
        try:
            return t.inputUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_U_r_i(t, value):
        try:
            t.inputUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_i_n_g_U_r_i(t):
        try:
            return t.ringUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_i_n_g_U_r_i(t, value):
        try:
            t.ringUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_p_e_c_i_a_l_C_h_a_r_a_c_t_e_r_U_r_i(t):
        try:
            return t.specialCharacterUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_p_e_c_i_a_l_C_h_a_r_a_c_t_e_r_U_r_i(t, value):
        try:
            t.specialCharacterUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_I_m_g_C_h_e_c_k(t):
        try:
            return t.firefoxImgCheck
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_i_r_e_f_o_x_I_m_g_C_h_e_c_k(t, value):
        try:
            t.firefoxImgCheck = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_D_o_m_U_i(t):
        try:
            return t.hasDomUi
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_D_o_m_U_i(t, value):
        try:
            t.hasDomUi = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_U_i(n):
        try:
            return n.hasUi
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_U_i(n, value):
        try:
            n.hasUi = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_a_r_e_n_t_U_i(n):
        try:
            return n.parentUi
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_e_v_i_o_u_s_U_i(n):
        try:
            return n.previousUi
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_e_x_t_U_i(n):
        try:
            return n.nextUi
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_M_o_z_C_h_e_c_k_b_o_x(n):
        try:
            return n.hasMozCheckBox
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_M_o_z_C_h_e_c_k_b_o_x(n, value):
        try:
            n.hasMozCheckBox = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_M_o_z_M_o_n_o(b):
        try:
            return b.hasMozMono
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_M_o_z_M_o_n_o(b, value):
        try:
            b.hasMozMono = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_M_o_z_R_a_d_i_o(n):
        try:
            return n.hasMozRadio
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_M_o_z_R_a_d_i_o(n, value):
        try:
            n.hasMozRadio = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_a_r_e_n_t_B_i_n_d_i_n_g(b):
        try:
            return b.parentBinding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_e_v_i_o_u_s_B_i_n_d_i_n_g(b):
        try:
            return b.previousBinding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_e_x_t_B_i_n_d_i_n_g(b):
        try:
            return b.nextBinding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_D_o_m_B_i_n_d_i_n_g(n):
        try:
            return n.hasDomBinding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_D_o_m_B_i_n_d_i_n_g(n, value):
        try:
            n.hasDomBinding = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_F_l_a_g(b):
        try:
            return b.bindingFlag
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_F_l_a_g(b, value):
        try:
            b.bindingFlag = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_X_m_l_U_r_i(n):
        try:
            return n.hasXmlUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_a_s_X_m_l_U_r_i(n, value):
        try:
            n.hasXmlUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_P_o_l_i_c_y_P_u_s_h(t):
        try:
            return t.isPolicyPush
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_s_P_o_l_i_c_y_P_u_s_h(t, value):
        try:
            t.isPolicyPush = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_l_i_c_y_U_r_i(t):
        try:
            return t.policyUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_l_i_c_y_U_r_i(t, value):
        try:
            t.policyUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_l_i_c_y(t):
        try:
            return t.policy
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_o_l_i_c_y(t, value):
        try:
            t.policy = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_s_p_o_n_s_e_U_r_i(t):
        try:
            return t.responseUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_s_p_o_n_s_e_U_r_i(t, value):
        try:
            t.responseUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_t_m_l_U_r_i(t):
        try:
            return t.htmlUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_t_m_l_U_r_i(t, value):
        try:
            t.htmlUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_s_a_b_a_s_e_U_r_i(n):
        try:
            return n.nsABaseUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_s_a_b_a_s_e_U_r_i(n, value):
        try:
            n.nsABaseUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_a_d_o_n_l_y(n):
        try:
            return n.readOnly
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_a_d_o_n_l_y(n, value):
        try:
            n.readOnly = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_a_d_U_r_i(n):
        try:
            return n.loadUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_a_d_U_r_i(n, value):
        try:
            n.loadUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_s_e_U_r_i(n):
        try:
            return n.baseUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_a_s_e_U_r_i(n, value):
        try:
            n.baseUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_I_d(n):
        try:
            return n.inputCharacterId
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_I_d(n, value):
        try:
            n.inputCharacterId = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_U_r_i(n):
        try:
            return n.inputCharacterUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_U_r_i(n, value):
        try:
            n.inputCharacterUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_S_t_a_t_e(n):
        try:
            return n.inputCharacterState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_S_t_a_t_e(n, value):
        try:
            n.inputCharacterState = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_U_r_i(n):
        try:
            return n.placeholderUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_U_r_i(n, value):
        try:
            n.placeholderUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n_U_r_i(n):
        try:
            return n.selectionUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n_U_r_i(n, value):
        try:
            n.selectionUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n(n):
        try:
            return n.selection
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n(n, value):
        try:
            n.selection = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y(n):
        try:
            return n.validity
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y(n, value):
        try:
            n.validity = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_a_d_o_n_l_y_U_r_i(n):
        try:
            return n.readOnlyUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_a_d_o_n_l_y_U_r_i(n, value):
        try:
            n.readOnlyUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_U_r_i(n):
        try:
            return n.validityUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_U_r_i(n, value):
        try:
            n.validityUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_o_f_R_a_n_g_e_U_r_i(n):
        try:
            return n.outOfRangeUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_o_u_t_o_f_R_a_n_g_e_U_r_i(n, value):
        try:
            n.outOfRangeUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_S_t_a_t_e(n):
        try:
            return n.validityState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_v_a_l_i_d_i_t_y_S_t_a_t_e(n, value):
        try:
            n.validityState = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_u_r_r_e_n_t_I_n_d_i_c_a_t_o_r(n):
        try:
            return n.currentIndicator
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_u_r_r_e_n_t_I_n_d_i_c_a_t_o_r(n, value):
        try:
            n.currentIndicator = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_f_u_l_l_y_V_i_s_i_b_l_e(n):
        try:
            return n.fullyVisible
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_f_u_l_l_y_V_i_s_i_b_l_e(n, value):
        try:
            n.fullyVisible = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_u_r_r_e_n_t_S_e_l_e_c_t_i_o_n_U_r_i(n):
        try:
            return n.currentSelectionUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_u_r_r_e_n_t_S_e_l_e_c_t_i_o_n_U_r_i(n, value):
        try:
            n.currentSelectionUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n_R_a_n_g_e(n):
        try:
            return n.selectionRange
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n_R_a_n_g_e(n, value):
        try:
            n.selectionRange = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n_S_t_a_t_e(n):
        try:
            return n.selectionState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_e_l_e_c_t_i_o_n_S_t_a_t_e(n, value):
        try:
            n.selectionState = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_a_b_e_l(n):
        try:
            return n.label
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_a_b_e_l(n, value):
        try:
            n.label = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r(n):
        try:
            return n.placeholder
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r(n, value):
        try:
            n.placeholder = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_a_b_l_e_d(n):
        try:
            return n.disabled
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_a_b_l_e_d(n, value):
        try:
            n.disabled = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_s_k_e_y(n):
        try:
            return n.accessKey
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_c_c_e_s_s_k_e_y(n, value):
        try:
            n.accessKey = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_1(n):
        try:
            return n.mozHtmlCheckBox1
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_1(n, value):
        try:
            n.mozHtmlCheckBox1 = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_2(n):
        try:
            return n.mozHtmlCheckBox2
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_2(n, value):
        try:
            n.mozHtmlCheckBox2 = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_3(n):
        try:
            return n.mozHtmlCheckBox3
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_3(n, value):
        try:
            n.mozHtmlCheckBox3 = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_4(n):
        try:
            return n.mozHtmlCheckBox4
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_4(n, value):
        try:
            n.mozHtmlCheckBox4 = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_5(n):
        try:
            return n.mozHtmlCheckBox5
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_m_o_z_H_t_m_l_C_h_e_c_k_b_o_x_5(n, value):
        try:
            n.mozHtmlCheckBox5 = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_e_c_k_e_d(n):
        try:
            return n.checked
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_e_c_k_e_d(n, value):
        try:
            n.checked = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_a_d_i_o_g_r_o_u_p(n):
        try:
            return n.radioGroup
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_a_d_i_o_g_r_o_u_p(n, value):
        try:
            n.radioGroup = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_T_y_p_e(n):
        try:
            return n.placeholderType
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_T_y_p_e(n, value):
        try:
            n.placeholderType = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_T_e_x_t(n):
        try:
            return n.placeholderText
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_T_e_x_t(n, value):
        try:
            n.placeholderText = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_a_d_i_o(n):
        try:
            return n.radio
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_a_d_i_o(n, value):
        try:
            n.radio = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_N_o_d_e(n):
        try:
            return n.placeholderNode
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_N_o_d_e(n, value):
        try:
            n.placeholderNode = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_S_t_r_i_n_g(n):
        try:
            return n.placeholderString
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_S_t_r_i_n_g(n, value):
        try:
            n.placeholderString = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_d_e_t_e_x_t(n):
        try:
            return n.indetext
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_d_e_t_e_x_t(n, value):
        try:
            n.indetext = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_I_n_d_e_x(n):
        try:
            return n.placeholderIndex
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_l_a_c_e_h_o_l_d_e_r_I_n_d_e_x(n, value):
        try:
            n.placeholderIndex = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_a_b_l_e_d_U_r_i(n):
        try:
            return n.disabledUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_i_s_a_b_l_e_d_U_r_i(n, value):
        try:
            n.disabledUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_H_i_n_t(n):
        try:
            return n.inputCharacterHint
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_C_h_a_r_a_c_t_e_r_H_i_n_t(n, value):
        try:
            n.inputCharacterHint = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_a_d_I_n_d_i_c_a_t_o_r(n):
        try:
            return n.loadIndicator
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_o_a_d_I_n_d_i_c_a_t_o_r(n, value):
        try:
            n.loadIndicator = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_e_v_i_o_u_s_I_n_d_i_c_a_t_o_r(n):
        try:
            return n.previousIndicator
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_e_v_i_o_u_s_I_n_d_i_c_a_t_o_r(n, value):
        try:
            n.previousIndicator = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_e_x_t_I_n_d_i_c_a_t_o_r(n):
        try:
            return n.nextIndicator
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_e_x_t_I_n_d_i_c_a_t_o_r(n, value):
        try:
            n.nextIndicator = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_h_i_d_d_e_n(n):
        try:
            return n.hidden
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_h_i_d_d_e_n(n, value):
        try:
            n.hidden = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_u_t_o_f_i_l_l(n):
        try:
            return n.autofill
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_u_t_o_f_i_l_l(n, value):
        try:
            n.autofill = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_a_u_t_o_c_o_m_p_l_e_t_e(n):
        try:
            return n.autocomplete
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_a_u_t_o_c_o_m_p_l_e_t_e(n, value):
        try:
            n.autocomplete = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_a_b_e_l_U_r_i(n):
        try:
            return n.labelUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_a_b_e_l_U_r_i(n, value):
        try:
            n.labelUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g(n):
        try:
            return n.binding
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g(n, value):
        try:
            n.binding = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_U_r_i(n):
        try:
            return n.bindingUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_U_r_i(n, value):
        try:
            n.bindingUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_R_a_n_g_e(n):
        try:
            return n.bindingRange
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_R_a_n_g_e(n, value):
        try:
            n.bindingRange = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_S_t_a_t_e(n):
        try:
            return n.bindingState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_S_t_a_t_e(n, value):
        try:
            n.bindingState = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_S_t_a_t_e_U_r_i(n):
        try:
            return n.bindingStateUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_b_i_n_d_i_n_g_S_t_a_t_e_U_r_i(n, value):
        try:
            n.bindingStateUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_e_c_k_i_n_d_e_t_e_x_t(n):
        try:
            return n.checkindetext
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_e_c_k_i_n_d_e_t_e_x_t(n, value):
        try:
            n.checkindetext = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_e_c_k_i_n_d_e_t_e_x_t_U_r_i(n):
        try:
            return n.checkindetextUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_c_h_e_c_k_i_n_d_e_t_e_x_t_U_r_i(n, value):
        try:
            n.checkindetextUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_s_t_U_r_i(n):
        try:
            return n.listUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_s_t_U_r_i(n, value):
        try:
            n.listUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_s_t(n):
        try:
            return n.list
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_s_t(n, value):
        try:
            n.list = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_l_o_t_U_r_i(n):
        try:
            return n.slotUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_l_o_t_U_r_i(n, value):
        try:
            n.slotUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_s_l_o_t(n):
        try:
            return n.slot
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_s_l_o_t(n, value):
        try:
            n.slot = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_l_i_n_e_U_r_i(n):
        try:
            return n.inlineUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_l_i_n_e_U_r_i(n, value):
        try:
            n.inlineUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_l_i_n_e(n):
        try:
            return n.inline
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_l_i_n_e(n, value):
        try:
            n.inline = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_o_m_p_t_T_y_p_e(n):
        try:
            return n.promptType
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_o_m_p_t_T_y_p_e(n, value):
        try:
            n.promptType = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_o_m_p_t(n):
        try:
            return n.prompt
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_p_r_o_m_p_t(n, value):
        try:
            n.prompt = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_q_u_i_r_e_s(n):
        try:
            return n.requires
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_q_u_i_r_e_s(n, value):
        try:
            n.requires = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_q_u_i_r_e_s_U_r_i(n):
        try:
            return n.requiresUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_r_e_q_u_i_r_e_s_U_r_i(n, value):
        try:
            n.requiresUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_s_t_i_n_d_i_c_a_t_o_r(n):
        try:
            return n.listindicator
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_l_i_s_t_i_n_d_i_c_a_t_o_r(n, value):
        try:
            n.listindicator = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_V_a_l_i_d_i_t_y_U_r_i(n):
        try:
            return n.defaultValidityUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_V_a_l_i_d_i_t_y_U_r_i(n, value):
        try:
            n.defaultValidityUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_V_a_l_i_d_i_t_y_S_t_a_t_e(n):
        try:
            return n.defaultValidityState
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_V_a_l_i_d_i_t_y_S_t_a_t_e(n, value):
        try:
            n.defaultValidityState = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_V_a_l_i_d_i_t_y(n):
        try:
            return n.defaultValidity
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_V_a_l_i_d_i_t_y(n, value):
        try:
            n.defaultValidity = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_I_n_d_i_c_a_t_o_r(n):
        try:
            return n.defaultIndicator
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_d_e_f_a_u_l_t_I_n_d_i_c_a_t_o_r(n, value):
        try:
            n.defaultIndicator = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e_S_p_a_c_e(n):
        try:
            return n.nameSpace
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_n_a_m_e_S_p_a_c_e(n, value):
        try:
            n.nameSpace = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_M_o_d_e(n):
        try:
            return n.inputMode
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_M_o_d_e(n, value):
        try:
            n.inputMode = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_M_o_d_e_U_r_i(n):
        try:
            return n.inputModeUri
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def s_e_t_f_o_r_m_e_l_e_m_e_n_t_i_n_p_u_t_M_o_d_e_U_r_i(n, value):
        try:
            n.inputModeUri = value
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

    @staticmethod
    def g_e_t_f_o_r_m_e_l_e_m_e_n_t_c_u_r_r_e_n_t_I_n_p_u_t_M_o_d_e(n):
        try:
            return n.currentInputMode
        except Exception as ee:
            raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_current_input_mode(n, value):
    try:
        n.currentInputMode = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_default_input_mode(n):
    try:
        return n.defaultInputMode
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_default_input_mode(n, value):
    try:
        n.defaultInputMode = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_autocapitalize(n):
    try:
        return n.autocapitalize
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_autocapitalize(n, value):
    try:
        n.autocapitalize = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_autocapitalize_uri(n):
    try:
        return n.autocapitalizeUri
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_autocapitalize_uri(n, value):
    try:
        n.autocapitalizeUri = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_default_autocapitalize(n):
    try:
        return n.defaultAutocapitalize
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_default_autocapitalize(n, value):
    try:
        n.defaultAutocapitalize = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_input_mode(n):
    try:
        return n.inputmode
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_input_mode(n, value):
    try:
        n.inputmode = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_default_input_mode(n):
    try:
        return n.defaultinputmode
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_default_input_mode(n, value):
    try:
        n.defaultinputmode = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_input_mode_uri(n):
    try:
        return n.inputmodeuri
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_input_mode_uri(n, value):
    try:
        n.inputmodeuri = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_default_input_mode_uri(n):
    try:
        return n.defaultinputmodeuri
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_default_input_mode_uri(n, value):
    try:
        n.defaultinputmodeuri = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_compliance(n):
    try:
        return n.compliance
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_compliance(n, value):
    try:
        n.compliance = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_compliance_uri(n):
    try:
        return n.complianceuri
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_compliance_uri(n, value):
    try:
        n.complianceuri = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_language(n):
    try:
        return n.language
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_language(n, value):
    try:
        n.language = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def get_form_element_language_uri(n):
    try:
        return n.languageuri
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

@staticmethod
def set_form_element_language_uri(n, value):
    try:
        n.languageuri = value
    except Exception as ee:
        raise D_o_m.DomError(str(ee))

