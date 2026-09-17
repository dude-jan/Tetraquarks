# This file was automatically created by FeynRules 2.3.41
# Mathematica version: 11.0.1 for Microsoft Windows (64-bit) (September 20, 2016)
# Date: Thu 31 Mar 2022 19:27:36



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
CQ10Q10MZ = Parameter(name = 'CQ10Q10MZ',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{CQ10Q10MZ}',
                      lhablock = 'CQ10Q10MZ',
                      lhacode = [ 1 ])

CQ11Q10W = Parameter(name = 'CQ11Q10W',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{CQ11Q10W}',
                     lhablock = 'CQ11Q10W',
                     lhacode = [ 1 ])

CQ80MS323t = Parameter(name = 'CQ80MS323t',
                       nature = 'external',
                       type = 'real',
                       value = 0.1,
                       texname = '\\text{CQ80MS323t}',
                       lhablock = 'CQ80MS323t',
                       lhacode = [ 1 ])

CQ80MS80Q10M = Parameter(name = 'CQ80MS80Q10M',
                         nature = 'external',
                         type = 'real',
                         value = 0.1,
                         texname = '\\text{CQ80MS80Q10M}',
                         lhablock = 'CQ80MS80Q10M',
                         lhacode = [ 1 ])

CQ80S323t = Parameter(name = 'CQ80S323t',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{CQ80S323t}',
                      lhablock = 'CQ80S323t',
                      lhacode = [ 1 ])

CQ80S80Q10 = Parameter(name = 'CQ80S80Q10',
                       nature = 'external',
                       type = 'real',
                       value = 0.1,
                       texname = '\\text{CQ80S80Q10}',
                       lhablock = 'CQ80S80Q10',
                       lhacode = [ 1 ])

CQ81S323t = Parameter(name = 'CQ81S323t',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{CQ81S323t}',
                      lhablock = 'CQ81S323t',
                      lhacode = [ 1 ])

CQ81S80Q11 = Parameter(name = 'CQ81S80Q11',
                       nature = 'external',
                       type = 'real',
                       value = 0.1,
                       texname = '\\text{CQ81S80Q11}',
                       lhablock = 'CQ81S80Q11',
                       lhacode = [ 1 ])

CS323Q10Mt = Parameter(name = 'CS323Q10Mt',
                       nature = 'external',
                       type = 'real',
                       value = 0.1,
                       texname = '\\text{CS323Q10Mt}',
                       lhablock = 'CS323Q10Mt',
                       lhacode = [ 1 ])

CS323tab = Parameter(name = 'CS323tab',
                     nature = 'external',
                     type = 'real',
                     value = 0.101,
                     texname = '\\text{CS323tab}',
                     lhablock = 'CS323tab',
                     lhacode = [ 1 ])

CS323vtt = Parameter(name = 'CS323vtt',
                     nature = 'external',
                     type = 'real',
                     value = 0.102,
                     texname = '\\text{CS323vtt}',
                     lhablock = 'CS323vtt',
                     lhacode = [ 1 ])

CVLQSCQL = Parameter(name = 'CVLQSCQL',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{CVLQSCQL}',
                     lhablock = 'CVLQSCQL',
                     lhacode = [ 1 ])

CVLQSCQR = Parameter(name = 'CVLQSCQR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{CVLQSCQR}',
                     lhablock = 'CVLQSCQR',
                     lhacode = [ 1 ])

CVLQSEWQL = Parameter(name = 'CVLQSEWQL',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{CVLQSEWQL}',
                      lhablock = 'CVLQSEWQL',
                      lhacode = [ 1 ])

CVLQSEWQR = Parameter(name = 'CVLQSEWQR',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{CVLQSEWQR}',
                      lhablock = 'CVLQSEWQR',
                      lhacode = [ 1 ])

fpsi = Parameter(name = 'fpsi',
                 nature = 'external',
                 type = 'real',
                 value = 1000,
                 texname = '\\text{fpsi}',
                 lhablock = 'fpsi',
                 lhacode = [ 1 ])

ftgi = Parameter(name = 'ftgi',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{ftgi}',
                 lhablock = 'ftgi',
                 lhacode = [ 1 ])

GP102BB = Parameter(name = 'GP102BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GP102BB}',
                    lhablock = 'GP102BB',
                    lhacode = [ 1 ])

GP102D1x1 = Parameter(name = 'GP102D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.114,
                      texname = '\\text{GP102D1x1}',
                      lhablock = 'GP102D',
                      lhacode = [ 1, 1 ])

GP102D2x2 = Parameter(name = 'GP102D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.115,
                      texname = '\\text{GP102D2x2}',
                      lhablock = 'GP102D',
                      lhacode = [ 2, 2 ])

GP102D3x3 = Parameter(name = 'GP102D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.116,
                      texname = '\\text{GP102D3x3}',
                      lhablock = 'GP102D',
                      lhacode = [ 3, 3 ])

GP102E1x1 = Parameter(name = 'GP102E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.124,
                      texname = '\\text{GP102E1x1}',
                      lhablock = 'GP102E',
                      lhacode = [ 1, 1 ])

GP102E2x2 = Parameter(name = 'GP102E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.125,
                      texname = '\\text{GP102E2x2}',
                      lhablock = 'GP102E',
                      lhacode = [ 2, 2 ])

GP102E3x3 = Parameter(name = 'GP102E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.126,
                      texname = '\\text{GP102E3x3}',
                      lhablock = 'GP102E',
                      lhacode = [ 3, 3 ])

GP102N1x1 = Parameter(name = 'GP102N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.134,
                      texname = '\\text{GP102N1x1}',
                      lhablock = 'GP102N',
                      lhacode = [ 1, 1 ])

GP102N2x2 = Parameter(name = 'GP102N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.135,
                      texname = '\\text{GP102N2x2}',
                      lhablock = 'GP102N',
                      lhacode = [ 2, 2 ])

GP102N3x3 = Parameter(name = 'GP102N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.136,
                      texname = '\\text{GP102N3x3}',
                      lhablock = 'GP102N',
                      lhacode = [ 3, 3 ])

GP102TT = Parameter(name = 'GP102TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GP102TT}',
                    lhablock = 'GP102TT',
                    lhacode = [ 1 ])

GP102U1x1 = Parameter(name = 'GP102U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.104,
                      texname = '\\text{GP102U1x1}',
                      lhablock = 'GP102U',
                      lhacode = [ 1, 1 ])

GP102U2x2 = Parameter(name = 'GP102U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.105,
                      texname = '\\text{GP102U2x2}',
                      lhablock = 'GP102U',
                      lhacode = [ 2, 2 ])

GP102U3x3 = Parameter(name = 'GP102U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.106,
                      texname = '\\text{GP102U3x3}',
                      lhablock = 'GP102U',
                      lhacode = [ 3, 3 ])

GP102XX = Parameter(name = 'GP102XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GP102XX}',
                    lhablock = 'GP102XX',
                    lhacode = [ 1 ])

GP102YY = Parameter(name = 'GP102YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GP102YY}',
                    lhablock = 'GP102YY',
                    lhacode = [ 1 ])

GP103BB = Parameter(name = 'GP103BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GP103BB}',
                    lhablock = 'GP103BB',
                    lhacode = [ 1 ])

GP103D1x1 = Parameter(name = 'GP103D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.114,
                      texname = '\\text{GP103D1x1}',
                      lhablock = 'GP103D',
                      lhacode = [ 1, 1 ])

GP103D2x2 = Parameter(name = 'GP103D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.115,
                      texname = '\\text{GP103D2x2}',
                      lhablock = 'GP103D',
                      lhacode = [ 2, 2 ])

GP103D3x3 = Parameter(name = 'GP103D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.116,
                      texname = '\\text{GP103D3x3}',
                      lhablock = 'GP103D',
                      lhacode = [ 3, 3 ])

GP103E1x1 = Parameter(name = 'GP103E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.124,
                      texname = '\\text{GP103E1x1}',
                      lhablock = 'GP103E',
                      lhacode = [ 1, 1 ])

GP103E2x2 = Parameter(name = 'GP103E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.125,
                      texname = '\\text{GP103E2x2}',
                      lhablock = 'GP103E',
                      lhacode = [ 2, 2 ])

GP103E3x3 = Parameter(name = 'GP103E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.126,
                      texname = '\\text{GP103E3x3}',
                      lhablock = 'GP103E',
                      lhacode = [ 3, 3 ])

GP103N1x1 = Parameter(name = 'GP103N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.134,
                      texname = '\\text{GP103N1x1}',
                      lhablock = 'GP103N',
                      lhacode = [ 1, 1 ])

GP103N2x2 = Parameter(name = 'GP103N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.135,
                      texname = '\\text{GP103N2x2}',
                      lhablock = 'GP103N',
                      lhacode = [ 2, 2 ])

GP103N3x3 = Parameter(name = 'GP103N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.136,
                      texname = '\\text{GP103N3x3}',
                      lhablock = 'GP103N',
                      lhacode = [ 3, 3 ])

GP103TT = Parameter(name = 'GP103TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GP103TT}',
                    lhablock = 'GP103TT',
                    lhacode = [ 1 ])

GP103U1x1 = Parameter(name = 'GP103U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.104,
                      texname = '\\text{GP103U1x1}',
                      lhablock = 'GP103U',
                      lhacode = [ 1, 1 ])

GP103U2x2 = Parameter(name = 'GP103U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.105,
                      texname = '\\text{GP103U2x2}',
                      lhablock = 'GP103U',
                      lhacode = [ 2, 2 ])

GP103U3x3 = Parameter(name = 'GP103U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.106,
                      texname = '\\text{GP103U3x3}',
                      lhablock = 'GP103U',
                      lhacode = [ 3, 3 ])

GP103XX = Parameter(name = 'GP103XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GP103XX}',
                    lhablock = 'GP103XX',
                    lhacode = [ 1 ])

GP103YY = Parameter(name = 'GP103YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GP103YY}',
                    lhablock = 'GP103YY',
                    lhacode = [ 1 ])

GP104BB = Parameter(name = 'GP104BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GP104BB}',
                    lhablock = 'GP104BB',
                    lhacode = [ 1 ])

GP104D1x1 = Parameter(name = 'GP104D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.114,
                      texname = '\\text{GP104D1x1}',
                      lhablock = 'GP104D',
                      lhacode = [ 1, 1 ])

GP104D2x2 = Parameter(name = 'GP104D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.115,
                      texname = '\\text{GP104D2x2}',
                      lhablock = 'GP104D',
                      lhacode = [ 2, 2 ])

GP104D3x3 = Parameter(name = 'GP104D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.116,
                      texname = '\\text{GP104D3x3}',
                      lhablock = 'GP104D',
                      lhacode = [ 3, 3 ])

GP104E1x1 = Parameter(name = 'GP104E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.124,
                      texname = '\\text{GP104E1x1}',
                      lhablock = 'GP104E',
                      lhacode = [ 1, 1 ])

GP104E2x2 = Parameter(name = 'GP104E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.125,
                      texname = '\\text{GP104E2x2}',
                      lhablock = 'GP104E',
                      lhacode = [ 2, 2 ])

GP104E3x3 = Parameter(name = 'GP104E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.126,
                      texname = '\\text{GP104E3x3}',
                      lhablock = 'GP104E',
                      lhacode = [ 3, 3 ])

GP104N1x1 = Parameter(name = 'GP104N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.134,
                      texname = '\\text{GP104N1x1}',
                      lhablock = 'GP104N',
                      lhacode = [ 1, 1 ])

GP104N2x2 = Parameter(name = 'GP104N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.135,
                      texname = '\\text{GP104N2x2}',
                      lhablock = 'GP104N',
                      lhacode = [ 2, 2 ])

GP104N3x3 = Parameter(name = 'GP104N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.136,
                      texname = '\\text{GP104N3x3}',
                      lhablock = 'GP104N',
                      lhacode = [ 3, 3 ])

GP104TT = Parameter(name = 'GP104TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GP104TT}',
                    lhablock = 'GP104TT',
                    lhacode = [ 1 ])

GP104U1x1 = Parameter(name = 'GP104U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.104,
                      texname = '\\text{GP104U1x1}',
                      lhablock = 'GP104U',
                      lhacode = [ 1, 1 ])

GP104U2x2 = Parameter(name = 'GP104U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.105,
                      texname = '\\text{GP104U2x2}',
                      lhablock = 'GP104U',
                      lhacode = [ 2, 2 ])

GP104U3x3 = Parameter(name = 'GP104U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.106,
                      texname = '\\text{GP104U3x3}',
                      lhablock = 'GP104U',
                      lhacode = [ 3, 3 ])

GP104XX = Parameter(name = 'GP104XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GP104XX}',
                    lhablock = 'GP104XX',
                    lhacode = [ 1 ])

GP104YY = Parameter(name = 'GP104YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GP104YY}',
                    lhablock = 'GP104YY',
                    lhacode = [ 1 ])

GP105BB = Parameter(name = 'GP105BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GP105BB}',
                    lhablock = 'GP105BB',
                    lhacode = [ 1 ])

GP105D1x1 = Parameter(name = 'GP105D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.114,
                      texname = '\\text{GP105D1x1}',
                      lhablock = 'GP105D',
                      lhacode = [ 1, 1 ])

GP105D2x2 = Parameter(name = 'GP105D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.115,
                      texname = '\\text{GP105D2x2}',
                      lhablock = 'GP105D',
                      lhacode = [ 2, 2 ])

GP105D3x3 = Parameter(name = 'GP105D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.116,
                      texname = '\\text{GP105D3x3}',
                      lhablock = 'GP105D',
                      lhacode = [ 3, 3 ])

GP105E1x1 = Parameter(name = 'GP105E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.124,
                      texname = '\\text{GP105E1x1}',
                      lhablock = 'GP105E',
                      lhacode = [ 1, 1 ])

GP105E2x2 = Parameter(name = 'GP105E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.125,
                      texname = '\\text{GP105E2x2}',
                      lhablock = 'GP105E',
                      lhacode = [ 2, 2 ])

GP105E3x3 = Parameter(name = 'GP105E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.126,
                      texname = '\\text{GP105E3x3}',
                      lhablock = 'GP105E',
                      lhacode = [ 3, 3 ])

GP105N1x1 = Parameter(name = 'GP105N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.134,
                      texname = '\\text{GP105N1x1}',
                      lhablock = 'GP105N',
                      lhacode = [ 1, 1 ])

GP105N2x2 = Parameter(name = 'GP105N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.135,
                      texname = '\\text{GP105N2x2}',
                      lhablock = 'GP105N',
                      lhacode = [ 2, 2 ])

GP105N3x3 = Parameter(name = 'GP105N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.136,
                      texname = '\\text{GP105N3x3}',
                      lhablock = 'GP105N',
                      lhacode = [ 3, 3 ])

GP105TT = Parameter(name = 'GP105TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GP105TT}',
                    lhablock = 'GP105TT',
                    lhacode = [ 1 ])

GP105U1x1 = Parameter(name = 'GP105U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.104,
                      texname = '\\text{GP105U1x1}',
                      lhablock = 'GP105U',
                      lhacode = [ 1, 1 ])

GP105U2x2 = Parameter(name = 'GP105U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.105,
                      texname = '\\text{GP105U2x2}',
                      lhablock = 'GP105U',
                      lhacode = [ 2, 2 ])

GP105U3x3 = Parameter(name = 'GP105U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.106,
                      texname = '\\text{GP105U3x3}',
                      lhablock = 'GP105U',
                      lhacode = [ 3, 3 ])

GP105XX = Parameter(name = 'GP105XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GP105XX}',
                    lhablock = 'GP105XX',
                    lhacode = [ 1 ])

GP105YY = Parameter(name = 'GP105YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GP105YY}',
                    lhablock = 'GP105YY',
                    lhacode = [ 1 ])

GP10BB = Parameter(name = 'GP10BB',
                   nature = 'external',
                   type = 'real',
                   value = 0.154,
                   texname = '\\text{GP10BB}',
                   lhablock = 'GP10BB',
                   lhacode = [ 1 ])

GP10D1x1 = Parameter(name = 'GP10D1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.114,
                     texname = '\\text{GP10D1x1}',
                     lhablock = 'GP10D',
                     lhacode = [ 1, 1 ])

GP10D2x2 = Parameter(name = 'GP10D2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.115,
                     texname = '\\text{GP10D2x2}',
                     lhablock = 'GP10D',
                     lhacode = [ 2, 2 ])

GP10D3x3 = Parameter(name = 'GP10D3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.116,
                     texname = '\\text{GP10D3x3}',
                     lhablock = 'GP10D',
                     lhacode = [ 3, 3 ])

GP10E1x1 = Parameter(name = 'GP10E1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.124,
                     texname = '\\text{GP10E1x1}',
                     lhablock = 'GP10E',
                     lhacode = [ 1, 1 ])

GP10E2x2 = Parameter(name = 'GP10E2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.125,
                     texname = '\\text{GP10E2x2}',
                     lhablock = 'GP10E',
                     lhacode = [ 2, 2 ])

GP10E3x3 = Parameter(name = 'GP10E3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.126,
                     texname = '\\text{GP10E3x3}',
                     lhablock = 'GP10E',
                     lhacode = [ 3, 3 ])

GP10N1x1 = Parameter(name = 'GP10N1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.134,
                     texname = '\\text{GP10N1x1}',
                     lhablock = 'GP10N',
                     lhacode = [ 1, 1 ])

GP10N2x2 = Parameter(name = 'GP10N2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.135,
                     texname = '\\text{GP10N2x2}',
                     lhablock = 'GP10N',
                     lhacode = [ 2, 2 ])

GP10N3x3 = Parameter(name = 'GP10N3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.136,
                     texname = '\\text{GP10N3x3}',
                     lhablock = 'GP10N',
                     lhacode = [ 3, 3 ])

GP10TT = Parameter(name = 'GP10TT',
                   nature = 'external',
                   type = 'real',
                   value = 0.153,
                   texname = '\\text{GP10TT}',
                   lhablock = 'GP10TT',
                   lhacode = [ 1 ])

GP10U1x1 = Parameter(name = 'GP10U1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.104,
                     texname = '\\text{GP10U1x1}',
                     lhablock = 'GP10U',
                     lhacode = [ 1, 1 ])

GP10U2x2 = Parameter(name = 'GP10U2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.105,
                     texname = '\\text{GP10U2x2}',
                     lhablock = 'GP10U',
                     lhacode = [ 2, 2 ])

GP10U3x3 = Parameter(name = 'GP10U3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.106,
                     texname = '\\text{GP10U3x3}',
                     lhablock = 'GP10U',
                     lhacode = [ 3, 3 ])

GP10XX = Parameter(name = 'GP10XX',
                   nature = 'external',
                   type = 'real',
                   value = 0.155,
                   texname = '\\text{GP10XX}',
                   lhablock = 'GP10XX',
                   lhacode = [ 1 ])

GP10YY = Parameter(name = 'GP10YY',
                   nature = 'external',
                   type = 'real',
                   value = 0.156,
                   texname = '\\text{GP10YY}',
                   lhablock = 'GP10YY',
                   lhacode = [ 1 ])

GP112ll1x1 = Parameter(name = 'GP112ll1x1',
                       nature = 'external',
                       type = 'real',
                       value = 0.0101,
                       texname = '\\text{GP112ll1x1}',
                       lhablock = 'GP112ll',
                       lhacode = [ 1, 1 ])

GP112ll2x2 = Parameter(name = 'GP112ll2x2',
                       nature = 'external',
                       type = 'real',
                       value = 0.0102,
                       texname = '\\text{GP112ll2x2}',
                       lhablock = 'GP112ll',
                       lhacode = [ 2, 2 ])

GP112ll3x3 = Parameter(name = 'GP112ll3x3',
                       nature = 'external',
                       type = 'real',
                       value = 0.0103,
                       texname = '\\text{GP112ll3x3}',
                       lhablock = 'GP112ll',
                       lhacode = [ 3, 3 ])

GP112qq1x1 = Parameter(name = 'GP112qq1x1',
                       nature = 'external',
                       type = 'real',
                       value = 0.101,
                       texname = '\\text{GP112qq1x1}',
                       lhablock = 'GP112qq',
                       lhacode = [ 1, 1 ])

GP112qq2x2 = Parameter(name = 'GP112qq2x2',
                       nature = 'external',
                       type = 'real',
                       value = 0.102,
                       texname = '\\text{GP112qq2x2}',
                       lhablock = 'GP112qq',
                       lhacode = [ 2, 2 ])

GP112qq3x3 = Parameter(name = 'GP112qq3x3',
                       nature = 'external',
                       type = 'real',
                       value = 0.103,
                       texname = '\\text{GP112qq3x3}',
                       lhablock = 'GP112qq',
                       lhacode = [ 3, 3 ])

GP11ll1x1 = Parameter(name = 'GP11ll1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.0101,
                      texname = '\\text{GP11ll1x1}',
                      lhablock = 'GP11ll',
                      lhacode = [ 1, 1 ])

GP11ll2x2 = Parameter(name = 'GP11ll2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.0102,
                      texname = '\\text{GP11ll2x2}',
                      lhablock = 'GP11ll',
                      lhacode = [ 2, 2 ])

GP11ll3x3 = Parameter(name = 'GP11ll3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.0103,
                      texname = '\\text{GP11ll3x3}',
                      lhablock = 'GP11ll',
                      lhacode = [ 3, 3 ])

GP11qq1x1 = Parameter(name = 'GP11qq1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{GP11qq1x1}',
                      lhablock = 'GP11qq',
                      lhacode = [ 1, 1 ])

GP11qq2x2 = Parameter(name = 'GP11qq2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.102,
                      texname = '\\text{GP11qq2x2}',
                      lhablock = 'GP11qq',
                      lhacode = [ 2, 2 ])

GP11qq3x3 = Parameter(name = 'GP11qq3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{GP11qq3x3}',
                      lhablock = 'GP11qq',
                      lhacode = [ 3, 3 ])

GP80B = Parameter(name = 'GP80B',
                  nature = 'external',
                  type = 'real',
                  value = 0.155,
                  texname = '\\text{GP80B}',
                  lhablock = 'GP80B',
                  lhacode = [ 1 ])

GP80D1x1 = Parameter(name = 'GP80D1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.101,
                     texname = '\\text{GP80D1x1}',
                     lhablock = 'GP80D',
                     lhacode = [ 1, 1 ])

GP80D2x2 = Parameter(name = 'GP80D2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.102,
                     texname = '\\text{GP80D2x2}',
                     lhablock = 'GP80D',
                     lhacode = [ 2, 2 ])

GP80D3x3 = Parameter(name = 'GP80D3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.103,
                     texname = '\\text{GP80D3x3}',
                     lhablock = 'GP80D',
                     lhacode = [ 3, 3 ])

GP80T = Parameter(name = 'GP80T',
                  nature = 'external',
                  type = 'real',
                  value = 0.154,
                  texname = '\\text{GP80T}',
                  lhablock = 'GP80T',
                  lhacode = [ 1 ])

GP80U1x1 = Parameter(name = 'GP80U1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.101,
                     texname = '\\text{GP80U1x1}',
                     lhablock = 'GP80U',
                     lhacode = [ 1, 1 ])

GP80U2x2 = Parameter(name = 'GP80U2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.102,
                     texname = '\\text{GP80U2x2}',
                     lhablock = 'GP80U',
                     lhacode = [ 2, 2 ])

GP80U3x3 = Parameter(name = 'GP80U3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.103,
                     texname = '\\text{GP80U3x3}',
                     lhablock = 'GP80U',
                     lhacode = [ 3, 3 ])

GP80X = Parameter(name = 'GP80X',
                  nature = 'external',
                  type = 'real',
                  value = 0.153,
                  texname = '\\text{GP80X}',
                  lhablock = 'GP80X',
                  lhacode = [ 1 ])

GP80Y = Parameter(name = 'GP80Y',
                  nature = 'external',
                  type = 'real',
                  value = 0.156,
                  texname = '\\text{GP80Y}',
                  lhablock = 'GP80Y',
                  lhacode = [ 1 ])

GS102BB = Parameter(name = 'GS102BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS102BB}',
                    lhablock = 'GS102BB',
                    lhacode = [ 1 ])

GS102BL1 = Parameter(name = 'GS102BL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.161,
                     texname = '\\text{GS102BL1}',
                     lhablock = 'GS102BL',
                     lhacode = [ 1 ])

GS102BL2 = Parameter(name = 'GS102BL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.162,
                     texname = '\\text{GS102BL2}',
                     lhablock = 'GS102BL',
                     lhacode = [ 2 ])

GS102BL3 = Parameter(name = 'GS102BL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.163,
                     texname = '\\text{GS102BL3}',
                     lhablock = 'GS102BL',
                     lhacode = [ 3 ])

GS102BR1 = Parameter(name = 'GS102BR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.164,
                     texname = '\\text{GS102BR1}',
                     lhablock = 'GS102BR',
                     lhacode = [ 1 ])

GS102BR2 = Parameter(name = 'GS102BR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.165,
                     texname = '\\text{GS102BR2}',
                     lhablock = 'GS102BR',
                     lhacode = [ 2 ])

GS102BR3 = Parameter(name = 'GS102BR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.166,
                     texname = '\\text{GS102BR3}',
                     lhablock = 'GS102BR',
                     lhacode = [ 3 ])

GS102D1x1 = Parameter(name = 'GS102D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.111,
                      texname = '\\text{GS102D1x1}',
                      lhablock = 'GS102D',
                      lhacode = [ 1, 1 ])

GS102D2x2 = Parameter(name = 'GS102D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.112,
                      texname = '\\text{GS102D2x2}',
                      lhablock = 'GS102D',
                      lhacode = [ 2, 2 ])

GS102D3x3 = Parameter(name = 'GS102D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.113,
                      texname = '\\text{GS102D3x3}',
                      lhablock = 'GS102D',
                      lhacode = [ 3, 3 ])

GS102E1x1 = Parameter(name = 'GS102E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.121,
                      texname = '\\text{GS102E1x1}',
                      lhablock = 'GS102E',
                      lhacode = [ 1, 1 ])

GS102E2x2 = Parameter(name = 'GS102E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.122,
                      texname = '\\text{GS102E2x2}',
                      lhablock = 'GS102E',
                      lhacode = [ 2, 2 ])

GS102E3x3 = Parameter(name = 'GS102E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.123,
                      texname = '\\text{GS102E3x3}',
                      lhablock = 'GS102E',
                      lhacode = [ 3, 3 ])

GS102N1x1 = Parameter(name = 'GS102N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.131,
                      texname = '\\text{GS102N1x1}',
                      lhablock = 'GS102N',
                      lhacode = [ 1, 1 ])

GS102N2x2 = Parameter(name = 'GS102N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.132,
                      texname = '\\text{GS102N2x2}',
                      lhablock = 'GS102N',
                      lhacode = [ 2, 2 ])

GS102N3x3 = Parameter(name = 'GS102N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.133,
                      texname = '\\text{GS102N3x3}',
                      lhablock = 'GS102N',
                      lhacode = [ 3, 3 ])

GS102TL1 = Parameter(name = 'GS102TL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS102TL1}',
                     lhablock = 'GS102TL',
                     lhacode = [ 1 ])

GS102TL2 = Parameter(name = 'GS102TL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS102TL2}',
                     lhablock = 'GS102TL',
                     lhacode = [ 2 ])

GS102TL3 = Parameter(name = 'GS102TL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS102TL3}',
                     lhablock = 'GS102TL',
                     lhacode = [ 3 ])

GS102TR1 = Parameter(name = 'GS102TR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS102TR1}',
                     lhablock = 'GS102TR',
                     lhacode = [ 1 ])

GS102TR2 = Parameter(name = 'GS102TR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS102TR2}',
                     lhablock = 'GS102TR',
                     lhacode = [ 2 ])

GS102TR3 = Parameter(name = 'GS102TR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.156,
                     texname = '\\text{GS102TR3}',
                     lhablock = 'GS102TR',
                     lhacode = [ 3 ])

GS102TT = Parameter(name = 'GS102TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS102TT}',
                    lhablock = 'GS102TT',
                    lhacode = [ 1 ])

GS102U1x1 = Parameter(name = 'GS102U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{GS102U1x1}',
                      lhablock = 'GS102U',
                      lhacode = [ 1, 1 ])

GS102U2x2 = Parameter(name = 'GS102U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.102,
                      texname = '\\text{GS102U2x2}',
                      lhablock = 'GS102U',
                      lhacode = [ 2, 2 ])

GS102U3x3 = Parameter(name = 'GS102U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{GS102U3x3}',
                      lhablock = 'GS102U',
                      lhacode = [ 3, 3 ])

GS102XX = Parameter(name = 'GS102XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GS102XX}',
                    lhablock = 'GS102XX',
                    lhacode = [ 1 ])

GS102YY = Parameter(name = 'GS102YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GS102YY}',
                    lhablock = 'GS102YY',
                    lhacode = [ 1 ])

GS103BB = Parameter(name = 'GS103BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS103BB}',
                    lhablock = 'GS103BB',
                    lhacode = [ 1 ])

GS103BL1 = Parameter(name = 'GS103BL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.161,
                     texname = '\\text{GS103BL1}',
                     lhablock = 'GS103BL',
                     lhacode = [ 1 ])

GS103BL2 = Parameter(name = 'GS103BL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.162,
                     texname = '\\text{GS103BL2}',
                     lhablock = 'GS103BL',
                     lhacode = [ 2 ])

GS103BL3 = Parameter(name = 'GS103BL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.163,
                     texname = '\\text{GS103BL3}',
                     lhablock = 'GS103BL',
                     lhacode = [ 3 ])

GS103BR1 = Parameter(name = 'GS103BR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.164,
                     texname = '\\text{GS103BR1}',
                     lhablock = 'GS103BR',
                     lhacode = [ 1 ])

GS103BR2 = Parameter(name = 'GS103BR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.165,
                     texname = '\\text{GS103BR2}',
                     lhablock = 'GS103BR',
                     lhacode = [ 2 ])

GS103BR3 = Parameter(name = 'GS103BR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.166,
                     texname = '\\text{GS103BR3}',
                     lhablock = 'GS103BR',
                     lhacode = [ 3 ])

GS103D1x1 = Parameter(name = 'GS103D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.111,
                      texname = '\\text{GS103D1x1}',
                      lhablock = 'GS103D',
                      lhacode = [ 1, 1 ])

GS103D2x2 = Parameter(name = 'GS103D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.112,
                      texname = '\\text{GS103D2x2}',
                      lhablock = 'GS103D',
                      lhacode = [ 2, 2 ])

GS103D3x3 = Parameter(name = 'GS103D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.113,
                      texname = '\\text{GS103D3x3}',
                      lhablock = 'GS103D',
                      lhacode = [ 3, 3 ])

GS103E1x1 = Parameter(name = 'GS103E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.121,
                      texname = '\\text{GS103E1x1}',
                      lhablock = 'GS103E',
                      lhacode = [ 1, 1 ])

GS103E2x2 = Parameter(name = 'GS103E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.122,
                      texname = '\\text{GS103E2x2}',
                      lhablock = 'GS103E',
                      lhacode = [ 2, 2 ])

GS103E3x3 = Parameter(name = 'GS103E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.123,
                      texname = '\\text{GS103E3x3}',
                      lhablock = 'GS103E',
                      lhacode = [ 3, 3 ])

GS103N1x1 = Parameter(name = 'GS103N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.131,
                      texname = '\\text{GS103N1x1}',
                      lhablock = 'GS103N',
                      lhacode = [ 1, 1 ])

GS103N2x2 = Parameter(name = 'GS103N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.132,
                      texname = '\\text{GS103N2x2}',
                      lhablock = 'GS103N',
                      lhacode = [ 2, 2 ])

GS103N3x3 = Parameter(name = 'GS103N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.133,
                      texname = '\\text{GS103N3x3}',
                      lhablock = 'GS103N',
                      lhacode = [ 3, 3 ])

GS103TL1 = Parameter(name = 'GS103TL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS103TL1}',
                     lhablock = 'GS103TL',
                     lhacode = [ 1 ])

GS103TL2 = Parameter(name = 'GS103TL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS103TL2}',
                     lhablock = 'GS103TL',
                     lhacode = [ 2 ])

GS103TL3 = Parameter(name = 'GS103TL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS103TL3}',
                     lhablock = 'GS103TL',
                     lhacode = [ 3 ])

GS103TR1 = Parameter(name = 'GS103TR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS103TR1}',
                     lhablock = 'GS103TR',
                     lhacode = [ 1 ])

GS103TR2 = Parameter(name = 'GS103TR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS103TR2}',
                     lhablock = 'GS103TR',
                     lhacode = [ 2 ])

GS103TR3 = Parameter(name = 'GS103TR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.156,
                     texname = '\\text{GS103TR3}',
                     lhablock = 'GS103TR',
                     lhacode = [ 3 ])

GS103TT = Parameter(name = 'GS103TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS103TT}',
                    lhablock = 'GS103TT',
                    lhacode = [ 1 ])

GS103U1x1 = Parameter(name = 'GS103U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{GS103U1x1}',
                      lhablock = 'GS103U',
                      lhacode = [ 1, 1 ])

GS103U2x2 = Parameter(name = 'GS103U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{GS103U2x2}',
                      lhablock = 'GS103U',
                      lhacode = [ 2, 2 ])

GS103U3x3 = Parameter(name = 'GS103U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{GS103U3x3}',
                      lhablock = 'GS103U',
                      lhacode = [ 3, 3 ])

GS103XX = Parameter(name = 'GS103XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GS103XX}',
                    lhablock = 'GS103XX',
                    lhacode = [ 1 ])

GS103YY = Parameter(name = 'GS103YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GS103YY}',
                    lhablock = 'GS103YY',
                    lhacode = [ 1 ])

GS104BB = Parameter(name = 'GS104BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS104BB}',
                    lhablock = 'GS104BB',
                    lhacode = [ 1 ])

GS104BL1 = Parameter(name = 'GS104BL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.161,
                     texname = '\\text{GS104BL1}',
                     lhablock = 'GS104BL',
                     lhacode = [ 1 ])

GS104BL2 = Parameter(name = 'GS104BL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.162,
                     texname = '\\text{GS104BL2}',
                     lhablock = 'GS104BL',
                     lhacode = [ 2 ])

GS104BL3 = Parameter(name = 'GS104BL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.163,
                     texname = '\\text{GS104BL3}',
                     lhablock = 'GS104BL',
                     lhacode = [ 3 ])

GS104BR1 = Parameter(name = 'GS104BR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.164,
                     texname = '\\text{GS104BR1}',
                     lhablock = 'GS104BR',
                     lhacode = [ 1 ])

GS104BR2 = Parameter(name = 'GS104BR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.165,
                     texname = '\\text{GS104BR2}',
                     lhablock = 'GS104BR',
                     lhacode = [ 2 ])

GS104BR3 = Parameter(name = 'GS104BR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.166,
                     texname = '\\text{GS104BR3}',
                     lhablock = 'GS104BR',
                     lhacode = [ 3 ])

GS104D1x1 = Parameter(name = 'GS104D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.111,
                      texname = '\\text{GS104D1x1}',
                      lhablock = 'GS104D',
                      lhacode = [ 1, 1 ])

GS104D2x2 = Parameter(name = 'GS104D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.112,
                      texname = '\\text{GS104D2x2}',
                      lhablock = 'GS104D',
                      lhacode = [ 2, 2 ])

GS104D3x3 = Parameter(name = 'GS104D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.113,
                      texname = '\\text{GS104D3x3}',
                      lhablock = 'GS104D',
                      lhacode = [ 3, 3 ])

GS104E1x1 = Parameter(name = 'GS104E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.121,
                      texname = '\\text{GS104E1x1}',
                      lhablock = 'GS104E',
                      lhacode = [ 1, 1 ])

GS104E2x2 = Parameter(name = 'GS104E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.122,
                      texname = '\\text{GS104E2x2}',
                      lhablock = 'GS104E',
                      lhacode = [ 2, 2 ])

GS104E3x3 = Parameter(name = 'GS104E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.123,
                      texname = '\\text{GS104E3x3}',
                      lhablock = 'GS104E',
                      lhacode = [ 3, 3 ])

GS104N1x1 = Parameter(name = 'GS104N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.131,
                      texname = '\\text{GS104N1x1}',
                      lhablock = 'GS104N',
                      lhacode = [ 1, 1 ])

GS104N2x2 = Parameter(name = 'GS104N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.132,
                      texname = '\\text{GS104N2x2}',
                      lhablock = 'GS104N',
                      lhacode = [ 2, 2 ])

GS104N3x3 = Parameter(name = 'GS104N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.133,
                      texname = '\\text{GS104N3x3}',
                      lhablock = 'GS104N',
                      lhacode = [ 3, 3 ])

GS104TL1 = Parameter(name = 'GS104TL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS104TL1}',
                     lhablock = 'GS104TL',
                     lhacode = [ 1 ])

GS104TL2 = Parameter(name = 'GS104TL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS104TL2}',
                     lhablock = 'GS104TL',
                     lhacode = [ 2 ])

GS104TL3 = Parameter(name = 'GS104TL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS104TL3}',
                     lhablock = 'GS104TL',
                     lhacode = [ 3 ])

GS104TR1 = Parameter(name = 'GS104TR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS104TR1}',
                     lhablock = 'GS104TR',
                     lhacode = [ 1 ])

GS104TR2 = Parameter(name = 'GS104TR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS104TR2}',
                     lhablock = 'GS104TR',
                     lhacode = [ 2 ])

GS104TR3 = Parameter(name = 'GS104TR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.156,
                     texname = '\\text{GS104TR3}',
                     lhablock = 'GS104TR',
                     lhacode = [ 3 ])

GS104TT = Parameter(name = 'GS104TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS104TT}',
                    lhablock = 'GS104TT',
                    lhacode = [ 1 ])

GS104U1x1 = Parameter(name = 'GS104U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{GS104U1x1}',
                      lhablock = 'GS104U',
                      lhacode = [ 1, 1 ])

GS104U2x2 = Parameter(name = 'GS104U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.104,
                      texname = '\\text{GS104U2x2}',
                      lhablock = 'GS104U',
                      lhacode = [ 2, 2 ])

GS104U3x3 = Parameter(name = 'GS104U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{GS104U3x3}',
                      lhablock = 'GS104U',
                      lhacode = [ 3, 3 ])

GS104XX = Parameter(name = 'GS104XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GS104XX}',
                    lhablock = 'GS104XX',
                    lhacode = [ 1 ])

GS104YY = Parameter(name = 'GS104YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GS104YY}',
                    lhablock = 'GS104YY',
                    lhacode = [ 1 ])

GS105BB = Parameter(name = 'GS105BB',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS105BB}',
                    lhablock = 'GS105BB',
                    lhacode = [ 1 ])

GS105BL1 = Parameter(name = 'GS105BL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.161,
                     texname = '\\text{GS105BL1}',
                     lhablock = 'GS105BL',
                     lhacode = [ 1 ])

GS105BL2 = Parameter(name = 'GS105BL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.162,
                     texname = '\\text{GS105BL2}',
                     lhablock = 'GS105BL',
                     lhacode = [ 2 ])

GS105BL3 = Parameter(name = 'GS105BL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.163,
                     texname = '\\text{GS105BL3}',
                     lhablock = 'GS105BL',
                     lhacode = [ 3 ])

GS105BR1 = Parameter(name = 'GS105BR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.164,
                     texname = '\\text{GS105BR1}',
                     lhablock = 'GS105BR',
                     lhacode = [ 1 ])

GS105BR2 = Parameter(name = 'GS105BR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.165,
                     texname = '\\text{GS105BR2}',
                     lhablock = 'GS105BR',
                     lhacode = [ 2 ])

GS105BR3 = Parameter(name = 'GS105BR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.166,
                     texname = '\\text{GS105BR3}',
                     lhablock = 'GS105BR',
                     lhacode = [ 3 ])

GS105D1x1 = Parameter(name = 'GS105D1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.111,
                      texname = '\\text{GS105D1x1}',
                      lhablock = 'GS105D',
                      lhacode = [ 1, 1 ])

GS105D2x2 = Parameter(name = 'GS105D2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.112,
                      texname = '\\text{GS105D2x2}',
                      lhablock = 'GS105D',
                      lhacode = [ 2, 2 ])

GS105D3x3 = Parameter(name = 'GS105D3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.113,
                      texname = '\\text{GS105D3x3}',
                      lhablock = 'GS105D',
                      lhacode = [ 3, 3 ])

GS105E1x1 = Parameter(name = 'GS105E1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.121,
                      texname = '\\text{GS105E1x1}',
                      lhablock = 'GS105E',
                      lhacode = [ 1, 1 ])

GS105E2x2 = Parameter(name = 'GS105E2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.122,
                      texname = '\\text{GS105E2x2}',
                      lhablock = 'GS105E',
                      lhacode = [ 2, 2 ])

GS105E3x3 = Parameter(name = 'GS105E3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.123,
                      texname = '\\text{GS105E3x3}',
                      lhablock = 'GS105E',
                      lhacode = [ 3, 3 ])

GS105N1x1 = Parameter(name = 'GS105N1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.131,
                      texname = '\\text{GS105N1x1}',
                      lhablock = 'GS105N',
                      lhacode = [ 1, 1 ])

GS105N2x2 = Parameter(name = 'GS105N2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.132,
                      texname = '\\text{GS105N2x2}',
                      lhablock = 'GS105N',
                      lhacode = [ 2, 2 ])

GS105N3x3 = Parameter(name = 'GS105N3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.133,
                      texname = '\\text{GS105N3x3}',
                      lhablock = 'GS105N',
                      lhacode = [ 3, 3 ])

GS105TL1 = Parameter(name = 'GS105TL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS105TL1}',
                     lhablock = 'GS105TL',
                     lhacode = [ 1 ])

GS105TL2 = Parameter(name = 'GS105TL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS105TL2}',
                     lhablock = 'GS105TL',
                     lhacode = [ 2 ])

GS105TL3 = Parameter(name = 'GS105TL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS105TL3}',
                     lhablock = 'GS105TL',
                     lhacode = [ 3 ])

GS105TR1 = Parameter(name = 'GS105TR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS105TR1}',
                     lhablock = 'GS105TR',
                     lhacode = [ 1 ])

GS105TR2 = Parameter(name = 'GS105TR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS105TR2}',
                     lhablock = 'GS105TR',
                     lhacode = [ 2 ])

GS105TR3 = Parameter(name = 'GS105TR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.156,
                     texname = '\\text{GS105TR3}',
                     lhablock = 'GS105TR',
                     lhacode = [ 3 ])

GS105TT = Parameter(name = 'GS105TT',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS105TT}',
                    lhablock = 'GS105TT',
                    lhacode = [ 1 ])

GS105U1x1 = Parameter(name = 'GS105U1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{GS105U1x1}',
                      lhablock = 'GS105U',
                      lhacode = [ 1, 1 ])

GS105U2x2 = Parameter(name = 'GS105U2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.105,
                      texname = '\\text{GS105U2x2}',
                      lhablock = 'GS105U',
                      lhacode = [ 2, 2 ])

GS105U3x3 = Parameter(name = 'GS105U3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{GS105U3x3}',
                      lhablock = 'GS105U',
                      lhacode = [ 3, 3 ])

GS105XX = Parameter(name = 'GS105XX',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GS105XX}',
                    lhablock = 'GS105XX',
                    lhacode = [ 1 ])

GS105YY = Parameter(name = 'GS105YY',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GS105YY}',
                    lhablock = 'GS105YY',
                    lhacode = [ 1 ])

GS10BB = Parameter(name = 'GS10BB',
                   nature = 'external',
                   type = 'real',
                   value = 0.154,
                   texname = '\\text{GS10BB}',
                   lhablock = 'GS10BB',
                   lhacode = [ 1 ])

GS10BL1 = Parameter(name = 'GS10BL1',
                    nature = 'external',
                    type = 'real',
                    value = 0.161,
                    texname = '\\text{GS10BL1}',
                    lhablock = 'GS10BL',
                    lhacode = [ 1 ])

GS10BL2 = Parameter(name = 'GS10BL2',
                    nature = 'external',
                    type = 'real',
                    value = 0.162,
                    texname = '\\text{GS10BL2}',
                    lhablock = 'GS10BL',
                    lhacode = [ 2 ])

GS10BL3 = Parameter(name = 'GS10BL3',
                    nature = 'external',
                    type = 'real',
                    value = 0.163,
                    texname = '\\text{GS10BL3}',
                    lhablock = 'GS10BL',
                    lhacode = [ 3 ])

GS10BR1 = Parameter(name = 'GS10BR1',
                    nature = 'external',
                    type = 'real',
                    value = 0.164,
                    texname = '\\text{GS10BR1}',
                    lhablock = 'GS10BR',
                    lhacode = [ 1 ])

GS10BR2 = Parameter(name = 'GS10BR2',
                    nature = 'external',
                    type = 'real',
                    value = 0.165,
                    texname = '\\text{GS10BR2}',
                    lhablock = 'GS10BR',
                    lhacode = [ 2 ])

GS10BR3 = Parameter(name = 'GS10BR3',
                    nature = 'external',
                    type = 'real',
                    value = 0.166,
                    texname = '\\text{GS10BR3}',
                    lhablock = 'GS10BR',
                    lhacode = [ 3 ])

GS10D1x1 = Parameter(name = 'GS10D1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.111,
                     texname = '\\text{GS10D1x1}',
                     lhablock = 'GS10D',
                     lhacode = [ 1, 1 ])

GS10D2x2 = Parameter(name = 'GS10D2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.112,
                     texname = '\\text{GS10D2x2}',
                     lhablock = 'GS10D',
                     lhacode = [ 2, 2 ])

GS10D3x3 = Parameter(name = 'GS10D3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.113,
                     texname = '\\text{GS10D3x3}',
                     lhablock = 'GS10D',
                     lhacode = [ 3, 3 ])

GS10E1x1 = Parameter(name = 'GS10E1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.121,
                     texname = '\\text{GS10E1x1}',
                     lhablock = 'GS10E',
                     lhacode = [ 1, 1 ])

GS10E2x2 = Parameter(name = 'GS10E2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.122,
                     texname = '\\text{GS10E2x2}',
                     lhablock = 'GS10E',
                     lhacode = [ 2, 2 ])

GS10E3x3 = Parameter(name = 'GS10E3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.123,
                     texname = '\\text{GS10E3x3}',
                     lhablock = 'GS10E',
                     lhacode = [ 3, 3 ])

GS10N1x1 = Parameter(name = 'GS10N1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.131,
                     texname = '\\text{GS10N1x1}',
                     lhablock = 'GS10N',
                     lhacode = [ 1, 1 ])

GS10N2x2 = Parameter(name = 'GS10N2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.132,
                     texname = '\\text{GS10N2x2}',
                     lhablock = 'GS10N',
                     lhacode = [ 2, 2 ])

GS10N3x3 = Parameter(name = 'GS10N3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.133,
                     texname = '\\text{GS10N3x3}',
                     lhablock = 'GS10N',
                     lhacode = [ 3, 3 ])

GS10TL1 = Parameter(name = 'GS10TL1',
                    nature = 'external',
                    type = 'real',
                    value = 0.151,
                    texname = '\\text{GS10TL1}',
                    lhablock = 'GS10TL',
                    lhacode = [ 1 ])

GS10TL2 = Parameter(name = 'GS10TL2',
                    nature = 'external',
                    type = 'real',
                    value = 0.152,
                    texname = '\\text{GS10TL2}',
                    lhablock = 'GS10TL',
                    lhacode = [ 2 ])

GS10TL3 = Parameter(name = 'GS10TL3',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS10TL3}',
                    lhablock = 'GS10TL',
                    lhacode = [ 3 ])

GS10TR1 = Parameter(name = 'GS10TR1',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS10TR1}',
                    lhablock = 'GS10TR',
                    lhacode = [ 1 ])

GS10TR2 = Parameter(name = 'GS10TR2',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GS10TR2}',
                    lhablock = 'GS10TR',
                    lhacode = [ 2 ])

GS10TR3 = Parameter(name = 'GS10TR3',
                    nature = 'external',
                    type = 'real',
                    value = 0.156,
                    texname = '\\text{GS10TR3}',
                    lhablock = 'GS10TR',
                    lhacode = [ 3 ])

GS10TT = Parameter(name = 'GS10TT',
                   nature = 'external',
                   type = 'real',
                   value = 0.153,
                   texname = '\\text{GS10TT}',
                   lhablock = 'GS10TT',
                   lhacode = [ 1 ])

GS10U1x1 = Parameter(name = 'GS10U1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.101,
                     texname = '\\text{GS10U1x1}',
                     lhablock = 'GS10U',
                     lhacode = [ 1, 1 ])

GS10U2x2 = Parameter(name = 'GS10U2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.102,
                     texname = '\\text{GS10U2x2}',
                     lhablock = 'GS10U',
                     lhacode = [ 2, 2 ])

GS10U3x3 = Parameter(name = 'GS10U3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.103,
                     texname = '\\text{GS10U3x3}',
                     lhablock = 'GS10U',
                     lhacode = [ 3, 3 ])

GS10XX = Parameter(name = 'GS10XX',
                   nature = 'external',
                   type = 'real',
                   value = 0.155,
                   texname = '\\text{GS10XX}',
                   lhablock = 'GS10XX',
                   lhacode = [ 1 ])

GS10YY = Parameter(name = 'GS10YY',
                   nature = 'external',
                   type = 'real',
                   value = 0.156,
                   texname = '\\text{GS10YY}',
                   lhablock = 'GS10YY',
                   lhacode = [ 1 ])

GS112BuL1 = Parameter(name = 'GS112BuL1',
                      nature = 'external',
                      type = 'real',
                      value = 0.161,
                      texname = '\\text{GS112BuL1}',
                      lhablock = 'GS112BuL',
                      lhacode = [ 1 ])

GS112BuL2 = Parameter(name = 'GS112BuL2',
                      nature = 'external',
                      type = 'real',
                      value = 0.162,
                      texname = '\\text{GS112BuL2}',
                      lhablock = 'GS112BuL',
                      lhacode = [ 2 ])

GS112BuL3 = Parameter(name = 'GS112BuL3',
                      nature = 'external',
                      type = 'real',
                      value = 0.163,
                      texname = '\\text{GS112BuL3}',
                      lhablock = 'GS112BuL',
                      lhacode = [ 3 ])

GS112BuR1 = Parameter(name = 'GS112BuR1',
                      nature = 'external',
                      type = 'real',
                      value = 0.164,
                      texname = '\\text{GS112BuR1}',
                      lhablock = 'GS112BuR',
                      lhacode = [ 1 ])

GS112BuR2 = Parameter(name = 'GS112BuR2',
                      nature = 'external',
                      type = 'real',
                      value = 0.165,
                      texname = '\\text{GS112BuR2}',
                      lhablock = 'GS112BuR',
                      lhacode = [ 2 ])

GS112BuR3 = Parameter(name = 'GS112BuR3',
                      nature = 'external',
                      type = 'real',
                      value = 0.166,
                      texname = '\\text{GS112BuR3}',
                      lhablock = 'GS112BuR',
                      lhacode = [ 3 ])

GS112BYL = Parameter(name = 'GS112BYL',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS112BYL}',
                     lhablock = 'GS112BYL',
                     lhacode = [ 1 ])

GS112BYR = Parameter(name = 'GS112BYR',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS112BYR}',
                     lhablock = 'GS112BYR',
                     lhacode = [ 1 ])

GS112ll1x1 = Parameter(name = 'GS112ll1x1',
                       nature = 'external',
                       type = 'real',
                       value = 0.0101,
                       texname = '\\text{GS112ll1x1}',
                       lhablock = 'GS112ll',
                       lhacode = [ 1, 1 ])

GS112ll2x2 = Parameter(name = 'GS112ll2x2',
                       nature = 'external',
                       type = 'real',
                       value = 0.0102,
                       texname = '\\text{GS112ll2x2}',
                       lhablock = 'GS112ll',
                       lhacode = [ 2, 2 ])

GS112ll3x3 = Parameter(name = 'GS112ll3x3',
                       nature = 'external',
                       type = 'real',
                       value = 0.0103,
                       texname = '\\text{GS112ll3x3}',
                       lhablock = 'GS112ll',
                       lhacode = [ 3, 3 ])

GS112qq1x1 = Parameter(name = 'GS112qq1x1',
                       nature = 'external',
                       type = 'real',
                       value = 0.101,
                       texname = '\\text{GS112qq1x1}',
                       lhablock = 'GS112qq',
                       lhacode = [ 1, 1 ])

GS112qq2x2 = Parameter(name = 'GS112qq2x2',
                       nature = 'external',
                       type = 'real',
                       value = 0.102,
                       texname = '\\text{GS112qq2x2}',
                       lhablock = 'GS112qq',
                       lhacode = [ 2, 2 ])

GS112qq3x3 = Parameter(name = 'GS112qq3x3',
                       nature = 'external',
                       type = 'real',
                       value = 0.103,
                       texname = '\\text{GS112qq3x3}',
                       lhablock = 'GS112qq',
                       lhacode = [ 3, 3 ])

GS112TBL = Parameter(name = 'GS112TBL',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS112TBL}',
                     lhablock = 'GS112TBL',
                     lhacode = [ 1 ])

GS112TBR = Parameter(name = 'GS112TBR',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS112TBR}',
                     lhablock = 'GS112TBR',
                     lhacode = [ 1 ])

GS112TdL1 = Parameter(name = 'GS112TdL1',
                      nature = 'external',
                      type = 'real',
                      value = 0.151,
                      texname = '\\text{GS112TdL1}',
                      lhablock = 'GS112TdL',
                      lhacode = [ 1 ])

GS112TdL2 = Parameter(name = 'GS112TdL2',
                      nature = 'external',
                      type = 'real',
                      value = 0.152,
                      texname = '\\text{GS112TdL2}',
                      lhablock = 'GS112TdL',
                      lhacode = [ 2 ])

GS112TdL3 = Parameter(name = 'GS112TdL3',
                      nature = 'external',
                      type = 'real',
                      value = 0.153,
                      texname = '\\text{GS112TdL3}',
                      lhablock = 'GS112TdL',
                      lhacode = [ 3 ])

GS112TdR1 = Parameter(name = 'GS112TdR1',
                      nature = 'external',
                      type = 'real',
                      value = 0.154,
                      texname = '\\text{GS112TdR1}',
                      lhablock = 'GS112TdR',
                      lhacode = [ 1 ])

GS112TdR2 = Parameter(name = 'GS112TdR2',
                      nature = 'external',
                      type = 'real',
                      value = 0.155,
                      texname = '\\text{GS112TdR2}',
                      lhablock = 'GS112TdR',
                      lhacode = [ 2 ])

GS112TdR3 = Parameter(name = 'GS112TdR3',
                      nature = 'external',
                      type = 'real',
                      value = 0.156,
                      texname = '\\text{GS112TdR3}',
                      lhablock = 'GS112TdR',
                      lhacode = [ 3 ])

GS112tqbqL = Parameter(name = 'GS112tqbqL',
                       nature = 'external',
                       type = 'real',
                       value = 0.1,
                       texname = '\\text{GS112tqbqL}',
                       lhablock = 'GS112tqbqL',
                       lhacode = [ 1 ])

GS112tqbqR = Parameter(name = 'GS112tqbqR',
                       nature = 'external',
                       type = 'real',
                       value = 0.1,
                       texname = '\\text{GS112tqbqR}',
                       lhablock = 'GS112tqbqR',
                       lhacode = [ 1 ])

GS112XTL = Parameter(name = 'GS112XTL',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS112XTL}',
                     lhablock = 'GS112XTL',
                     lhacode = [ 1 ])

GS112XTR = Parameter(name = 'GS112XTR',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS112XTR}',
                     lhablock = 'GS112XTR',
                     lhacode = [ 1 ])

GS112XuL1 = Parameter(name = 'GS112XuL1',
                      nature = 'external',
                      type = 'real',
                      value = 0.161,
                      texname = '\\text{GS112XuL1}',
                      lhablock = 'GS112XuL',
                      lhacode = [ 1 ])

GS112XuL2 = Parameter(name = 'GS112XuL2',
                      nature = 'external',
                      type = 'real',
                      value = 0.162,
                      texname = '\\text{GS112XuL2}',
                      lhablock = 'GS112XuL',
                      lhacode = [ 2 ])

GS112XuL3 = Parameter(name = 'GS112XuL3',
                      nature = 'external',
                      type = 'real',
                      value = 0.163,
                      texname = '\\text{GS112XuL3}',
                      lhablock = 'GS112XuL',
                      lhacode = [ 3 ])

GS112XuR1 = Parameter(name = 'GS112XuR1',
                      nature = 'external',
                      type = 'real',
                      value = 0.164,
                      texname = '\\text{GS112XuR1}',
                      lhablock = 'GS112XuR',
                      lhacode = [ 1 ])

GS112XuR2 = Parameter(name = 'GS112XuR2',
                      nature = 'external',
                      type = 'real',
                      value = 0.165,
                      texname = '\\text{GS112XuR2}',
                      lhablock = 'GS112XuR',
                      lhacode = [ 2 ])

GS112XuR3 = Parameter(name = 'GS112XuR3',
                      nature = 'external',
                      type = 'real',
                      value = 0.166,
                      texname = '\\text{GS112XuR3}',
                      lhablock = 'GS112XuR',
                      lhacode = [ 3 ])

GS112YdL1 = Parameter(name = 'GS112YdL1',
                      nature = 'external',
                      type = 'real',
                      value = 0.151,
                      texname = '\\text{GS112YdL1}',
                      lhablock = 'GS112YdL',
                      lhacode = [ 1 ])

GS112YdL2 = Parameter(name = 'GS112YdL2',
                      nature = 'external',
                      type = 'real',
                      value = 0.152,
                      texname = '\\text{GS112YdL2}',
                      lhablock = 'GS112YdL',
                      lhacode = [ 2 ])

GS112YdL3 = Parameter(name = 'GS112YdL3',
                      nature = 'external',
                      type = 'real',
                      value = 0.153,
                      texname = '\\text{GS112YdL3}',
                      lhablock = 'GS112YdL',
                      lhacode = [ 3 ])

GS112YdR1 = Parameter(name = 'GS112YdR1',
                      nature = 'external',
                      type = 'real',
                      value = 0.154,
                      texname = '\\text{GS112YdR1}',
                      lhablock = 'GS112YdR',
                      lhacode = [ 1 ])

GS112YdR2 = Parameter(name = 'GS112YdR2',
                      nature = 'external',
                      type = 'real',
                      value = 0.155,
                      texname = '\\text{GS112YdR2}',
                      lhablock = 'GS112YdR',
                      lhacode = [ 2 ])

GS112YdR3 = Parameter(name = 'GS112YdR3',
                      nature = 'external',
                      type = 'real',
                      value = 0.156,
                      texname = '\\text{GS112YdR3}',
                      lhablock = 'GS112YdR',
                      lhacode = [ 3 ])

GS11BuL1 = Parameter(name = 'GS11BuL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.161,
                     texname = '\\text{GS11BuL1}',
                     lhablock = 'GS11BuL',
                     lhacode = [ 1 ])

GS11BuL2 = Parameter(name = 'GS11BuL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.162,
                     texname = '\\text{GS11BuL2}',
                     lhablock = 'GS11BuL',
                     lhacode = [ 2 ])

GS11BuL3 = Parameter(name = 'GS11BuL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.163,
                     texname = '\\text{GS11BuL3}',
                     lhablock = 'GS11BuL',
                     lhacode = [ 3 ])

GS11BuR1 = Parameter(name = 'GS11BuR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.164,
                     texname = '\\text{GS11BuR1}',
                     lhablock = 'GS11BuR',
                     lhacode = [ 1 ])

GS11BuR2 = Parameter(name = 'GS11BuR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.165,
                     texname = '\\text{GS11BuR2}',
                     lhablock = 'GS11BuR',
                     lhacode = [ 2 ])

GS11BuR3 = Parameter(name = 'GS11BuR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.166,
                     texname = '\\text{GS11BuR3}',
                     lhablock = 'GS11BuR',
                     lhacode = [ 3 ])

GS11BYL = Parameter(name = 'GS11BYL',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS11BYL}',
                    lhablock = 'GS11BYL',
                    lhacode = [ 1 ])

GS11BYR = Parameter(name = 'GS11BYR',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS11BYR}',
                    lhablock = 'GS11BYR',
                    lhacode = [ 1 ])

GS11ll1x1 = Parameter(name = 'GS11ll1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.0101,
                      texname = '\\text{GS11ll1x1}',
                      lhablock = 'GS11ll',
                      lhacode = [ 1, 1 ])

GS11ll2x2 = Parameter(name = 'GS11ll2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.0102,
                      texname = '\\text{GS11ll2x2}',
                      lhablock = 'GS11ll',
                      lhacode = [ 2, 2 ])

GS11ll3x3 = Parameter(name = 'GS11ll3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.0103,
                      texname = '\\text{GS11ll3x3}',
                      lhablock = 'GS11ll',
                      lhacode = [ 3, 3 ])

GS11qq1x1 = Parameter(name = 'GS11qq1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{GS11qq1x1}',
                      lhablock = 'GS11qq',
                      lhacode = [ 1, 1 ])

GS11qq2x2 = Parameter(name = 'GS11qq2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.102,
                      texname = '\\text{GS11qq2x2}',
                      lhablock = 'GS11qq',
                      lhacode = [ 2, 2 ])

GS11qq3x3 = Parameter(name = 'GS11qq3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.103,
                      texname = '\\text{GS11qq3x3}',
                      lhablock = 'GS11qq',
                      lhacode = [ 3, 3 ])

GS11TBL = Parameter(name = 'GS11TBL',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS11TBL}',
                    lhablock = 'GS11TBL',
                    lhacode = [ 1 ])

GS11TBR = Parameter(name = 'GS11TBR',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS11TBR}',
                    lhablock = 'GS11TBR',
                    lhacode = [ 1 ])

GS11TdL1 = Parameter(name = 'GS11TdL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS11TdL1}',
                     lhablock = 'GS11TdL',
                     lhacode = [ 1 ])

GS11TdL2 = Parameter(name = 'GS11TdL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS11TdL2}',
                     lhablock = 'GS11TdL',
                     lhacode = [ 2 ])

GS11TdL3 = Parameter(name = 'GS11TdL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS11TdL3}',
                     lhablock = 'GS11TdL',
                     lhacode = [ 3 ])

GS11TdR1 = Parameter(name = 'GS11TdR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS11TdR1}',
                     lhablock = 'GS11TdR',
                     lhacode = [ 1 ])

GS11TdR2 = Parameter(name = 'GS11TdR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS11TdR2}',
                     lhablock = 'GS11TdR',
                     lhacode = [ 2 ])

GS11TdR3 = Parameter(name = 'GS11TdR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.156,
                     texname = '\\text{GS11TdR3}',
                     lhablock = 'GS11TdR',
                     lhacode = [ 3 ])

GS11tqbqL = Parameter(name = 'GS11tqbqL',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{GS11tqbqL}',
                      lhablock = 'GS11tqbqL',
                      lhacode = [ 1 ])

GS11tqbqR = Parameter(name = 'GS11tqbqR',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{GS11tqbqR}',
                      lhablock = 'GS11tqbqR',
                      lhacode = [ 1 ])

GS11XTL = Parameter(name = 'GS11XTL',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GS11XTL}',
                    lhablock = 'GS11XTL',
                    lhacode = [ 1 ])

GS11XTR = Parameter(name = 'GS11XTR',
                    nature = 'external',
                    type = 'real',
                    value = 0.155,
                    texname = '\\text{GS11XTR}',
                    lhablock = 'GS11XTR',
                    lhacode = [ 1 ])

GS11XuL1 = Parameter(name = 'GS11XuL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.161,
                     texname = '\\text{GS11XuL1}',
                     lhablock = 'GS11XuL',
                     lhacode = [ 1 ])

GS11XuL2 = Parameter(name = 'GS11XuL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.162,
                     texname = '\\text{GS11XuL2}',
                     lhablock = 'GS11XuL',
                     lhacode = [ 2 ])

GS11XuL3 = Parameter(name = 'GS11XuL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.163,
                     texname = '\\text{GS11XuL3}',
                     lhablock = 'GS11XuL',
                     lhacode = [ 3 ])

GS11XuR1 = Parameter(name = 'GS11XuR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.164,
                     texname = '\\text{GS11XuR1}',
                     lhablock = 'GS11XuR',
                     lhacode = [ 1 ])

GS11XuR2 = Parameter(name = 'GS11XuR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.165,
                     texname = '\\text{GS11XuR2}',
                     lhablock = 'GS11XuR',
                     lhacode = [ 2 ])

GS11XuR3 = Parameter(name = 'GS11XuR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.166,
                     texname = '\\text{GS11XuR3}',
                     lhablock = 'GS11XuR',
                     lhacode = [ 3 ])

GS11YdL1 = Parameter(name = 'GS11YdL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS11YdL1}',
                     lhablock = 'GS11YdL',
                     lhacode = [ 1 ])

GS11YdL2 = Parameter(name = 'GS11YdL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS11YdL2}',
                     lhablock = 'GS11YdL',
                     lhacode = [ 2 ])

GS11YdL3 = Parameter(name = 'GS11YdL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS11YdL3}',
                     lhablock = 'GS11YdL',
                     lhacode = [ 3 ])

GS11YdR1 = Parameter(name = 'GS11YdR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS11YdR1}',
                     lhablock = 'GS11YdR',
                     lhacode = [ 1 ])

GS11YdR2 = Parameter(name = 'GS11YdR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS11YdR2}',
                     lhablock = 'GS11YdR',
                     lhacode = [ 2 ])

GS11YdR3 = Parameter(name = 'GS11YdR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.156,
                     texname = '\\text{GS11YdR3}',
                     lhablock = 'GS11YdR',
                     lhacode = [ 3 ])

GS12XBL = Parameter(name = 'GS12XBL',
                    nature = 'external',
                    type = 'real',
                    value = 0.151,
                    texname = '\\text{GS12XBL}',
                    lhablock = 'GS12XBL',
                    lhacode = [ 1 ])

GS12XBR = Parameter(name = 'GS12XBR',
                    nature = 'external',
                    type = 'real',
                    value = 0.152,
                    texname = '\\text{GS12XBR}',
                    lhablock = 'GS12XBR',
                    lhacode = [ 1 ])

GS12XDL1 = Parameter(name = 'GS12XDL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS12XDL1}',
                     lhablock = 'GS12XDL',
                     lhacode = [ 1 ])

GS12XDL2 = Parameter(name = 'GS12XDL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS12XDL2}',
                     lhablock = 'GS12XDL',
                     lhacode = [ 2 ])

GS12XDL3 = Parameter(name = 'GS12XDL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS12XDL3}',
                     lhablock = 'GS12XDL',
                     lhacode = [ 3 ])

GS12XDR1 = Parameter(name = 'GS12XDR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS12XDR1}',
                     lhablock = 'GS12XDR',
                     lhacode = [ 1 ])

GS12XDR2 = Parameter(name = 'GS12XDR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS12XDR2}',
                     lhablock = 'GS12XDR',
                     lhacode = [ 2 ])

GS12XDR3 = Parameter(name = 'GS12XDR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS12XDR3}',
                     lhablock = 'GS12XDR',
                     lhacode = [ 3 ])

GS12YTL = Parameter(name = 'GS12YTL',
                    nature = 'external',
                    type = 'real',
                    value = 0.153,
                    texname = '\\text{GS12YTL}',
                    lhablock = 'GS12YTL',
                    lhacode = [ 1 ])

GS12YTR = Parameter(name = 'GS12YTR',
                    nature = 'external',
                    type = 'real',
                    value = 0.154,
                    texname = '\\text{GS12YTR}',
                    lhablock = 'GS12YTR',
                    lhacode = [ 1 ])

GS12YUL1 = Parameter(name = 'GS12YUL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS12YUL1}',
                     lhablock = 'GS12YUL',
                     lhacode = [ 1 ])

GS12YUL2 = Parameter(name = 'GS12YUL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS12YUL2}',
                     lhablock = 'GS12YUL',
                     lhacode = [ 2 ])

GS12YUL3 = Parameter(name = 'GS12YUL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS12YUL3}',
                     lhablock = 'GS12YUL',
                     lhacode = [ 3 ])

GS12YUR1 = Parameter(name = 'GS12YUR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS12YUR1}',
                     lhablock = 'GS12YUR',
                     lhacode = [ 1 ])

GS12YUR2 = Parameter(name = 'GS12YUR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS12YUR2}',
                     lhablock = 'GS12YUR',
                     lhacode = [ 2 ])

GS12YUR3 = Parameter(name = 'GS12YUR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS12YUR3}',
                     lhablock = 'GS12YUR',
                     lhacode = [ 3 ])

GS80B = Parameter(name = 'GS80B',
                  nature = 'external',
                  type = 'real',
                  value = 0.155,
                  texname = '\\text{GS80B}',
                  lhablock = 'GS80B',
                  lhacode = [ 1 ])

GS80BDL1 = Parameter(name = 'GS80BDL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.151,
                     texname = '\\text{GS80BDL1}',
                     lhablock = 'GS80BDL',
                     lhacode = [ 1 ])

GS80BDL2 = Parameter(name = 'GS80BDL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.152,
                     texname = '\\text{GS80BDL2}',
                     lhablock = 'GS80BDL',
                     lhacode = [ 2 ])

GS80BDL3 = Parameter(name = 'GS80BDL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.153,
                     texname = '\\text{GS80BDL3}',
                     lhablock = 'GS80BDL',
                     lhacode = [ 3 ])

GS80BDR1 = Parameter(name = 'GS80BDR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.154,
                     texname = '\\text{GS80BDR1}',
                     lhablock = 'GS80BDR',
                     lhacode = [ 1 ])

GS80BDR2 = Parameter(name = 'GS80BDR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.155,
                     texname = '\\text{GS80BDR2}',
                     lhablock = 'GS80BDR',
                     lhacode = [ 2 ])

GS80BDR3 = Parameter(name = 'GS80BDR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.156,
                     texname = '\\text{GS80BDR3}',
                     lhablock = 'GS80BDR',
                     lhacode = [ 3 ])

GS80D1x1 = Parameter(name = 'GS80D1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.101,
                     texname = '\\text{GS80D1x1}',
                     lhablock = 'GS80D',
                     lhacode = [ 1, 1 ])

GS80D2x2 = Parameter(name = 'GS80D2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.102,
                     texname = '\\text{GS80D2x2}',
                     lhablock = 'GS80D',
                     lhacode = [ 2, 2 ])

GS80D3x3 = Parameter(name = 'GS80D3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.103,
                     texname = '\\text{GS80D3x3}',
                     lhablock = 'GS80D',
                     lhacode = [ 3, 3 ])

GS80T = Parameter(name = 'GS80T',
                  nature = 'external',
                  type = 'real',
                  value = 0.154,
                  texname = '\\text{GS80T}',
                  lhablock = 'GS80T',
                  lhacode = [ 1 ])

GS80TUL1 = Parameter(name = 'GS80TUL1',
                     nature = 'external',
                     type = 'real',
                     value = 0.157,
                     texname = '\\text{GS80TUL1}',
                     lhablock = 'GS80TUL',
                     lhacode = [ 1 ])

GS80TUL2 = Parameter(name = 'GS80TUL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.158,
                     texname = '\\text{GS80TUL2}',
                     lhablock = 'GS80TUL',
                     lhacode = [ 2 ])

GS80TUL3 = Parameter(name = 'GS80TUL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.159,
                     texname = '\\text{GS80TUL3}',
                     lhablock = 'GS80TUL',
                     lhacode = [ 3 ])

GS80TUR1 = Parameter(name = 'GS80TUR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.16,
                     texname = '\\text{GS80TUR1}',
                     lhablock = 'GS80TUR',
                     lhacode = [ 1 ])

GS80TUR2 = Parameter(name = 'GS80TUR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.161,
                     texname = '\\text{GS80TUR2}',
                     lhablock = 'GS80TUR',
                     lhacode = [ 2 ])

GS80TUR3 = Parameter(name = 'GS80TUR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.162,
                     texname = '\\text{GS80TUR3}',
                     lhablock = 'GS80TUR',
                     lhacode = [ 3 ])

GS80U1x1 = Parameter(name = 'GS80U1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.101,
                     texname = '\\text{GS80U1x1}',
                     lhablock = 'GS80U',
                     lhacode = [ 1, 1 ])

GS80U2x2 = Parameter(name = 'GS80U2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.102,
                     texname = '\\text{GS80U2x2}',
                     lhablock = 'GS80U',
                     lhacode = [ 2, 2 ])

GS80U3x3 = Parameter(name = 'GS80U3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.103,
                     texname = '\\text{GS80U3x3}',
                     lhablock = 'GS80U',
                     lhacode = [ 3, 3 ])

GS80X = Parameter(name = 'GS80X',
                  nature = 'external',
                  type = 'real',
                  value = 0.153,
                  texname = '\\text{GS80X}',
                  lhablock = 'GS80X',
                  lhacode = [ 1 ])

GS80Y = Parameter(name = 'GS80Y',
                  nature = 'external',
                  type = 'real',
                  value = 0.156,
                  texname = '\\text{GS80Y}',
                  lhablock = 'GS80Y',
                  lhacode = [ 1 ])

includeWZW = Parameter(name = 'includeWZW',
                       nature = 'external',
                       type = 'real',
                       value = 1,
                       texname = '\\text{includeWZW}',
                       lhablock = 'includeWZW',
                       lhacode = [ 1 ])

K5Q10MZ = Parameter(name = 'K5Q10MZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.103,
                    texname = '\\text{K5Q10MZ}',
                    lhablock = 'K5Q10MZ',
                    lhacode = [ 1 ])

K5Q10Z = Parameter(name = 'K5Q10Z',
                   nature = 'external',
                   type = 'real',
                   value = 0.103,
                   texname = '\\text{K5Q10Z}',
                   lhablock = 'K5Q10Z',
                   lhacode = [ 1 ])

K5Q11Z = Parameter(name = 'K5Q11Z',
                   nature = 'external',
                   type = 'real',
                   value = 0.102,
                   texname = '\\text{K5Q11Z}',
                   lhablock = 'K5Q11Z',
                   lhacode = [ 1 ])

K5Q80MZ = Parameter(name = 'K5Q80MZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.103,
                    texname = '\\text{K5Q80MZ}',
                    lhablock = 'K5Q80MZ',
                    lhacode = [ 1 ])

K5Q80Z = Parameter(name = 'K5Q80Z',
                   nature = 'external',
                   type = 'real',
                   value = 0.103,
                   texname = '\\text{K5Q80Z}',
                   lhablock = 'K5Q80Z',
                   lhacode = [ 1 ])

K5Q81Z = Parameter(name = 'K5Q81Z',
                   nature = 'external',
                   type = 'real',
                   value = 0.102,
                   texname = '\\text{K5Q81Z}',
                   lhablock = 'K5Q81Z',
                   lhacode = [ 1 ])

KBLh1 = Parameter(name = 'KBLh1',
                  nature = 'external',
                  type = 'real',
                  value = 0.479336,
                  texname = '\\text{KBLh1}',
                  lhablock = 'KBLH',
                  lhacode = [ 1 ])

KBLh2 = Parameter(name = 'KBLh2',
                  nature = 'external',
                  type = 'real',
                  value = 0.479336,
                  texname = '\\text{KBLh2}',
                  lhablock = 'KBLH',
                  lhacode = [ 2 ])

KBLh3 = Parameter(name = 'KBLh3',
                  nature = 'external',
                  type = 'real',
                  value = 0.639117,
                  texname = '\\text{KBLh3}',
                  lhablock = 'KBLH',
                  lhacode = [ 3 ])

KBLw1 = Parameter(name = 'KBLw1',
                  nature = 'external',
                  type = 'real',
                  value = 0.120112,
                  texname = '\\text{KBLw1}',
                  lhablock = 'KBLW',
                  lhacode = [ 1 ])

KBLw2 = Parameter(name = 'KBLw2',
                  nature = 'external',
                  type = 'real',
                  value = 0.120112,
                  texname = '\\text{KBLw2}',
                  lhablock = 'KBLW',
                  lhacode = [ 2 ])

KBLw3 = Parameter(name = 'KBLw3',
                  nature = 'external',
                  type = 'real',
                  value = 0.160149,
                  texname = '\\text{KBLw3}',
                  lhablock = 'KBLW',
                  lhacode = [ 3 ])

KBLz1 = Parameter(name = 'KBLz1',
                  nature = 'external',
                  type = 'real',
                  value = 0.180284,
                  texname = '\\text{KBLz1}',
                  lhablock = 'KBLZ',
                  lhacode = [ 1 ])

KBLz2 = Parameter(name = 'KBLz2',
                  nature = 'external',
                  type = 'real',
                  value = 0.180284,
                  texname = '\\text{KBLz2}',
                  lhablock = 'KBLZ',
                  lhacode = [ 2 ])

KBLz3 = Parameter(name = 'KBLz3',
                  nature = 'external',
                  type = 'real',
                  value = 0.240379,
                  texname = '\\text{KBLz3}',
                  lhablock = 'KBLZ',
                  lhacode = [ 3 ])

KBRh1 = Parameter(name = 'KBRh1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRh1}',
                  lhablock = 'KBRH',
                  lhacode = [ 1 ])

KBRh2 = Parameter(name = 'KBRh2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRh2}',
                  lhablock = 'KBRH',
                  lhacode = [ 2 ])

KBRh3 = Parameter(name = 'KBRh3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRh3}',
                  lhablock = 'KBRH',
                  lhacode = [ 3 ])

KBRw1 = Parameter(name = 'KBRw1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRw1}',
                  lhablock = 'KBRW',
                  lhacode = [ 1 ])

KBRw2 = Parameter(name = 'KBRw2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRw2}',
                  lhablock = 'KBRW',
                  lhacode = [ 2 ])

KBRw3 = Parameter(name = 'KBRw3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRw3}',
                  lhablock = 'KBRW',
                  lhacode = [ 3 ])

KBRz1 = Parameter(name = 'KBRz1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRz1}',
                  lhablock = 'KBRZ',
                  lhacode = [ 1 ])

KBRz2 = Parameter(name = 'KBRz2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRz2}',
                  lhablock = 'KBRZ',
                  lhacode = [ 2 ])

KBRz3 = Parameter(name = 'KBRz3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KBRz3}',
                  lhablock = 'KBRZ',
                  lhacode = [ 3 ])

KP102G = Parameter(name = 'KP102G',
                   nature = 'external',
                   type = 'real',
                   value = 0.146,
                   texname = '\\text{KP102G}',
                   lhablock = 'KP102VV',
                   lhacode = [ 1 ])

KP102W = Parameter(name = 'KP102W',
                   nature = 'external',
                   type = 'real',
                   value = 0.147,
                   texname = '\\text{KP102W}',
                   lhablock = 'KP102VV',
                   lhacode = [ 2 ])

KP102ZZ = Parameter(name = 'KP102ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.148,
                    texname = '\\text{KP102ZZ}',
                    lhablock = 'KP102VV',
                    lhacode = [ 3 ])

KP102ZA = Parameter(name = 'KP102ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.149,
                    texname = '\\text{KP102ZA}',
                    lhablock = 'KP102VV',
                    lhacode = [ 4 ])

KP102AA = Parameter(name = 'KP102AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.15,
                    texname = '\\text{KP102AA}',
                    lhablock = 'KP102VV',
                    lhacode = [ 5 ])

KP103G = Parameter(name = 'KP103G',
                   nature = 'external',
                   type = 'real',
                   value = 0.146,
                   texname = '\\text{KP103G}',
                   lhablock = 'KP103VV',
                   lhacode = [ 1 ])

KP103W = Parameter(name = 'KP103W',
                   nature = 'external',
                   type = 'real',
                   value = 0.147,
                   texname = '\\text{KP103W}',
                   lhablock = 'KP103VV',
                   lhacode = [ 2 ])

KP103ZZ = Parameter(name = 'KP103ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.148,
                    texname = '\\text{KP103ZZ}',
                    lhablock = 'KP103VV',
                    lhacode = [ 3 ])

KP103ZA = Parameter(name = 'KP103ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.149,
                    texname = '\\text{KP103ZA}',
                    lhablock = 'KP103VV',
                    lhacode = [ 4 ])

KP103AA = Parameter(name = 'KP103AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.15,
                    texname = '\\text{KP103AA}',
                    lhablock = 'KP103VV',
                    lhacode = [ 5 ])

KP104G = Parameter(name = 'KP104G',
                   nature = 'external',
                   type = 'real',
                   value = 0.146,
                   texname = '\\text{KP104G}',
                   lhablock = 'KP104VV',
                   lhacode = [ 1 ])

KP104W = Parameter(name = 'KP104W',
                   nature = 'external',
                   type = 'real',
                   value = 0.147,
                   texname = '\\text{KP104W}',
                   lhablock = 'KP104VV',
                   lhacode = [ 2 ])

KP104ZZ = Parameter(name = 'KP104ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.148,
                    texname = '\\text{KP104ZZ}',
                    lhablock = 'KP104VV',
                    lhacode = [ 3 ])

KP104ZA = Parameter(name = 'KP104ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.149,
                    texname = '\\text{KP104ZA}',
                    lhablock = 'KP104VV',
                    lhacode = [ 4 ])

KP104AA = Parameter(name = 'KP104AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.15,
                    texname = '\\text{KP104AA}',
                    lhablock = 'KP104VV',
                    lhacode = [ 5 ])

KP105G = Parameter(name = 'KP105G',
                   nature = 'external',
                   type = 'real',
                   value = 0.146,
                   texname = '\\text{KP105G}',
                   lhablock = 'KP105VV',
                   lhacode = [ 1 ])

KP105W = Parameter(name = 'KP105W',
                   nature = 'external',
                   type = 'real',
                   value = 0.147,
                   texname = '\\text{KP105W}',
                   lhablock = 'KP105VV',
                   lhacode = [ 2 ])

KP105ZZ = Parameter(name = 'KP105ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.148,
                    texname = '\\text{KP105ZZ}',
                    lhablock = 'KP105VV',
                    lhacode = [ 3 ])

KP105ZA = Parameter(name = 'KP105ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.149,
                    texname = '\\text{KP105ZA}',
                    lhablock = 'KP105VV',
                    lhacode = [ 4 ])

KP105AA = Parameter(name = 'KP105AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.15,
                    texname = '\\text{KP105AA}',
                    lhablock = 'KP105VV',
                    lhacode = [ 5 ])

KP10G = Parameter(name = 'KP10G',
                  nature = 'external',
                  type = 'real',
                  value = 0.146,
                  texname = '\\text{KP10G}',
                  lhablock = 'KP10VV',
                  lhacode = [ 1 ])

KP10W = Parameter(name = 'KP10W',
                  nature = 'external',
                  type = 'real',
                  value = 0.147,
                  texname = '\\text{KP10W}',
                  lhablock = 'KP10VV',
                  lhacode = [ 2 ])

KP10ZZ = Parameter(name = 'KP10ZZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.148,
                   texname = '\\text{KP10ZZ}',
                   lhablock = 'KP10VV',
                   lhacode = [ 3 ])

KP10ZA = Parameter(name = 'KP10ZA',
                   nature = 'external',
                   type = 'real',
                   value = 0.149,
                   texname = '\\text{KP10ZA}',
                   lhablock = 'KP10VV',
                   lhacode = [ 4 ])

KP10AA = Parameter(name = 'KP10AA',
                   nature = 'external',
                   type = 'real',
                   value = 0.15,
                   texname = '\\text{KP10AA}',
                   lhablock = 'KP10VV',
                   lhacode = [ 5 ])

KP112WA = Parameter(name = 'KP112WA',
                    nature = 'external',
                    type = 'real',
                    value = 0.144,
                    texname = '\\text{KP112WA}',
                    lhablock = 'KP112VV',
                    lhacode = [ 1 ])

KP112WZ = Parameter(name = 'KP112WZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.145,
                    texname = '\\text{KP112WZ}',
                    lhablock = 'KP112VV',
                    lhacode = [ 2 ])

KP11WA = Parameter(name = 'KP11WA',
                   nature = 'external',
                   type = 'real',
                   value = 0.144,
                   texname = '\\text{KP11WA}',
                   lhablock = 'KP11VV',
                   lhacode = [ 1 ])

KP11WZ = Parameter(name = 'KP11WZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.145,
                   texname = '\\text{KP11WZ}',
                   lhablock = 'KP11VV',
                   lhacode = [ 2 ])

KP12W = Parameter(name = 'KP12W',
                  nature = 'external',
                  type = 'real',
                  value = 0.141,
                  texname = '\\text{KP12W}',
                  lhablock = 'KP12W',
                  lhacode = [ 1 ])

KP80G = Parameter(name = 'KP80G',
                  nature = 'external',
                  type = 'real',
                  value = 0.141,
                  texname = '\\text{KP80G}',
                  lhablock = 'KP80VV',
                  lhacode = [ 1 ])

KP80GZ = Parameter(name = 'KP80GZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.142,
                   texname = '\\text{KP80GZ}',
                   lhablock = 'KP80VV',
                   lhacode = [ 2 ])

KP80GA = Parameter(name = 'KP80GA',
                   nature = 'external',
                   type = 'real',
                   value = 0.143,
                   texname = '\\text{KP80GA}',
                   lhablock = 'KP80VV',
                   lhacode = [ 3 ])

KQ10Z = Parameter(name = 'KQ10Z',
                  nature = 'external',
                  type = 'real',
                  value = 0.102,
                  texname = '\\text{KQ10Z}',
                  lhablock = 'KQ10Z',
                  lhacode = [ 1 ])

KQ11Z = Parameter(name = 'KQ11Z',
                  nature = 'external',
                  type = 'real',
                  value = 0.101,
                  texname = '\\text{KQ11Z}',
                  lhablock = 'KQ11Z',
                  lhacode = [ 1 ])

KQ80Z = Parameter(name = 'KQ80Z',
                  nature = 'external',
                  type = 'real',
                  value = 0.102,
                  texname = '\\text{KQ80Z}',
                  lhablock = 'KQ80Z',
                  lhacode = [ 1 ])

KQ81Z = Parameter(name = 'KQ81Z',
                  nature = 'external',
                  type = 'real',
                  value = 0.101,
                  texname = '\\text{KQ81Z}',
                  lhablock = 'KQ81Z',
                  lhacode = [ 1 ])

KS102H1 = Parameter(name = 'KS102H1',
                    nature = 'external',
                    type = 'real',
                    value = 0.171,
                    texname = '\\text{KS102H1}',
                    lhablock = 'KS102H',
                    lhacode = [ 1 ])

KS102H2 = Parameter(name = 'KS102H2',
                    nature = 'external',
                    type = 'real',
                    value = 0.172,
                    texname = '\\text{KS102H2}',
                    lhablock = 'KS102H',
                    lhacode = [ 2 ])

KS102HH = Parameter(name = 'KS102HH',
                    nature = 'external',
                    type = 'real',
                    value = 0.173,
                    texname = '\\text{KS102HH}',
                    lhablock = 'KS102H',
                    lhacode = [ 3 ])

KS102HZ = Parameter(name = 'KS102HZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.174,
                    texname = '\\text{KS102HZ}',
                    lhablock = 'KS102H',
                    lhacode = [ 4 ])

KS102G = Parameter(name = 'KS102G',
                   nature = 'external',
                   type = 'real',
                   value = 0.141,
                   texname = '\\text{KS102G}',
                   lhablock = 'KS102VV',
                   lhacode = [ 1 ])

KS102W = Parameter(name = 'KS102W',
                   nature = 'external',
                   type = 'real',
                   value = 0.142,
                   texname = '\\text{KS102W}',
                   lhablock = 'KS102VV',
                   lhacode = [ 2 ])

KS102ZZ = Parameter(name = 'KS102ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.143,
                    texname = '\\text{KS102ZZ}',
                    lhablock = 'KS102VV',
                    lhacode = [ 3 ])

KS102ZA = Parameter(name = 'KS102ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.144,
                    texname = '\\text{KS102ZA}',
                    lhablock = 'KS102VV',
                    lhacode = [ 4 ])

KS102AA = Parameter(name = 'KS102AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.145,
                    texname = '\\text{KS102AA}',
                    lhablock = 'KS102VV',
                    lhacode = [ 5 ])

KS103H1 = Parameter(name = 'KS103H1',
                    nature = 'external',
                    type = 'real',
                    value = 0.171,
                    texname = '\\text{KS103H1}',
                    lhablock = 'KS103H',
                    lhacode = [ 1 ])

KS103H2 = Parameter(name = 'KS103H2',
                    nature = 'external',
                    type = 'real',
                    value = 0.172,
                    texname = '\\text{KS103H2}',
                    lhablock = 'KS103H',
                    lhacode = [ 2 ])

KS103HH = Parameter(name = 'KS103HH',
                    nature = 'external',
                    type = 'real',
                    value = 0.173,
                    texname = '\\text{KS103HH}',
                    lhablock = 'KS103H',
                    lhacode = [ 3 ])

KS103HZ = Parameter(name = 'KS103HZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.174,
                    texname = '\\text{KS103HZ}',
                    lhablock = 'KS103H',
                    lhacode = [ 4 ])

KS103G = Parameter(name = 'KS103G',
                   nature = 'external',
                   type = 'real',
                   value = 0.141,
                   texname = '\\text{KS103G}',
                   lhablock = 'KS103VV',
                   lhacode = [ 1 ])

KS103W = Parameter(name = 'KS103W',
                   nature = 'external',
                   type = 'real',
                   value = 0.142,
                   texname = '\\text{KS103W}',
                   lhablock = 'KS103VV',
                   lhacode = [ 2 ])

KS103ZZ = Parameter(name = 'KS103ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.143,
                    texname = '\\text{KS103ZZ}',
                    lhablock = 'KS103VV',
                    lhacode = [ 3 ])

KS103ZA = Parameter(name = 'KS103ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.144,
                    texname = '\\text{KS103ZA}',
                    lhablock = 'KS103VV',
                    lhacode = [ 4 ])

KS103AA = Parameter(name = 'KS103AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.145,
                    texname = '\\text{KS103AA}',
                    lhablock = 'KS103VV',
                    lhacode = [ 5 ])

KS104H1 = Parameter(name = 'KS104H1',
                    nature = 'external',
                    type = 'real',
                    value = 0.171,
                    texname = '\\text{KS104H1}',
                    lhablock = 'KS104H',
                    lhacode = [ 1 ])

KS104H2 = Parameter(name = 'KS104H2',
                    nature = 'external',
                    type = 'real',
                    value = 0.172,
                    texname = '\\text{KS104H2}',
                    lhablock = 'KS104H',
                    lhacode = [ 2 ])

KS104HH = Parameter(name = 'KS104HH',
                    nature = 'external',
                    type = 'real',
                    value = 0.173,
                    texname = '\\text{KS104HH}',
                    lhablock = 'KS104H',
                    lhacode = [ 3 ])

KS104HZ = Parameter(name = 'KS104HZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.174,
                    texname = '\\text{KS104HZ}',
                    lhablock = 'KS104H',
                    lhacode = [ 4 ])

KS104G = Parameter(name = 'KS104G',
                   nature = 'external',
                   type = 'real',
                   value = 0.141,
                   texname = '\\text{KS104G}',
                   lhablock = 'KS104VV',
                   lhacode = [ 1 ])

KS104W = Parameter(name = 'KS104W',
                   nature = 'external',
                   type = 'real',
                   value = 0.142,
                   texname = '\\text{KS104W}',
                   lhablock = 'KS104VV',
                   lhacode = [ 2 ])

KS104ZZ = Parameter(name = 'KS104ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.143,
                    texname = '\\text{KS104ZZ}',
                    lhablock = 'KS104VV',
                    lhacode = [ 3 ])

KS104ZA = Parameter(name = 'KS104ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.144,
                    texname = '\\text{KS104ZA}',
                    lhablock = 'KS104VV',
                    lhacode = [ 4 ])

KS104AA = Parameter(name = 'KS104AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.145,
                    texname = '\\text{KS104AA}',
                    lhablock = 'KS104VV',
                    lhacode = [ 5 ])

KS105H1 = Parameter(name = 'KS105H1',
                    nature = 'external',
                    type = 'real',
                    value = 0.171,
                    texname = '\\text{KS105H1}',
                    lhablock = 'KS105H',
                    lhacode = [ 1 ])

KS105H2 = Parameter(name = 'KS105H2',
                    nature = 'external',
                    type = 'real',
                    value = 0.172,
                    texname = '\\text{KS105H2}',
                    lhablock = 'KS105H',
                    lhacode = [ 2 ])

KS105HH = Parameter(name = 'KS105HH',
                    nature = 'external',
                    type = 'real',
                    value = 0.173,
                    texname = '\\text{KS105HH}',
                    lhablock = 'KS105H',
                    lhacode = [ 3 ])

KS105HZ = Parameter(name = 'KS105HZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.174,
                    texname = '\\text{KS105HZ}',
                    lhablock = 'KS105H',
                    lhacode = [ 4 ])

KS105G = Parameter(name = 'KS105G',
                   nature = 'external',
                   type = 'real',
                   value = 0.141,
                   texname = '\\text{KS105G}',
                   lhablock = 'KS105VV',
                   lhacode = [ 1 ])

KS105W = Parameter(name = 'KS105W',
                   nature = 'external',
                   type = 'real',
                   value = 0.142,
                   texname = '\\text{KS105W}',
                   lhablock = 'KS105VV',
                   lhacode = [ 2 ])

KS105ZZ = Parameter(name = 'KS105ZZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.143,
                    texname = '\\text{KS105ZZ}',
                    lhablock = 'KS105VV',
                    lhacode = [ 3 ])

KS105ZA = Parameter(name = 'KS105ZA',
                    nature = 'external',
                    type = 'real',
                    value = 0.144,
                    texname = '\\text{KS105ZA}',
                    lhablock = 'KS105VV',
                    lhacode = [ 4 ])

KS105AA = Parameter(name = 'KS105AA',
                    nature = 'external',
                    type = 'real',
                    value = 0.145,
                    texname = '\\text{KS105AA}',
                    lhablock = 'KS105VV',
                    lhacode = [ 5 ])

KS10H1 = Parameter(name = 'KS10H1',
                   nature = 'external',
                   type = 'real',
                   value = 0.171,
                   texname = '\\text{KS10H1}',
                   lhablock = 'KS10H',
                   lhacode = [ 1 ])

KS10H2 = Parameter(name = 'KS10H2',
                   nature = 'external',
                   type = 'real',
                   value = 0.172,
                   texname = '\\text{KS10H2}',
                   lhablock = 'KS10H',
                   lhacode = [ 2 ])

KS10HH = Parameter(name = 'KS10HH',
                   nature = 'external',
                   type = 'real',
                   value = 0.173,
                   texname = '\\text{KS10HH}',
                   lhablock = 'KS10H',
                   lhacode = [ 3 ])

KS10HZ = Parameter(name = 'KS10HZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.174,
                   texname = '\\text{KS10HZ}',
                   lhablock = 'KS10H',
                   lhacode = [ 4 ])

KS10G = Parameter(name = 'KS10G',
                  nature = 'external',
                  type = 'real',
                  value = 0.141,
                  texname = '\\text{KS10G}',
                  lhablock = 'KS10VV',
                  lhacode = [ 1 ])

KS10W = Parameter(name = 'KS10W',
                  nature = 'external',
                  type = 'real',
                  value = 0.142,
                  texname = '\\text{KS10W}',
                  lhablock = 'KS10VV',
                  lhacode = [ 2 ])

KS10ZZ = Parameter(name = 'KS10ZZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.143,
                   texname = '\\text{KS10ZZ}',
                   lhablock = 'KS10VV',
                   lhacode = [ 3 ])

KS10ZA = Parameter(name = 'KS10ZA',
                   nature = 'external',
                   type = 'real',
                   value = 0.144,
                   texname = '\\text{KS10ZA}',
                   lhablock = 'KS10VV',
                   lhacode = [ 4 ])

KS10AA = Parameter(name = 'KS10AA',
                   nature = 'external',
                   type = 'real',
                   value = 0.145,
                   texname = '\\text{KS10AA}',
                   lhablock = 'KS10VV',
                   lhacode = [ 5 ])

KS112H1 = Parameter(name = 'KS112H1',
                    nature = 'external',
                    type = 'real',
                    value = 0.171,
                    texname = '\\text{KS112H1}',
                    lhablock = 'KS112H',
                    lhacode = [ 1 ])

KS112H2 = Parameter(name = 'KS112H2',
                    nature = 'external',
                    type = 'real',
                    value = 0.172,
                    texname = '\\text{KS112H2}',
                    lhablock = 'KS112H',
                    lhacode = [ 2 ])

KS112HW = Parameter(name = 'KS112HW',
                    nature = 'external',
                    type = 'real',
                    value = 0.174,
                    texname = '\\text{KS112HW}',
                    lhablock = 'KS112H',
                    lhacode = [ 3 ])

KS112WA = Parameter(name = 'KS112WA',
                    nature = 'external',
                    type = 'real',
                    value = 0.142,
                    texname = '\\text{KS112WA}',
                    lhablock = 'KS112VV',
                    lhacode = [ 1 ])

KS112WZ = Parameter(name = 'KS112WZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.143,
                    texname = '\\text{KS112WZ}',
                    lhablock = 'KS112VV',
                    lhacode = [ 2 ])

KS11H1 = Parameter(name = 'KS11H1',
                   nature = 'external',
                   type = 'real',
                   value = 0.171,
                   texname = '\\text{KS11H1}',
                   lhablock = 'KS11H',
                   lhacode = [ 1 ])

KS11H2 = Parameter(name = 'KS11H2',
                   nature = 'external',
                   type = 'real',
                   value = 0.172,
                   texname = '\\text{KS11H2}',
                   lhablock = 'KS11H',
                   lhacode = [ 2 ])

KS11HW = Parameter(name = 'KS11HW',
                   nature = 'external',
                   type = 'real',
                   value = 0.174,
                   texname = '\\text{KS11HW}',
                   lhablock = 'KS11H',
                   lhacode = [ 3 ])

KS11WA = Parameter(name = 'KS11WA',
                   nature = 'external',
                   type = 'real',
                   value = 0.142,
                   texname = '\\text{KS11WA}',
                   lhablock = 'KS11VV',
                   lhacode = [ 1 ])

KS11WZ = Parameter(name = 'KS11WZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.143,
                   texname = '\\text{KS11WZ}',
                   lhablock = 'KS11VV',
                   lhacode = [ 2 ])

KS12H1 = Parameter(name = 'KS12H1',
                   nature = 'external',
                   type = 'real',
                   value = 0.171,
                   texname = '\\text{KS12H1}',
                   lhablock = 'KS12H',
                   lhacode = [ 1 ])

KS12H2 = Parameter(name = 'KS12H2',
                   nature = 'external',
                   type = 'real',
                   value = 0.172,
                   texname = '\\text{KS12H2}',
                   lhablock = 'KS12H',
                   lhacode = [ 2 ])

KS12HH = Parameter(name = 'KS12HH',
                   nature = 'external',
                   type = 'real',
                   value = 0.173,
                   texname = '\\text{KS12HH}',
                   lhablock = 'KS12H',
                   lhacode = [ 3 ])

KS12W = Parameter(name = 'KS12W',
                  nature = 'external',
                  type = 'real',
                  value = 0.141,
                  texname = '\\text{KS12W}',
                  lhablock = 'KS12W',
                  lhacode = [ 1 ])

KS323H1 = Parameter(name = 'KS323H1',
                    nature = 'external',
                    type = 'real',
                    value = 0.171,
                    texname = '\\text{KS323H1}',
                    lhablock = 'KS323H',
                    lhacode = [ 1 ])

KS323H2 = Parameter(name = 'KS323H2',
                    nature = 'external',
                    type = 'real',
                    value = 0.172,
                    texname = '\\text{KS323H2}',
                    lhablock = 'KS323H',
                    lhacode = [ 2 ])

KS323HH = Parameter(name = 'KS323HH',
                    nature = 'external',
                    type = 'real',
                    value = 0.173,
                    texname = '\\text{KS323HH}',
                    lhablock = 'KS323H',
                    lhacode = [ 3 ])

KS80H1 = Parameter(name = 'KS80H1',
                   nature = 'external',
                   type = 'real',
                   value = 0.171,
                   texname = '\\text{KS80H1}',
                   lhablock = 'KS80H',
                   lhacode = [ 1 ])

KS80H2 = Parameter(name = 'KS80H2',
                   nature = 'external',
                   type = 'real',
                   value = 0.172,
                   texname = '\\text{KS80H2}',
                   lhablock = 'KS80H',
                   lhacode = [ 2 ])

KS80HH = Parameter(name = 'KS80HH',
                   nature = 'external',
                   type = 'real',
                   value = 0.173,
                   texname = '\\text{KS80HH}',
                   lhablock = 'KS80H',
                   lhacode = [ 3 ])

KS80G = Parameter(name = 'KS80G',
                  nature = 'external',
                  type = 'real',
                  value = 0.141,
                  texname = '\\text{KS80G}',
                  lhablock = 'KS80VV',
                  lhacode = [ 1 ])

KS80GZ = Parameter(name = 'KS80GZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.142,
                   texname = '\\text{KS80GZ}',
                   lhablock = 'KS80VV',
                   lhacode = [ 2 ])

KS80GA = Parameter(name = 'KS80GA',
                   nature = 'external',
                   type = 'real',
                   value = 0.143,
                   texname = '\\text{KS80GA}',
                   lhablock = 'KS80VV',
                   lhacode = [ 3 ])

KT2Lh1 = Parameter(name = 'KT2Lh1',
                   nature = 'external',
                   type = 'real',
                   value = 0.479336,
                   texname = '\\text{KT2Lh1}',
                   lhablock = 'KT2LH',
                   lhacode = [ 1 ])

KT2Lh2 = Parameter(name = 'KT2Lh2',
                   nature = 'external',
                   type = 'real',
                   value = 0.479336,
                   texname = '\\text{KT2Lh2}',
                   lhablock = 'KT2LH',
                   lhacode = [ 2 ])

KT2Lh3 = Parameter(name = 'KT2Lh3',
                   nature = 'external',
                   type = 'real',
                   value = 0.639117,
                   texname = '\\text{KT2Lh3}',
                   lhablock = 'KT2LH',
                   lhacode = [ 3 ])

KT2Lw1 = Parameter(name = 'KT2Lw1',
                   nature = 'external',
                   type = 'real',
                   value = 0.120112,
                   texname = '\\text{KT2Lw1}',
                   lhablock = 'KT2LW',
                   lhacode = [ 1 ])

KT2Lw2 = Parameter(name = 'KT2Lw2',
                   nature = 'external',
                   type = 'real',
                   value = 0.120112,
                   texname = '\\text{KT2Lw2}',
                   lhablock = 'KT2LW',
                   lhacode = [ 2 ])

KT2Lw3 = Parameter(name = 'KT2Lw3',
                   nature = 'external',
                   type = 'real',
                   value = 0.160149,
                   texname = '\\text{KT2Lw3}',
                   lhablock = 'KT2LW',
                   lhacode = [ 3 ])

KT2Lz1 = Parameter(name = 'KT2Lz1',
                   nature = 'external',
                   type = 'real',
                   value = 0.180284,
                   texname = '\\text{KT2Lz1}',
                   lhablock = 'KT2LZ',
                   lhacode = [ 1 ])

KT2Lz2 = Parameter(name = 'KT2Lz2',
                   nature = 'external',
                   type = 'real',
                   value = 0.180284,
                   texname = '\\text{KT2Lz2}',
                   lhablock = 'KT2LZ',
                   lhacode = [ 2 ])

KT2Lz3 = Parameter(name = 'KT2Lz3',
                   nature = 'external',
                   type = 'real',
                   value = 0.240379,
                   texname = '\\text{KT2Lz3}',
                   lhablock = 'KT2LZ',
                   lhacode = [ 3 ])

KT2Rh1 = Parameter(name = 'KT2Rh1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rh1}',
                   lhablock = 'KT2RH',
                   lhacode = [ 1 ])

KT2Rh2 = Parameter(name = 'KT2Rh2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rh2}',
                   lhablock = 'KT2RH',
                   lhacode = [ 2 ])

KT2Rh3 = Parameter(name = 'KT2Rh3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rh3}',
                   lhablock = 'KT2RH',
                   lhacode = [ 3 ])

KT2Rw1 = Parameter(name = 'KT2Rw1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rw1}',
                   lhablock = 'KT2RW',
                   lhacode = [ 1 ])

KT2Rw2 = Parameter(name = 'KT2Rw2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rw2}',
                   lhablock = 'KT2RW',
                   lhacode = [ 2 ])

KT2Rw3 = Parameter(name = 'KT2Rw3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rw3}',
                   lhablock = 'KT2RW',
                   lhacode = [ 3 ])

KT2Rz1 = Parameter(name = 'KT2Rz1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rz1}',
                   lhablock = 'KT2RZ',
                   lhacode = [ 1 ])

KT2Rz2 = Parameter(name = 'KT2Rz2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rz2}',
                   lhablock = 'KT2RZ',
                   lhacode = [ 2 ])

KT2Rz3 = Parameter(name = 'KT2Rz3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT2Rz3}',
                   lhablock = 'KT2RZ',
                   lhacode = [ 3 ])

KT3Lh1 = Parameter(name = 'KT3Lh1',
                   nature = 'external',
                   type = 'real',
                   value = 0.479336,
                   texname = '\\text{KT3Lh1}',
                   lhablock = 'KT3LH',
                   lhacode = [ 1 ])

KT3Lh2 = Parameter(name = 'KT3Lh2',
                   nature = 'external',
                   type = 'real',
                   value = 0.479336,
                   texname = '\\text{KT3Lh2}',
                   lhablock = 'KT3LH',
                   lhacode = [ 2 ])

KT3Lh3 = Parameter(name = 'KT3Lh3',
                   nature = 'external',
                   type = 'real',
                   value = 0.639117,
                   texname = '\\text{KT3Lh3}',
                   lhablock = 'KT3LH',
                   lhacode = [ 3 ])

KT3Lw1 = Parameter(name = 'KT3Lw1',
                   nature = 'external',
                   type = 'real',
                   value = 0.120112,
                   texname = '\\text{KT3Lw1}',
                   lhablock = 'KT3LW',
                   lhacode = [ 1 ])

KT3Lw2 = Parameter(name = 'KT3Lw2',
                   nature = 'external',
                   type = 'real',
                   value = 0.120112,
                   texname = '\\text{KT3Lw2}',
                   lhablock = 'KT3LW',
                   lhacode = [ 2 ])

KT3Lw3 = Parameter(name = 'KT3Lw3',
                   nature = 'external',
                   type = 'real',
                   value = 0.160149,
                   texname = '\\text{KT3Lw3}',
                   lhablock = 'KT3LW',
                   lhacode = [ 3 ])

KT3Lz1 = Parameter(name = 'KT3Lz1',
                   nature = 'external',
                   type = 'real',
                   value = 0.180284,
                   texname = '\\text{KT3Lz1}',
                   lhablock = 'KT3LZ',
                   lhacode = [ 1 ])

KT3Lz2 = Parameter(name = 'KT3Lz2',
                   nature = 'external',
                   type = 'real',
                   value = 0.180284,
                   texname = '\\text{KT3Lz2}',
                   lhablock = 'KT3LZ',
                   lhacode = [ 2 ])

KT3Lz3 = Parameter(name = 'KT3Lz3',
                   nature = 'external',
                   type = 'real',
                   value = 0.240379,
                   texname = '\\text{KT3Lz3}',
                   lhablock = 'KT3LZ',
                   lhacode = [ 3 ])

KT3Rh1 = Parameter(name = 'KT3Rh1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rh1}',
                   lhablock = 'KT3RH',
                   lhacode = [ 1 ])

KT3Rh2 = Parameter(name = 'KT3Rh2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rh2}',
                   lhablock = 'KT3RH',
                   lhacode = [ 2 ])

KT3Rh3 = Parameter(name = 'KT3Rh3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rh3}',
                   lhablock = 'KT3RH',
                   lhacode = [ 3 ])

KT3Rw1 = Parameter(name = 'KT3Rw1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rw1}',
                   lhablock = 'KT3RW',
                   lhacode = [ 1 ])

KT3Rw2 = Parameter(name = 'KT3Rw2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rw2}',
                   lhablock = 'KT3RW',
                   lhacode = [ 2 ])

KT3Rw3 = Parameter(name = 'KT3Rw3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rw3}',
                   lhablock = 'KT3RW',
                   lhacode = [ 3 ])

KT3Rz1 = Parameter(name = 'KT3Rz1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rz1}',
                   lhablock = 'KT3RZ',
                   lhacode = [ 1 ])

KT3Rz2 = Parameter(name = 'KT3Rz2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rz2}',
                   lhablock = 'KT3RZ',
                   lhacode = [ 2 ])

KT3Rz3 = Parameter(name = 'KT3Rz3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KT3Rz3}',
                   lhablock = 'KT3RZ',
                   lhacode = [ 3 ])

KTLh1 = Parameter(name = 'KTLh1',
                  nature = 'external',
                  type = 'real',
                  value = 0.479336,
                  texname = '\\text{KTLh1}',
                  lhablock = 'KTLH',
                  lhacode = [ 1 ])

KTLh2 = Parameter(name = 'KTLh2',
                  nature = 'external',
                  type = 'real',
                  value = 0.479336,
                  texname = '\\text{KTLh2}',
                  lhablock = 'KTLH',
                  lhacode = [ 2 ])

KTLh3 = Parameter(name = 'KTLh3',
                  nature = 'external',
                  type = 'real',
                  value = 0.639117,
                  texname = '\\text{KTLh3}',
                  lhablock = 'KTLH',
                  lhacode = [ 3 ])

KTLw1 = Parameter(name = 'KTLw1',
                  nature = 'external',
                  type = 'real',
                  value = 0.120112,
                  texname = '\\text{KTLw1}',
                  lhablock = 'KTLW',
                  lhacode = [ 1 ])

KTLw2 = Parameter(name = 'KTLw2',
                  nature = 'external',
                  type = 'real',
                  value = 0.120112,
                  texname = '\\text{KTLw2}',
                  lhablock = 'KTLW',
                  lhacode = [ 2 ])

KTLw3 = Parameter(name = 'KTLw3',
                  nature = 'external',
                  type = 'real',
                  value = 0.160149,
                  texname = '\\text{KTLw3}',
                  lhablock = 'KTLW',
                  lhacode = [ 3 ])

KTLz1 = Parameter(name = 'KTLz1',
                  nature = 'external',
                  type = 'real',
                  value = 0.180284,
                  texname = '\\text{KTLz1}',
                  lhablock = 'KTLZ',
                  lhacode = [ 1 ])

KTLz2 = Parameter(name = 'KTLz2',
                  nature = 'external',
                  type = 'real',
                  value = 0.180284,
                  texname = '\\text{KTLz2}',
                  lhablock = 'KTLZ',
                  lhacode = [ 2 ])

KTLz3 = Parameter(name = 'KTLz3',
                  nature = 'external',
                  type = 'real',
                  value = 0.240379,
                  texname = '\\text{KTLz3}',
                  lhablock = 'KTLZ',
                  lhacode = [ 3 ])

KTRh1 = Parameter(name = 'KTRh1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRh1}',
                  lhablock = 'KTRH',
                  lhacode = [ 1 ])

KTRh2 = Parameter(name = 'KTRh2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRh2}',
                  lhablock = 'KTRH',
                  lhacode = [ 2 ])

KTRh3 = Parameter(name = 'KTRh3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRh3}',
                  lhablock = 'KTRH',
                  lhacode = [ 3 ])

KTRw1 = Parameter(name = 'KTRw1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRw1}',
                  lhablock = 'KTRW',
                  lhacode = [ 1 ])

KTRw2 = Parameter(name = 'KTRw2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRw2}',
                  lhablock = 'KTRW',
                  lhacode = [ 2 ])

KTRw3 = Parameter(name = 'KTRw3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRw3}',
                  lhablock = 'KTRW',
                  lhacode = [ 3 ])

KTRz1 = Parameter(name = 'KTRz1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRz1}',
                  lhablock = 'KTRZ',
                  lhacode = [ 1 ])

KTRz2 = Parameter(name = 'KTRz2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRz2}',
                  lhablock = 'KTRZ',
                  lhacode = [ 2 ])

KTRz3 = Parameter(name = 'KTRz3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KTRz3}',
                  lhablock = 'KTRZ',
                  lhacode = [ 3 ])

KXL1 = Parameter(name = 'KXL1',
                 nature = 'external',
                 type = 'real',
                 value = 0.300279,
                 texname = '\\text{KXL1}',
                 lhablock = 'KXLW',
                 lhacode = [ 1 ])

KXL2 = Parameter(name = 'KXL2',
                 nature = 'external',
                 type = 'real',
                 value = 0.300279,
                 texname = '\\text{KXL2}',
                 lhablock = 'KXLW',
                 lhacode = [ 2 ])

KXL3 = Parameter(name = 'KXL3',
                 nature = 'external',
                 type = 'real',
                 value = 0.400379,
                 texname = '\\text{KXL3}',
                 lhablock = 'KXLW',
                 lhacode = [ 3 ])

KXR1 = Parameter(name = 'KXR1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{KXR1}',
                 lhablock = 'KXRW',
                 lhacode = [ 1 ])

KXR2 = Parameter(name = 'KXR2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{KXR2}',
                 lhablock = 'KXRW',
                 lhacode = [ 2 ])

KXR3 = Parameter(name = 'KXR3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{KXR3}',
                 lhablock = 'KXRW',
                 lhacode = [ 3 ])

KYL1 = Parameter(name = 'KYL1',
                 nature = 'external',
                 type = 'real',
                 value = 0.300279,
                 texname = '\\text{KYL1}',
                 lhablock = 'KYLW',
                 lhacode = [ 1 ])

KYL2 = Parameter(name = 'KYL2',
                 nature = 'external',
                 type = 'real',
                 value = 0.300279,
                 texname = '\\text{KYL2}',
                 lhablock = 'KYLW',
                 lhacode = [ 2 ])

KYL3 = Parameter(name = 'KYL3',
                 nature = 'external',
                 type = 'real',
                 value = 0.400379,
                 texname = '\\text{KYL3}',
                 lhablock = 'KYLW',
                 lhacode = [ 3 ])

KYR1 = Parameter(name = 'KYR1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{KYR1}',
                 lhablock = 'KYRW',
                 lhacode = [ 1 ])

KYR2 = Parameter(name = 'KYR2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{KYR2}',
                 lhablock = 'KYRW',
                 lhacode = [ 2 ])

KYR3 = Parameter(name = 'KYR3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{KYR3}',
                 lhablock = 'KYRW',
                 lhacode = [ 3 ])

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

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

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

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MX = Parameter(name = 'MX',
               nature = 'external',
               type = 'real',
               value = 600.1,
               texname = '\\text{MX}',
               lhablock = 'MASS',
               lhacode = [ 6000005 ])

MTP = Parameter(name = 'MTP',
                nature = 'external',
                type = 'real',
                value = 600.2,
                texname = '\\text{MTP}',
                lhablock = 'MASS',
                lhacode = [ 6000006 ])

MBP = Parameter(name = 'MBP',
                nature = 'external',
                type = 'real',
                value = 600.3,
                texname = '\\text{MBP}',
                lhablock = 'MASS',
                lhacode = [ 6000007 ])

MY = Parameter(name = 'MY',
               nature = 'external',
               type = 'real',
               value = 600.4,
               texname = '\\text{MY}',
               lhablock = 'MASS',
               lhacode = [ 6000008 ])

MTP2 = Parameter(name = 'MTP2',
                 nature = 'external',
                 type = 'real',
                 value = 600.5,
                 texname = '\\text{MTP2}',
                 lhablock = 'MASS',
                 lhacode = [ 6002006 ])

MTP3 = Parameter(name = 'MTP3',
                 nature = 'external',
                 type = 'real',
                 value = 600.6,
                 texname = '\\text{MTP3}',
                 lhablock = 'MASS',
                 lhacode = [ 6003006 ])

MS10 = Parameter(name = 'MS10',
                 nature = 'external',
                 type = 'real',
                 value = 500.1,
                 texname = '\\text{MS10}',
                 lhablock = 'MASS',
                 lhacode = [ 6100001 ])

MS102 = Parameter(name = 'MS102',
                  nature = 'external',
                  type = 'real',
                  value = 510,
                  texname = '\\text{MS102}',
                  lhablock = 'MASS',
                  lhacode = [ 6102001 ])

MS103 = Parameter(name = 'MS103',
                  nature = 'external',
                  type = 'real',
                  value = 511,
                  texname = '\\text{MS103}',
                  lhablock = 'MASS',
                  lhacode = [ 6103001 ])

MS104 = Parameter(name = 'MS104',
                  nature = 'external',
                  type = 'real',
                  value = 512,
                  texname = '\\text{MS104}',
                  lhablock = 'MASS',
                  lhacode = [ 6104001 ])

MS105 = Parameter(name = 'MS105',
                  nature = 'external',
                  type = 'real',
                  value = 513,
                  texname = '\\text{MS105}',
                  lhablock = 'MASS',
                  lhacode = [ 6105001 ])

MS11 = Parameter(name = 'MS11',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{MS11}',
                 lhablock = 'MASS',
                 lhacode = [ 6100002 ])

MS112 = Parameter(name = 'MS112',
                  nature = 'external',
                  type = 'real',
                  value = 501,
                  texname = '\\text{MS112}',
                  lhablock = 'MASS',
                  lhacode = [ 6102002 ])

MS12 = Parameter(name = 'MS12',
                 nature = 'external',
                 type = 'real',
                 value = 500.5,
                 texname = '\\text{MS12}',
                 lhablock = 'MASS',
                 lhacode = [ 6100003 ])

MQ11 = Parameter(name = 'MQ11',
                 nature = 'external',
                 type = 'real',
                 value = 1003,
                 texname = '\\text{MQ11}',
                 lhablock = 'MASS',
                 lhacode = [ 6000011 ])

MQ10 = Parameter(name = 'MQ10',
                 nature = 'external',
                 type = 'real',
                 value = 1002,
                 texname = '\\text{MQ10}',
                 lhablock = 'MASS',
                 lhacode = [ 6000010 ])

MQ10M = Parameter(name = 'MQ10M',
                  nature = 'external',
                  type = 'real',
                  value = 1001,
                  texname = '\\text{MQ10M}',
                  lhablock = 'MASS',
                  lhacode = [ 6001010 ])

MQ81 = Parameter(name = 'MQ81',
                 nature = 'external',
                 type = 'real',
                 value = 1013,
                 texname = '\\text{MQ81}',
                 lhablock = 'MASS',
                 lhacode = [ 6000081 ])

MQ80 = Parameter(name = 'MQ80',
                 nature = 'external',
                 type = 'real',
                 value = 1012,
                 texname = '\\text{MQ80}',
                 lhablock = 'MASS',
                 lhacode = [ 6000080 ])

MQ80M = Parameter(name = 'MQ80M',
                  nature = 'external',
                  type = 'real',
                  value = 1011,
                  texname = '\\text{MQ80M}',
                  lhablock = 'MASS',
                  lhacode = [ 6001080 ])

MS80 = Parameter(name = 'MS80',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MS80}',
                 lhablock = 'MASS',
                 lhacode = [ 6108000 ])

MS323 = Parameter(name = 'MS323',
                  nature = 'external',
                  type = 'real',
                  value = 900,
                  texname = '\\text{MS323}',
                  lhablock = 'MASS',
                  lhacode = [ 6100300 ])

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

WX = Parameter(name = 'WX',
               nature = 'external',
               type = 'real',
               value = 5.,
               texname = '\\text{WX}',
               lhablock = 'DECAY',
               lhacode = [ 6000005 ])

WTP = Parameter(name = 'WTP',
                nature = 'external',
                type = 'real',
                value = 5.,
                texname = '\\text{WTP}',
                lhablock = 'DECAY',
                lhacode = [ 6000006 ])

WBP = Parameter(name = 'WBP',
                nature = 'external',
                type = 'real',
                value = 5.,
                texname = '\\text{WBP}',
                lhablock = 'DECAY',
                lhacode = [ 6000007 ])

WY = Parameter(name = 'WY',
               nature = 'external',
               type = 'real',
               value = 5.,
               texname = '\\text{WY}',
               lhablock = 'DECAY',
               lhacode = [ 6000008 ])

WTP2 = Parameter(name = 'WTP2',
                 nature = 'external',
                 type = 'real',
                 value = 5.,
                 texname = '\\text{WTP2}',
                 lhablock = 'DECAY',
                 lhacode = [ 6002006 ])

WTP3 = Parameter(name = 'WTP3',
                 nature = 'external',
                 type = 'real',
                 value = 5.,
                 texname = '\\text{WTP3}',
                 lhablock = 'DECAY',
                 lhacode = [ 6003006 ])

WS10 = Parameter(name = 'WS10',
                 nature = 'external',
                 type = 'real',
                 value = 1.1,
                 texname = '\\text{WS10}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100001 ])

WS102 = Parameter(name = 'WS102',
                  nature = 'external',
                  type = 'real',
                  value = 1.1,
                  texname = '\\text{WS102}',
                  lhablock = 'DECAY',
                  lhacode = [ 6102001 ])

WS103 = Parameter(name = 'WS103',
                  nature = 'external',
                  type = 'real',
                  value = 1.1,
                  texname = '\\text{WS103}',
                  lhablock = 'DECAY',
                  lhacode = [ 6103001 ])

WS104 = Parameter(name = 'WS104',
                  nature = 'external',
                  type = 'real',
                  value = 1.1,
                  texname = '\\text{WS104}',
                  lhablock = 'DECAY',
                  lhacode = [ 6104001 ])

WS105 = Parameter(name = 'WS105',
                  nature = 'external',
                  type = 'real',
                  value = 1.1,
                  texname = '\\text{WS105}',
                  lhablock = 'DECAY',
                  lhacode = [ 6105001 ])

WS11 = Parameter(name = 'WS11',
                 nature = 'external',
                 type = 'real',
                 value = 15,
                 texname = '\\text{WS11}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100002 ])

WS112 = Parameter(name = 'WS112',
                  nature = 'external',
                  type = 'real',
                  value = 15,
                  texname = '\\text{WS112}',
                  lhablock = 'DECAY',
                  lhacode = [ 6102002 ])

WS12 = Parameter(name = 'WS12',
                 nature = 'external',
                 type = 'real',
                 value = 1.1,
                 texname = '\\text{WS12}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100003 ])

WQ11 = Parameter(name = 'WQ11',
                 nature = 'external',
                 type = 'real',
                 value = 5.,
                 texname = '\\text{WQ11}',
                 lhablock = 'DECAY',
                 lhacode = [ 6000011 ])

WQ10 = Parameter(name = 'WQ10',
                 nature = 'external',
                 type = 'real',
                 value = 5.,
                 texname = '\\text{WQ10}',
                 lhablock = 'DECAY',
                 lhacode = [ 6000010 ])

WQ10M = Parameter(name = 'WQ10M',
                  nature = 'external',
                  type = 'real',
                  value = 5.,
                  texname = '\\text{WQ10M}',
                  lhablock = 'DECAY',
                  lhacode = [ 6001010 ])

WQ81 = Parameter(name = 'WQ81',
                 nature = 'external',
                 type = 'real',
                 value = 5.,
                 texname = '\\text{WQ81}',
                 lhablock = 'DECAY',
                 lhacode = [ 6000081 ])

WQ80 = Parameter(name = 'WQ80',
                 nature = 'external',
                 type = 'real',
                 value = 5.,
                 texname = '\\text{WQ80}',
                 lhablock = 'DECAY',
                 lhacode = [ 6000080 ])

WQ80M = Parameter(name = 'WQ80M',
                  nature = 'external',
                  type = 'real',
                  value = 5.,
                  texname = '\\text{WQ80M}',
                  lhablock = 'DECAY',
                  lhacode = [ 6001080 ])

WS80 = Parameter(name = 'WS80',
                 nature = 'external',
                 type = 'real',
                 value = 1.1,
                 texname = '\\text{WS80}',
                 lhablock = 'DECAY',
                 lhacode = [ 6108000 ])

WS323 = Parameter(name = 'WS323',
                  nature = 'external',
                  type = 'real',
                  value = 1.1,
                  texname = '\\text{WS323}',
                  lhablock = 'DECAY',
                  lhacode = [ 6100300 ])

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

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

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

