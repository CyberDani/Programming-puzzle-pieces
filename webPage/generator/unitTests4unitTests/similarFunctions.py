import functools

from decorator import *

def simpleFunc():
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

def \
    \
        simpleFunc2 \
                \
                (

        )\
        \
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

# def simpleFunc3
def \
    \
        simpleFunc3 \
                \
                (

        )\
        \
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@decorator
def defdeco(func, *args, **kw):
  return func(*args)

@defdeco
def \
        simpleFunc4 \
                (
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@decorator
def defdef (func, arg):
  return func(arg)

@defdef (arg = " def ")
def \
        simpleFunc5 \
                ( arg
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@defdef (arg = " def simpleFunc6 ")
def \
        simpleFunc6 \
                ( arg
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@defdef \
  (arg = "\
          def simpleFunc7 ( ) ")
def \
        simpleFunc7 \
                ( arg
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@defdef \
  (arg = "\
def simpleFunc8(): ")
def \
        simpleFunc8 \
                ( arg
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " (dec\
) def simpleFunc9(): ")
def \
        simpleFunc9 \
                ( arg
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " (dec\
)o def simpleFunc10(): ")
def \
        simpleFunc10 \
                ( arg
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc11(): ")
def \
        simpleFunc11 \
                ( arg
        )\
        :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

def simpleFunc_sameImpl():
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@decorator
def invertBool(func, *args, **kw):
  # print("- = -   H E L L O   - = -")
  return not func(*args)

def simpleFunc_sameImpl_differentSignature(
                                           arg1 ,
                                           arg2
                                          )     :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@invertBool
def simpleFunc_sameImpl_differentSignature_decorated(
                                           arg1 ,
                                           arg2
                                          )     :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

@invertBool
def simpleFunc_sameImpl_differentSignature_decorated_annotated (
                                           arg1   :    int,
                                           arg2   :    str
                                          )       ->   bool \
    :
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

class SimpleClass:
  def simpleFunc( self ) \
          :
    a = 2
    b = 3
    return ((a + b) * 10) % 2 == 0
