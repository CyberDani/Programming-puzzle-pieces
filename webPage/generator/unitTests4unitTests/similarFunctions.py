from decorator import decorator
from unitTests4unitTests import otherFunctions

def simpleFunc_noReturn():
  a = 2
  b = 3
  isTrue = ((a + b) * 10) % 2 == 0
  if isTrue:
    isTrue = not otherFunctions.getTrue()

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

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc12(): ")
def \
        simpleFunc12 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
        :
  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc13(): ")
def \
        simpleFunc13 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :

  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0


@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc14(): ")
def \
        simpleFunc14 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :



  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@decorator
def invertBool(func, *args, **kw):
  # print("- = -   H E L L O   - = -")
  return not func(*args)

@invertBool
@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc15(): ")
def \
        simpleFunc15 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :



  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@invertBool
@defdeco
@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc16(): ")
def \
        simpleFunc16 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :



  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

def simpleFunc17(str = "2:1", d = {"one": 1}):
  a = simpleFunc16()
  b = simpleFunc2()
  cl = SimpleClass()
  cl.simpleFunc()
  return (len(str) + len(d) < 5) or (a and b)

def simpleFunc18(str = "2:1", d = [1, 2, 4]):
  fl = otherFunctions.getFalseIfNotTrue()
  other = otherFunctions.OtherClass()
  a = simpleFunc16()
  b = simpleFunc2()
  cl = SimpleClass()
  other.saySomething()
  cl.simpleFunc()
  return fl or (len(str) + len(d) < 5) or (a and b)

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc19(): ")
def \
        simpleFunc19 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon



  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc20(): ")
def \
        simpleFunc20 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon

# there is another comment here

  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc21(): ")
def \
        simpleFunc21 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon


  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc22(): ")
def \
        simpleFunc22 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon
  """Function documentation... hello"""

  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc23(): ")
def \
        simpleFunc23 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon
  """Function documentation... \n
hello:\n
* option"""

  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc24(): ")
def \
        simpleFunc24 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon
  # comment before doc
# another comment before doc
  """Function documentation... \n
hello:\n
* option"""

  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc25(): ")
def \
        simpleFunc25 \
                ( str = "2:1",  # here is a ::comment::
                  d = {"one": 1}
        )\
        :
  a = len(d)
  b = len(str)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc26(): ")
def \
        simpleFunc26 \
                  \
                \
                (   # put a comment here
                  # another here
                  str1 = "2:1=\"2\"",  # here is a ::comment::
                  str2 = "'hello'",  # here is a ::comment2::
                  d = {"one": 1}    # here is another comment
                # also a comment in this line
        )\
\
\
        : # comment after the colon
  a = len(d)
  b = len(str1) - len(str2)
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc27(): ")
def \
        simpleFunc27 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon
  # comment before doc
# another comment before doc
  """Function documentation... \n
hello:\n
* option"""

  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)


  b = len(str)
  # comment before return 1

  # return 12
  return ((a + b) * 10) % 2 == 0


@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc28(): ")
def \
        simpleFunc28 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon
  # comment before doc
# another comment before doc
  """Function documentation... \n
hello:\n
* option"""

  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)
  if not d:
    a += 2
    if a == 20:
      a = 12

  b = len(str)
  # comment before return 1

  # return 12
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc29(): ")
def \
        simpleFunc29 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon
  # comment before doc
# another comment before doc
  """Function documentation... \n
hello:\n
* option"""

  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)
  if not d:
    a += 2
    if a == 20:return True

  b = len(str)
  # comment before return 1

  # return 12
  return ((a + b) * 10) % 2 == 0

@\
defdef \
  (arg = " @defdef(dec) \
 def simpleFunc30(): ")
def \
        simpleFunc30 \
                ( str = "2:1",
                  d = {"one": 1}
        )\
\
        :   # random comment after the colon
  # comment before doc
# another comment before doc
  """Function documentation... \n
hello:\n
* option"""

  # some comment in the first line

# there is another comment here



   # another comment, cause why not

  a = len(d)
  if not d:
    a += 2
    if a == 20 :  return True

  b = len(str)
  # comment before return 1

  # return 12
  return ((a + b) * 10) % 2 == 0

def simpleFunc_sameImpl():
  a = 2
  b = 3
  return ((a + b) * 10) % 2 == 0

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
