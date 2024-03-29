
import sys

__verbose = False
__debug = False
__color = True

__style = { "normal" :  "\33[0m",
            "verbose" : "\33[37;2m",
            "debug" : "\33[37;2m",
            "warning" : "\33[31m",
            "error" : "\33[37;41;1m",
          }

def set_verbose( v ):
    global __verbose
    __verbose = v

def set_debug( d ):
    global __debug
    __debug = d

def set_color( c ):
    global __color
    __color = c

def __Color(style):
    if __color:
        return __style[style]
    else:
        return ""

def __build_texte (txt, sep, end, level):
        textes = []
        for arg in txt:
            textes.append(str(arg))
        msg = sep.join(textes) + end
        if msg[0] == "\n":
            msg = "\n" + __Color(level) + msg[1:]
        else:
            msg = __Color(level) + msg
        if msg[-1] == "\n":
            msg = msg[0:-1] + __Color("normal") + "\n"
        else:
            msg =  msg + __Color("normal")
        return (msg)

def Verbose(*txt, sep=" ", end="\n"):
    if __verbose:
        msg = __build_texte (txt, sep, end, "verbose")
        sys.stderr.write (msg)

def Warning(*txt, sep=" ", end="\n"):
    msg = __build_texte (txt, sep, end, "warning")
    sys.stderr.write (msg)

def Error(*txt, sep=" ", end="\n"):
    msg = __build_texte (txt, sep, end, "error")
    sys.stderr.write (msg)

def Debug(*txt, sep=" ", end="\n"):
    if __debug:
        msg = __build_texte (txt, sep, end, "debug")
        sys.stderr.write (msg)

