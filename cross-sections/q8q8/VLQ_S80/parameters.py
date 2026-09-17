# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 27, 2023)
# Date: Mon 26 Jan 2026 15:48:52



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
                     value = 0.,
                     texname = '\\text{GP80D1x1}',
                     lhablock = 'GP80D',
                     lhacode = [ 1, 1 ])

GP80D2x2 = Parameter(name = 'GP80D2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GP80D2x2}',
                     lhablock = 'GP80D',
                     lhacode = [ 2, 2 ])

GP80D3x3 = Parameter(name = 'GP80D3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
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
                     value = 0.,
                     texname = '\\text{GP80U1x1}',
                     lhablock = 'GP80U',
                     lhacode = [ 1, 1 ])

GP80U2x2 = Parameter(name = 'GP80U2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GP80U2x2}',
                     lhablock = 'GP80U',
                     lhacode = [ 2, 2 ])

GP80U3x3 = Parameter(name = 'GP80U3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
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
                     value = 0.,
                     texname = '\\text{GS80BDL1}',
                     lhablock = 'GS80BDL',
                     lhacode = [ 1 ])

GS80BDL2 = Parameter(name = 'GS80BDL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80BDL2}',
                     lhablock = 'GS80BDL',
                     lhacode = [ 2 ])

GS80BDL3 = Parameter(name = 'GS80BDL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80BDL3}',
                     lhablock = 'GS80BDL',
                     lhacode = [ 3 ])

GS80BDR1 = Parameter(name = 'GS80BDR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80BDR1}',
                     lhablock = 'GS80BDR',
                     lhacode = [ 1 ])

GS80BDR2 = Parameter(name = 'GS80BDR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80BDR2}',
                     lhablock = 'GS80BDR',
                     lhacode = [ 2 ])

GS80BDR3 = Parameter(name = 'GS80BDR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80BDR3}',
                     lhablock = 'GS80BDR',
                     lhacode = [ 3 ])

GS80D1x1 = Parameter(name = 'GS80D1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80D1x1}',
                     lhablock = 'GS80D',
                     lhacode = [ 1, 1 ])

GS80D2x2 = Parameter(name = 'GS80D2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80D2x2}',
                     lhablock = 'GS80D',
                     lhacode = [ 2, 2 ])

GS80D3x3 = Parameter(name = 'GS80D3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
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
                     value = 0.,
                     texname = '\\text{GS80TUL1}',
                     lhablock = 'GS80TUL',
                     lhacode = [ 1 ])

GS80TUL2 = Parameter(name = 'GS80TUL2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80TUL2}',
                     lhablock = 'GS80TUL',
                     lhacode = [ 2 ])

GS80TUL3 = Parameter(name = 'GS80TUL3',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{GS80TUL3}',
                     lhablock = 'GS80TUL',
                     lhacode = [ 3 ])

GS80TUR1 = Parameter(name = 'GS80TUR1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80TUR1}',
                     lhablock = 'GS80TUR',
                     lhacode = [ 1 ])

GS80TUR2 = Parameter(name = 'GS80TUR2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80TUR2}',
                     lhablock = 'GS80TUR',
                     lhacode = [ 2 ])

GS80TUR3 = Parameter(name = 'GS80TUR3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80TUR3}',
                     lhablock = 'GS80TUR',
                     lhacode = [ 3 ])

GS80U1x1 = Parameter(name = 'GS80U1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80U1x1}',
                     lhablock = 'GS80U',
                     lhacode = [ 1, 1 ])

GS80U2x2 = Parameter(name = 'GS80U2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{GS80U2x2}',
                     lhablock = 'GS80U',
                     lhacode = [ 2, 2 ])

GS80U3x3 = Parameter(name = 'GS80U3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
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

KP80G = Parameter(name = 'KP80G',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KP80G}',
                  lhablock = 'KP80VV',
                  lhacode = [ 1 ])

KP80GZ = Parameter(name = 'KP80GZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KP80GZ}',
                   lhablock = 'KP80VV',
                   lhacode = [ 2 ])

KP80GA = Parameter(name = 'KP80GA',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KP80GA}',
                   lhablock = 'KP80VV',
                   lhacode = [ 3 ])

KS80H1 = Parameter(name = 'KS80H1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KS80H1}',
                   lhablock = 'KS80H',
                   lhacode = [ 1 ])

KS80H2 = Parameter(name = 'KS80H2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KS80H2}',
                   lhablock = 'KS80H',
                   lhacode = [ 2 ])

KS80HH = Parameter(name = 'KS80HH',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KS80HH}',
                   lhablock = 'KS80H',
                   lhacode = [ 3 ])

KS80G = Parameter(name = 'KS80G',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{KS80G}',
                  lhablock = 'KS80VV',
                  lhacode = [ 1 ])

KS80GZ = Parameter(name = 'KS80GZ',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{KS80GZ}',
                   lhablock = 'KS80VV',
                   lhacode = [ 2 ])

KS80GA = Parameter(name = 'KS80GA',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
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

MS80 = Parameter(name = 'MS80',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MS80}',
                 lhablock = 'MASS',
                 lhacode = [ 6108000 ])

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

WS80 = Parameter(name = 'WS80',
                 nature = 'external',
                 type = 'real',
                 value = 1.1,
                 texname = '\\text{WS80}',
                 lhablock = 'DECAY',
                 lhacode = [ 6108000 ])

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

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

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

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x3)',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yup',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yup',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yup',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yc',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yt',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yt',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yt',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ydo',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ys',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I4a33}')

