# This file was automatically created by FeynRules 2.4.16
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Fri 21 Aug 2015 09:21:20



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
MstLR = Parameter(name = 'MstLR',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{MstLR}',
                  lhablock = 'MSoft',
                  lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

Mgo = Parameter(name = 'Mgo',
                nature = 'external',
                type = 'real',
                value = 500,
                texname = '\\text{Mgo}',
                lhablock = 'MASS',
                lhacode = [ 1000021 ])

Mchi = Parameter(name = 'Mchi',
                 nature = 'external',
                 type = 'real',
                 value = 50,
                 texname = '\\text{Mchi}',
                 lhablock = 'MASS',
                 lhacode = [ 1000022 ])

MsuL = Parameter(name = 'MsuL',
                 nature = 'external',
                 type = 'real',
                 value = 9000,
                 texname = '\\text{MsuL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

MscL = Parameter(name = 'MscL',
                 nature = 'external',
                 type = 'real',
                 value = 9000,
                 texname = '\\text{MscL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

MstL = Parameter(name = 'MstL',
                 nature = 'external',
                 type = 'real',
                 value = 9000,
                 texname = '\\text{MstL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

MsuR = Parameter(name = 'MsuR',
                 nature = 'external',
                 type = 'real',
                 value = 8000,
                 texname = '\\text{MsuR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

MscR = Parameter(name = 'MscR',
                 nature = 'external',
                 type = 'real',
                 value = 8000,
                 texname = '\\text{MscR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

MstR = Parameter(name = 'MstR',
                 nature = 'external',
                 type = 'real',
                 value = 8000,
                 texname = '\\text{MstR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

MsdL = Parameter(name = 'MsdL',
                 nature = 'external',
                 type = 'real',
                 value = 9000,
                 texname = '\\text{MsdL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

MssL = Parameter(name = 'MssL',
                 nature = 'external',
                 type = 'real',
                 value = 9000,
                 texname = '\\text{MssL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

MsbL = Parameter(name = 'MsbL',
                 nature = 'external',
                 type = 'real',
                 value = 9000,
                 texname = '\\text{MsbL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

MsdR = Parameter(name = 'MsdR',
                 nature = 'external',
                 type = 'real',
                 value = 8000,
                 texname = '\\text{MsdR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

MssR = Parameter(name = 'MssR',
                 nature = 'external',
                 type = 'real',
                 value = 8000,
                 texname = '\\text{MssR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

MsbR = Parameter(name = 'MsbR',
                 nature = 'external',
                 type = 'real',
                 value = 8000,
                 texname = '\\text{MsbR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

Wgo = Parameter(name = 'Wgo',
                nature = 'external',
                type = 'real',
                value = 10,
                texname = '\\text{Wgo}',
                lhablock = 'DECAY',
                lhacode = [ 1000021 ])

WsuL = Parameter(name = 'WsuL',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WsuL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

WscL = Parameter(name = 'WscL',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WscL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

WstL = Parameter(name = 'WstL',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WstL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

WsuR = Parameter(name = 'WsuR',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WsuR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

WscR = Parameter(name = 'WscR',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WscR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

WstR = Parameter(name = 'WstR',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WstR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

WsdL = Parameter(name = 'WsdL',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WsdL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

WssL = Parameter(name = 'WssL',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WssL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

WsbL = Parameter(name = 'WsbL',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WsbL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

WsdR = Parameter(name = 'WsdR',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WsdR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

WssR = Parameter(name = 'WssR',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WssR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

WsbR = Parameter(name = 'WsbR',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WsbR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

