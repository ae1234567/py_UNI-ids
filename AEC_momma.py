# -*- coding: utf-8 -*-
""" Æ CLASS TESTING SCRIPT  
      Nov 27 v.1.0  s.a.m. @ Æ 
      Nov 28 v.2.0  printout 
        UNICODE python identifiers
 Class prefix	  TIF YASH      [Tifinagh]	ⵛ  
 Var for self	  TIF YABH      [Tifinagh]	ⴲ 
 Func print  	LAT PSTROKE	 	[Lat ext-C]	Ᵽ  
 List name		LAT MHOOK		[Lat ext-C]	Ɱ 
""" # end of DocString ###############################
Ɱ =     {
    'vname' : 'UNICODE python identifiers', 
    'ver'   : '2.0',
    'fname' : '', # filled by getScriptName()
    'msgOS' : 'os filename =',
    'chars' : 'ⵛ  ⴲ Ᵽ Ɱ', #add sp
    'delmsg': 'That was deleted.', 
    'D1'    : 'momma.butte',
    'D2'    : 'del .butte (no report),',
    'D3'    : 'retry access [AttrErr]'}
print(Ɱ['vname'],' ',Ɱ['ver'])
import os
def getScriptName():
    return os.path.basename(__file__)
Ɱ['fname'] = getScriptName()
msgOS = 'os filename ='
str_char_print = 'ⵛ  ⴲ Ᵽ Ɱ'; #add sp 
Ᵽ = print; Ᵽ(Ɱ['chars'])
Ᵽ("*************************** \nÆ Begin; getScriptName")
Ᵽ ('{} "{}"'.format(Ɱ['msgOS'],Ɱ['fname']))
if __name__ == '__main__': # module __name__
    Ᵽ('{} as {}'.format(Ɱ['fname'],__name__))
Ᵽ("*************************** ")

class ⵛ_momma:
    ''' UNIcode self ⴲ'''
    def __init__(ⴲ):
        ⴲ.i = 0 
        ⴲ.ⱮL = [ 
        'dummy', 'init', 'get', 'set', 'delete',
        'AEC_momma.py running as' ] 
        ⴲ.Ɱ =     {
    'INIT'  : 'Ɱ __init__', 
    'GET'   : 'Ɱ __get__',
    'SET'   : 'Ɱ __set__',
    'DELETE': 'Ɱ __delete__' }
        Ᵽ(ⴲ.Ɱ['INIT'], end='|')
    def __set__(ⴲ, i, value):
        Ᵽ (ⴲ.Ɱ['SET'], end='|')
        ⴲ.value = value
    def __get__(ⴲ, i, owner):
        Ᵽ (ⴲ.Ɱ['GET'])
        return ⴲ.value
    def __delete__(ⴲ, i):
        Ᵽ (ⴲ.Ɱ['DELETE'])
        del ⴲ.value

    def move(ⴲ, x, y):
        ⴲ.x = x # uni char 1-per-line
        ⴲ.y = y # avoid ;-concat here

    def reset(ⴲ):
        ⴲ.move(0, 0)

    def calculate_distance(ⴲ, other_point):
        return (
                (ⴲ.x - other_point.x) +
                (ⴲ.y - other_point.y))
        # end class
Ᵽ("Æ Foo.momma =ⵛ_momma() ")
class Foo(object):
    momma =ⵛ_momma() 
    #end class
foo = Foo()   #  class in class
foo.momma = 10  #  implicit call on __set__
Ᵽ ("foo.momma = {}".format(foo.momma))
del foo.momma
try:
    Ᵽ (foo.momma)
except AttributeError:
    Ᵽ (Ɱ['delmsg'])
Ᵽ("Æ instance of ⵛ_momma() ")
momma = ⵛ_momma() # should print init
momma.butte = 10
Ᵽ ("{} = {}".format(Ɱ['D1'],momma.butte))
Ᵽ (Ɱ['D2']); Ᵽ (Ɱ['D3'])
del momma.butte
try:
    Ᵽ (momma.butte)
except AttributeError:
    Ᵽ (Ɱ['delmsg'])
Ᵽ("*************************** \nÆ End")
''' # pasted output
UNICODE python identifiers   2.0
ⵛ  ⴲ Ᵽ Ɱ
*************************** 
Æ Begin; getScriptName
os filename = "AEC_momma.py"
AEC_momma.py as __main__
*************************** 
Æ Foo.momma =ⵛ_momma() 
Ɱ __init__|Ɱ __set__|Ɱ __get__
foo.momma = 10
Ɱ __delete__
Ɱ __get__
That was deleted.
Æ instance of ⵛ_momma() 
Ɱ __init__|momma.butte = 10
del .butte (no report),
retry access [AttrErr]
That was deleted.
*************************** 
Æ En
''' # end Result
# end of file 