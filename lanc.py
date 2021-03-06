from tkinter import *
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.title('lan_c')
root.geometry('900x500+600+400')
# root.configure('black')
root.resizable(0, 0)
root.wm_attributes('-transparentcolor', 'white')
root.attributes('-alpha', 0.20)
root.overrideredirect(1)


def op():
    root.f = filedialog.askopenfilename()
    root.fs1 = open(root.f)
    root.fs = root.fs1.read()
    root.fs1.close()
    t.delete(0.0, END)
    t.insert(INSERT, root.fs)
    rkp_()


def sa():
    ty = t.get(0.0, END)
    ro = filedialog.asksaveasfile(mode='w')
    ro.write(ty)
    ro.close()


def a(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('a', '1:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def b(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('b', '2:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def c(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('c', '3:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def d(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('d', '4:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def e(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('e', '5:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def f(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('f', '6:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def g(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('g', '7:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def h(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('h', '8:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def i(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('i', '9:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def j(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('j', '10:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def k(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('k', '11:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def l(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('l', '12:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def m(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('m', '13:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def n(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('n', '14:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def o(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('o', '15:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def p(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('p', '16:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def q(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('q', '17:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def r(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('r', '18:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def s(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('s', '19:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def tpsk(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('t', '20:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def u(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('u', '21:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def v(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('v', '22:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def w(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('w', '23:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def x(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('x', '24:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def y(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('y', '25:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def z(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('z', '26:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def fj(e=''):
    for ijklom in range(0, 60):
        tyi = t.get(0.0, END)
        if '1:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('1:', 'a')
            t.insert(INSERT, uios1)
        if '2:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('2:', 'b')
            t.insert(INSERT, uios1)
        if '3:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('3:', 'c')
            t.insert(INSERT, uios1)
        if '4:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('4:', 'd')
            t.insert(INSERT, uios1)
        if ';::.?.;' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace(';::.?.;', '')
            t.insert(INSERT, uios1)
        if '5:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('5:', 'e')
            t.insert(INSERT, uios1)
        if '6:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('6:', 'f')
            t.insert(INSERT, uios1)
        if '7:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('7:', 'g')
            t.insert(INSERT, uios1)
        if '8:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('8:', 'h')
            t.insert(INSERT, uios1)
        if '9:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9:', 'i')
            t.insert(INSERT, uios1)
        if '10:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('10:', 'j')
            t.insert(INSERT, uios1)
        if '11:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('11:', 'k')
            t.insert(INSERT, uios1)
        if '12:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('12:', 'l')
            t.insert(INSERT, uios1)
        if '13:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('13:', 'm')
            t.insert(INSERT, uios1)
        if '14:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('14:', 'n')
            t.insert(INSERT, uios1)
        if '15:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('15:', 'o')
            t.insert(INSERT, uios1)
        if '16:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('16:', 'p')
            t.insert(INSERT, uios1)
        if '17:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('17:', 'q')
            t.insert(INSERT, uios1)
        if '18:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('18:', 'r')
            t.insert(INSERT, uios1)
        if '19:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('19:', 's')
            t.insert(INSERT, uios1)
        if '20:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('20:', 't')
            t.insert(INSERT, uios1)
        if '21:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('21:', 'u')
            t.insert(INSERT, uios1)
        if '22:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('22:', 'v')
            t.insert(INSERT, uios1)
        if '23:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('23:', 'w')
            t.insert(INSERT, uios1)
        if '24:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('24:', 'x')
            t.insert(INSERT, uios1)
        if '25:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('25:', 'y')
            t.insert(INSERT, uios1)
        if '26:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('26:', 'z')
            t.insert(INSERT, uios1)
        if '919:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('919:', 'A')
            t.insert(INSERT, uios1)
        if '929:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('929:', 'B')
            t.insert(INSERT, uios1)
        if '939:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('939:', 'C')
            t.insert(INSERT, uios1)
        if '949:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('949:', 'D')
            t.insert(INSERT, uios1)
        if ';::.?.;' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace(';::.?.;', '')
            t.insert(INSERT, uios1)
        if '959:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('959:', 'E')
            t.insert(INSERT, uios1)
        if '969:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('969:', 'F')
            t.insert(INSERT, uios1)
        if '979:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('979:', 'G')
            t.insert(INSERT, uios1)
        if '989:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('989:', 'H')
            t.insert(INSERT, uios1)
        if '999:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('999:', 'I')
            t.insert(INSERT, uios1)
        if '9109:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9109:', 'J')
            t.insert(INSERT, uios1)
        if '9119:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9119:', 'K')
            t.insert(INSERT, uios1)
        if '9129:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9129:', 'L')
            t.insert(INSERT, uios1)
        if '9139:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9139:', 'M')
            t.insert(INSERT, uios1)
        if '9149:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9149:', 'N')
            t.insert(INSERT, uios1)
        if '9159:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9159:', 'O')
            t.insert(INSERT, uios1)
        if '9169:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9169:', 'P')
            t.insert(INSERT, uios1)
        if '9179:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9179:', 'Q')
            t.insert(INSERT, uios1)
        if '9189:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9189:', 'R')
            t.insert(INSERT, uios1)
        if '9199:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9199:', 'S')
            t.insert(INSERT, uios1)
        if '9209:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9209:', 'T')
            t.insert(INSERT, uios1)
        if '9219:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9219:', 'U')
            t.insert(INSERT, uios1)
        if '9229:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9229:', 'V')
            t.insert(INSERT, uios1)
        if '9239:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9239:', 'W')
            t.insert(INSERT, uios1)
        if '9249:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9249:', 'X')
            t.insert(INSERT, uios1)
        if '9259:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9259:', 'Y')
            t.insert(INSERT, uios1)
        if '9269:' in tyi:
            uios = str(tyi)
            t.delete(0.0, END)
            uios1 = uios.replace('9269:', 'Z')
            t.insert(INSERT, uios1)


def rkp_(e=''):
    for ioplsss in range(0, 100):
        pyttsx2 = t.get(0.0, END)
        pyttsx23 = str(pyttsx2)
        if 'a' in pyttsx23:
            pys = pyttsx23.replace('a', '1:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'A' in pyttsx23:
            pys = pyttsx23.replace('A', '919:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'b' in pyttsx23:
            pys = pyttsx23.replace('b', '2:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'B' in pyttsx23:
            pys = pyttsx23.replace('B', '929:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'c' in pyttsx23:
            pys = pyttsx23.replace('c', '3:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'C' in pyttsx23:
            pys = pyttsx23.replace('C', '939:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'd' in pyttsx23:
            pys = pyttsx23.replace('d', '4:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'D' in pyttsx23:
            pys = pyttsx23.replace('D', '949:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'e' in pyttsx23:
            pys = pyttsx23.replace('e', '5:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'E' in pyttsx23:
            pys = pyttsx23.replace('E', '959:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'f' in pyttsx23:
            pys = pyttsx23.replace('f', '6:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'F' in pyttsx23:
            pys = pyttsx23.replace('F', '969:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'g' in pyttsx23:
            pys = pyttsx23.replace('g', '7:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'G' in pyttsx23:
            pys = pyttsx23.replace('G', '979:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'h' in pyttsx23:
            pys = pyttsx23.replace('h', '8:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'H' in pyttsx23:
            pys = pyttsx23.replace('H', '989:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'i' in pyttsx23:
            pys = pyttsx23.replace('i', '9:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'I' in pyttsx23:
            pys = pyttsx23.replace('I', '999:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'J' in pyttsx23:
            pys = pyttsx23.replace('J', '9109:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'j' in pyttsx23:
            pys = pyttsx23.replace('j', '10:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'k' in pyttsx23:
            pys = pyttsx23.replace('k', '11:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'K' in pyttsx23:
            pys = pyttsx23.replace('K', '9119:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'l' in pyttsx23:
            pys = pyttsx23.replace('l', '12:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'L' in pyttsx23:
            pys = pyttsx23.replace('L', '9129:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'm' in pyttsx23:
            pys = pyttsx23.replace('m', '13:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'M' in pyttsx23:
            pys = pyttsx23.replace('M', '9139:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'n' in pyttsx23:
            pys = pyttsx23.replace('n', '14:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'N' in pyttsx23:
            pys = pyttsx23.replace('N', '9149:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'o' in pyttsx23:
            pys = pyttsx23.replace('o', '15:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'O' in pyttsx23:
            pys = pyttsx23.replace('O', '9159:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'p' in pyttsx23:
            pys = pyttsx23.replace('p', '16:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'P' in pyttsx23:
            pys = pyttsx23.replace('P', '9169:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'q' in pyttsx23:
            pys = pyttsx23.replace('q', '17:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'Q' in pyttsx23:
            pys = pyttsx23.replace('Q', '9179:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'r' in pyttsx23:
            pys = pyttsx23.replace('r', '18:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'R' in pyttsx23:
            pys = pyttsx23.replace('R', '9189:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 's' in pyttsx23:
            pys = pyttsx23.replace('s', '19:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'S' in pyttsx23:
            pys = pyttsx23.replace('S', '9199:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 't' in pyttsx23:
            pys = pyttsx23.replace('t', '20:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'T' in pyttsx23:
            pys = pyttsx23.replace('T', '9209:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'u' in pyttsx23:
            pys = pyttsx23.replace('u', '21:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'U' in pyttsx23:
            pys = pyttsx23.replace('U', '9219:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'v' in pyttsx23:
            pys = pyttsx23.replace('v', '22:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'V' in pyttsx23:
            pys = pyttsx23.replace('V', '9229:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'w' in pyttsx23:
            pys = pyttsx23.replace('w', '23:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'W' in pyttsx23:
            pys = pyttsx23.replace('W', '9239:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'x' in pyttsx23:
            pys = pyttsx23.replace('x', '24:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'X' in pyttsx23:
            pys = pyttsx23.replace('X', '9249:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'y' in pyttsx23:
            pys = pyttsx23.replace('y', '25:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'Y' in pyttsx23:
            pys = pyttsx23.replace('Y', '9259:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'z' in pyttsx23:
            pys = pyttsx23.replace('z', '26:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)
        if 'Z' in pyttsx23:
            pys = pyttsx23.replace('Z', '9269:')
            t.delete(0.0, END)
            t.insert(INSERT, pys)


ldsk = Label(pady=900, bg='black', width=5).place(x=0, y=0)
bs = Button(text='open', command=op, width=5, bg='black', fg='red')
bsk = Button(text='trans', command=fj, width=5, bg='black', fg='red')
bsdk = Button(text='cvs', command=rkp_, width=5, bg='black', fg='red')
bs1 = Button(text='save', command=sa, width=5, bg='black', fg='red')
# root.bind('', fj)


def m_take(args=''):
    quit()


bs10000ty = Button(text='exit', command=m_take, width=5, bg='black', fg='red')
bs.place(x=0, y=0)
bsk.place(x=0, y=50)
bsdk.place(x=0, y=80 - 5)
bs10000ty.place(x=0, y=100)
bs1.place(x=0, y=25)
t = Text(fg='pink', bg='gray', width=900, pady=100)
t.place(x=40, y=0)


# root_c = Canvas(t)
# root_c.place(x = 40, y = 0)
# scroll = ttk.Scrollbar(t, orient = 'vertical', command = root_c.yview)
# scroll.place(y = 0, x = 40)


def A(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('A', '919:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def B(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('B', '929:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def C(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('C', '939:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def D(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('D', '949:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def E(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('E', '959:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def F(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('F', '969:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def G(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('G', '979:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def H(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('H', '989:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def I(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('I', '999:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def J(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('J', '9109:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def K(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('K', '9119:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def L(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('L', '9129:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def M(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('M', '9139:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def N(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('N', '9149:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def O(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('O', '9159:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def P(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('P', '9169:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def Q(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('Q', '9179:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def R(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('R', '9189:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


# def s(e):
#     ty = t.get(0.0, END)
#     # tys = len(ty)
#     # kc = tys-1
#     # hj = t.get(END-1, END)
#     # t.delete(END, END)
#     typ = str(ty)
#     typf = typ.replace('s', '19:')
#     t.delete(0.0, END)
#     t.insert(INSERT, typf)


def T(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('T', '9209:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def U(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('U', '9219:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def V(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('V', '9229:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def W(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('W', '9239:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def X(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('X', '9249:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def Y(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('Y', '9259:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def Z(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('Z', '9269:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


typf = ''


def Srs(e):
    ty = t.get(0.0, END)
    # tys = len(ty)
    # kc = tys-1
    # hj = t.get(END-1, END)
    # t.delete(END, END)
    typ = str(ty)
    typf = typ.replace('S', '9199:')
    t.delete(0.0, END)
    t.insert(INSERT, typf)


def m_take(e=''):
    quit()


root.bind('a', rkp_)
# bsk.bind('<Enter>', fj)
root.bind('A', A)
root.bind('b', b)
root.bind('B', B)
root.bind('c', c)
root.bind('C', C)
root.bind('d', d)
root.bind('D', D)
root.bind('e', e)
root.bind('E', E)
root.bind('f', f)
root.bind('F', F)
root.bind('g', g)
root.bind('G', G)
root.bind('h', h)
root.bind('H', H)
root.bind('i', i)
root.bind('I', I)
root.bind('J', J)
root.bind('j', j)
root.bind('k', k)
root.bind('K', K)
root.bind('l', l)
root.bind('L', L)
root.bind('m', m)
root.bind('M', M)
root.bind('n', n)
root.bind('N', N)
root.bind('o', o)
root.bind('O', O)
root.bind('p', p)
root.bind('P', P)
root.bind('q', q)
root.bind('Q', Q)
root.bind('r', r)
root.bind('R', R)
root.bind('s', s)
# root.bind('/', slash)
root.bind('S', Srs)
root.bind('t', tpsk)
root.bind('T', T)
root.bind('u', u)
root.bind('U', U)
root.bind('V', V)
root.bind('v', v)
root.bind('w', w)
root.bind('W', W)
root.bind('x', x)
root.bind('X', X)
root.bind('y', y)
root.bind('Y', Y)
root.bind('z', z)
root.bind('Z', Z)

root.mainloop()
