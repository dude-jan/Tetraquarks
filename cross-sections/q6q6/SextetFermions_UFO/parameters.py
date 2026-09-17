# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 12.3.0 for Microsoft Windows (64-bit) (May 10, 2021)
# Date: Thu 11 Dec 2025 10:52:06



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
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
                  value = 0,
                  texname = '\\text{KBLh1}',
                  lhablock = 'KBLH',
                  lhacode = [ 1 ])

KBLh2 = Parameter(name = 'KBLh2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLh2}',
                  lhablock = 'KBLH',
                  lhacode = [ 2 ])

KBLh3 = Parameter(name = 'KBLh3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLh3}',
                  lhablock = 'KBLH',
                  lhacode = [ 3 ])

KBLw1 = Parameter(name = 'KBLw1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLw1}',
                  lhablock = 'KBLW',
                  lhacode = [ 1 ])

KBLw2 = Parameter(name = 'KBLw2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLw2}',
                  lhablock = 'KBLW',
                  lhacode = [ 2 ])

KBLw3 = Parameter(name = 'KBLw3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLw3}',
                  lhablock = 'KBLW',
                  lhacode = [ 3 ])

KBLz1 = Parameter(name = 'KBLz1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLz1}',
                  lhablock = 'KBLZ',
                  lhacode = [ 1 ])

KBLz2 = Parameter(name = 'KBLz2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLz2}',
                  lhablock = 'KBLZ',
                  lhacode = [ 2 ])

KBLz3 = Parameter(name = 'KBLz3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBLz3}',
                  lhablock = 'KBLZ',
                  lhacode = [ 3 ])

KBRh1 = Parameter(name = 'KBRh1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRh1}',
                  lhablock = 'KBRH',
                  lhacode = [ 1 ])

KBRh2 = Parameter(name = 'KBRh2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRh2}',
                  lhablock = 'KBRH',
                  lhacode = [ 2 ])

KBRh3 = Parameter(name = 'KBRh3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRh3}',
                  lhablock = 'KBRH',
                  lhacode = [ 3 ])

KBRw1 = Parameter(name = 'KBRw1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRw1}',
                  lhablock = 'KBRW',
                  lhacode = [ 1 ])

KBRw2 = Parameter(name = 'KBRw2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRw2}',
                  lhablock = 'KBRW',
                  lhacode = [ 2 ])

KBRw3 = Parameter(name = 'KBRw3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRw3}',
                  lhablock = 'KBRW',
                  lhacode = [ 3 ])

KBRz1 = Parameter(name = 'KBRz1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRz1}',
                  lhablock = 'KBRZ',
                  lhacode = [ 1 ])

KBRz2 = Parameter(name = 'KBRz2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRz2}',
                  lhablock = 'KBRZ',
                  lhacode = [ 2 ])

KBRz3 = Parameter(name = 'KBRz3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KBRz3}',
                  lhablock = 'KBRZ',
                  lhacode = [ 3 ])

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

KQ613p6q1 = Parameter(name = 'KQ613p6q1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ613p6q1}',
                      lhablock = 'KQ613p6q1',
                      lhacode = [ 1 ])

KQ613p6q8 = Parameter(name = 'KQ613p6q8',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ613p6q8}',
                      lhablock = 'KQ613p6q8',
                      lhacode = [ 1 ])

KQ613p8q3 = Parameter(name = 'KQ613p8q3',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ613p8q3}',
                      lhablock = 'KQ613p8q3',
                      lhacode = [ 1 ])

KQ623p6q1 = Parameter(name = 'KQ623p6q1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ623p6q1}',
                      lhablock = 'KQ623p6q1',
                      lhacode = [ 1 ])

KQ623p6q1M = Parameter(name = 'KQ623p6q1M',
                       nature = 'external',
                       type = 'real',
                       value = 0.101,
                       texname = '\\text{KQ623p6q1M}',
                       lhablock = 'KQ623p6q1M',
                       lhacode = [ 1 ])

KQ623p6q8 = Parameter(name = 'KQ623p6q8',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ623p6q8}',
                      lhablock = 'KQ623p6q8',
                      lhacode = [ 1 ])

KQ623p6q8M = Parameter(name = 'KQ623p6q8M',
                       nature = 'external',
                       type = 'real',
                       value = 0.101,
                       texname = '\\text{KQ623p6q8M}',
                       lhablock = 'KQ623p6q8M',
                       lhacode = [ 1 ])

KQ623p8q3 = Parameter(name = 'KQ623p8q3',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ623p8q3}',
                      lhablock = 'KQ623p8q3',
                      lhacode = [ 1 ])

KQ653p6q1 = Parameter(name = 'KQ653p6q1',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ653p6q1}',
                      lhablock = 'KQ653p6q1',
                      lhacode = [ 1 ])

KQ653p6q8 = Parameter(name = 'KQ653p6q8',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ653p6q8}',
                      lhablock = 'KQ653p6q8',
                      lhacode = [ 1 ])

KQ653p8q3 = Parameter(name = 'KQ653p8q3',
                      nature = 'external',
                      type = 'real',
                      value = 0.101,
                      texname = '\\text{KQ653p8q3}',
                      lhablock = 'KQ653p8q3',
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

Ks12s11w = Parameter(name = 'Ks12s11w',
                     nature = 'external',
                     type = 'real',
                     value = 0.101,
                     texname = '\\text{Ks12s11w}',
                     lhablock = 'Ks12s11w',
                     lhacode = [ 1 ])

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

KTLh1 = Parameter(name = 'KTLh1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLh1}',
                  lhablock = 'KTLH',
                  lhacode = [ 1 ])

KTLh2 = Parameter(name = 'KTLh2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLh2}',
                  lhablock = 'KTLH',
                  lhacode = [ 2 ])

KTLh3 = Parameter(name = 'KTLh3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLh3}',
                  lhablock = 'KTLH',
                  lhacode = [ 3 ])

KTLw1 = Parameter(name = 'KTLw1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLw1}',
                  lhablock = 'KTLW',
                  lhacode = [ 1 ])

KTLw2 = Parameter(name = 'KTLw2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLw2}',
                  lhablock = 'KTLW',
                  lhacode = [ 2 ])

KTLw3 = Parameter(name = 'KTLw3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLw3}',
                  lhablock = 'KTLW',
                  lhacode = [ 3 ])

KTLz1 = Parameter(name = 'KTLz1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLz1}',
                  lhablock = 'KTLZ',
                  lhacode = [ 1 ])

KTLz2 = Parameter(name = 'KTLz2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLz2}',
                  lhablock = 'KTLZ',
                  lhacode = [ 2 ])

KTLz3 = Parameter(name = 'KTLz3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTLz3}',
                  lhablock = 'KTLZ',
                  lhacode = [ 3 ])

KTRh1 = Parameter(name = 'KTRh1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRh1}',
                  lhablock = 'KTRH',
                  lhacode = [ 1 ])

KTRh2 = Parameter(name = 'KTRh2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRh2}',
                  lhablock = 'KTRH',
                  lhacode = [ 2 ])

KTRh3 = Parameter(name = 'KTRh3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRh3}',
                  lhablock = 'KTRH',
                  lhacode = [ 3 ])

KTRw1 = Parameter(name = 'KTRw1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRw1}',
                  lhablock = 'KTRW',
                  lhacode = [ 1 ])

KTRw2 = Parameter(name = 'KTRw2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRw2}',
                  lhablock = 'KTRW',
                  lhacode = [ 2 ])

KTRw3 = Parameter(name = 'KTRw3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRw3}',
                  lhablock = 'KTRW',
                  lhacode = [ 3 ])

KTRz1 = Parameter(name = 'KTRz1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRz1}',
                  lhablock = 'KTRZ',
                  lhacode = [ 1 ])

KTRz2 = Parameter(name = 'KTRz2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRz2}',
                  lhablock = 'KTRZ',
                  lhacode = [ 2 ])

KTRz3 = Parameter(name = 'KTRz3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{KTRz3}',
                  lhablock = 'KTRZ',
                  lhacode = [ 3 ])

KXL1 = Parameter(name = 'KXL1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KXL1}',
                 lhablock = 'KXLW',
                 lhacode = [ 1 ])

KXL2 = Parameter(name = 'KXL2',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KXL2}',
                 lhablock = 'KXLW',
                 lhacode = [ 2 ])

KXL3 = Parameter(name = 'KXL3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KXL3}',
                 lhablock = 'KXLW',
                 lhacode = [ 3 ])

KXR1 = Parameter(name = 'KXR1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KXR1}',
                 lhablock = 'KXRW',
                 lhacode = [ 1 ])

KXR2 = Parameter(name = 'KXR2',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KXR2}',
                 lhablock = 'KXRW',
                 lhacode = [ 2 ])

KXR3 = Parameter(name = 'KXR3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KXR3}',
                 lhablock = 'KXRW',
                 lhacode = [ 3 ])

KYL1 = Parameter(name = 'KYL1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KYL1}',
                 lhablock = 'KYLW',
                 lhacode = [ 1 ])

KYL2 = Parameter(name = 'KYL2',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KYL2}',
                 lhablock = 'KYLW',
                 lhacode = [ 2 ])

KYL3 = Parameter(name = 'KYL3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KYL3}',
                 lhablock = 'KYLW',
                 lhacode = [ 3 ])

KYR1 = Parameter(name = 'KYR1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KYR1}',
                 lhablock = 'KYRW',
                 lhacode = [ 1 ])

KYR2 = Parameter(name = 'KYR2',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KYR2}',
                 lhablock = 'KYRW',
                 lhacode = [ 2 ])

KYR3 = Parameter(name = 'KYR3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
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

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

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

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

LQQRR1x1 = Parameter(name = 'LQQRR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LQQRR1x1}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 1, 1 ])

LQQRR1x2 = Parameter(name = 'LQQRR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRR1x2}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 1, 2 ])

LQQRR1x3 = Parameter(name = 'LQQRR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRR1x3}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 1, 3 ])

LQQRR2x1 = Parameter(name = 'LQQRR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRR2x1}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 2, 1 ])

LQQRR2x2 = Parameter(name = 'LQQRR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LQQRR2x2}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 2, 2 ])

LQQRR2x3 = Parameter(name = 'LQQRR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRR2x3}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 2, 3 ])

LQQRR3x1 = Parameter(name = 'LQQRR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRR3x1}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 3, 1 ])

LQQRR3x2 = Parameter(name = 'LQQRR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRR3x2}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 3, 2 ])

LQQRR3x3 = Parameter(name = 'LQQRR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LQQRR3x3}',
                     lhablock = 'FRBlock42',
                     lhacode = [ 3, 3 ])

LQQRI1x1 = Parameter(name = 'LQQRI1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI1x1}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 1, 1 ])

LQQRI1x2 = Parameter(name = 'LQQRI1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI1x2}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 1, 2 ])

LQQRI1x3 = Parameter(name = 'LQQRI1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI1x3}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 1, 3 ])

LQQRI2x1 = Parameter(name = 'LQQRI2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI2x1}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 2, 1 ])

LQQRI2x2 = Parameter(name = 'LQQRI2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI2x2}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 2, 2 ])

LQQRI2x3 = Parameter(name = 'LQQRI2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI2x3}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 2, 3 ])

LQQRI3x1 = Parameter(name = 'LQQRI3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI3x1}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 3, 1 ])

LQQRI3x2 = Parameter(name = 'LQQRI3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI3x2}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 3, 2 ])

LQQRI3x3 = Parameter(name = 'LQQRI3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LQQRI3x3}',
                     lhablock = 'FRBlock43',
                     lhacode = [ 3, 3 ])

LUDLR1x1 = Parameter(name = 'LUDLR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LUDLR1x1}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 1, 1 ])

LUDLR1x2 = Parameter(name = 'LUDLR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLR1x2}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 1, 2 ])

LUDLR1x3 = Parameter(name = 'LUDLR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLR1x3}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 1, 3 ])

LUDLR2x1 = Parameter(name = 'LUDLR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLR2x1}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 2, 1 ])

LUDLR2x2 = Parameter(name = 'LUDLR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LUDLR2x2}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 2, 2 ])

LUDLR2x3 = Parameter(name = 'LUDLR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLR2x3}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 2, 3 ])

LUDLR3x1 = Parameter(name = 'LUDLR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLR3x1}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 3, 1 ])

LUDLR3x2 = Parameter(name = 'LUDLR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLR3x2}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 3, 2 ])

LUDLR3x3 = Parameter(name = 'LUDLR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LUDLR3x3}',
                     lhablock = 'FRBlock44',
                     lhacode = [ 3, 3 ])

LUDLI1x1 = Parameter(name = 'LUDLI1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI1x1}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 1, 1 ])

LUDLI1x2 = Parameter(name = 'LUDLI1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI1x2}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 1, 2 ])

LUDLI1x3 = Parameter(name = 'LUDLI1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI1x3}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 1, 3 ])

LUDLI2x1 = Parameter(name = 'LUDLI2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI2x1}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 2, 1 ])

LUDLI2x2 = Parameter(name = 'LUDLI2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI2x2}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 2, 2 ])

LUDLI2x3 = Parameter(name = 'LUDLI2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI2x3}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 2, 3 ])

LUDLI3x1 = Parameter(name = 'LUDLI3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI3x1}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 3, 1 ])

LUDLI3x2 = Parameter(name = 'LUDLI3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI3x2}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 3, 2 ])

LUDLI3x3 = Parameter(name = 'LUDLI3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUDLI3x3}',
                     lhablock = 'FRBlock45',
                     lhacode = [ 3, 3 ])

LUULR1x1 = Parameter(name = 'LUULR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LUULR1x1}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 1, 1 ])

LUULR1x2 = Parameter(name = 'LUULR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULR1x2}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 1, 2 ])

LUULR1x3 = Parameter(name = 'LUULR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULR1x3}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 1, 3 ])

LUULR2x1 = Parameter(name = 'LUULR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULR2x1}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 2, 1 ])

LUULR2x2 = Parameter(name = 'LUULR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LUULR2x2}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 2, 2 ])

LUULR2x3 = Parameter(name = 'LUULR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULR2x3}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 2, 3 ])

LUULR3x1 = Parameter(name = 'LUULR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULR3x1}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 3, 1 ])

LUULR3x2 = Parameter(name = 'LUULR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULR3x2}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 3, 2 ])

LUULR3x3 = Parameter(name = 'LUULR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LUULR3x3}',
                     lhablock = 'FRBlock46',
                     lhacode = [ 3, 3 ])

LUULI1x1 = Parameter(name = 'LUULI1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI1x1}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 1, 1 ])

LUULI1x2 = Parameter(name = 'LUULI1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI1x2}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 1, 2 ])

LUULI1x3 = Parameter(name = 'LUULI1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI1x3}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 1, 3 ])

LUULI2x1 = Parameter(name = 'LUULI2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI2x1}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 2, 1 ])

LUULI2x2 = Parameter(name = 'LUULI2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI2x2}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 2, 2 ])

LUULI2x3 = Parameter(name = 'LUULI2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI2x3}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 2, 3 ])

LUULI3x1 = Parameter(name = 'LUULI3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI3x1}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 3, 1 ])

LUULI3x2 = Parameter(name = 'LUULI3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI3x2}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 3, 2 ])

LUULI3x3 = Parameter(name = 'LUULI3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LUULI3x3}',
                     lhablock = 'FRBlock47',
                     lhacode = [ 3, 3 ])

LDDLR1x1 = Parameter(name = 'LDDLR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LDDLR1x1}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 1, 1 ])

LDDLR1x2 = Parameter(name = 'LDDLR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLR1x2}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 1, 2 ])

LDDLR1x3 = Parameter(name = 'LDDLR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLR1x3}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 1, 3 ])

LDDLR2x1 = Parameter(name = 'LDDLR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLR2x1}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 2, 1 ])

LDDLR2x2 = Parameter(name = 'LDDLR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LDDLR2x2}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 2, 2 ])

LDDLR2x3 = Parameter(name = 'LDDLR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLR2x3}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 2, 3 ])

LDDLR3x1 = Parameter(name = 'LDDLR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLR3x1}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 3, 1 ])

LDDLR3x2 = Parameter(name = 'LDDLR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLR3x2}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 3, 2 ])

LDDLR3x3 = Parameter(name = 'LDDLR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{LDDLR3x3}',
                     lhablock = 'FRBlock48',
                     lhacode = [ 3, 3 ])

LDDLI1x1 = Parameter(name = 'LDDLI1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI1x1}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 1, 1 ])

LDDLI1x2 = Parameter(name = 'LDDLI1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI1x2}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 1, 2 ])

LDDLI1x3 = Parameter(name = 'LDDLI1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI1x3}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 1, 3 ])

LDDLI2x1 = Parameter(name = 'LDDLI2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI2x1}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 2, 1 ])

LDDLI2x2 = Parameter(name = 'LDDLI2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI2x2}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 2, 2 ])

LDDLI2x3 = Parameter(name = 'LDDLI2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI2x3}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 2, 3 ])

LDDLI3x1 = Parameter(name = 'LDDLI3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI3x1}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 3, 1 ])

LDDLI3x2 = Parameter(name = 'LDDLI3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI3x2}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 3, 2 ])

LDDLI3x3 = Parameter(name = 'LDDLI3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{LDDLI3x3}',
                     lhablock = 'FRBlock49',
                     lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

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

MQ653 = Parameter(name = 'MQ653',
                  nature = 'external',
                  type = 'real',
                  value = 1000,
                  texname = '\\text{MQ653}',
                  lhablock = 'MASS',
                  lhacode = [ 6000653 ])

MQ623 = Parameter(name = 'MQ623',
                  nature = 'external',
                  type = 'real',
                  value = 1001,
                  texname = '\\text{MQ623}',
                  lhablock = 'MASS',
                  lhacode = [ 6000623 ])

MQ613 = Parameter(name = 'MQ613',
                  nature = 'external',
                  type = 'real',
                  value = 1002,
                  texname = '\\text{MQ613}',
                  lhablock = 'MASS',
                  lhacode = [ 6000613 ])

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

MS10 = Parameter(name = 'MS10',
                 nature = 'external',
                 type = 'real',
                 value = 500.1,
                 texname = '\\text{MS10}',
                 lhablock = 'MASS',
                 lhacode = [ 6100001 ])

MS80 = Parameter(name = 'MS80',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MS80}',
                 lhablock = 'MASS',
                 lhacode = [ 6108000 ])

MS11 = Parameter(name = 'MS11',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{MS11}',
                 lhablock = 'MASS',
                 lhacode = [ 6100002 ])

MS12 = Parameter(name = 'MS12',
                 nature = 'external',
                 type = 'real',
                 value = 500.5,
                 texname = '\\text{MS12}',
                 lhablock = 'MASS',
                 lhacode = [ 6100003 ])

MS323 = Parameter(name = 'MS323',
                  nature = 'external',
                  type = 'real',
                  value = 900,
                  texname = '\\text{MS323}',
                  lhablock = 'MASS',
                  lhacode = [ 6100300 ])

MSIX1 = Parameter(name = 'MSIX1',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MSIX1}',
                  lhablock = 'MASS',
                  lhacode = [ 9000005 ])

MS623 = Parameter(name = 'MS623',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MS623}',
                  lhablock = 'MASS',
                  lhacode = [ 9000006 ])

MSIX3 = Parameter(name = 'MSIX3',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MSIX3}',
                  lhablock = 'MASS',
                  lhacode = [ 9000007 ])

MX = Parameter(name = 'MX',
               nature = 'external',
               type = 'real',
               value = 1000,
               texname = '\\text{MX}',
               lhablock = 'MASS',
               lhacode = [ 6000005 ])

MTP = Parameter(name = 'MTP',
                nature = 'external',
                type = 'real',
                value = 1100,
                texname = '\\text{MTP}',
                lhablock = 'MASS',
                lhacode = [ 6000006 ])

MBP = Parameter(name = 'MBP',
                nature = 'external',
                type = 'real',
                value = 1200,
                texname = '\\text{MBP}',
                lhablock = 'MASS',
                lhacode = [ 6000007 ])

MY = Parameter(name = 'MY',
               nature = 'external',
               type = 'real',
               value = 1300,
               texname = '\\text{MY}',
               lhablock = 'MASS',
               lhacode = [ 6000008 ])

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

WQ653 = Parameter(name = 'WQ653',
                  nature = 'external',
                  type = 'real',
                  value = 5.,
                  texname = '\\text{WQ653}',
                  lhablock = 'DECAY',
                  lhacode = [ 6000653 ])

WQ623 = Parameter(name = 'WQ623',
                  nature = 'external',
                  type = 'real',
                  value = 5.,
                  texname = '\\text{WQ623}',
                  lhablock = 'DECAY',
                  lhacode = [ 6000623 ])

WQ613 = Parameter(name = 'WQ613',
                  nature = 'external',
                  type = 'real',
                  value = 5.,
                  texname = '\\text{WQ613}',
                  lhablock = 'DECAY',
                  lhacode = [ 6000613 ])

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

WS10 = Parameter(name = 'WS10',
                 nature = 'external',
                 type = 'real',
                 value = 1.1,
                 texname = '\\text{WS10}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100001 ])

WS80 = Parameter(name = 'WS80',
                 nature = 'external',
                 type = 'real',
                 value = 1.1,
                 texname = '\\text{WS80}',
                 lhablock = 'DECAY',
                 lhacode = [ 6108000 ])

WS11 = Parameter(name = 'WS11',
                 nature = 'external',
                 type = 'real',
                 value = 15,
                 texname = '\\text{WS11}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100002 ])

WS12 = Parameter(name = 'WS12',
                 nature = 'external',
                 type = 'real',
                 value = 1.1,
                 texname = '\\text{WS12}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100003 ])

WS323 = Parameter(name = 'WS323',
                  nature = 'external',
                  type = 'real',
                  value = 1.1,
                  texname = '\\text{WS323}',
                  lhablock = 'DECAY',
                  lhacode = [ 6100300 ])

WSIX1 = Parameter(name = 'WSIX1',
                  nature = 'external',
                  type = 'real',
                  value = 4.4108,
                  texname = '\\text{WSIX1}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000005 ])

WS623 = Parameter(name = 'WS623',
                  nature = 'external',
                  type = 'real',
                  value = 4.774,
                  texname = '\\text{WS623}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000006 ])

WSIX3 = Parameter(name = 'WSIX3',
                  nature = 'external',
                  type = 'real',
                  value = 4.0647,
                  texname = '\\text{WSIX3}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000007 ])

WX = Parameter(name = 'WX',
               nature = 'external',
               type = 'real',
               value = 10.,
               texname = '\\text{WX}',
               lhablock = 'DECAY',
               lhacode = [ 6000005 ])

WTP = Parameter(name = 'WTP',
                nature = 'external',
                type = 'real',
                value = 11.,
                texname = '\\text{WTP}',
                lhablock = 'DECAY',
                lhacode = [ 6000006 ])

WBP = Parameter(name = 'WBP',
                nature = 'external',
                type = 'real',
                value = 12.,
                texname = '\\text{WBP}',
                lhablock = 'DECAY',
                lhacode = [ 6000007 ])

WY = Parameter(name = 'WY',
               nature = 'external',
               type = 'real',
               value = 13.,
               texname = '\\text{WY}',
               lhablock = 'DECAY',
               lhacode = [ 6000008 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '(1)/(aEWM1)',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

LQQR1x1 = Parameter(name = 'LQQR1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LQQRI1x1)+(LQQRR1x1)',
                    texname = '\\text{LQQR1x1}')

LQQR1x2 = Parameter(name = 'LQQR1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LQQRI1x2)+(LQQRR1x2)',
                    texname = '\\text{LQQR1x2}')

LQQR1x3 = Parameter(name = 'LQQR1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LQQRI1x3)+(LQQRR1x3)',
                    texname = '\\text{LQQR1x3}')

LQQR2x2 = Parameter(name = 'LQQR2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LQQRI2x2)+(LQQRR2x2)',
                    texname = '\\text{LQQR2x2}')

LQQR2x3 = Parameter(name = 'LQQR2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LQQRI2x3)+(LQQRR2x3)',
                    texname = '\\text{LQQR2x3}')

LQQR3x3 = Parameter(name = 'LQQR3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LQQRI3x3)+(LQQRR3x3)',
                    texname = '\\text{LQQR3x3}')

LUDL1x1 = Parameter(name = 'LUDL1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUDLI1x1)+(LUDLR1x1)',
                    texname = '\\text{LUDL1x1}')

LUDL1x2 = Parameter(name = 'LUDL1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUDLI1x2)+(LUDLR1x2)',
                    texname = '\\text{LUDL1x2}')

LUDL1x3 = Parameter(name = 'LUDL1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUDLI1x3)+(LUDLR1x3)',
                    texname = '\\text{LUDL1x3}')

LUDL2x2 = Parameter(name = 'LUDL2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUDLI2x2)+(LUDLR2x2)',
                    texname = '\\text{LUDL2x2}')

LUDL2x3 = Parameter(name = 'LUDL2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUDLI2x3)+(LUDLR2x3)',
                    texname = '\\text{LUDL2x3}')

LUDL3x3 = Parameter(name = 'LUDL3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUDLI3x3)+(LUDLR3x3)',
                    texname = '\\text{LUDL3x3}')

LUUL1x1 = Parameter(name = 'LUUL1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUULI1x1)+(LUULR1x1)',
                    texname = '\\text{LUUL1x1}')

LUUL1x2 = Parameter(name = 'LUUL1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUULI1x2)+(LUULR1x2)',
                    texname = '\\text{LUUL1x2}')

LUUL1x3 = Parameter(name = 'LUUL1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUULI1x3)+(LUULR1x3)',
                    texname = '\\text{LUUL1x3}')

LUUL2x2 = Parameter(name = 'LUUL2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUULI2x2)+(LUULR2x2)',
                    texname = '\\text{LUUL2x2}')

LUUL2x3 = Parameter(name = 'LUUL2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUULI2x3)+(LUULR2x3)',
                    texname = '\\text{LUUL2x3}')

LUUL3x3 = Parameter(name = 'LUUL3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LUULI3x3)+(LUULR3x3)',
                    texname = '\\text{LUUL3x3}')

LDDL1x1 = Parameter(name = 'LDDL1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LDDLI1x1)+(LDDLR1x1)',
                    texname = '\\text{LDDL1x1}')

LDDL1x2 = Parameter(name = 'LDDL1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LDDLI1x2)+(LDDLR1x2)',
                    texname = '\\text{LDDL1x2}')

LDDL1x3 = Parameter(name = 'LDDL1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LDDLI1x3)+(LDDLR1x3)',
                    texname = '\\text{LDDL1x3}')

LDDL2x2 = Parameter(name = 'LDDL2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LDDLI2x2)+(LDDLR2x2)',
                    texname = '\\text{LDDL2x2}')

LDDL2x3 = Parameter(name = 'LDDL2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LDDLI2x3)+(LDDLR2x3)',
                    texname = '\\text{LDDL2x3}')

LDDL3x3 = Parameter(name = 'LDDL3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = '(complex(0,1)*LDDLI3x3)+(LDDLR3x3)',
                    texname = '\\text{LDDL3x3}')

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
                value = '(1)+(-MW**2)/(MZ**2)',
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
               value = '(ee)/(cw)',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = '(ee)/(sw)',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/(ee)',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = '(MH**2)/(2*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/(vev)',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/(vev)',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/(vev)',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/(vev)',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/(vev)',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/(vev)',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/(vev)',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/(vev)',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/(vev)',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

