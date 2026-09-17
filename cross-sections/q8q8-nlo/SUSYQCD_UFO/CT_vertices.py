# This file was automatically created by FeynRules 2.4.16
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Fri 21 Aug 2015 09:21:21


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.go] ] ],
               couplings = {(0,0,0):C.R2GC_109_19,(0,0,1):C.R2GC_109_20,(0,0,2):C.R2GC_109_21,(0,1,0):C.R2GC_108_16,(0,1,1):C.R2GC_108_17,(0,1,2):C.R2GC_108_18,(0,2,0):C.R2GC_108_16,(0,2,1):C.R2GC_108_17,(0,2,2):C.R2GC_108_18,(0,3,0):C.R2GC_109_19,(0,3,1):C.R2GC_109_20,(0,3,2):C.R2GC_109_21,(0,4,0):C.R2GC_109_19,(0,4,1):C.R2GC_109_20,(0,4,2):C.R2GC_109_21,(0,5,0):C.R2GC_108_16,(0,5,1):C.R2GC_108_17,(0,5,2):C.R2GC_108_18})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.go] ] ],
               couplings = {(2,0,0):C.R2GC_101_4,(2,0,1):C.R2GC_100_3,(2,0,2):C.R2GC_100_2,(0,0,0):C.R2GC_101_4,(0,0,1):C.R2GC_100_3,(0,0,2):C.R2GC_100_2,(4,0,0):C.R2GC_99_171,(4,0,1):C.R2GC_99_172,(4,0,2):C.R2GC_99_173,(3,0,0):C.R2GC_99_171,(3,0,1):C.R2GC_99_172,(3,0,2):C.R2GC_99_173,(8,0,0):C.R2GC_100_1,(8,0,1):C.R2GC_100_2,(8,0,2):C.R2GC_100_3,(6,0,0):C.R2GC_110_22,(6,0,1):C.R2GC_112_26,(6,0,2):C.R2GC_110_23,(7,0,0):C.R2GC_111_24,(7,0,1):C.R2GC_105_11,(7,0,2):C.R2GC_111_25,(5,0,0):C.R2GC_99_171,(5,0,1):C.R2GC_99_172,(5,0,2):C.R2GC_99_173,(1,0,0):C.R2GC_99_171,(1,0,1):C.R2GC_99_172,(1,0,2):C.R2GC_99_173,(11,0,0):C.R2GC_103_7,(11,0,1):C.R2GC_103_8,(11,0,2):C.R2GC_103_9,(10,0,0):C.R2GC_103_7,(10,0,1):C.R2GC_103_8,(10,0,2):C.R2GC_103_9,(9,0,1):C.R2GC_102_5,(9,0,2):C.R2GC_102_6,(2,1,0):C.R2GC_101_4,(2,1,1):C.R2GC_100_3,(2,1,2):C.R2GC_100_2,(0,1,0):C.R2GC_101_4,(0,1,1):C.R2GC_100_3,(0,1,2):C.R2GC_100_2,(4,1,0):C.R2GC_99_171,(4,1,1):C.R2GC_99_172,(4,1,2):C.R2GC_99_173,(3,1,0):C.R2GC_99_171,(3,1,1):C.R2GC_99_172,(3,1,2):C.R2GC_99_173,(8,1,0):C.R2GC_100_1,(8,1,1):C.R2GC_105_11,(8,1,2):C.R2GC_100_3,(6,1,0):C.R2GC_115_29,(6,1,1):C.R2GC_115_30,(6,1,2):C.R2GC_115_31,(7,1,0):C.R2GC_111_24,(7,1,1):C.R2GC_100_2,(7,1,2):C.R2GC_111_25,(5,1,0):C.R2GC_99_171,(5,1,1):C.R2GC_99_172,(5,1,2):C.R2GC_99_173,(1,1,0):C.R2GC_99_171,(1,1,1):C.R2GC_99_172,(1,1,2):C.R2GC_99_173,(11,1,0):C.R2GC_103_7,(11,1,1):C.R2GC_103_8,(11,1,2):C.R2GC_103_9,(10,1,0):C.R2GC_103_7,(10,1,1):C.R2GC_103_8,(10,1,2):C.R2GC_103_9,(9,1,1):C.R2GC_102_5,(9,1,2):C.R2GC_102_6,(0,2,0):C.R2GC_101_4,(0,2,1):C.R2GC_100_3,(0,2,2):C.R2GC_100_2,(2,2,0):C.R2GC_101_4,(2,2,1):C.R2GC_100_3,(2,2,2):C.R2GC_100_2,(5,2,0):C.R2GC_99_171,(5,2,1):C.R2GC_99_172,(5,2,2):C.R2GC_99_173,(1,2,0):C.R2GC_99_171,(1,2,1):C.R2GC_99_172,(1,2,2):C.R2GC_99_173,(7,2,0):C.R2GC_114_27,(7,2,1):C.R2GC_104_10,(7,2,2):C.R2GC_114_28,(4,2,0):C.R2GC_99_171,(4,2,1):C.R2GC_99_172,(4,2,2):C.R2GC_99_173,(3,2,0):C.R2GC_99_171,(3,2,1):C.R2GC_99_172,(3,2,2):C.R2GC_99_173,(8,2,0):C.R2GC_100_1,(8,2,1):C.R2GC_104_10,(8,2,2):C.R2GC_100_3,(6,2,0):C.R2GC_110_22,(6,2,2):C.R2GC_110_23,(11,2,0):C.R2GC_103_7,(11,2,1):C.R2GC_103_8,(11,2,2):C.R2GC_103_9,(10,2,0):C.R2GC_103_7,(10,2,1):C.R2GC_103_8,(10,2,2):C.R2GC_103_9,(9,2,1):C.R2GC_102_5,(9,2,2):C.R2GC_102_6})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.go, P.go, P.g ],
               color = [ 'd(3,2,1)', 'f(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
               loop_particles = [ [ [P.b, P.sbL], [P.b, P.sbR], [P.c, P.scL], [P.d, P.sdL], [P.d, P.sdR], [P.s, P.ssL], [P.s, P.ssR], [P.stL, P.t], [P.stR, P.t], [P.suL, P.u] ], [ [P.b, P.sbL], [P.c, P.scL], [P.d, P.sdL], [P.s, P.ssL], [P.stL, P.t], [P.suL, P.u] ], [ [P.b, P.sbR], [P.d, P.sdR], [P.s, P.ssR], [P.stR, P.t] ], [ [P.c, P.scR], [P.suR, P.u] ], [ [P.g, P.go] ] ],
               couplings = {(0,0,3):C.R2GC_88_166,(1,0,3):C.R2GC_87_163,(0,1,1):C.R2GC_88_166,(0,1,2):C.R2GC_88_165,(1,1,0):C.R2GC_87_163,(1,1,3):C.R2GC_91_170,(1,1,4):C.R2GC_87_164,(0,2,1):C.R2GC_88_165,(0,2,2):C.R2GC_88_166,(1,2,0):C.R2GC_87_163,(1,2,4):C.R2GC_87_164})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_432_130})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_269_86})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_268_85})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_431_129})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.chi, P.b, P.sbL__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.sbL] ] ],
               couplings = {(0,0,0):C.R2GC_347_108})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.b__tilde__, P.chi, P.sbL ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.sbL] ] ],
               couplings = {(0,0,0):C.R2GC_347_108})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.chi, P.b, P.sbR__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.sbR] ] ],
                couplings = {(0,0,0):C.R2GC_348_109})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.b__tilde__, P.chi, P.sbR ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.sbR] ] ],
                couplings = {(0,0,0):C.R2GC_348_109})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.chi, P.c, P.scL__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.scL] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.c__tilde__, P.chi, P.scL ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.scL] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.chi, P.c, P.scR__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.scR] ] ],
                couplings = {(0,0,0):C.R2GC_350_110})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.c__tilde__, P.chi, P.scR ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.scR] ] ],
                couplings = {(0,0,0):C.R2GC_350_110})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.chi, P.d, P.sdL__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.sdL] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.chi, P.sdL ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.sdL] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.chi, P.d, P.sdR__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.sdR] ] ],
                couplings = {(0,0,0):C.R2GC_348_109})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.chi, P.sdR ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.sdR] ] ],
                couplings = {(0,0,0):C.R2GC_348_109})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.chi, P.s, P.ssL__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.ssL] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.chi, P.ssL ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.ssL] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.chi, P.s, P.ssR__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.ssR] ] ],
                couplings = {(0,0,0):C.R2GC_348_109})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.chi, P.ssR ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.ssR] ] ],
                couplings = {(0,0,0):C.R2GC_348_109})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.chi, P.t, P.stL__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.stL, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.t__tilde__, P.chi, P.stL ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.stL, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.chi, P.t, P.stR__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.stR, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_350_110})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.chi, P.stR ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.stR, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_350_110})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.chi, P.u, P.suL__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.suL, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.chi, P.suL ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.suL, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_347_108})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.chi, P.u, P.suR__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.suR, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_350_110})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.chi, P.suR ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.suR, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_350_110})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.go, P.sbL ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbL] ], [ [P.g, P.go, P.sbL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_139,(0,0,2):C.R2GC_525_140})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.go, P.b, P.sbR__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbR] ], [ [P.g, P.go, P.sbR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_142,(0,0,2):C.R2GC_531_143})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.go, P.scL ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scL] ], [ [P.g, P.go, P.scL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_139,(0,0,2):C.R2GC_525_140})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.go, P.c, P.scR__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scR] ], [ [P.g, P.go, P.scR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_142,(0,0,2):C.R2GC_531_143})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.go, P.sdL ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdL] ], [ [P.g, P.go, P.sdL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_139,(0,0,2):C.R2GC_525_140})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.go, P.d, P.sdR__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdR] ], [ [P.g, P.go, P.sdR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_142,(0,0,2):C.R2GC_531_143})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.s__tilde__, P.go, P.ssL ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssL] ], [ [P.g, P.s, P.ssL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_140,(0,0,2):C.R2GC_525_139})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.go, P.s, P.ssR__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssR] ], [ [P.g, P.s, P.ssR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_143,(0,0,2):C.R2GC_531_142})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.go, P.stL ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.go, P.stL] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stL, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_525_140,(0,0,1):C.R2GC_525_138,(0,0,2):C.R2GC_525_139})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.go, P.t, P.stR__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.go, P.stR] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stR, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_531_143,(0,0,1):C.R2GC_531_141,(0,0,2):C.R2GC_531_142})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.u__tilde__, P.go, P.suL ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.go, P.suL] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suL, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_525_140,(0,0,1):C.R2GC_525_138,(0,0,2):C.R2GC_525_139})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.go, P.u, P.suR__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.go, P.suR] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suR, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_531_143,(0,0,1):C.R2GC_531_141,(0,0,2):C.R2GC_531_142})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.go, P.b, P.sbL__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbL] ], [ [P.g, P.go, P.sbL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_139,(0,0,2):C.R2GC_525_140})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.b__tilde__, P.go, P.sbR ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbR] ], [ [P.g, P.go, P.sbR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_142,(0,0,2):C.R2GC_531_143})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.go, P.c, P.scL__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scL] ], [ [P.g, P.go, P.scL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_139,(0,0,2):C.R2GC_525_140})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.c__tilde__, P.go, P.scR ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scR] ], [ [P.g, P.go, P.scR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_142,(0,0,2):C.R2GC_531_143})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.go, P.d, P.sdL__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdL] ], [ [P.g, P.go, P.sdL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_139,(0,0,2):C.R2GC_525_140})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.d__tilde__, P.go, P.sdR ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdR] ], [ [P.g, P.go, P.sdR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_142,(0,0,2):C.R2GC_531_143})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.go, P.s, P.ssL__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssL] ], [ [P.g, P.s, P.ssL] ] ],
                couplings = {(0,0,0):C.R2GC_525_138,(0,0,1):C.R2GC_525_140,(0,0,2):C.R2GC_525_139})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.s__tilde__, P.go, P.ssR ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssR] ], [ [P.g, P.s, P.ssR] ] ],
                couplings = {(0,0,0):C.R2GC_531_141,(0,0,1):C.R2GC_531_143,(0,0,2):C.R2GC_531_142})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.go, P.t, P.stL__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.go, P.stL] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stL, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_525_140,(0,0,1):C.R2GC_525_138,(0,0,2):C.R2GC_525_139})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.go, P.stR ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.go, P.stR] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stR, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_531_143,(0,0,1):C.R2GC_531_141,(0,0,2):C.R2GC_531_142})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.go, P.u, P.suL__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.go, P.suL] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suL, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_525_140,(0,0,1):C.R2GC_525_138,(0,0,2):C.R2GC_525_139})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.u__tilde__, P.go, P.suR ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.go, P.suR] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suR, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_531_143,(0,0,1):C.R2GC_531_141,(0,0,2):C.R2GC_531_142})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL__tilde__, P.sbL, P.sbL ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.g, P.sbL] ] ],
                couplings = {(1,0,1):C.R2GC_162_66,(1,0,0):C.R2GC_162_67,(1,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_66,(0,0,0):C.R2GC_162_67,(0,0,2):C.R2GC_162_68})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.sbR__tilde__, P.sbR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.sbR] ], [ [P.g, P.sbL, P.sbR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,0):C.R2GC_361_123,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,0):C.R2GC_360_119,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR__tilde__, P.sbR, P.sbR ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.g, P.sbR] ] ],
                couplings = {(1,0,1):C.R2GC_162_66,(1,0,0):C.R2GC_162_67,(1,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_66,(0,0,0):C.R2GC_162_67,(0,0,2):C.R2GC_162_68})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.scL__tilde__, P.scL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.scL] ], [ [P.g, P.sbL, P.scL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR, P.scL__tilde__, P.scL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.scL] ], [ [P.g, P.sbR, P.scL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.scL__tilde__, P.scL__tilde__, P.scL, P.scL ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.g, P.scL] ] ],
                couplings = {(1,0,1):C.R2GC_162_66,(1,0,0):C.R2GC_162_67,(1,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_66,(0,0,0):C.R2GC_162_67,(0,0,2):C.R2GC_162_68})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.scR__tilde__, P.scR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.scR] ], [ [P.g, P.sbL, P.scR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR, P.scR__tilde__, P.scR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.scR] ], [ [P.g, P.sbR, P.scR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.scL__tilde__, P.scL, P.scR__tilde__, P.scR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.scR] ], [ [P.g, P.scL, P.scR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,0):C.R2GC_361_123,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,0):C.R2GC_360_119,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.scR__tilde__, P.scR__tilde__, P.scR, P.scR ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.g, P.scR] ] ],
                couplings = {(1,0,1):C.R2GC_162_66,(1,0,0):C.R2GC_162_67,(1,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_66,(0,0,0):C.R2GC_162_67,(0,0,2):C.R2GC_162_68})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.sdL__tilde__, P.sdL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.sdL] ], [ [P.g, P.sbL, P.sdL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR, P.sdL__tilde__, P.sdL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.sdL] ], [ [P.g, P.sbR, P.sdL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.scL__tilde__, P.scL, P.sdL__tilde__, P.sdL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.sdL] ], [ [P.g, P.scL, P.sdL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.scR__tilde__, P.scR, P.sdL__tilde__, P.sdL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.sdL] ], [ [P.g, P.scR, P.sdL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.sdL__tilde__, P.sdL__tilde__, P.sdL, P.sdL ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.g, P.sdL] ] ],
                couplings = {(1,0,1):C.R2GC_162_66,(1,0,0):C.R2GC_162_67,(1,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_66,(0,0,0):C.R2GC_162_67,(0,0,2):C.R2GC_162_68})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.sdR__tilde__, P.sdR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.sdR] ], [ [P.g, P.sbL, P.sdR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR, P.sdR__tilde__, P.sdR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.sdR] ], [ [P.g, P.sbR, P.sdR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.scL__tilde__, P.scL, P.sdR__tilde__, P.sdR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.sdR] ], [ [P.g, P.scL, P.sdR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.scR__tilde__, P.scR, P.sdR__tilde__, P.sdR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.sdR] ], [ [P.g, P.scR, P.sdR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.sdL__tilde__, P.sdL, P.sdR__tilde__, P.sdR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.g, P.sdL], [P.g, P.sdR] ], [ [P.g, P.sdL, P.sdR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,0):C.R2GC_361_123,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,0):C.R2GC_360_119,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.sdR__tilde__, P.sdR__tilde__, P.sdR, P.sdR ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.g, P.sdR] ] ],
                couplings = {(1,0,1):C.R2GC_162_66,(1,0,0):C.R2GC_162_67,(1,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_66,(0,0,0):C.R2GC_162_67,(0,0,2):C.R2GC_162_68})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.ssL__tilde__, P.ssL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.ssL] ], [ [P.g, P.sbL, P.ssL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR, P.ssL__tilde__, P.ssL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.ssL] ], [ [P.g, P.sbR, P.ssL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.scL__tilde__, P.scL, P.ssL__tilde__, P.ssL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.ssL] ], [ [P.g, P.scL, P.ssL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.scR__tilde__, P.scR, P.ssL__tilde__, P.ssL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.ssL] ], [ [P.g, P.scR, P.ssL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.sdL__tilde__, P.sdL, P.ssL__tilde__, P.ssL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sdL], [P.g, P.ssL] ], [ [P.g, P.sdL, P.ssL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.sdR__tilde__, P.sdR, P.ssL__tilde__, P.ssL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sdR], [P.g, P.ssL] ], [ [P.g, P.sdR, P.ssL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.ssL__tilde__, P.ssL__tilde__, P.ssL, P.ssL ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.go, P.s] ], [ [P.g, P.ssL] ] ],
                couplings = {(1,0,0):C.R2GC_162_66,(1,0,2):C.R2GC_162_68,(1,0,1):C.R2GC_162_67,(0,0,0):C.R2GC_162_66,(0,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_67})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.ssR__tilde__, P.ssR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.ssR] ], [ [P.g, P.sbL, P.ssR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR, P.ssR__tilde__, P.ssR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.ssR] ], [ [P.g, P.sbR, P.ssR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.scL__tilde__, P.scL, P.ssR__tilde__, P.ssR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.ssR] ], [ [P.g, P.scL, P.ssR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.scR__tilde__, P.scR, P.ssR__tilde__, P.ssR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.ssR] ], [ [P.g, P.scR, P.ssR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.sdL__tilde__, P.sdL, P.ssR__tilde__, P.ssR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sdL], [P.g, P.ssR] ], [ [P.g, P.sdL, P.ssR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.sdR__tilde__, P.sdR, P.ssR__tilde__, P.ssR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.g, P.sdR], [P.g, P.ssR] ], [ [P.g, P.sdR, P.ssR] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.ssL__tilde__, P.ssL, P.ssR__tilde__, P.ssR ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.go, P.s] ], [ [P.g, P.ssL], [P.g, P.ssR] ], [ [P.g, P.ssL, P.ssR] ] ],
                couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,1):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,1):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.ssR__tilde__, P.ssR__tilde__, P.ssR, P.ssR ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.go, P.s] ], [ [P.g, P.ssR] ] ],
                couplings = {(1,0,0):C.R2GC_162_66,(1,0,2):C.R2GC_162_68,(1,0,1):C.R2GC_162_67,(0,0,0):C.R2GC_162_66,(0,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_67})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.sbL__tilde__, P.sbL, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.stL] ], [ [P.g, P.sbL, P.stL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.sbR__tilde__, P.sbR, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.stL] ], [ [P.g, P.sbR, P.stL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.scL__tilde__, P.scL, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.stL] ], [ [P.g, P.scL, P.stL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.scR__tilde__, P.scR, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.stL] ], [ [P.g, P.scR, P.stL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.sdL__tilde__, P.sdL, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sdL], [P.g, P.stL] ], [ [P.g, P.sdL, P.stL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.sdR__tilde__, P.sdR, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sdR], [P.g, P.stL] ], [ [P.g, P.sdR, P.stL] ] ],
                couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.ssL__tilde__, P.ssL, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.t] ], [ [P.g, P.ssL], [P.g, P.stL] ], [ [P.g, P.ssL, P.stL] ] ],
                couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,3):C.R2GC_365_128,(1,0,1):C.R2GC_365_127,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,3):C.R2GC_364_126,(0,0,1):C.R2GC_364_125})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.ssR__tilde__, P.ssR, P.stL__tilde__, P.stL ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.t] ], [ [P.g, P.ssR], [P.g, P.stL] ], [ [P.g, P.ssR, P.stL] ] ],
                couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(1,0,1):C.R2GC_361_123,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121,(0,0,1):C.R2GC_360_119})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.stL__tilde__, P.stL__tilde__, P.stL, P.stL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t] ], [ [P.g, P.stL] ] ],
                 couplings = {(1,0,0):C.R2GC_162_66,(1,0,2):C.R2GC_162_68,(1,0,1):C.R2GC_162_67,(0,0,0):C.R2GC_162_66,(0,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_67})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.sbL__tilde__, P.sbL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.stR] ], [ [P.g, P.sbL, P.stR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.sbR__tilde__, P.sbR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.stR] ], [ [P.g, P.sbR, P.stR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.scL__tilde__, P.scL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.stR] ], [ [P.g, P.scL, P.stR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.scR__tilde__, P.scR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.stR] ], [ [P.g, P.scR, P.stR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.sdL__tilde__, P.sdL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sdL], [P.g, P.stR] ], [ [P.g, P.sdL, P.stR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.sdR__tilde__, P.sdR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.g, P.sdR], [P.g, P.stR] ], [ [P.g, P.sdR, P.stR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.ssL__tilde__, P.ssL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.t] ], [ [P.g, P.ssL], [P.g, P.stR] ], [ [P.g, P.ssL, P.stR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(1,0,1):C.R2GC_361_123,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121,(0,0,1):C.R2GC_360_119})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.ssR__tilde__, P.ssR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.t] ], [ [P.g, P.ssR], [P.g, P.stR] ], [ [P.g, P.ssR, P.stR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,3):C.R2GC_365_128,(1,0,1):C.R2GC_365_127,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,3):C.R2GC_364_126,(0,0,1):C.R2GC_364_125})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.stL__tilde__, P.stL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t] ], [ [P.g, P.stL], [P.g, P.stR] ], [ [P.g, P.stL, P.stR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,1):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,1):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.stR__tilde__, P.stR__tilde__, P.stR, P.stR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t] ], [ [P.g, P.stR] ] ],
                 couplings = {(1,0,0):C.R2GC_162_66,(1,0,2):C.R2GC_162_68,(1,0,1):C.R2GC_162_67,(0,0,0):C.R2GC_162_66,(0,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_67})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.sbL__tilde__, P.sbL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.suL] ], [ [P.g, P.sbL, P.suL] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.sbR__tilde__, P.sbR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.suL] ], [ [P.g, P.sbR, P.suL] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.scL__tilde__, P.scL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.suL] ], [ [P.g, P.scL, P.suL] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.scR__tilde__, P.scR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.suL] ], [ [P.g, P.scR, P.suL] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.sdL__tilde__, P.sdL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sdL], [P.g, P.suL] ], [ [P.g, P.sdL, P.suL] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.sdR__tilde__, P.sdR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sdR], [P.g, P.suL] ], [ [P.g, P.sdR, P.suL] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.ssL__tilde__, P.ssL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.u] ], [ [P.g, P.ssL], [P.g, P.suL] ], [ [P.g, P.ssL, P.suL] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,3):C.R2GC_365_128,(1,0,1):C.R2GC_365_127,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,3):C.R2GC_364_126,(0,0,1):C.R2GC_364_125})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.ssR__tilde__, P.ssR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.u] ], [ [P.g, P.ssR], [P.g, P.suL] ], [ [P.g, P.ssR, P.suL] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(1,0,1):C.R2GC_361_123,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121,(0,0,1):C.R2GC_360_119})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.stL__tilde__, P.stL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t, P.u] ], [ [P.g, P.stL], [P.g, P.suL] ], [ [P.g, P.stL, P.suL] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,3):C.R2GC_365_128,(1,0,1):C.R2GC_365_127,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,3):C.R2GC_364_126,(0,0,1):C.R2GC_364_125})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.stR__tilde__, P.stR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t, P.u] ], [ [P.g, P.stR], [P.g, P.suL] ], [ [P.g, P.stR, P.suL] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(1,0,1):C.R2GC_361_123,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121,(0,0,1):C.R2GC_360_119})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.suL__tilde__, P.suL__tilde__, P.suL, P.suL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.u] ], [ [P.g, P.suL] ] ],
                 couplings = {(1,0,0):C.R2GC_162_66,(1,0,2):C.R2GC_162_68,(1,0,1):C.R2GC_162_67,(0,0,0):C.R2GC_162_66,(0,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_67})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.sbL__tilde__, P.sbL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sbL], [P.g, P.suR] ], [ [P.g, P.sbL, P.suR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.sbR__tilde__, P.sbR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sbR], [P.g, P.suR] ], [ [P.g, P.sbR, P.suR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.scL__tilde__, P.scL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.g, P.scL], [P.g, P.suR] ], [ [P.g, P.scL, P.suR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.scR__tilde__, P.scR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.g, P.scR], [P.g, P.suR] ], [ [P.g, P.scR, P.suR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.sdL__tilde__, P.sdL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sdL], [P.g, P.suR] ], [ [P.g, P.sdL, P.suR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,0):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,0):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.sdR__tilde__, P.sdR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.g, P.sdR], [P.g, P.suR] ], [ [P.g, P.sdR, P.suR] ] ],
                 couplings = {(1,0,1):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,0):C.R2GC_365_127,(1,0,3):C.R2GC_365_128,(0,0,1):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,0):C.R2GC_364_125,(0,0,3):C.R2GC_364_126})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.ssL__tilde__, P.ssL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.u] ], [ [P.g, P.ssL], [P.g, P.suR] ], [ [P.g, P.ssL, P.suR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(1,0,1):C.R2GC_361_123,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121,(0,0,1):C.R2GC_360_119})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.ssR__tilde__, P.ssR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s, P.u] ], [ [P.g, P.ssR], [P.g, P.suR] ], [ [P.g, P.ssR, P.suR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,3):C.R2GC_365_128,(1,0,1):C.R2GC_365_127,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,3):C.R2GC_364_126,(0,0,1):C.R2GC_364_125})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.stL__tilde__, P.stL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t, P.u] ], [ [P.g, P.stL], [P.g, P.suR] ], [ [P.g, P.stL, P.suR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,3):C.R2GC_161_65,(1,0,1):C.R2GC_361_123,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,3):C.R2GC_360_121,(0,0,1):C.R2GC_360_119})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.stR__tilde__, P.stR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t, P.u] ], [ [P.g, P.stR], [P.g, P.suR] ], [ [P.g, P.stR, P.suR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_364_124,(1,0,3):C.R2GC_365_128,(1,0,1):C.R2GC_365_127,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_364_124,(0,0,3):C.R2GC_364_126,(0,0,1):C.R2GC_364_125})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.suL__tilde__, P.suL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.u] ], [ [P.g, P.suL], [P.g, P.suR] ], [ [P.g, P.suL, P.suR] ] ],
                 couplings = {(1,0,0):C.R2GC_361_122,(1,0,2):C.R2GC_100_2,(1,0,1):C.R2GC_361_123,(1,0,3):C.R2GC_161_65,(0,0,0):C.R2GC_360_118,(0,0,2):C.R2GC_360_120,(0,0,1):C.R2GC_360_119,(0,0,3):C.R2GC_360_121})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.suR__tilde__, P.suR__tilde__, P.suR, P.suR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.u] ], [ [P.g, P.suR] ] ],
                 couplings = {(1,0,0):C.R2GC_162_66,(1,0,2):C.R2GC_162_68,(1,0,1):C.R2GC_162_67,(0,0,0):C.R2GC_162_66,(0,0,2):C.R2GC_162_68,(0,0,1):C.R2GC_162_67})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.g, P.scL__tilde__, P.scL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g, P.scL] ] ],
                 couplings = {(0,0,0):C.R2GC_159_60,(0,0,1):C.R2GC_159_61})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.g, P.stL__tilde__, P.stL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ], [ [P.g, P.stL] ] ],
                 couplings = {(0,0,1):C.R2GC_159_61,(0,0,0):C.R2GC_159_60})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.g, P.suL__tilde__, P.suL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.u] ], [ [P.g, P.suL] ] ],
                 couplings = {(0,0,1):C.R2GC_159_61,(0,0,0):C.R2GC_159_60})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.g, P.g, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.g, P.scL] ] ],
                 couplings = {(2,0,1):C.R2GC_161_63,(2,0,0):C.R2GC_161_64,(2,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_63,(1,0,0):C.R2GC_161_64,(1,0,2):C.R2GC_161_65,(0,0,1):C.R2GC_103_8,(0,0,0):C.R2GC_110_22,(0,0,2):C.R2GC_160_62})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.g, P.g, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t] ], [ [P.g, P.stL] ] ],
                 couplings = {(2,0,0):C.R2GC_161_63,(2,0,2):C.R2GC_161_65,(2,0,1):C.R2GC_161_64,(1,0,0):C.R2GC_161_63,(1,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_64,(0,0,0):C.R2GC_103_8,(0,0,2):C.R2GC_160_62,(0,0,1):C.R2GC_110_22})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.g, P.g, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.u] ], [ [P.g, P.suL] ] ],
                 couplings = {(2,0,0):C.R2GC_161_63,(2,0,2):C.R2GC_161_65,(2,0,1):C.R2GC_161_64,(1,0,0):C.R2GC_161_63,(1,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_64,(0,0,0):C.R2GC_103_8,(0,0,2):C.R2GC_160_62,(0,0,1):C.R2GC_110_22})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.g, P.scR__tilde__, P.scR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g, P.scR] ] ],
                 couplings = {(0,0,0):C.R2GC_159_60,(0,0,1):C.R2GC_159_61})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.g, P.stR__tilde__, P.stR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ], [ [P.g, P.stR] ] ],
                 couplings = {(0,0,1):C.R2GC_159_61,(0,0,0):C.R2GC_159_60})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.g, P.suR__tilde__, P.suR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.u] ], [ [P.g, P.suR] ] ],
                 couplings = {(0,0,1):C.R2GC_159_61,(0,0,0):C.R2GC_159_60})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.g, P.g, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.g, P.scR] ] ],
                 couplings = {(2,0,1):C.R2GC_161_63,(2,0,0):C.R2GC_161_64,(2,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_63,(1,0,0):C.R2GC_161_64,(1,0,2):C.R2GC_161_65,(0,0,1):C.R2GC_103_8,(0,0,0):C.R2GC_110_22,(0,0,2):C.R2GC_160_62})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.g, P.g, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.t] ], [ [P.g, P.stR] ] ],
                 couplings = {(2,0,0):C.R2GC_161_63,(2,0,2):C.R2GC_161_65,(2,0,1):C.R2GC_161_64,(1,0,0):C.R2GC_161_63,(1,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_64,(0,0,0):C.R2GC_103_8,(0,0,2):C.R2GC_160_62,(0,0,1):C.R2GC_110_22})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.g, P.g, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.u] ], [ [P.g, P.suR] ] ],
                 couplings = {(2,0,0):C.R2GC_161_63,(2,0,2):C.R2GC_161_65,(2,0,1):C.R2GC_161_64,(1,0,0):C.R2GC_161_63,(1,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_64,(0,0,0):C.R2GC_103_8,(0,0,2):C.R2GC_160_62,(0,0,1):C.R2GC_110_22})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.sbL__tilde__, P.sbL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g, P.sbL] ] ],
                 couplings = {(0,0,0):C.R2GC_159_60,(0,0,1):C.R2GC_159_61})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.g, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g, P.sdL] ] ],
                 couplings = {(0,0,0):C.R2GC_159_60,(0,0,1):C.R2GC_159_61})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.g, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.g, P.ssL] ] ],
                 couplings = {(0,0,1):C.R2GC_159_61,(0,0,0):C.R2GC_159_60})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.g, P.g, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.g, P.sbL] ] ],
                 couplings = {(2,0,1):C.R2GC_161_63,(2,0,0):C.R2GC_161_64,(2,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_63,(1,0,0):C.R2GC_161_64,(1,0,2):C.R2GC_161_65,(0,0,1):C.R2GC_103_8,(0,0,0):C.R2GC_110_22,(0,0,2):C.R2GC_160_62})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.g, P.g, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.g, P.sdL] ] ],
                 couplings = {(2,0,1):C.R2GC_161_63,(2,0,0):C.R2GC_161_64,(2,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_63,(1,0,0):C.R2GC_161_64,(1,0,2):C.R2GC_161_65,(0,0,1):C.R2GC_103_8,(0,0,0):C.R2GC_110_22,(0,0,2):C.R2GC_160_62})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.g, P.g, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s] ], [ [P.g, P.ssL] ] ],
                 couplings = {(2,0,0):C.R2GC_161_63,(2,0,2):C.R2GC_161_65,(2,0,1):C.R2GC_161_64,(1,0,0):C.R2GC_161_63,(1,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_64,(0,0,0):C.R2GC_103_8,(0,0,2):C.R2GC_160_62,(0,0,1):C.R2GC_110_22})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.g, P.sbR__tilde__, P.sbR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g, P.sbR] ] ],
                 couplings = {(0,0,0):C.R2GC_159_60,(0,0,1):C.R2GC_159_61})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.g, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g, P.sdR] ] ],
                 couplings = {(0,0,0):C.R2GC_159_60,(0,0,1):C.R2GC_159_61})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.g, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.g, P.ssR] ] ],
                 couplings = {(0,0,1):C.R2GC_159_61,(0,0,0):C.R2GC_159_60})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.g, P.g, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.g, P.sbR] ] ],
                 couplings = {(2,0,1):C.R2GC_161_63,(2,0,0):C.R2GC_161_64,(2,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_63,(1,0,0):C.R2GC_161_64,(1,0,2):C.R2GC_161_65,(0,0,1):C.R2GC_103_8,(0,0,0):C.R2GC_110_22,(0,0,2):C.R2GC_160_62})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.g, P.g, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.g, P.sdR] ] ],
                 couplings = {(2,0,1):C.R2GC_161_63,(2,0,0):C.R2GC_161_64,(2,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_63,(1,0,0):C.R2GC_161_64,(1,0,2):C.R2GC_161_65,(0,0,1):C.R2GC_103_8,(0,0,0):C.R2GC_110_22,(0,0,2):C.R2GC_160_62})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.g, P.g, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go, P.s] ], [ [P.g, P.ssR] ] ],
                 couplings = {(2,0,0):C.R2GC_161_63,(2,0,2):C.R2GC_161_65,(2,0,1):C.R2GC_161_64,(1,0,0):C.R2GC_161_63,(1,0,2):C.R2GC_161_65,(1,0,1):C.R2GC_161_64,(0,0,0):C.R2GC_103_8,(0,0,2):C.R2GC_160_62,(0,0,1):C.R2GC_110_22})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_131_46})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_131_46})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_131_46})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.suL] ], [ [P.go, P.suR] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.R2GC_118_34,(0,1,0):C.R2GC_203_77,(0,2,1):C.R2GC_203_77})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.go, P.scL] ], [ [P.go, P.scR] ] ],
                 couplings = {(0,0,0):C.R2GC_118_34,(0,1,1):C.R2GC_203_77,(0,2,2):C.R2GC_203_77})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,2):C.R2GC_118_34,(0,1,0):C.R2GC_203_77,(0,2,1):C.R2GC_203_77})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_351_111})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_351_111})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_351_111})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_212_80,(0,1,0):C.R2GC_216_81})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_212_80,(0,1,0):C.R2GC_216_81})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_212_80,(0,1,0):C.R2GC_216_81})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_117_33})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_117_33})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_117_33})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.go, P.sdL] ], [ [P.go, P.sdR] ] ],
                 couplings = {(0,0,0):C.R2GC_118_34,(0,1,1):C.R2GC_203_77,(0,2,2):C.R2GC_203_77})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.ssL] ], [ [P.go, P.ssR] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,2):C.R2GC_118_34,(0,1,0):C.R2GC_203_77,(0,2,1):C.R2GC_203_77})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.go, P.sbL] ], [ [P.go, P.sbR] ] ],
                 couplings = {(0,0,0):C.R2GC_118_34,(0,1,1):C.R2GC_203_77,(0,2,2):C.R2GC_203_77})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_351_111})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_351_111})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_351_111})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_204_78,(0,1,0):C.R2GC_208_79})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_204_78,(0,1,0):C.R2GC_208_79})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_204_78,(0,1,0):C.R2GC_208_79})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.go, P.go ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF4, L.FF5, L.FF6 ],
                 loop_particles = [ [ [P.g, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_342_99,(0,2,0):C.R2GC_342_99,(0,1,0):C.R2GC_200_76,(0,3,0):C.R2GC_200_76})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_116_32})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_116_32})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF4, L.FF5, L.FF6 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_265_84,(0,2,0):C.R2GC_265_84,(0,1,0):C.R2GC_116_32,(0,3,0):C.R2GC_116_32})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_116_32})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_116_32})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_116_32})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.u] ], [ [P.g, P.suL] ] ],
                 couplings = {(0,0,1):C.R2GC_330_96,(0,0,0):C.R2GC_163_69,(0,1,1):C.R2GC_158_59,(0,1,0):C.R2GC_158_58})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.scL__tilde__, P.scL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g, P.scL] ] ],
                 couplings = {(0,0,0):C.R2GC_163_69,(0,0,1):C.R2GC_175_72,(0,1,0):C.R2GC_158_58,(0,1,1):C.R2GC_158_59})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.t] ], [ [P.g, P.stL] ] ],
                 couplings = {(0,0,1):C.R2GC_292_87,(0,0,0):C.R2GC_292_88,(0,1,1):C.R2GC_158_59,(0,1,0):C.R2GC_158_58})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.u] ], [ [P.g, P.suR] ] ],
                 couplings = {(0,0,1):C.R2GC_331_97,(0,0,0):C.R2GC_163_69,(0,1,1):C.R2GC_158_59,(0,1,0):C.R2GC_158_58})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.scR__tilde__, P.scR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g, P.scR] ] ],
                 couplings = {(0,0,0):C.R2GC_163_69,(0,0,1):C.R2GC_181_73,(0,1,0):C.R2GC_158_58,(0,1,1):C.R2GC_158_59})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.t] ], [ [P.g, P.stR] ] ],
                 couplings = {(0,0,1):C.R2GC_293_89,(0,0,0):C.R2GC_292_88,(0,1,1):C.R2GC_158_59,(0,1,0):C.R2GC_158_58})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g, P.sdL] ] ],
                 couplings = {(0,0,0):C.R2GC_163_69,(0,0,1):C.R2GC_187_74,(0,1,0):C.R2GC_158_58,(0,1,1):C.R2GC_158_59})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.g, P.ssL] ] ],
                 couplings = {(0,0,1):C.R2GC_247_82,(0,0,0):C.R2GC_163_69,(0,1,1):C.R2GC_158_59,(0,1,0):C.R2GC_158_58})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g, P.sbL] ] ],
                 couplings = {(0,0,0):C.R2GC_163_69,(0,0,1):C.R2GC_163_70,(0,1,0):C.R2GC_158_58,(0,1,1):C.R2GC_158_59})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g, P.sdR] ] ],
                 couplings = {(0,0,0):C.R2GC_163_69,(0,0,1):C.R2GC_193_75,(0,1,0):C.R2GC_158_58,(0,1,1):C.R2GC_158_59})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.g, P.ssR] ] ],
                 couplings = {(0,0,1):C.R2GC_248_83,(0,0,0):C.R2GC_163_69,(0,1,1):C.R2GC_158_59,(0,1,0):C.R2GC_158_58})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g, P.sbR] ] ],
                 couplings = {(0,0,0):C.R2GC_163_69,(0,0,1):C.R2GC_169_71,(0,1,0):C.R2GC_158_58,(0,1,1):C.R2GC_158_59})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.go] ], [ [P.t] ] ],
                 couplings = {(0,0,1):C.R2GC_106_12,(0,1,2):C.R2GC_77_146,(0,1,3):C.R2GC_77_147,(0,2,0):C.R2GC_107_13,(0,2,1):C.R2GC_107_14,(0,2,2):C.R2GC_107_15})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.go, P.go, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.sbL], [P.d, P.sdL], [P.s, P.ssL] ], [ [P.b, P.sbR], [P.d, P.sdR], [P.s, P.ssR] ], [ [P.c, P.scL], [P.stL, P.t], [P.suL, P.u] ], [ [P.c, P.scR], [P.stR, P.t], [P.suR, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_344_100,(0,0,1):C.R2GC_344_101,(0,0,2):C.R2GC_344_102,(0,0,3):C.R2GC_344_103})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.go, P.go, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.sbL], [P.d, P.sdL], [P.s, P.ssL] ], [ [P.b, P.sbR], [P.d, P.sdR], [P.s, P.ssR] ], [ [P.c, P.scL], [P.stL, P.t], [P.suL, P.u] ], [ [P.c, P.scR], [P.stR, P.t], [P.suR, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_346_104,(0,0,1):C.R2GC_346_105,(0,0,2):C.R2GC_346_106,(0,0,3):C.R2GC_346_107})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.chi, P.go, P.g ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.sbL], [P.c, P.scL], [P.d, P.sdL], [P.s, P.ssL], [P.stL, P.t], [P.suL, P.u] ], [ [P.b, P.sbR], [P.d, P.sdR], [P.s, P.ssR] ], [ [P.c, P.scR], [P.stR, P.t], [P.suR, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_90_167,(0,0,1):C.R2GC_90_168,(0,0,2):C.R2GC_90_169})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVV1, L.VVV2 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_80_152,(0,0,1):C.R2GC_80_153,(0,1,0):C.R2GC_80_153,(0,1,1):C.R2GC_80_152})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_74_144})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.a, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_133_47,(0,1,0):C.R2GC_320_95})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_136_50,(0,1,0):C.R2GC_333_98})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.a, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_133_47})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_136_50})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.a, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_133_47})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_136_50})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.a, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_133_47})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_137_51})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.a, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_133_47})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_137_51})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.a, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_133_47})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_137_51})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.W__plus__, P.sdL, P.suL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_354_114})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.W__minus__, P.sdL__tilde__, P.suL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_355_115})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.a, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_119_35})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_122_38})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.W__plus__, P.scL__tilde__, P.ssL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_355_115})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.W__minus__, P.scL, P.ssL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_354_114})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.a, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_119_35})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_122_38})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.W__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_354_114})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.W__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_355_115})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.a, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_119_35})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_122_38})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.a, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_119_35})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_123_39})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.a, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_119_35})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_123_39})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.a, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_119_35})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_123_39})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.H, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_305_93})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.H, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_303_91})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.G0, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_304_92})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.H, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_303_91})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.G0, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_302_90})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.H, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_305_93})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.G__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_450_134})

V_244 = CTVertex(name = 'V_244',
                 type = 'R2',
                 particles = [ P.G__plus__, P.sbL, P.stR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_447_131})

V_245 = CTVertex(name = 'V_245',
                 type = 'R2',
                 particles = [ P.G__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_449_133})

V_246 = CTVertex(name = 'V_246',
                 type = 'R2',
                 particles = [ P.G__minus__, P.sbL__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_448_132})

V_247 = CTVertex(name = 'V_247',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_86_162})

V_248 = CTVertex(name = 'V_248',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_82_154,(0,0,1):C.R2GC_82_155})

V_249 = CTVertex(name = 'V_249',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_85_160,(0,0,1):C.R2GC_85_161})

V_250 = CTVertex(name = 'V_250',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_78_148,(0,0,1):C.R2GC_78_149})

V_251 = CTVertex(name = 'V_251',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,0,0):C.R2GC_84_158,(1,0,1):C.R2GC_84_159,(0,1,0):C.R2GC_83_156,(0,1,1):C.R2GC_83_157})

V_252 = CTVertex(name = 'V_252',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_79_150,(0,0,1):C.R2GC_79_151})

V_253 = CTVertex(name = 'V_253',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_75_145})

V_254 = CTVertex(name = 'V_254',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_75_145})

V_255 = CTVertex(name = 'V_255',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_75_145})

V_256 = CTVertex(name = 'V_256',
                 type = 'R2',
                 particles = [ P.a, P.a, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_134_48})

V_257 = CTVertex(name = 'V_257',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_353_113})

V_258 = CTVertex(name = 'V_258',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_138_52})

V_259 = CTVertex(name = 'V_259',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_142_56})

V_260 = CTVertex(name = 'V_260',
                 type = 'R2',
                 particles = [ P.a, P.g, P.suL__tilde__, P.suL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_135_49})

V_261 = CTVertex(name = 'V_261',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_140_54})

V_262 = CTVertex(name = 'V_262',
                 type = 'R2',
                 particles = [ P.a, P.a, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_134_48})

V_263 = CTVertex(name = 'V_263',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_353_113})

V_264 = CTVertex(name = 'V_264',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_138_52})

V_265 = CTVertex(name = 'V_265',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_142_56})

V_266 = CTVertex(name = 'V_266',
                 type = 'R2',
                 particles = [ P.a, P.g, P.scL__tilde__, P.scL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_135_49})

V_267 = CTVertex(name = 'V_267',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_140_54})

V_268 = CTVertex(name = 'V_268',
                 type = 'R2',
                 particles = [ P.a, P.a, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_134_48})

V_269 = CTVertex(name = 'V_269',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_353_113})

V_270 = CTVertex(name = 'V_270',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_138_52})

V_271 = CTVertex(name = 'V_271',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_142_56})

V_272 = CTVertex(name = 'V_272',
                 type = 'R2',
                 particles = [ P.a, P.g, P.stL__tilde__, P.stL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_135_49})

V_273 = CTVertex(name = 'V_273',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_140_54})

V_274 = CTVertex(name = 'V_274',
                 type = 'R2',
                 particles = [ P.a, P.a, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_134_48})

V_275 = CTVertex(name = 'V_275',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_139_53})

V_276 = CTVertex(name = 'V_276',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_143_57})

V_277 = CTVertex(name = 'V_277',
                 type = 'R2',
                 particles = [ P.a, P.g, P.suR__tilde__, P.suR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_135_49})

V_278 = CTVertex(name = 'V_278',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_141_55})

V_279 = CTVertex(name = 'V_279',
                 type = 'R2',
                 particles = [ P.a, P.a, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_134_48})

V_280 = CTVertex(name = 'V_280',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_139_53})

V_281 = CTVertex(name = 'V_281',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_143_57})

V_282 = CTVertex(name = 'V_282',
                 type = 'R2',
                 particles = [ P.a, P.g, P.scR__tilde__, P.scR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_135_49})

V_283 = CTVertex(name = 'V_283',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_141_55})

V_284 = CTVertex(name = 'V_284',
                 type = 'R2',
                 particles = [ P.a, P.a, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_134_48})

V_285 = CTVertex(name = 'V_285',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_139_53})

V_286 = CTVertex(name = 'V_286',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_143_57})

V_287 = CTVertex(name = 'V_287',
                 type = 'R2',
                 particles = [ P.a, P.g, P.stR__tilde__, P.stR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_135_49})

V_288 = CTVertex(name = 'V_288',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_141_55})

V_289 = CTVertex(name = 'V_289',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.sdL, P.suL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_356_116})

V_290 = CTVertex(name = 'V_290',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.sdL, P.suL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_352_112})

V_291 = CTVertex(name = 'V_291',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.sdL, P.suL__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_357_117})

V_292 = CTVertex(name = 'V_292',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.sdL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_356_116})

V_293 = CTVertex(name = 'V_293',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.sdL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_352_112})

V_294 = CTVertex(name = 'V_294',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.sdL__tilde__, P.suL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_357_117})

V_295 = CTVertex(name = 'V_295',
                 type = 'R2',
                 particles = [ P.a, P.a, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_120_36})

V_296 = CTVertex(name = 'V_296',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_353_113})

V_297 = CTVertex(name = 'V_297',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_124_40})

V_298 = CTVertex(name = 'V_298',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_128_44})

V_299 = CTVertex(name = 'V_299',
                 type = 'R2',
                 particles = [ P.a, P.g, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_121_37})

V_300 = CTVertex(name = 'V_300',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_126_42})

V_301 = CTVertex(name = 'V_301',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.scL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_356_116})

V_302 = CTVertex(name = 'V_302',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.scL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_352_112})

V_303 = CTVertex(name = 'V_303',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.scL__tilde__, P.ssL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_357_117})

V_304 = CTVertex(name = 'V_304',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.scL, P.ssL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_356_116})

V_305 = CTVertex(name = 'V_305',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.scL, P.ssL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_352_112})

V_306 = CTVertex(name = 'V_306',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.scL, P.ssL__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_357_117})

V_307 = CTVertex(name = 'V_307',
                 type = 'R2',
                 particles = [ P.a, P.a, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_120_36})

V_308 = CTVertex(name = 'V_308',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_353_113})

V_309 = CTVertex(name = 'V_309',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_124_40})

V_310 = CTVertex(name = 'V_310',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_128_44})

V_311 = CTVertex(name = 'V_311',
                 type = 'R2',
                 particles = [ P.a, P.g, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_121_37})

V_312 = CTVertex(name = 'V_312',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_126_42})

V_313 = CTVertex(name = 'V_313',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_356_116})

V_314 = CTVertex(name = 'V_314',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_352_112})

V_315 = CTVertex(name = 'V_315',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_357_117})

V_316 = CTVertex(name = 'V_316',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_356_116})

V_317 = CTVertex(name = 'V_317',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_352_112})

V_318 = CTVertex(name = 'V_318',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_357_117})

V_319 = CTVertex(name = 'V_319',
                 type = 'R2',
                 particles = [ P.a, P.a, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_120_36})

V_320 = CTVertex(name = 'V_320',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_353_113})

V_321 = CTVertex(name = 'V_321',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_124_40})

V_322 = CTVertex(name = 'V_322',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_128_44})

V_323 = CTVertex(name = 'V_323',
                 type = 'R2',
                 particles = [ P.a, P.g, P.sbL__tilde__, P.sbL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_121_37})

V_324 = CTVertex(name = 'V_324',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_126_42})

V_325 = CTVertex(name = 'V_325',
                 type = 'R2',
                 particles = [ P.a, P.a, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_120_36})

V_326 = CTVertex(name = 'V_326',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_125_41})

V_327 = CTVertex(name = 'V_327',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_129_45})

V_328 = CTVertex(name = 'V_328',
                 type = 'R2',
                 particles = [ P.a, P.g, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_121_37})

V_329 = CTVertex(name = 'V_329',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_127_43})

V_330 = CTVertex(name = 'V_330',
                 type = 'R2',
                 particles = [ P.a, P.a, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_120_36})

V_331 = CTVertex(name = 'V_331',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_125_41})

V_332 = CTVertex(name = 'V_332',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_129_45})

V_333 = CTVertex(name = 'V_333',
                 type = 'R2',
                 particles = [ P.a, P.g, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_121_37})

V_334 = CTVertex(name = 'V_334',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_127_43})

V_335 = CTVertex(name = 'V_335',
                 type = 'R2',
                 particles = [ P.a, P.a, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_120_36})

V_336 = CTVertex(name = 'V_336',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_125_41})

V_337 = CTVertex(name = 'V_337',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_129_45})

V_338 = CTVertex(name = 'V_338',
                 type = 'R2',
                 particles = [ P.a, P.g, P.sbR__tilde__, P.sbR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_121_37})

V_339 = CTVertex(name = 'V_339',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.R2GC_127_43})

V_340 = CTVertex(name = 'V_340',
                 type = 'R2',
                 particles = [ P.H, P.H, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_306_94})

V_341 = CTVertex(name = 'V_341',
                 type = 'R2',
                 particles = [ P.G0, P.G0, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_306_94})

V_342 = CTVertex(name = 'V_342',
                 type = 'R2',
                 particles = [ P.H, P.H, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_306_94})

V_343 = CTVertex(name = 'V_343',
                 type = 'R2',
                 particles = [ P.G0, P.G0, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_306_94})

V_344 = CTVertex(name = 'V_344',
                 type = 'R2',
                 particles = [ P.G__minus__, P.G__plus__, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_306_94})

V_345 = CTVertex(name = 'V_345',
                 type = 'R2',
                 particles = [ P.G__plus__, P.H, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_454_137})

V_346 = CTVertex(name = 'V_346',
                 type = 'R2',
                 particles = [ P.G0, P.G__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_453_136})

V_347 = CTVertex(name = 'V_347',
                 type = 'R2',
                 particles = [ P.G__minus__, P.H, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_452_135})

V_348 = CTVertex(name = 'V_348',
                 type = 'R2',
                 particles = [ P.G0, P.G__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_453_136})

V_349 = CTVertex(name = 'V_349',
                 type = 'R2',
                 particles = [ P.G__minus__, P.G__plus__, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_306_94})

V_350 = CTVertex(name = 'V_350',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_109_112,(0,0,1):C.UVGC_109_113,(0,0,2):C.UVGC_109_114,(0,0,3):C.UVGC_109_115,(0,0,4):C.UVGC_109_116,(0,0,5):C.UVGC_109_117,(0,0,6):C.UVGC_109_118,(0,0,7):C.UVGC_109_119,(0,0,8):C.UVGC_109_120,(0,0,9):C.UVGC_109_121,(0,0,10):C.UVGC_109_122,(0,0,11):C.UVGC_109_123,(0,0,12):C.UVGC_109_124,(0,0,13):C.UVGC_109_125,(0,0,14):C.UVGC_109_126,(0,0,15):C.UVGC_109_127,(0,0,16):C.UVGC_109_128,(0,0,17):C.UVGC_109_129,(0,0,18):C.UVGC_109_130,(0,0,19):C.UVGC_109_131,(0,0,20):C.UVGC_109_132,(0,1,0):C.UVGC_108_91,(0,1,1):C.UVGC_108_92,(0,1,2):C.UVGC_108_93,(0,1,3):C.UVGC_108_94,(0,1,4):C.UVGC_108_95,(0,1,5):C.UVGC_108_96,(0,1,6):C.UVGC_108_97,(0,1,7):C.UVGC_108_98,(0,1,8):C.UVGC_108_99,(0,1,9):C.UVGC_108_100,(0,1,10):C.UVGC_108_101,(0,1,11):C.UVGC_108_102,(0,1,12):C.UVGC_108_103,(0,1,13):C.UVGC_108_104,(0,1,14):C.UVGC_108_105,(0,1,15):C.UVGC_108_106,(0,1,16):C.UVGC_108_107,(0,1,17):C.UVGC_108_108,(0,1,18):C.UVGC_108_109,(0,1,19):C.UVGC_108_110,(0,1,20):C.UVGC_108_111,(0,2,0):C.UVGC_108_91,(0,2,1):C.UVGC_108_92,(0,2,2):C.UVGC_108_93,(0,2,3):C.UVGC_108_94,(0,2,4):C.UVGC_108_95,(0,2,5):C.UVGC_108_96,(0,2,6):C.UVGC_108_97,(0,2,7):C.UVGC_108_98,(0,2,8):C.UVGC_108_99,(0,2,9):C.UVGC_108_100,(0,2,10):C.UVGC_108_101,(0,2,11):C.UVGC_108_102,(0,2,12):C.UVGC_108_103,(0,2,13):C.UVGC_108_104,(0,2,14):C.UVGC_108_105,(0,2,15):C.UVGC_108_106,(0,2,16):C.UVGC_108_107,(0,2,17):C.UVGC_108_108,(0,2,18):C.UVGC_108_109,(0,2,19):C.UVGC_108_110,(0,2,20):C.UVGC_108_111,(0,3,0):C.UVGC_109_112,(0,3,1):C.UVGC_109_113,(0,3,2):C.UVGC_109_114,(0,3,3):C.UVGC_109_115,(0,3,4):C.UVGC_109_116,(0,3,5):C.UVGC_109_117,(0,3,6):C.UVGC_109_118,(0,3,7):C.UVGC_109_119,(0,3,8):C.UVGC_109_120,(0,3,9):C.UVGC_109_121,(0,3,10):C.UVGC_109_122,(0,3,11):C.UVGC_109_123,(0,3,12):C.UVGC_109_124,(0,3,13):C.UVGC_109_125,(0,3,14):C.UVGC_109_126,(0,3,15):C.UVGC_109_127,(0,3,16):C.UVGC_109_128,(0,3,17):C.UVGC_109_129,(0,3,18):C.UVGC_109_130,(0,3,19):C.UVGC_109_131,(0,3,20):C.UVGC_109_132,(0,4,0):C.UVGC_109_112,(0,4,1):C.UVGC_109_113,(0,4,2):C.UVGC_109_114,(0,4,3):C.UVGC_109_115,(0,4,4):C.UVGC_109_116,(0,4,5):C.UVGC_109_117,(0,4,6):C.UVGC_109_118,(0,4,7):C.UVGC_109_119,(0,4,8):C.UVGC_109_120,(0,4,9):C.UVGC_109_121,(0,4,10):C.UVGC_109_122,(0,4,11):C.UVGC_109_123,(0,4,12):C.UVGC_109_124,(0,4,13):C.UVGC_109_125,(0,4,14):C.UVGC_109_126,(0,4,15):C.UVGC_109_127,(0,4,16):C.UVGC_109_128,(0,4,17):C.UVGC_109_129,(0,4,18):C.UVGC_109_130,(0,4,19):C.UVGC_109_131,(0,4,20):C.UVGC_109_132,(0,5,0):C.UVGC_108_91,(0,5,1):C.UVGC_108_92,(0,5,2):C.UVGC_108_93,(0,5,3):C.UVGC_108_94,(0,5,4):C.UVGC_108_95,(0,5,5):C.UVGC_108_96,(0,5,6):C.UVGC_108_97,(0,5,7):C.UVGC_108_98,(0,5,8):C.UVGC_108_99,(0,5,9):C.UVGC_108_100,(0,5,10):C.UVGC_108_101,(0,5,11):C.UVGC_108_102,(0,5,12):C.UVGC_108_103,(0,5,13):C.UVGC_108_104,(0,5,14):C.UVGC_108_105,(0,5,15):C.UVGC_108_106,(0,5,16):C.UVGC_108_107,(0,5,17):C.UVGC_108_108,(0,5,18):C.UVGC_108_109,(0,5,19):C.UVGC_108_110,(0,5,20):C.UVGC_108_111})

V_351 = CTVertex(name = 'V_351',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.sbL], [P.sbR], [P.scL], [P.scR], [P.sdL], [P.sdR], [P.ssL], [P.ssR], [P.stL], [P.stR], [P.suL], [P.suR], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbL], [P.sbR], [P.scL], [P.scR], [P.sdL], [P.sdR], [P.ssL], [P.ssR], [P.stL], [P.stR], [P.suL], [P.suR] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,5):C.UVGC_100_2,(2,0,6):C.UVGC_100_1,(0,0,5):C.UVGC_100_2,(0,0,6):C.UVGC_100_1,(4,0,5):C.UVGC_99_1085,(4,0,6):C.UVGC_99_1086,(3,0,5):C.UVGC_99_1085,(3,0,6):C.UVGC_99_1086,(8,0,5):C.UVGC_100_1,(8,0,6):C.UVGC_100_2,(6,0,0):C.UVGC_112_137,(6,0,3):C.UVGC_112_138,(6,0,4):C.UVGC_112_139,(6,0,5):C.UVGC_112_140,(6,0,6):C.UVGC_112_141,(6,0,7):C.UVGC_112_142,(6,0,8):C.UVGC_112_143,(6,0,9):C.UVGC_112_144,(6,0,11):C.UVGC_112_145,(6,0,12):C.UVGC_112_146,(6,0,13):C.UVGC_112_147,(6,0,14):C.UVGC_112_148,(6,0,15):C.UVGC_112_149,(6,0,16):C.UVGC_112_150,(6,0,17):C.UVGC_112_151,(6,0,18):C.UVGC_112_152,(6,0,19):C.UVGC_112_153,(6,0,20):C.UVGC_112_154,(6,0,21):C.UVGC_112_155,(6,0,22):C.UVGC_112_156,(6,0,23):C.UVGC_112_157,(7,0,0):C.UVGC_112_137,(7,0,3):C.UVGC_112_138,(7,0,4):C.UVGC_112_139,(7,0,5):C.UVGC_105_31,(7,0,6):C.UVGC_113_158,(7,0,7):C.UVGC_112_142,(7,0,8):C.UVGC_112_143,(7,0,9):C.UVGC_112_144,(7,0,11):C.UVGC_112_145,(7,0,12):C.UVGC_112_146,(7,0,13):C.UVGC_112_147,(7,0,14):C.UVGC_112_148,(7,0,15):C.UVGC_112_149,(7,0,16):C.UVGC_112_150,(7,0,17):C.UVGC_112_151,(7,0,18):C.UVGC_112_152,(7,0,19):C.UVGC_112_153,(7,0,20):C.UVGC_112_154,(7,0,21):C.UVGC_112_155,(7,0,22):C.UVGC_112_156,(7,0,23):C.UVGC_112_157,(5,0,5):C.UVGC_99_1085,(5,0,6):C.UVGC_99_1086,(1,0,5):C.UVGC_99_1085,(1,0,6):C.UVGC_99_1086,(11,0,5):C.UVGC_103_5,(11,0,6):C.UVGC_103_6,(10,0,5):C.UVGC_103_5,(10,0,6):C.UVGC_103_6,(9,0,5):C.UVGC_102_3,(9,0,6):C.UVGC_102_4,(2,1,5):C.UVGC_100_2,(2,1,6):C.UVGC_100_1,(0,1,5):C.UVGC_100_2,(0,1,6):C.UVGC_100_1,(4,1,5):C.UVGC_99_1085,(4,1,6):C.UVGC_99_1086,(3,1,5):C.UVGC_99_1085,(3,1,6):C.UVGC_99_1086,(8,1,0):C.UVGC_105_28,(8,1,3):C.UVGC_105_29,(8,1,4):C.UVGC_105_30,(8,1,5):C.UVGC_105_31,(8,1,6):C.UVGC_105_32,(8,1,7):C.UVGC_105_33,(8,1,8):C.UVGC_105_34,(8,1,9):C.UVGC_105_35,(8,1,11):C.UVGC_105_36,(8,1,12):C.UVGC_105_37,(8,1,13):C.UVGC_105_38,(8,1,14):C.UVGC_105_39,(8,1,15):C.UVGC_105_40,(8,1,16):C.UVGC_105_41,(8,1,17):C.UVGC_105_42,(8,1,18):C.UVGC_105_43,(8,1,19):C.UVGC_105_44,(8,1,20):C.UVGC_105_45,(8,1,21):C.UVGC_105_46,(8,1,22):C.UVGC_105_47,(8,1,23):C.UVGC_105_48,(6,1,0):C.UVGC_114_159,(6,1,3):C.UVGC_114_160,(6,1,4):C.UVGC_114_161,(6,1,5):C.UVGC_115_179,(6,1,6):C.UVGC_115_180,(6,1,7):C.UVGC_114_163,(6,1,8):C.UVGC_114_164,(6,1,9):C.UVGC_115_181,(6,1,11):C.UVGC_115_182,(6,1,12):C.UVGC_115_183,(6,1,13):C.UVGC_115_184,(6,1,14):C.UVGC_115_185,(6,1,15):C.UVGC_115_186,(6,1,16):C.UVGC_115_187,(6,1,17):C.UVGC_115_188,(6,1,18):C.UVGC_115_189,(6,1,19):C.UVGC_115_190,(6,1,20):C.UVGC_115_191,(6,1,21):C.UVGC_115_192,(6,1,22):C.UVGC_114_177,(6,1,23):C.UVGC_114_178,(7,1,1):C.UVGC_110_133,(7,1,5):C.UVGC_100_1,(7,1,6):C.UVGC_111_136,(7,1,7):C.UVGC_110_134,(5,1,5):C.UVGC_99_1085,(5,1,6):C.UVGC_99_1086,(1,1,5):C.UVGC_99_1085,(1,1,6):C.UVGC_99_1086,(11,1,5):C.UVGC_103_5,(11,1,6):C.UVGC_103_6,(10,1,5):C.UVGC_103_5,(10,1,6):C.UVGC_103_6,(9,1,5):C.UVGC_102_3,(9,1,6):C.UVGC_102_4,(0,2,5):C.UVGC_100_2,(0,2,6):C.UVGC_100_1,(2,2,5):C.UVGC_100_2,(2,2,6):C.UVGC_100_1,(5,2,5):C.UVGC_99_1085,(5,2,6):C.UVGC_99_1086,(1,2,5):C.UVGC_99_1085,(1,2,6):C.UVGC_99_1086,(7,2,0):C.UVGC_114_159,(7,2,3):C.UVGC_114_160,(7,2,4):C.UVGC_114_161,(7,2,5):C.UVGC_104_10,(7,2,6):C.UVGC_114_162,(7,2,7):C.UVGC_114_163,(7,2,8):C.UVGC_114_164,(7,2,9):C.UVGC_114_165,(7,2,11):C.UVGC_114_166,(7,2,12):C.UVGC_114_167,(7,2,13):C.UVGC_114_168,(7,2,14):C.UVGC_114_169,(7,2,15):C.UVGC_114_170,(7,2,16):C.UVGC_114_171,(7,2,17):C.UVGC_114_172,(7,2,18):C.UVGC_114_173,(7,2,19):C.UVGC_114_174,(7,2,20):C.UVGC_114_175,(7,2,21):C.UVGC_114_176,(7,2,22):C.UVGC_114_177,(7,2,23):C.UVGC_114_178,(4,2,5):C.UVGC_99_1085,(4,2,6):C.UVGC_99_1086,(3,2,5):C.UVGC_99_1085,(3,2,6):C.UVGC_99_1086,(8,2,0):C.UVGC_104_7,(8,2,3):C.UVGC_104_8,(8,2,4):C.UVGC_104_9,(8,2,5):C.UVGC_104_10,(8,2,6):C.UVGC_104_11,(8,2,7):C.UVGC_104_12,(8,2,8):C.UVGC_104_13,(8,2,9):C.UVGC_104_14,(8,2,11):C.UVGC_104_15,(8,2,12):C.UVGC_104_16,(8,2,13):C.UVGC_104_17,(8,2,14):C.UVGC_104_18,(8,2,15):C.UVGC_104_19,(8,2,16):C.UVGC_104_20,(8,2,17):C.UVGC_104_21,(8,2,18):C.UVGC_104_22,(8,2,19):C.UVGC_104_23,(8,2,20):C.UVGC_104_24,(8,2,21):C.UVGC_104_25,(8,2,22):C.UVGC_104_26,(8,2,23):C.UVGC_104_27,(6,2,2):C.UVGC_110_133,(6,2,6):C.UVGC_102_3,(6,2,7):C.UVGC_110_134,(6,2,10):C.UVGC_110_135,(11,2,5):C.UVGC_103_5,(11,2,6):C.UVGC_103_6,(10,2,5):C.UVGC_103_5,(10,2,6):C.UVGC_103_6,(9,2,5):C.UVGC_102_3,(9,2,6):C.UVGC_102_4})

V_352 = CTVertex(name = 'V_352',
                 type = 'UV',
                 particles = [ P.go, P.go, P.g ],
                 color = [ 'f(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.go] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_345_617,(0,0,3):C.UVGC_345_618,(0,0,6):C.UVGC_345_619,(0,0,9):C.UVGC_345_620,(0,0,10):C.UVGC_345_621,(0,0,11):C.UVGC_345_622,(0,0,13):C.UVGC_345_623,(0,0,14):C.UVGC_345_624,(0,0,15):C.UVGC_345_625,(0,0,16):C.UVGC_345_626,(0,0,17):C.UVGC_345_627,(0,0,18):C.UVGC_345_628,(0,0,19):C.UVGC_345_629,(0,0,22):C.UVGC_345_630,(0,0,23):C.UVGC_345_631,(0,0,24):C.UVGC_345_632,(0,0,26):C.UVGC_345_633,(0,0,28):C.UVGC_345_634,(0,0,30):C.UVGC_345_635,(0,0,32):C.UVGC_345_636,(0,0,33):C.UVGC_345_637,(0,0,1):C.UVGC_345_638,(0,0,2):C.UVGC_345_639,(0,0,4):C.UVGC_345_640,(0,0,5):C.UVGC_345_641,(0,0,7):C.UVGC_345_642,(0,0,8):C.UVGC_345_643,(0,0,12):C.UVGC_345_644,(0,0,20):C.UVGC_345_645,(0,0,21):C.UVGC_345_646,(0,0,25):C.UVGC_345_647,(0,0,27):C.UVGC_345_648,(0,0,29):C.UVGC_345_649,(0,0,31):C.UVGC_345_650})

V_353 = CTVertex(name = 'V_353',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.go, P.sbL] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_432_920,(0,0,5):C.UVGC_432_921,(0,0,2):C.UVGC_432_922,(0,0,3):C.UVGC_432_923,(0,0,4):C.UVGC_432_924,(0,0,1):C.UVGC_432_925})

V_354 = CTVertex(name = 'V_354',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,2):C.UVGC_269_489,(0,0,0):C.UVGC_269_490,(0,0,1):C.UVGC_269_491})

V_355 = CTVertex(name = 'V_355',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,2):C.UVGC_268_486,(0,0,0):C.UVGC_268_487,(0,0,1):C.UVGC_268_488})

V_356 = CTVertex(name = 'V_356',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.go, P.sbL] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_431_914,(0,0,5):C.UVGC_431_915,(0,0,2):C.UVGC_431_916,(0,0,3):C.UVGC_431_917,(0,0,4):C.UVGC_431_918,(0,0,1):C.UVGC_431_919})

V_357 = CTVertex(name = 'V_357',
                 type = 'UV',
                 particles = [ P.chi, P.b, P.sbL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.sbL] ], [ [P.go, P.sbL] ], [ [P.g, P.sbL] ] ],
                 couplings = {(0,0,0):C.UVGC_347_655,(0,0,1):C.UVGC_347_656,(0,0,4):C.UVGC_347_657,(0,0,3):C.UVGC_347_658,(0,0,2):C.UVGC_347_659})

V_358 = CTVertex(name = 'V_358',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.chi, P.sbL ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.sbL] ], [ [P.go, P.sbL] ], [ [P.g, P.sbL] ] ],
                 couplings = {(0,0,0):C.UVGC_347_655,(0,0,1):C.UVGC_347_656,(0,0,4):C.UVGC_347_657,(0,0,3):C.UVGC_347_658,(0,0,2):C.UVGC_347_659})

V_359 = CTVertex(name = 'V_359',
                 type = 'UV',
                 particles = [ P.chi, P.b, P.sbR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.sbR] ], [ [P.go, P.sbR] ], [ [P.g, P.sbR] ] ],
                 couplings = {(0,0,0):C.UVGC_348_660,(0,0,1):C.UVGC_348_661,(0,0,4):C.UVGC_348_662,(0,0,3):C.UVGC_348_663,(0,0,2):C.UVGC_348_664})

V_360 = CTVertex(name = 'V_360',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.chi, P.sbR ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.sbR] ], [ [P.go, P.sbR] ], [ [P.g, P.sbR] ] ],
                 couplings = {(0,0,0):C.UVGC_348_660,(0,0,1):C.UVGC_348_661,(0,0,4):C.UVGC_348_662,(0,0,3):C.UVGC_348_663,(0,0,2):C.UVGC_348_664})

V_361 = CTVertex(name = 'V_361',
                 type = 'UV',
                 particles = [ P.chi, P.c, P.scL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.scL] ], [ [P.go, P.scL] ], [ [P.g, P.scL] ] ],
                 couplings = {(0,0,0):C.UVGC_349_665,(0,0,1):C.UVGC_349_666,(0,0,4):C.UVGC_349_667,(0,0,3):C.UVGC_349_668,(0,0,2):C.UVGC_347_659})

V_362 = CTVertex(name = 'V_362',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.chi, P.scL ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.scL] ], [ [P.go, P.scL] ], [ [P.g, P.scL] ] ],
                 couplings = {(0,0,0):C.UVGC_349_665,(0,0,1):C.UVGC_349_666,(0,0,4):C.UVGC_349_667,(0,0,3):C.UVGC_349_668,(0,0,2):C.UVGC_347_659})

V_363 = CTVertex(name = 'V_363',
                 type = 'UV',
                 particles = [ P.chi, P.c, P.scR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.scR] ], [ [P.go, P.scR] ], [ [P.g, P.scR] ] ],
                 couplings = {(0,0,0):C.UVGC_350_669,(0,0,1):C.UVGC_350_670,(0,0,4):C.UVGC_350_671,(0,0,3):C.UVGC_350_672,(0,0,2):C.UVGC_350_673})

V_364 = CTVertex(name = 'V_364',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.chi, P.scR ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.scR] ], [ [P.go, P.scR] ], [ [P.g, P.scR] ] ],
                 couplings = {(0,0,0):C.UVGC_350_669,(0,0,1):C.UVGC_350_670,(0,0,4):C.UVGC_350_671,(0,0,3):C.UVGC_350_672,(0,0,2):C.UVGC_350_673})

V_365 = CTVertex(name = 'V_365',
                 type = 'UV',
                 particles = [ P.chi, P.d, P.sdL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.sdL] ], [ [P.go, P.sdL] ], [ [P.g, P.sdL] ] ],
                 couplings = {(0,0,0):C.UVGC_358_685,(0,0,1):C.UVGC_358_686,(0,0,4):C.UVGC_358_687,(0,0,3):C.UVGC_358_688,(0,0,2):C.UVGC_347_659})

V_366 = CTVertex(name = 'V_366',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.chi, P.sdL ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.sdL] ], [ [P.go, P.sdL] ], [ [P.g, P.sdL] ] ],
                 couplings = {(0,0,0):C.UVGC_358_685,(0,0,1):C.UVGC_358_686,(0,0,4):C.UVGC_358_687,(0,0,3):C.UVGC_358_688,(0,0,2):C.UVGC_347_659})

V_367 = CTVertex(name = 'V_367',
                 type = 'UV',
                 particles = [ P.chi, P.d, P.sdR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.sdR] ], [ [P.go, P.sdR] ], [ [P.g, P.sdR] ] ],
                 couplings = {(0,0,0):C.UVGC_359_689,(0,0,1):C.UVGC_359_690,(0,0,4):C.UVGC_359_691,(0,0,3):C.UVGC_359_692,(0,0,2):C.UVGC_348_664})

V_368 = CTVertex(name = 'V_368',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.chi, P.sdR ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.sdR] ], [ [P.go, P.sdR] ], [ [P.g, P.sdR] ] ],
                 couplings = {(0,0,0):C.UVGC_359_689,(0,0,1):C.UVGC_359_690,(0,0,4):C.UVGC_359_691,(0,0,3):C.UVGC_359_692,(0,0,2):C.UVGC_348_664})

V_369 = CTVertex(name = 'V_369',
                 type = 'UV',
                 particles = [ P.chi, P.s, P.ssL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.go, P.ssL] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssL] ], [ [P.g, P.ssL] ] ],
                 couplings = {(0,0,2):C.UVGC_428_901,(0,0,4):C.UVGC_428_902,(0,0,0):C.UVGC_428_903,(0,0,1):C.UVGC_428_904,(0,0,3):C.UVGC_347_659})

V_370 = CTVertex(name = 'V_370',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.chi, P.ssL ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.go, P.ssL] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssL] ], [ [P.g, P.ssL] ] ],
                 couplings = {(0,0,2):C.UVGC_428_901,(0,0,4):C.UVGC_428_902,(0,0,0):C.UVGC_428_903,(0,0,1):C.UVGC_428_904,(0,0,3):C.UVGC_347_659})

V_371 = CTVertex(name = 'V_371',
                 type = 'UV',
                 particles = [ P.chi, P.s, P.ssR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.go, P.ssR] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssR] ], [ [P.g, P.ssR] ] ],
                 couplings = {(0,0,2):C.UVGC_429_905,(0,0,4):C.UVGC_429_906,(0,0,0):C.UVGC_429_907,(0,0,1):C.UVGC_429_908,(0,0,3):C.UVGC_348_664})

V_372 = CTVertex(name = 'V_372',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.chi, P.ssR ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.go, P.ssR] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssR] ], [ [P.g, P.ssR] ] ],
                 couplings = {(0,0,2):C.UVGC_429_905,(0,0,4):C.UVGC_429_906,(0,0,0):C.UVGC_429_907,(0,0,1):C.UVGC_429_908,(0,0,3):C.UVGC_348_664})

V_373 = CTVertex(name = 'V_373',
                 type = 'UV',
                 particles = [ P.chi, P.t, P.stL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.stL] ], [ [P.g, P.stL, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,1,3):C.UVGC_463_933,(0,1,5):C.UVGC_463_934,(0,1,0):C.UVGC_463_935,(0,1,1):C.UVGC_463_936,(0,1,2):C.UVGC_463_937,(0,1,4):C.UVGC_347_659,(0,0,2):C.UVGC_96_1082})

V_374 = CTVertex(name = 'V_374',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.chi, P.stL ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.stL] ], [ [P.g, P.stL, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,3):C.UVGC_463_933,(0,0,5):C.UVGC_463_934,(0,0,0):C.UVGC_463_935,(0,0,1):C.UVGC_463_936,(0,0,2):C.UVGC_463_937,(0,0,4):C.UVGC_347_659,(0,1,2):C.UVGC_96_1082})

V_375 = CTVertex(name = 'V_375',
                 type = 'UV',
                 particles = [ P.chi, P.t, P.stR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.stR] ], [ [P.g, P.stR, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,3):C.UVGC_464_938,(0,0,5):C.UVGC_464_939,(0,0,0):C.UVGC_464_940,(0,0,1):C.UVGC_464_941,(0,0,2):C.UVGC_464_942,(0,0,4):C.UVGC_350_673,(0,1,2):C.UVGC_95_1081})

V_376 = CTVertex(name = 'V_376',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.chi, P.stR ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.stR] ], [ [P.g, P.stR, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,1,3):C.UVGC_464_938,(0,1,5):C.UVGC_464_939,(0,1,0):C.UVGC_464_940,(0,1,1):C.UVGC_464_941,(0,1,2):C.UVGC_464_942,(0,1,4):C.UVGC_350_673,(0,0,2):C.UVGC_95_1081})

V_377 = CTVertex(name = 'V_377',
                 type = 'UV',
                 particles = [ P.chi, P.u, P.suL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.go, P.suL] ], [ [P.go, P.u] ], [ [P.g, P.suL] ], [ [P.g, P.suL, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_504_963,(0,0,4):C.UVGC_504_964,(0,0,0):C.UVGC_504_965,(0,0,1):C.UVGC_504_966,(0,0,3):C.UVGC_347_659})

V_378 = CTVertex(name = 'V_378',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.chi, P.suL ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.go, P.suL] ], [ [P.go, P.u] ], [ [P.g, P.suL] ], [ [P.g, P.suL, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_504_963,(0,0,4):C.UVGC_504_964,(0,0,0):C.UVGC_504_965,(0,0,1):C.UVGC_504_966,(0,0,3):C.UVGC_347_659})

V_379 = CTVertex(name = 'V_379',
                 type = 'UV',
                 particles = [ P.chi, P.u, P.suR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.go, P.suR] ], [ [P.go, P.u] ], [ [P.g, P.suR] ], [ [P.g, P.suR, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_505_967,(0,0,4):C.UVGC_505_968,(0,0,0):C.UVGC_505_969,(0,0,1):C.UVGC_505_970,(0,0,3):C.UVGC_350_673})

V_380 = CTVertex(name = 'V_380',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.chi, P.suR ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.go, P.suR] ], [ [P.go, P.u] ], [ [P.g, P.suR] ], [ [P.g, P.suR, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_505_967,(0,0,4):C.UVGC_505_968,(0,0,0):C.UVGC_505_969,(0,0,1):C.UVGC_505_970,(0,0,3):C.UVGC_350_673})

V_381 = CTVertex(name = 'V_381',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.go, P.sbL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbL] ], [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sbL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sbL] ], [ [P.g, P.sbL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_985,(0,0,1):C.UVGC_525_986,(0,0,4):C.UVGC_525_987,(0,0,5):C.UVGC_525_988,(0,0,6):C.UVGC_525_989,(0,0,7):C.UVGC_525_990,(0,0,8):C.UVGC_525_991,(0,0,9):C.UVGC_525_992,(0,0,12):C.UVGC_525_993,(0,0,14):C.UVGC_525_994,(0,0,11):C.UVGC_525_995,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,2):C.UVGC_525_1002,(0,0,3):C.UVGC_525_1003,(0,0,13):C.UVGC_525_1004})

V_382 = CTVertex(name = 'V_382',
                 type = 'UV',
                 particles = [ P.go, P.b, P.sbR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbR] ], [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sbR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sbR] ], [ [P.g, P.sbR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1040,(0,0,1):C.UVGC_531_1041,(0,0,4):C.UVGC_531_1042,(0,0,5):C.UVGC_531_1043,(0,0,6):C.UVGC_531_1044,(0,0,7):C.UVGC_531_1045,(0,0,8):C.UVGC_531_1046,(0,0,9):C.UVGC_531_1047,(0,0,12):C.UVGC_531_1048,(0,0,14):C.UVGC_531_1049,(0,0,11):C.UVGC_531_1050,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,2):C.UVGC_531_1057,(0,0,3):C.UVGC_531_1058,(0,0,13):C.UVGC_531_1059})

V_383 = CTVertex(name = 'V_383',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.go, P.scL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scL] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.scL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.scL] ], [ [P.g, P.scL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_526_1005,(0,0,3):C.UVGC_526_1006,(0,0,6):C.UVGC_525_989,(0,0,7):C.UVGC_525_990,(0,0,8):C.UVGC_525_991,(0,0,9):C.UVGC_525_992,(0,0,12):C.UVGC_525_993,(0,0,14):C.UVGC_526_1007,(0,0,11):C.UVGC_526_1008,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,4):C.UVGC_525_1002,(0,0,5):C.UVGC_525_1003,(0,0,13):C.UVGC_525_1004})

V_384 = CTVertex(name = 'V_384',
                 type = 'UV',
                 particles = [ P.go, P.c, P.scR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.scR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.scR] ], [ [P.g, P.scR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_532_1060,(0,0,3):C.UVGC_532_1061,(0,0,6):C.UVGC_531_1044,(0,0,7):C.UVGC_531_1045,(0,0,8):C.UVGC_531_1046,(0,0,9):C.UVGC_531_1047,(0,0,12):C.UVGC_531_1048,(0,0,14):C.UVGC_532_1062,(0,0,11):C.UVGC_532_1063,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,4):C.UVGC_531_1057,(0,0,5):C.UVGC_531_1058,(0,0,13):C.UVGC_531_1059})

V_385 = CTVertex(name = 'V_385',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.go, P.sdL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdL] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sdL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sdL] ], [ [P.g, P.sdL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_525_989,(0,0,3):C.UVGC_525_990,(0,0,4):C.UVGC_527_1009,(0,0,5):C.UVGC_527_1010,(0,0,8):C.UVGC_525_991,(0,0,9):C.UVGC_525_992,(0,0,12):C.UVGC_525_993,(0,0,14):C.UVGC_527_1011,(0,0,11):C.UVGC_527_1012,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,6):C.UVGC_525_1002,(0,0,7):C.UVGC_525_1003,(0,0,13):C.UVGC_525_1004})

V_386 = CTVertex(name = 'V_386',
                 type = 'UV',
                 particles = [ P.go, P.d, P.sdR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sdR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sdR] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_531_1044,(0,0,3):C.UVGC_531_1045,(0,0,4):C.UVGC_533_1064,(0,0,5):C.UVGC_533_1065,(0,0,8):C.UVGC_531_1046,(0,0,9):C.UVGC_531_1047,(0,0,12):C.UVGC_531_1048,(0,0,14):C.UVGC_533_1066,(0,0,11):C.UVGC_533_1067,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,6):C.UVGC_531_1057,(0,0,7):C.UVGC_531_1058,(0,0,13):C.UVGC_531_1059})

V_387 = CTVertex(name = 'V_387',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.go, P.ssL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.ssL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssL] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_525_989,(0,0,3):C.UVGC_525_990,(0,0,4):C.UVGC_525_991,(0,0,5):C.UVGC_525_992,(0,0,9):C.UVGC_525_993,(0,0,12):C.UVGC_528_1013,(0,0,14):C.UVGC_528_1014,(0,0,7):C.UVGC_528_1015,(0,0,8):C.UVGC_528_1016,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,10):C.UVGC_525_1002,(0,0,11):C.UVGC_525_1004,(0,0,13):C.UVGC_525_1003})

V_388 = CTVertex(name = 'V_388',
                 type = 'UV',
                 particles = [ P.go, P.s, P.ssR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.ssR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssR] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_531_1044,(0,0,3):C.UVGC_531_1045,(0,0,4):C.UVGC_531_1046,(0,0,5):C.UVGC_531_1047,(0,0,9):C.UVGC_531_1048,(0,0,12):C.UVGC_534_1068,(0,0,14):C.UVGC_534_1069,(0,0,7):C.UVGC_534_1070,(0,0,8):C.UVGC_534_1071,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,10):C.UVGC_531_1057,(0,0,11):C.UVGC_531_1059,(0,0,13):C.UVGC_531_1058})

V_389 = CTVertex(name = 'V_389',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.go, P.stL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.go] ], [ [P.g, P.go, P.stL] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stL] ], [ [P.g, P.stL, P.t] ], [ [P.g, P.t] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_525_971,(0,0,16):C.UVGC_525_972,(0,0,17):C.UVGC_525_973,(0,0,18):C.UVGC_525_974,(0,0,19):C.UVGC_525_975,(0,0,20):C.UVGC_525_976,(0,0,21):C.UVGC_525_977,(0,0,24):C.UVGC_525_978,(0,0,25):C.UVGC_525_979,(0,0,26):C.UVGC_525_980,(0,0,28):C.UVGC_525_981,(0,0,30):C.UVGC_525_982,(0,0,32):C.UVGC_525_983,(0,0,34):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_525_989,(0,0,3):C.UVGC_525_990,(0,0,4):C.UVGC_525_991,(0,0,5):C.UVGC_525_992,(0,0,10):C.UVGC_525_993,(0,0,13):C.UVGC_529_1017,(0,0,15):C.UVGC_529_1018,(0,0,7):C.UVGC_529_1019,(0,0,8):C.UVGC_529_1020,(0,0,9):C.UVGC_529_1021,(0,0,22):C.UVGC_525_996,(0,0,23):C.UVGC_525_997,(0,0,27):C.UVGC_525_998,(0,0,29):C.UVGC_525_999,(0,0,31):C.UVGC_525_1000,(0,0,33):C.UVGC_525_1001,(0,0,11):C.UVGC_525_1004,(0,0,12):C.UVGC_525_1002,(0,0,14):C.UVGC_525_1003,(0,1,9):C.UVGC_98_1084})

V_390 = CTVertex(name = 'V_390',
                 type = 'UV',
                 particles = [ P.go, P.t, P.stR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.go] ], [ [P.g, P.go, P.stR] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stR] ], [ [P.g, P.stR, P.t] ], [ [P.g, P.t] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_531_1026,(0,0,16):C.UVGC_531_1027,(0,0,17):C.UVGC_531_1028,(0,0,18):C.UVGC_531_1029,(0,0,19):C.UVGC_531_1030,(0,0,20):C.UVGC_531_1031,(0,0,21):C.UVGC_531_1032,(0,0,24):C.UVGC_531_1033,(0,0,25):C.UVGC_531_1034,(0,0,26):C.UVGC_531_1035,(0,0,28):C.UVGC_531_1036,(0,0,30):C.UVGC_531_1037,(0,0,32):C.UVGC_531_1038,(0,0,34):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_531_1044,(0,0,3):C.UVGC_531_1045,(0,0,4):C.UVGC_531_1046,(0,0,5):C.UVGC_531_1047,(0,0,10):C.UVGC_531_1048,(0,0,13):C.UVGC_535_1072,(0,0,15):C.UVGC_535_1073,(0,0,7):C.UVGC_535_1074,(0,0,8):C.UVGC_535_1075,(0,0,9):C.UVGC_535_1076,(0,0,22):C.UVGC_531_1051,(0,0,23):C.UVGC_531_1052,(0,0,27):C.UVGC_531_1053,(0,0,29):C.UVGC_531_1054,(0,0,31):C.UVGC_531_1055,(0,0,33):C.UVGC_531_1056,(0,0,11):C.UVGC_531_1059,(0,0,12):C.UVGC_531_1057,(0,0,14):C.UVGC_531_1058,(0,1,9):C.UVGC_97_1083})

V_391 = CTVertex(name = 'V_391',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.go, P.suL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.suL] ], [ [P.go, P.u] ], [ [P.g, P.go] ], [ [P.g, P.go, P.suL] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suL] ], [ [P.g, P.suL, P.u] ], [ [P.g, P.u] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_525_989,(0,0,3):C.UVGC_525_990,(0,0,4):C.UVGC_525_991,(0,0,5):C.UVGC_525_992,(0,0,9):C.UVGC_525_993,(0,0,12):C.UVGC_530_1022,(0,0,14):C.UVGC_530_1023,(0,0,7):C.UVGC_530_1024,(0,0,8):C.UVGC_530_1025,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,10):C.UVGC_525_1004,(0,0,11):C.UVGC_525_1002,(0,0,13):C.UVGC_525_1003})

V_392 = CTVertex(name = 'V_392',
                 type = 'UV',
                 particles = [ P.go, P.u, P.suR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.suR] ], [ [P.go, P.u] ], [ [P.g, P.go] ], [ [P.g, P.go, P.suR] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suR] ], [ [P.g, P.suR, P.u] ], [ [P.g, P.u] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_531_1044,(0,0,3):C.UVGC_531_1045,(0,0,4):C.UVGC_531_1046,(0,0,5):C.UVGC_531_1047,(0,0,9):C.UVGC_531_1048,(0,0,12):C.UVGC_536_1077,(0,0,14):C.UVGC_536_1078,(0,0,7):C.UVGC_536_1079,(0,0,8):C.UVGC_536_1080,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,10):C.UVGC_531_1059,(0,0,11):C.UVGC_531_1057,(0,0,13):C.UVGC_531_1058})

V_393 = CTVertex(name = 'V_393',
                 type = 'UV',
                 particles = [ P.go, P.b, P.sbL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbL] ], [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sbL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sbL] ], [ [P.g, P.sbL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_985,(0,0,1):C.UVGC_525_986,(0,0,4):C.UVGC_525_987,(0,0,5):C.UVGC_525_988,(0,0,6):C.UVGC_525_989,(0,0,7):C.UVGC_525_990,(0,0,8):C.UVGC_525_991,(0,0,9):C.UVGC_525_992,(0,0,12):C.UVGC_525_993,(0,0,14):C.UVGC_525_994,(0,0,11):C.UVGC_525_995,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,2):C.UVGC_525_1002,(0,0,3):C.UVGC_525_1003,(0,0,13):C.UVGC_525_1004})

V_394 = CTVertex(name = 'V_394',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.go, P.sbR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.go] ], [ [P.b, P.g, P.go] ], [ [P.b, P.g, P.sbR] ], [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sbR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sbR] ], [ [P.g, P.sbR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1040,(0,0,1):C.UVGC_531_1041,(0,0,4):C.UVGC_531_1042,(0,0,5):C.UVGC_531_1043,(0,0,6):C.UVGC_531_1044,(0,0,7):C.UVGC_531_1045,(0,0,8):C.UVGC_531_1046,(0,0,9):C.UVGC_531_1047,(0,0,12):C.UVGC_531_1048,(0,0,14):C.UVGC_531_1049,(0,0,11):C.UVGC_531_1050,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,2):C.UVGC_531_1057,(0,0,3):C.UVGC_531_1058,(0,0,13):C.UVGC_531_1059})

V_395 = CTVertex(name = 'V_395',
                 type = 'UV',
                 particles = [ P.go, P.c, P.scL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scL] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.scL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.scL] ], [ [P.g, P.scL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_526_1005,(0,0,3):C.UVGC_526_1006,(0,0,6):C.UVGC_525_989,(0,0,7):C.UVGC_525_990,(0,0,8):C.UVGC_525_991,(0,0,9):C.UVGC_525_992,(0,0,12):C.UVGC_525_993,(0,0,14):C.UVGC_526_1007,(0,0,11):C.UVGC_526_1008,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,4):C.UVGC_525_1002,(0,0,5):C.UVGC_525_1003,(0,0,13):C.UVGC_525_1004})

V_396 = CTVertex(name = 'V_396',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.go, P.scR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.g] ], [ [P.c, P.go] ], [ [P.c, P.g, P.go] ], [ [P.c, P.g, P.scR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.scR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.scR] ], [ [P.g, P.scR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_532_1060,(0,0,3):C.UVGC_532_1061,(0,0,6):C.UVGC_531_1044,(0,0,7):C.UVGC_531_1045,(0,0,8):C.UVGC_531_1046,(0,0,9):C.UVGC_531_1047,(0,0,12):C.UVGC_531_1048,(0,0,14):C.UVGC_532_1062,(0,0,11):C.UVGC_532_1063,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,4):C.UVGC_531_1057,(0,0,5):C.UVGC_531_1058,(0,0,13):C.UVGC_531_1059})

V_397 = CTVertex(name = 'V_397',
                 type = 'UV',
                 particles = [ P.go, P.d, P.sdL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdL] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sdL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sdL] ], [ [P.g, P.sdL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_525_989,(0,0,3):C.UVGC_525_990,(0,0,4):C.UVGC_527_1009,(0,0,5):C.UVGC_527_1010,(0,0,8):C.UVGC_525_991,(0,0,9):C.UVGC_525_992,(0,0,12):C.UVGC_525_993,(0,0,14):C.UVGC_527_1011,(0,0,11):C.UVGC_527_1012,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,6):C.UVGC_525_1002,(0,0,7):C.UVGC_525_1003,(0,0,13):C.UVGC_525_1004})

V_398 = CTVertex(name = 'V_398',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.go, P.sdR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.g] ], [ [P.d, P.go] ], [ [P.d, P.g, P.go] ], [ [P.d, P.g, P.sdR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.sdR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.sdR] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,10):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_531_1044,(0,0,3):C.UVGC_531_1045,(0,0,4):C.UVGC_533_1064,(0,0,5):C.UVGC_533_1065,(0,0,8):C.UVGC_531_1046,(0,0,9):C.UVGC_531_1047,(0,0,12):C.UVGC_531_1048,(0,0,14):C.UVGC_533_1066,(0,0,11):C.UVGC_533_1067,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,6):C.UVGC_531_1057,(0,0,7):C.UVGC_531_1058,(0,0,13):C.UVGC_531_1059})

V_399 = CTVertex(name = 'V_399',
                 type = 'UV',
                 particles = [ P.go, P.s, P.ssL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.ssL] ], [ [P.g, P.go] ], [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssL] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_525_989,(0,0,3):C.UVGC_525_990,(0,0,4):C.UVGC_525_991,(0,0,5):C.UVGC_525_992,(0,0,9):C.UVGC_525_993,(0,0,12):C.UVGC_528_1013,(0,0,14):C.UVGC_528_1014,(0,0,7):C.UVGC_528_1015,(0,0,8):C.UVGC_528_1016,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,10):C.UVGC_525_1002,(0,0,11):C.UVGC_525_1004,(0,0,13):C.UVGC_525_1003})

V_400 = CTVertex(name = 'V_400',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.go, P.ssR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.ssR] ], [ [P.g, P.go] ], [ [P.g, P.go, P.s] ], [ [P.g, P.go, P.ssR] ], [ [P.g, P.s] ], [ [P.g, P.s, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_531_1044,(0,0,3):C.UVGC_531_1045,(0,0,4):C.UVGC_531_1046,(0,0,5):C.UVGC_531_1047,(0,0,9):C.UVGC_531_1048,(0,0,12):C.UVGC_534_1068,(0,0,14):C.UVGC_534_1069,(0,0,7):C.UVGC_534_1070,(0,0,8):C.UVGC_534_1071,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,10):C.UVGC_531_1057,(0,0,11):C.UVGC_531_1059,(0,0,13):C.UVGC_531_1058})

V_401 = CTVertex(name = 'V_401',
                 type = 'UV',
                 particles = [ P.go, P.t, P.stL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.go] ], [ [P.g, P.go, P.stL] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stL] ], [ [P.g, P.stL, P.t] ], [ [P.g, P.t] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,1,6):C.UVGC_525_971,(0,1,16):C.UVGC_525_972,(0,1,17):C.UVGC_525_973,(0,1,18):C.UVGC_525_974,(0,1,19):C.UVGC_525_975,(0,1,20):C.UVGC_525_976,(0,1,21):C.UVGC_525_977,(0,1,24):C.UVGC_525_978,(0,1,25):C.UVGC_525_979,(0,1,26):C.UVGC_525_980,(0,1,28):C.UVGC_525_981,(0,1,30):C.UVGC_525_982,(0,1,32):C.UVGC_525_983,(0,1,34):C.UVGC_525_984,(0,1,0):C.UVGC_525_987,(0,1,1):C.UVGC_525_988,(0,1,2):C.UVGC_525_989,(0,1,3):C.UVGC_525_990,(0,1,4):C.UVGC_525_991,(0,1,5):C.UVGC_525_992,(0,1,10):C.UVGC_525_993,(0,1,13):C.UVGC_529_1017,(0,1,15):C.UVGC_529_1018,(0,1,7):C.UVGC_529_1019,(0,1,8):C.UVGC_529_1020,(0,1,9):C.UVGC_529_1021,(0,1,22):C.UVGC_525_996,(0,1,23):C.UVGC_525_997,(0,1,27):C.UVGC_525_998,(0,1,29):C.UVGC_525_999,(0,1,31):C.UVGC_525_1000,(0,1,33):C.UVGC_525_1001,(0,1,11):C.UVGC_525_1004,(0,1,12):C.UVGC_525_1002,(0,1,14):C.UVGC_525_1003,(0,0,9):C.UVGC_98_1084})

V_402 = CTVertex(name = 'V_402',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.go, P.stR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.go, P.t] ], [ [P.g, P.go] ], [ [P.g, P.go, P.stR] ], [ [P.g, P.go, P.t] ], [ [P.g, P.stR] ], [ [P.g, P.stR, P.t] ], [ [P.g, P.t] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,1,6):C.UVGC_531_1026,(0,1,16):C.UVGC_531_1027,(0,1,17):C.UVGC_531_1028,(0,1,18):C.UVGC_531_1029,(0,1,19):C.UVGC_531_1030,(0,1,20):C.UVGC_531_1031,(0,1,21):C.UVGC_531_1032,(0,1,24):C.UVGC_531_1033,(0,1,25):C.UVGC_531_1034,(0,1,26):C.UVGC_531_1035,(0,1,28):C.UVGC_531_1036,(0,1,30):C.UVGC_531_1037,(0,1,32):C.UVGC_531_1038,(0,1,34):C.UVGC_531_1039,(0,1,0):C.UVGC_531_1042,(0,1,1):C.UVGC_531_1043,(0,1,2):C.UVGC_531_1044,(0,1,3):C.UVGC_531_1045,(0,1,4):C.UVGC_531_1046,(0,1,5):C.UVGC_531_1047,(0,1,10):C.UVGC_531_1048,(0,1,13):C.UVGC_535_1072,(0,1,15):C.UVGC_535_1073,(0,1,7):C.UVGC_535_1074,(0,1,8):C.UVGC_535_1075,(0,1,9):C.UVGC_535_1076,(0,1,22):C.UVGC_531_1051,(0,1,23):C.UVGC_531_1052,(0,1,27):C.UVGC_531_1053,(0,1,29):C.UVGC_531_1054,(0,1,31):C.UVGC_531_1055,(0,1,33):C.UVGC_531_1056,(0,1,11):C.UVGC_531_1059,(0,1,12):C.UVGC_531_1057,(0,1,14):C.UVGC_531_1058,(0,0,9):C.UVGC_97_1083})

V_403 = CTVertex(name = 'V_403',
                 type = 'UV',
                 particles = [ P.go, P.u, P.suL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.suL] ], [ [P.go, P.u] ], [ [P.g, P.go] ], [ [P.g, P.go, P.suL] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suL] ], [ [P.g, P.suL, P.u] ], [ [P.g, P.u] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_525_971,(0,0,15):C.UVGC_525_972,(0,0,16):C.UVGC_525_973,(0,0,17):C.UVGC_525_974,(0,0,18):C.UVGC_525_975,(0,0,19):C.UVGC_525_976,(0,0,20):C.UVGC_525_977,(0,0,23):C.UVGC_525_978,(0,0,24):C.UVGC_525_979,(0,0,25):C.UVGC_525_980,(0,0,27):C.UVGC_525_981,(0,0,29):C.UVGC_525_982,(0,0,31):C.UVGC_525_983,(0,0,33):C.UVGC_525_984,(0,0,0):C.UVGC_525_987,(0,0,1):C.UVGC_525_988,(0,0,2):C.UVGC_525_989,(0,0,3):C.UVGC_525_990,(0,0,4):C.UVGC_525_991,(0,0,5):C.UVGC_525_992,(0,0,9):C.UVGC_525_993,(0,0,12):C.UVGC_530_1022,(0,0,14):C.UVGC_530_1023,(0,0,7):C.UVGC_530_1024,(0,0,8):C.UVGC_530_1025,(0,0,21):C.UVGC_525_996,(0,0,22):C.UVGC_525_997,(0,0,26):C.UVGC_525_998,(0,0,28):C.UVGC_525_999,(0,0,30):C.UVGC_525_1000,(0,0,32):C.UVGC_525_1001,(0,0,10):C.UVGC_525_1004,(0,0,11):C.UVGC_525_1002,(0,0,13):C.UVGC_525_1003})

V_404 = CTVertex(name = 'V_404',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.go, P.suR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.go] ], [ [P.go, P.suR] ], [ [P.go, P.u] ], [ [P.g, P.go] ], [ [P.g, P.go, P.suR] ], [ [P.g, P.go, P.u] ], [ [P.g, P.suR] ], [ [P.g, P.suR, P.u] ], [ [P.g, P.u] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.t] ], [ [P.stR] ], [ [P.stR, P.t] ], [ [P.suL] ], [ [P.suL, P.u] ], [ [P.suR] ], [ [P.suR, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,6):C.UVGC_531_1026,(0,0,15):C.UVGC_531_1027,(0,0,16):C.UVGC_531_1028,(0,0,17):C.UVGC_531_1029,(0,0,18):C.UVGC_531_1030,(0,0,19):C.UVGC_531_1031,(0,0,20):C.UVGC_531_1032,(0,0,23):C.UVGC_531_1033,(0,0,24):C.UVGC_531_1034,(0,0,25):C.UVGC_531_1035,(0,0,27):C.UVGC_531_1036,(0,0,29):C.UVGC_531_1037,(0,0,31):C.UVGC_531_1038,(0,0,33):C.UVGC_531_1039,(0,0,0):C.UVGC_531_1042,(0,0,1):C.UVGC_531_1043,(0,0,2):C.UVGC_531_1044,(0,0,3):C.UVGC_531_1045,(0,0,4):C.UVGC_531_1046,(0,0,5):C.UVGC_531_1047,(0,0,9):C.UVGC_531_1048,(0,0,12):C.UVGC_536_1077,(0,0,14):C.UVGC_536_1078,(0,0,7):C.UVGC_536_1079,(0,0,8):C.UVGC_536_1080,(0,0,21):C.UVGC_531_1051,(0,0,22):C.UVGC_531_1052,(0,0,26):C.UVGC_531_1053,(0,0,28):C.UVGC_531_1054,(0,0,30):C.UVGC_531_1055,(0,0,32):C.UVGC_531_1056,(0,0,10):C.UVGC_531_1059,(0,0,11):C.UVGC_531_1057,(0,0,13):C.UVGC_531_1058})

V_405 = CTVertex(name = 'V_405',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL__tilde__, P.sbL, P.sbL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_162_268,(1,0,2):C.UVGC_162_269,(1,0,4):C.UVGC_162_270,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,0):C.UVGC_162_283,(1,0,3):C.UVGC_162_284,(0,0,1):C.UVGC_162_268,(0,0,2):C.UVGC_162_269,(0,0,4):C.UVGC_162_270,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,0):C.UVGC_162_283,(0,0,3):C.UVGC_162_284})

V_406 = CTVertex(name = 'V_406',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.sbR] ], [ [P.g, P.sbR] ], [ [P.sbL] ], [ [P.sbL, P.sbR] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_361_713,(1,0,2):C.UVGC_361_714,(1,0,6):C.UVGC_361_715,(1,0,8):C.UVGC_361_716,(1,0,9):C.UVGC_361_717,(1,0,10):C.UVGC_361_718,(1,0,11):C.UVGC_361_719,(1,0,12):C.UVGC_361_720,(1,0,13):C.UVGC_361_721,(1,0,14):C.UVGC_361_722,(1,0,15):C.UVGC_361_723,(1,0,16):C.UVGC_361_724,(1,0,17):C.UVGC_361_725,(1,0,18):C.UVGC_361_726,(1,0,19):C.UVGC_361_727,(1,0,0):C.UVGC_361_728,(1,0,3):C.UVGC_361_729,(1,0,5):C.UVGC_361_730,(1,0,7):C.UVGC_361_731,(1,0,4):C.UVGC_361_732,(0,0,1):C.UVGC_360_693,(0,0,2):C.UVGC_360_694,(0,0,6):C.UVGC_360_695,(0,0,8):C.UVGC_360_696,(0,0,9):C.UVGC_360_697,(0,0,10):C.UVGC_360_698,(0,0,11):C.UVGC_360_699,(0,0,12):C.UVGC_360_700,(0,0,13):C.UVGC_360_701,(0,0,14):C.UVGC_360_702,(0,0,15):C.UVGC_360_703,(0,0,16):C.UVGC_360_704,(0,0,17):C.UVGC_360_705,(0,0,18):C.UVGC_360_706,(0,0,19):C.UVGC_360_707,(0,0,0):C.UVGC_360_708,(0,0,3):C.UVGC_360_709,(0,0,5):C.UVGC_360_710,(0,0,7):C.UVGC_360_711,(0,0,4):C.UVGC_360_712})

V_407 = CTVertex(name = 'V_407',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR__tilde__, P.sbR, P.sbR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_162_268,(1,0,2):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_168_295,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,0):C.UVGC_168_296,(1,0,3):C.UVGC_168_297,(0,0,1):C.UVGC_162_268,(0,0,2):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_168_295,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,0):C.UVGC_168_296,(0,0,3):C.UVGC_168_297})

V_408 = CTVertex(name = 'V_408',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.b, P.go] ], [ [P.c, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.scL] ], [ [P.g, P.scL] ], [ [P.sbL] ], [ [P.sbL, P.scL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_365_765,(1,0,8):C.UVGC_365_766,(1,0,10):C.UVGC_365_767,(1,0,11):C.UVGC_365_768,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,1):C.UVGC_365_779,(1,0,2):C.UVGC_365_780,(1,0,5):C.UVGC_365_781,(1,0,7):C.UVGC_365_782,(1,0,9):C.UVGC_361_731,(1,0,0):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_364_745,(0,0,8):C.UVGC_364_746,(0,0,10):C.UVGC_364_747,(0,0,11):C.UVGC_364_748,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,1):C.UVGC_364_759,(0,0,2):C.UVGC_364_760,(0,0,5):C.UVGC_364_761,(0,0,7):C.UVGC_364_762,(0,0,9):C.UVGC_360_711,(0,0,0):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_409 = CTVertex(name = 'V_409',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.b, P.go] ], [ [P.c, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.scL] ], [ [P.g, P.scL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.scL] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_361_716,(1,0,11):C.UVGC_367_791,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,1):C.UVGC_367_792,(1,0,2):C.UVGC_367_793,(1,0,5):C.UVGC_361_730,(1,0,7):C.UVGC_367_794,(1,0,10):C.UVGC_361_731,(1,0,0):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_360_696,(0,0,11):C.UVGC_366_786,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,1):C.UVGC_366_787,(0,0,2):C.UVGC_366_788,(0,0,5):C.UVGC_360_710,(0,0,7):C.UVGC_366_789,(0,0,10):C.UVGC_360_711,(0,0,0):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_410 = CTVertex(name = 'V_410',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL__tilde__, P.scL, P.scL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.scL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_162_268,(1,0,2):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_174_307,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,0):C.UVGC_174_308,(1,0,3):C.UVGC_174_309,(0,0,1):C.UVGC_162_268,(0,0,2):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_174_307,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,0):C.UVGC_174_308,(0,0,3):C.UVGC_174_309})

V_411 = CTVertex(name = 'V_411',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.b, P.go] ], [ [P.c, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.scR] ], [ [P.g, P.scR] ], [ [P.sbL] ], [ [P.sbL, P.scR] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_361_714,(1,0,8):C.UVGC_361_715,(1,0,10):C.UVGC_363_739,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_369_798,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,1):C.UVGC_363_741,(1,0,2):C.UVGC_383_834,(1,0,5):C.UVGC_361_729,(1,0,7):C.UVGC_369_800,(1,0,9):C.UVGC_361_731,(1,0,0):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_360_694,(0,0,8):C.UVGC_360_695,(0,0,10):C.UVGC_362_733,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_368_795,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,1):C.UVGC_362_735,(0,0,2):C.UVGC_382_833,(0,0,5):C.UVGC_360_709,(0,0,7):C.UVGC_368_797,(0,0,9):C.UVGC_360_711,(0,0,0):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_412 = CTVertex(name = 'V_412',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.c, P.go] ], [ [P.b, P.go] ], [ [P.c, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.scR] ], [ [P.g, P.scR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.scR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_385_842,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_385_844,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,1):C.UVGC_385_845,(1,0,2):C.UVGC_385_846,(1,0,5):C.UVGC_385_847,(1,0,7):C.UVGC_385_848,(1,0,10):C.UVGC_361_731,(1,0,0):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_384_835,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_384_837,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,1):C.UVGC_384_838,(0,0,2):C.UVGC_384_839,(0,0,5):C.UVGC_384_840,(0,0,7):C.UVGC_384_841,(0,0,10):C.UVGC_360_711,(0,0,0):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_413 = CTVertex(name = 'V_413',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.scR] ], [ [P.g, P.scR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.scR] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_361_713,(1,0,2):C.UVGC_361_714,(1,0,6):C.UVGC_367_790,(1,0,7):C.UVGC_363_739,(1,0,8):C.UVGC_367_791,(1,0,10):C.UVGC_369_798,(1,0,11):C.UVGC_361_719,(1,0,12):C.UVGC_361_720,(1,0,13):C.UVGC_361_721,(1,0,14):C.UVGC_361_722,(1,0,15):C.UVGC_361_723,(1,0,16):C.UVGC_361_724,(1,0,17):C.UVGC_361_725,(1,0,18):C.UVGC_361_726,(1,0,19):C.UVGC_361_727,(1,0,0):C.UVGC_369_799,(1,0,3):C.UVGC_367_794,(1,0,5):C.UVGC_369_800,(1,0,9):C.UVGC_361_731,(1,0,4):C.UVGC_361_732,(0,0,1):C.UVGC_360_693,(0,0,2):C.UVGC_360_694,(0,0,6):C.UVGC_366_785,(0,0,7):C.UVGC_362_733,(0,0,8):C.UVGC_366_786,(0,0,10):C.UVGC_368_795,(0,0,11):C.UVGC_360_699,(0,0,12):C.UVGC_360_700,(0,0,13):C.UVGC_360_701,(0,0,14):C.UVGC_360_702,(0,0,15):C.UVGC_360_703,(0,0,16):C.UVGC_360_704,(0,0,17):C.UVGC_360_705,(0,0,18):C.UVGC_360_706,(0,0,19):C.UVGC_360_707,(0,0,0):C.UVGC_368_796,(0,0,3):C.UVGC_366_789,(0,0,5):C.UVGC_368_797,(0,0,9):C.UVGC_360_711,(0,0,4):C.UVGC_360_712})

V_414 = CTVertex(name = 'V_414',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR__tilde__, P.scR, P.scR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.scR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_162_268,(1,0,2):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_180_319,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,0):C.UVGC_180_320,(1,0,3):C.UVGC_180_321,(0,0,1):C.UVGC_162_268,(0,0,2):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_180_319,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,0):C.UVGC_180_320,(0,0,3):C.UVGC_180_321})

V_415 = CTVertex(name = 'V_415',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.b, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.sdL] ], [ [P.g, P.sdL] ], [ [P.sbL] ], [ [P.sbL, P.sdL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_365_765,(1,0,8):C.UVGC_365_766,(1,0,10):C.UVGC_365_767,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_371_806,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,1):C.UVGC_365_779,(1,0,2):C.UVGC_371_807,(1,0,5):C.UVGC_365_781,(1,0,7):C.UVGC_371_808,(1,0,9):C.UVGC_361_731,(1,0,0):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_364_745,(0,0,8):C.UVGC_364_746,(0,0,10):C.UVGC_364_747,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_370_802,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,1):C.UVGC_364_759,(0,0,2):C.UVGC_370_803,(0,0,5):C.UVGC_364_761,(0,0,7):C.UVGC_370_804,(0,0,9):C.UVGC_360_711,(0,0,0):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_416 = CTVertex(name = 'V_416',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.b, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.sdL] ], [ [P.g, P.sdL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.sdL] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_361_716,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_387_852,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,1):C.UVGC_367_792,(1,0,2):C.UVGC_387_853,(1,0,5):C.UVGC_361_730,(1,0,7):C.UVGC_387_854,(1,0,10):C.UVGC_361_731,(1,0,0):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_360_696,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_386_849,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,1):C.UVGC_366_787,(0,0,2):C.UVGC_386_850,(0,0,5):C.UVGC_360_710,(0,0,7):C.UVGC_386_851,(0,0,10):C.UVGC_360_711,(0,0,0):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_417 = CTVertex(name = 'V_417',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.c, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.sdL] ], [ [P.g, P.sdL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.sdL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_365_768,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_371_806,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,1):C.UVGC_365_780,(1,0,2):C.UVGC_371_807,(1,0,5):C.UVGC_365_782,(1,0,7):C.UVGC_371_808,(1,0,11):C.UVGC_361_731,(1,0,0):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_364_748,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_370_802,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,1):C.UVGC_364_760,(0,0,2):C.UVGC_370_803,(0,0,5):C.UVGC_364_762,(0,0,7):C.UVGC_370_804,(0,0,11):C.UVGC_360_711,(0,0,0):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_418 = CTVertex(name = 'V_418',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.c, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.sdL] ], [ [P.g, P.sdL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.sdL] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_369_798,(1,0,13):C.UVGC_387_852,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,1):C.UVGC_383_834,(1,0,2):C.UVGC_387_853,(1,0,5):C.UVGC_369_800,(1,0,7):C.UVGC_387_854,(1,0,12):C.UVGC_361_731,(1,0,0):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_368_795,(0,0,13):C.UVGC_386_849,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,1):C.UVGC_382_833,(0,0,2):C.UVGC_386_850,(0,0,5):C.UVGC_368_797,(0,0,7):C.UVGC_386_851,(0,0,12):C.UVGC_360_711,(0,0,0):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_419 = CTVertex(name = 'V_419',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL__tilde__, P.sdL, P.sdL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sdL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_162_268,(1,0,2):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_186_331,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,0):C.UVGC_186_332,(1,0,3):C.UVGC_186_333,(0,0,1):C.UVGC_162_268,(0,0,2):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_186_331,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,0):C.UVGC_186_332,(0,0,3):C.UVGC_186_333})

V_420 = CTVertex(name = 'V_420',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.b, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.sdR] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbL, P.sdR] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_361_714,(1,0,8):C.UVGC_361_715,(1,0,10):C.UVGC_363_739,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_363_740,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,1):C.UVGC_363_741,(1,0,2):C.UVGC_363_742,(1,0,5):C.UVGC_361_729,(1,0,7):C.UVGC_363_743,(1,0,9):C.UVGC_361_731,(1,0,0):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_360_694,(0,0,8):C.UVGC_360_695,(0,0,10):C.UVGC_362_733,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_362_734,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,1):C.UVGC_362_735,(0,0,2):C.UVGC_362_736,(0,0,5):C.UVGC_360_709,(0,0,7):C.UVGC_362_737,(0,0,9):C.UVGC_360_711,(0,0,0):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_421 = CTVertex(name = 'V_421',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.d, P.go] ], [ [P.b, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.sdR] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.sdR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_385_842,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_389_858,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,1):C.UVGC_385_845,(1,0,2):C.UVGC_389_859,(1,0,5):C.UVGC_385_847,(1,0,7):C.UVGC_389_860,(1,0,10):C.UVGC_361_731,(1,0,0):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_384_835,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_388_855,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,1):C.UVGC_384_838,(0,0,2):C.UVGC_388_856,(0,0,5):C.UVGC_384_840,(0,0,7):C.UVGC_388_857,(0,0,10):C.UVGC_360_711,(0,0,0):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_422 = CTVertex(name = 'V_422',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.c, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.sdR] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.sdR] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_367_791,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_363_740,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,1):C.UVGC_367_793,(1,0,2):C.UVGC_363_742,(1,0,5):C.UVGC_367_794,(1,0,7):C.UVGC_363_743,(1,0,11):C.UVGC_361_731,(1,0,0):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_366_786,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_362_734,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,1):C.UVGC_366_788,(0,0,2):C.UVGC_362_736,(0,0,5):C.UVGC_366_789,(0,0,7):C.UVGC_362_737,(0,0,11):C.UVGC_360_711,(0,0,0):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_423 = CTVertex(name = 'V_423',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.d, P.go] ], [ [P.c, P.go] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.sdR] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.sdR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,3):C.UVGC_361_713,(1,0,4):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_385_844,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_389_858,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,1):C.UVGC_385_846,(1,0,2):C.UVGC_389_859,(1,0,5):C.UVGC_385_848,(1,0,7):C.UVGC_389_860,(1,0,12):C.UVGC_361_731,(1,0,0):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,3):C.UVGC_360_693,(0,0,4):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_384_837,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_388_855,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,1):C.UVGC_384_839,(0,0,2):C.UVGC_388_856,(0,0,5):C.UVGC_384_841,(0,0,7):C.UVGC_388_857,(0,0,12):C.UVGC_360_711,(0,0,0):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_424 = CTVertex(name = 'V_424',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sdL] ], [ [P.g, P.sdL, P.sdR] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdL, P.sdR] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_361_713,(1,0,2):C.UVGC_361_714,(1,0,6):C.UVGC_367_790,(1,0,7):C.UVGC_363_739,(1,0,8):C.UVGC_361_717,(1,0,9):C.UVGC_361_718,(1,0,10):C.UVGC_387_852,(1,0,12):C.UVGC_363_740,(1,0,13):C.UVGC_361_721,(1,0,14):C.UVGC_361_722,(1,0,15):C.UVGC_361_723,(1,0,16):C.UVGC_361_724,(1,0,17):C.UVGC_361_725,(1,0,18):C.UVGC_361_726,(1,0,19):C.UVGC_361_727,(1,0,0):C.UVGC_401_880,(1,0,3):C.UVGC_387_854,(1,0,5):C.UVGC_363_743,(1,0,11):C.UVGC_361_731,(1,0,4):C.UVGC_361_732,(0,0,1):C.UVGC_360_693,(0,0,2):C.UVGC_360_694,(0,0,6):C.UVGC_366_785,(0,0,7):C.UVGC_362_733,(0,0,8):C.UVGC_360_697,(0,0,9):C.UVGC_360_698,(0,0,10):C.UVGC_386_849,(0,0,12):C.UVGC_362_734,(0,0,13):C.UVGC_360_701,(0,0,14):C.UVGC_360_702,(0,0,15):C.UVGC_360_703,(0,0,16):C.UVGC_360_704,(0,0,17):C.UVGC_360_705,(0,0,18):C.UVGC_360_706,(0,0,19):C.UVGC_360_707,(0,0,0):C.UVGC_400_879,(0,0,3):C.UVGC_386_851,(0,0,5):C.UVGC_362_737,(0,0,11):C.UVGC_360_711,(0,0,4):C.UVGC_360_712})

V_425 = CTVertex(name = 'V_425',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR__tilde__, P.sdR, P.sdR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g] ], [ [P.go] ], [ [P.g, P.sdR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,1):C.UVGC_162_268,(1,0,2):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_192_343,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,0):C.UVGC_192_344,(1,0,3):C.UVGC_192_345,(0,0,1):C.UVGC_162_268,(0,0,2):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_192_343,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,0):C.UVGC_192_344,(0,0,3):C.UVGC_192_345})

V_426 = CTVertex(name = 'V_426',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbL, P.ssL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_365_766,(1,0,10):C.UVGC_365_767,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_375_812,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_365_779,(1,0,5):C.UVGC_365_781,(1,0,7):C.UVGC_375_813,(1,0,4):C.UVGC_375_814,(1,0,9):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_364_746,(0,0,10):C.UVGC_364_747,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_374_809,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_364_759,(0,0,5):C.UVGC_364_761,(0,0,7):C.UVGC_374_810,(0,0,4):C.UVGC_374_811,(0,0,9):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_427 = CTVertex(name = 'V_427',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.ssL] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_361_716,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_391_864,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_367_792,(1,0,5):C.UVGC_361_730,(1,0,7):C.UVGC_391_865,(1,0,4):C.UVGC_391_866,(1,0,10):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_360_696,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_390_861,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_366_787,(0,0,5):C.UVGC_360_710,(0,0,7):C.UVGC_390_862,(0,0,4):C.UVGC_390_863,(0,0,10):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_428 = CTVertex(name = 'V_428',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.ssL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_365_768,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_375_812,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_365_780,(1,0,5):C.UVGC_365_782,(1,0,7):C.UVGC_375_813,(1,0,4):C.UVGC_375_814,(1,0,11):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_364_748,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_374_809,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_364_760,(0,0,5):C.UVGC_364_762,(0,0,7):C.UVGC_374_810,(0,0,4):C.UVGC_374_811,(0,0,11):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_429 = CTVertex(name = 'V_429',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.ssL] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_369_798,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_391_864,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_383_834,(1,0,5):C.UVGC_369_800,(1,0,7):C.UVGC_391_865,(1,0,4):C.UVGC_391_866,(1,0,12):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_368_795,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_390_861,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_382_833,(0,0,5):C.UVGC_368_797,(0,0,7):C.UVGC_390_862,(0,0,4):C.UVGC_390_863,(0,0,12):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_430 = CTVertex(name = 'V_430',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sdL] ], [ [P.g, P.sdL, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdL, P.ssL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_371_806,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_375_812,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_371_807,(1,0,5):C.UVGC_371_808,(1,0,7):C.UVGC_375_813,(1,0,4):C.UVGC_375_814,(1,0,13):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_370_802,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_374_809,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_370_803,(0,0,5):C.UVGC_370_804,(0,0,7):C.UVGC_374_810,(0,0,4):C.UVGC_374_811,(0,0,13):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_431 = CTVertex(name = 'V_431',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sdR] ], [ [P.g, P.sdR, P.ssL] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.sdR, P.ssL] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_363_740,(1,0,15):C.UVGC_391_864,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_363_742,(1,0,5):C.UVGC_363_743,(1,0,7):C.UVGC_391_865,(1,0,4):C.UVGC_391_866,(1,0,14):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_362_734,(0,0,15):C.UVGC_390_861,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_362_736,(0,0,5):C.UVGC_362_737,(0,0,7):C.UVGC_390_862,(0,0,4):C.UVGC_390_863,(0,0,14):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_432 = CTVertex(name = 'V_432',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL__tilde__, P.ssL, P.ssL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.ssL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_162_268,(1,0,1):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_245_447,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,3):C.UVGC_245_448,(1,0,2):C.UVGC_245_449,(0,0,0):C.UVGC_162_268,(0,0,1):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_245_447,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,3):C.UVGC_245_448,(0,0,2):C.UVGC_245_449})

V_433 = CTVertex(name = 'V_433',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbL, P.ssR] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_361_715,(1,0,10):C.UVGC_363_739,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_377_818,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_363_741,(1,0,5):C.UVGC_361_729,(1,0,7):C.UVGC_377_819,(1,0,4):C.UVGC_377_820,(1,0,9):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_360_695,(0,0,10):C.UVGC_362_733,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_376_815,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_362_735,(0,0,5):C.UVGC_360_709,(0,0,7):C.UVGC_376_816,(0,0,4):C.UVGC_376_817,(0,0,9):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_434 = CTVertex(name = 'V_434',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.ssR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_385_842,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_393_870,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_385_845,(1,0,5):C.UVGC_385_847,(1,0,7):C.UVGC_393_871,(1,0,4):C.UVGC_393_872,(1,0,10):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_384_835,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_392_867,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_384_838,(0,0,5):C.UVGC_384_840,(0,0,7):C.UVGC_392_868,(0,0,4):C.UVGC_392_869,(0,0,10):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_435 = CTVertex(name = 'V_435',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.ssR] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_367_791,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_377_818,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_367_793,(1,0,5):C.UVGC_367_794,(1,0,7):C.UVGC_377_819,(1,0,4):C.UVGC_377_820,(1,0,11):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_366_786,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_376_815,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_366_788,(0,0,5):C.UVGC_366_789,(0,0,7):C.UVGC_376_816,(0,0,4):C.UVGC_376_817,(0,0,11):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_436 = CTVertex(name = 'V_436',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.ssR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_385_844,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_393_870,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_385_846,(1,0,5):C.UVGC_385_848,(1,0,7):C.UVGC_393_871,(1,0,4):C.UVGC_393_872,(1,0,12):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_384_837,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_392_867,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_384_839,(0,0,5):C.UVGC_384_841,(0,0,7):C.UVGC_392_868,(0,0,4):C.UVGC_392_869,(0,0,12):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_437 = CTVertex(name = 'V_437',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sdL] ], [ [P.g, P.sdL, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdL, P.ssR] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_387_852,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_377_818,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_387_853,(1,0,5):C.UVGC_387_854,(1,0,7):C.UVGC_377_819,(1,0,4):C.UVGC_377_820,(1,0,13):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_386_849,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_376_815,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_386_850,(0,0,5):C.UVGC_386_851,(0,0,7):C.UVGC_376_816,(0,0,4):C.UVGC_376_817,(0,0,13):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_438 = CTVertex(name = 'V_438',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.s] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.sdR] ], [ [P.g, P.sdR, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.sdR, P.ssR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_389_858,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_393_870,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_389_859,(1,0,5):C.UVGC_389_860,(1,0,7):C.UVGC_393_871,(1,0,4):C.UVGC_393_872,(1,0,14):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_388_855,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_392_867,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_388_856,(0,0,5):C.UVGC_388_857,(0,0,7):C.UVGC_392_868,(0,0,4):C.UVGC_392_869,(0,0,14):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_439 = CTVertex(name = 'V_439',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.ssL] ], [ [P.g, P.ssL, P.ssR] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssL, P.ssR] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,6):C.UVGC_367_790,(1,0,7):C.UVGC_363_739,(1,0,8):C.UVGC_361_717,(1,0,9):C.UVGC_361_718,(1,0,10):C.UVGC_361_719,(1,0,11):C.UVGC_361_720,(1,0,12):C.UVGC_391_864,(1,0,14):C.UVGC_377_818,(1,0,15):C.UVGC_361_723,(1,0,16):C.UVGC_361_724,(1,0,17):C.UVGC_361_725,(1,0,18):C.UVGC_361_726,(1,0,19):C.UVGC_361_727,(1,0,3):C.UVGC_391_865,(1,0,5):C.UVGC_377_819,(1,0,2):C.UVGC_413_882,(1,0,13):C.UVGC_361_731,(1,0,4):C.UVGC_361_732,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,6):C.UVGC_366_785,(0,0,7):C.UVGC_362_733,(0,0,8):C.UVGC_360_697,(0,0,9):C.UVGC_360_698,(0,0,10):C.UVGC_360_699,(0,0,11):C.UVGC_360_700,(0,0,12):C.UVGC_390_861,(0,0,14):C.UVGC_376_815,(0,0,15):C.UVGC_360_703,(0,0,16):C.UVGC_360_704,(0,0,17):C.UVGC_360_705,(0,0,18):C.UVGC_360_706,(0,0,19):C.UVGC_360_707,(0,0,3):C.UVGC_390_862,(0,0,5):C.UVGC_376_816,(0,0,2):C.UVGC_412_881,(0,0,13):C.UVGC_360_711,(0,0,4):C.UVGC_360_712})

V_440 = CTVertex(name = 'V_440',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR__tilde__, P.ssR, P.ssR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.ssR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_162_268,(1,0,1):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_246_450,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,3):C.UVGC_246_451,(1,0,2):C.UVGC_246_452,(0,0,0):C.UVGC_162_268,(0,0,1):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_246_450,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,3):C.UVGC_246_451,(0,0,2):C.UVGC_246_452})

V_441 = CTVertex(name = 'V_441',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbL, P.stL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_365_766,(1,0,10):C.UVGC_365_767,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_379_824,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_365_779,(1,0,5):C.UVGC_365_781,(1,0,7):C.UVGC_379_825,(1,0,4):C.UVGC_379_826,(1,0,9):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_364_746,(0,0,10):C.UVGC_364_747,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_378_821,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_364_759,(0,0,5):C.UVGC_364_761,(0,0,7):C.UVGC_378_822,(0,0,4):C.UVGC_378_823,(0,0,9):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_442 = CTVertex(name = 'V_442',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.stL] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_361_716,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_415_886,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_367_792,(1,0,5):C.UVGC_361_730,(1,0,7):C.UVGC_415_887,(1,0,4):C.UVGC_415_888,(1,0,10):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_360_696,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_414_883,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_366_787,(0,0,5):C.UVGC_360_710,(0,0,7):C.UVGC_414_884,(0,0,4):C.UVGC_414_885,(0,0,10):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_443 = CTVertex(name = 'V_443',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.stL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_365_768,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_379_824,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_365_780,(1,0,5):C.UVGC_365_782,(1,0,7):C.UVGC_379_825,(1,0,4):C.UVGC_379_826,(1,0,11):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_364_748,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_378_821,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_364_760,(0,0,5):C.UVGC_364_762,(0,0,7):C.UVGC_378_822,(0,0,4):C.UVGC_378_823,(0,0,11):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_444 = CTVertex(name = 'V_444',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.stL] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_369_798,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_415_886,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_383_834,(1,0,5):C.UVGC_369_800,(1,0,7):C.UVGC_415_887,(1,0,4):C.UVGC_415_888,(1,0,12):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_368_795,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_414_883,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_382_833,(0,0,5):C.UVGC_368_797,(0,0,7):C.UVGC_414_884,(0,0,4):C.UVGC_414_885,(0,0,12):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_445 = CTVertex(name = 'V_445',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sdL] ], [ [P.g, P.sdL, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdL, P.stL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_371_806,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_379_824,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_371_807,(1,0,5):C.UVGC_371_808,(1,0,7):C.UVGC_379_825,(1,0,4):C.UVGC_379_826,(1,0,13):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_370_802,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_378_821,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_370_803,(0,0,5):C.UVGC_370_804,(0,0,7):C.UVGC_378_822,(0,0,4):C.UVGC_378_823,(0,0,13):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_446 = CTVertex(name = 'V_446',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sdR] ], [ [P.g, P.sdR, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.sdR, P.stL] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_363_740,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_415_886,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_363_742,(1,0,5):C.UVGC_363_743,(1,0,7):C.UVGC_415_887,(1,0,4):C.UVGC_415_888,(1,0,14):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_362_734,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_414_883,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_362_736,(0,0,5):C.UVGC_362_737,(0,0,7):C.UVGC_414_884,(0,0,4):C.UVGC_414_885,(0,0,14):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_447 = CTVertex(name = 'V_447',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.t] ], [ [P.go, P.t] ], [ [P.g, P.ssL] ], [ [P.g, P.ssL, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssL, P.stL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_365_771,(1,0,14):C.UVGC_375_812,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_379_824,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,5):C.UVGC_375_813,(1,0,7):C.UVGC_379_825,(1,0,2):C.UVGC_375_814,(1,0,4):C.UVGC_379_826,(1,0,15):C.UVGC_361_731,(1,0,6):C.UVGC_365_784,(1,0,3):C.UVGC_365_783,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_364_751,(0,0,14):C.UVGC_374_809,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_378_821,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,5):C.UVGC_374_810,(0,0,7):C.UVGC_378_822,(0,0,2):C.UVGC_374_811,(0,0,4):C.UVGC_378_823,(0,0,15):C.UVGC_360_711,(0,0,6):C.UVGC_364_764,(0,0,3):C.UVGC_364_763})

V_448 = CTVertex(name = 'V_448',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.t] ], [ [P.go, P.t] ], [ [P.g, P.ssR] ], [ [P.g, P.ssR, P.stL] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.ssR, P.stL] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_361_720,(1,0,14):C.UVGC_361_721,(1,0,15):C.UVGC_377_818,(1,0,17):C.UVGC_415_886,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,5):C.UVGC_377_819,(1,0,7):C.UVGC_415_887,(1,0,2):C.UVGC_377_820,(1,0,4):C.UVGC_415_888,(1,0,16):C.UVGC_361_731,(1,0,6):C.UVGC_361_732,(1,0,3):C.UVGC_363_744,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_360_700,(0,0,14):C.UVGC_360_701,(0,0,15):C.UVGC_376_815,(0,0,17):C.UVGC_414_883,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,5):C.UVGC_376_816,(0,0,7):C.UVGC_414_884,(0,0,2):C.UVGC_376_817,(0,0,4):C.UVGC_414_885,(0,0,16):C.UVGC_360_711,(0,0,6):C.UVGC_360_712,(0,0,3):C.UVGC_362_738})

V_449 = CTVertex(name = 'V_449',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stL__tilde__, P.stL, P.stL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.stL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_162_268,(1,0,1):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_289_514,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,3):C.UVGC_289_515,(1,0,2):C.UVGC_289_516,(0,0,0):C.UVGC_162_268,(0,0,1):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_289_514,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,3):C.UVGC_289_515,(0,0,2):C.UVGC_289_516})

V_450 = CTVertex(name = 'V_450',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbL, P.stR] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_361_715,(1,0,10):C.UVGC_363_739,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_381_830,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_363_741,(1,0,5):C.UVGC_361_729,(1,0,7):C.UVGC_381_831,(1,0,4):C.UVGC_381_832,(1,0,9):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_360_695,(0,0,10):C.UVGC_362_733,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_380_827,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_362_735,(0,0,5):C.UVGC_360_709,(0,0,7):C.UVGC_380_828,(0,0,4):C.UVGC_380_829,(0,0,9):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_451 = CTVertex(name = 'V_451',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.stR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_385_842,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_395_876,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_385_845,(1,0,5):C.UVGC_385_847,(1,0,7):C.UVGC_395_877,(1,0,4):C.UVGC_395_878,(1,0,10):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_384_835,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_394_873,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_384_838,(0,0,5):C.UVGC_384_840,(0,0,7):C.UVGC_394_874,(0,0,4):C.UVGC_394_875,(0,0,10):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_452 = CTVertex(name = 'V_452',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.stR] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_367_791,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_381_830,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_367_793,(1,0,5):C.UVGC_367_794,(1,0,7):C.UVGC_381_831,(1,0,4):C.UVGC_381_832,(1,0,11):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_366_786,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_380_827,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_366_788,(0,0,5):C.UVGC_366_789,(0,0,7):C.UVGC_380_828,(0,0,4):C.UVGC_380_829,(0,0,11):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_453 = CTVertex(name = 'V_453',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.stR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_385_844,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_395_876,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_385_846,(1,0,5):C.UVGC_385_848,(1,0,7):C.UVGC_395_877,(1,0,4):C.UVGC_395_878,(1,0,12):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_384_837,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_394_873,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_384_839,(0,0,5):C.UVGC_384_841,(0,0,7):C.UVGC_394_874,(0,0,4):C.UVGC_394_875,(0,0,12):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_454 = CTVertex(name = 'V_454',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sdL] ], [ [P.g, P.sdL, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdL, P.stR] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_387_852,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_381_830,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_387_853,(1,0,5):C.UVGC_387_854,(1,0,7):C.UVGC_381_831,(1,0,4):C.UVGC_381_832,(1,0,13):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_386_849,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_380_827,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_386_850,(0,0,5):C.UVGC_386_851,(0,0,7):C.UVGC_380_828,(0,0,4):C.UVGC_380_829,(0,0,13):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_455 = CTVertex(name = 'V_455',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.t] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.sdR] ], [ [P.g, P.sdR, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.sdR, P.stR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_389_858,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_395_876,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_389_859,(1,0,5):C.UVGC_389_860,(1,0,7):C.UVGC_395_877,(1,0,4):C.UVGC_395_878,(1,0,14):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_388_855,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_394_873,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_388_856,(0,0,5):C.UVGC_388_857,(0,0,7):C.UVGC_394_874,(0,0,4):C.UVGC_394_875,(0,0,14):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_456 = CTVertex(name = 'V_456',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.t] ], [ [P.go, P.t] ], [ [P.g, P.ssL] ], [ [P.g, P.ssL, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssL, P.stR] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_361_720,(1,0,14):C.UVGC_391_864,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_381_830,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,5):C.UVGC_391_865,(1,0,7):C.UVGC_381_831,(1,0,2):C.UVGC_391_866,(1,0,4):C.UVGC_381_832,(1,0,15):C.UVGC_361_731,(1,0,6):C.UVGC_361_732,(1,0,3):C.UVGC_363_744,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_360_700,(0,0,14):C.UVGC_390_861,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_380_827,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,5):C.UVGC_390_862,(0,0,7):C.UVGC_380_828,(0,0,2):C.UVGC_390_863,(0,0,4):C.UVGC_380_829,(0,0,15):C.UVGC_360_711,(0,0,6):C.UVGC_360_712,(0,0,3):C.UVGC_362_738})

V_457 = CTVertex(name = 'V_457',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.t] ], [ [P.go, P.t] ], [ [P.g, P.ssR] ], [ [P.g, P.ssR, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.ssR, P.stR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_365_771,(1,0,14):C.UVGC_365_772,(1,0,15):C.UVGC_393_870,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_395_876,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,5):C.UVGC_393_871,(1,0,7):C.UVGC_395_877,(1,0,2):C.UVGC_393_872,(1,0,4):C.UVGC_395_878,(1,0,16):C.UVGC_361_731,(1,0,6):C.UVGC_365_784,(1,0,3):C.UVGC_365_783,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_364_751,(0,0,14):C.UVGC_364_752,(0,0,15):C.UVGC_392_867,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_394_873,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,5):C.UVGC_392_868,(0,0,7):C.UVGC_394_874,(0,0,2):C.UVGC_392_869,(0,0,4):C.UVGC_394_875,(0,0,16):C.UVGC_360_711,(0,0,6):C.UVGC_364_764,(0,0,3):C.UVGC_364_763})

V_458 = CTVertex(name = 'V_458',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stL, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.stL] ], [ [P.g, P.stL, P.stR] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.stR] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,6):C.UVGC_367_790,(1,0,7):C.UVGC_363_739,(1,0,8):C.UVGC_361_717,(1,0,9):C.UVGC_361_718,(1,0,10):C.UVGC_361_719,(1,0,11):C.UVGC_361_720,(1,0,12):C.UVGC_361_721,(1,0,13):C.UVGC_361_722,(1,0,14):C.UVGC_415_886,(1,0,16):C.UVGC_381_830,(1,0,17):C.UVGC_361_725,(1,0,18):C.UVGC_361_726,(1,0,19):C.UVGC_361_727,(1,0,3):C.UVGC_415_887,(1,0,5):C.UVGC_381_831,(1,0,2):C.UVGC_417_890,(1,0,15):C.UVGC_361_731,(1,0,4):C.UVGC_361_732,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,6):C.UVGC_366_785,(0,0,7):C.UVGC_362_733,(0,0,8):C.UVGC_360_697,(0,0,9):C.UVGC_360_698,(0,0,10):C.UVGC_360_699,(0,0,11):C.UVGC_360_700,(0,0,12):C.UVGC_360_701,(0,0,13):C.UVGC_360_702,(0,0,14):C.UVGC_414_883,(0,0,16):C.UVGC_380_827,(0,0,17):C.UVGC_360_705,(0,0,18):C.UVGC_360_706,(0,0,19):C.UVGC_360_707,(0,0,3):C.UVGC_414_884,(0,0,5):C.UVGC_380_828,(0,0,2):C.UVGC_416_889,(0,0,15):C.UVGC_360_711,(0,0,4):C.UVGC_360_712})

V_459 = CTVertex(name = 'V_459',
                 type = 'UV',
                 particles = [ P.stR__tilde__, P.stR__tilde__, P.stR, P.stR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.stR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_162_268,(1,0,1):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_290_517,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,3):C.UVGC_290_518,(1,0,2):C.UVGC_290_519,(0,0,0):C.UVGC_162_268,(0,0,1):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_290_517,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,3):C.UVGC_290_518,(0,0,2):C.UVGC_290_519})

V_460 = CTVertex(name = 'V_460',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbL, P.suL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_365_766,(1,0,10):C.UVGC_365_767,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_479_953,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_365_779,(1,0,5):C.UVGC_365_781,(1,0,7):C.UVGC_479_954,(1,0,4):C.UVGC_479_955,(1,0,9):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_364_746,(0,0,10):C.UVGC_364_747,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_473_943,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_364_759,(0,0,5):C.UVGC_364_761,(0,0,7):C.UVGC_473_944,(0,0,4):C.UVGC_473_945,(0,0,9):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_461 = CTVertex(name = 'V_461',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.suL] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_361_716,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_419_896,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_367_792,(1,0,5):C.UVGC_361_730,(1,0,7):C.UVGC_419_898,(1,0,4):C.UVGC_475_949,(1,0,10):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_360_696,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_418_891,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_366_787,(0,0,5):C.UVGC_360_710,(0,0,7):C.UVGC_418_893,(0,0,4):C.UVGC_477_951,(0,0,10):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_462 = CTVertex(name = 'V_462',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.suL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_365_768,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_479_953,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_365_780,(1,0,5):C.UVGC_365_782,(1,0,7):C.UVGC_479_954,(1,0,4):C.UVGC_479_955,(1,0,11):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_364_748,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_473_943,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_364_760,(0,0,5):C.UVGC_364_762,(0,0,7):C.UVGC_473_944,(0,0,4):C.UVGC_473_945,(0,0,11):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_463 = CTVertex(name = 'V_463',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.suL] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_369_798,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_419_896,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_383_834,(1,0,5):C.UVGC_369_800,(1,0,7):C.UVGC_419_898,(1,0,4):C.UVGC_475_949,(1,0,12):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_368_795,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_418_891,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_382_833,(0,0,5):C.UVGC_368_797,(0,0,7):C.UVGC_418_893,(0,0,4):C.UVGC_477_951,(0,0,12):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_464 = CTVertex(name = 'V_464',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sdL] ], [ [P.g, P.sdL, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdL, P.suL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_371_806,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_479_953,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_371_807,(1,0,5):C.UVGC_371_808,(1,0,7):C.UVGC_479_954,(1,0,4):C.UVGC_479_955,(1,0,13):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_370_802,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_473_943,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_370_803,(0,0,5):C.UVGC_370_804,(0,0,7):C.UVGC_473_944,(0,0,4):C.UVGC_473_945,(0,0,13):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_465 = CTVertex(name = 'V_465',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sdR] ], [ [P.g, P.sdR, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.sdR, P.suL] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_363_740,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_419_896,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_363_742,(1,0,5):C.UVGC_363_743,(1,0,7):C.UVGC_419_898,(1,0,4):C.UVGC_475_949,(1,0,14):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_362_734,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_418_891,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_362_736,(0,0,5):C.UVGC_362_737,(0,0,7):C.UVGC_418_893,(0,0,4):C.UVGC_477_951,(0,0,14):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_466 = CTVertex(name = 'V_466',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.u] ], [ [P.go, P.u] ], [ [P.g, P.ssL] ], [ [P.g, P.ssL, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssL, P.suL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_365_771,(1,0,14):C.UVGC_375_812,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_479_953,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,5):C.UVGC_375_813,(1,0,7):C.UVGC_479_954,(1,0,2):C.UVGC_375_814,(1,0,4):C.UVGC_479_955,(1,0,15):C.UVGC_361_731,(1,0,6):C.UVGC_365_784,(1,0,3):C.UVGC_365_783,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_364_751,(0,0,14):C.UVGC_374_809,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_473_943,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,5):C.UVGC_374_810,(0,0,7):C.UVGC_473_944,(0,0,2):C.UVGC_374_811,(0,0,4):C.UVGC_473_945,(0,0,15):C.UVGC_360_711,(0,0,6):C.UVGC_364_764,(0,0,3):C.UVGC_364_763})

V_467 = CTVertex(name = 'V_467',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.u] ], [ [P.go, P.u] ], [ [P.g, P.ssR] ], [ [P.g, P.ssR, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.ssR, P.suL] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_361_720,(1,0,14):C.UVGC_361_721,(1,0,15):C.UVGC_377_818,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_419_896,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,5):C.UVGC_377_819,(1,0,7):C.UVGC_419_898,(1,0,2):C.UVGC_377_820,(1,0,4):C.UVGC_475_949,(1,0,16):C.UVGC_361_731,(1,0,6):C.UVGC_361_732,(1,0,3):C.UVGC_363_744,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_360_700,(0,0,14):C.UVGC_360_701,(0,0,15):C.UVGC_376_815,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_418_891,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,5):C.UVGC_376_816,(0,0,7):C.UVGC_418_893,(0,0,2):C.UVGC_376_817,(0,0,4):C.UVGC_477_951,(0,0,16):C.UVGC_360_711,(0,0,6):C.UVGC_360_712,(0,0,3):C.UVGC_362_738})

V_468 = CTVertex(name = 'V_468',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stL, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.go, P.t, P.u] ], [ [P.go, P.u] ], [ [P.g, P.stL] ], [ [P.g, P.stL, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.suL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_365_771,(1,0,14):C.UVGC_365_772,(1,0,15):C.UVGC_365_773,(1,0,16):C.UVGC_379_824,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_479_953,(1,0,20):C.UVGC_365_777,(1,0,21):C.UVGC_365_778,(1,0,5):C.UVGC_379_825,(1,0,7):C.UVGC_479_954,(1,0,2):C.UVGC_379_826,(1,0,4):C.UVGC_479_955,(1,0,17):C.UVGC_361_731,(1,0,6):C.UVGC_365_784,(1,0,3):C.UVGC_365_783,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_364_751,(0,0,14):C.UVGC_364_752,(0,0,15):C.UVGC_364_753,(0,0,16):C.UVGC_378_821,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_473_943,(0,0,20):C.UVGC_364_757,(0,0,21):C.UVGC_364_758,(0,0,5):C.UVGC_378_822,(0,0,7):C.UVGC_473_944,(0,0,2):C.UVGC_378_823,(0,0,4):C.UVGC_473_945,(0,0,17):C.UVGC_360_711,(0,0,6):C.UVGC_364_764,(0,0,3):C.UVGC_364_763})

V_469 = CTVertex(name = 'V_469',
                 type = 'UV',
                 particles = [ P.stR__tilde__, P.stR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.go, P.t, P.u] ], [ [P.go, P.u] ], [ [P.g, P.stR] ], [ [P.g, P.stR, P.suL] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.stR, P.suL] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_361_720,(1,0,14):C.UVGC_361_721,(1,0,15):C.UVGC_361_722,(1,0,16):C.UVGC_361_723,(1,0,17):C.UVGC_381_830,(1,0,19):C.UVGC_419_896,(1,0,20):C.UVGC_361_726,(1,0,21):C.UVGC_361_727,(1,0,5):C.UVGC_381_831,(1,0,7):C.UVGC_419_898,(1,0,2):C.UVGC_381_832,(1,0,4):C.UVGC_475_949,(1,0,18):C.UVGC_361_731,(1,0,6):C.UVGC_361_732,(1,0,3):C.UVGC_363_744,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_360_700,(0,0,14):C.UVGC_360_701,(0,0,15):C.UVGC_360_702,(0,0,16):C.UVGC_360_703,(0,0,17):C.UVGC_380_827,(0,0,19):C.UVGC_418_891,(0,0,20):C.UVGC_360_706,(0,0,21):C.UVGC_360_707,(0,0,5):C.UVGC_380_828,(0,0,7):C.UVGC_418_893,(0,0,2):C.UVGC_380_829,(0,0,4):C.UVGC_477_951,(0,0,18):C.UVGC_360_711,(0,0,6):C.UVGC_360_712,(0,0,3):C.UVGC_362_738})

V_470 = CTVertex(name = 'V_470',
                 type = 'UV',
                 particles = [ P.suL__tilde__, P.suL__tilde__, P.suL, P.suL ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.suL] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_162_268,(1,0,1):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_328_561,(1,0,15):C.UVGC_162_281,(1,0,16):C.UVGC_162_282,(1,0,3):C.UVGC_328_562,(1,0,2):C.UVGC_328_563,(0,0,0):C.UVGC_162_268,(0,0,1):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_328_561,(0,0,15):C.UVGC_162_281,(0,0,16):C.UVGC_162_282,(0,0,3):C.UVGC_328_562,(0,0,2):C.UVGC_328_563})

V_471 = CTVertex(name = 'V_471',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sbL] ], [ [P.g, P.sbL, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbL, P.suR] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_361_715,(1,0,10):C.UVGC_363_739,(1,0,11):C.UVGC_361_717,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_419_897,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_363_741,(1,0,5):C.UVGC_361_729,(1,0,7):C.UVGC_419_899,(1,0,4):C.UVGC_476_950,(1,0,9):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_360_695,(0,0,10):C.UVGC_362_733,(0,0,11):C.UVGC_360_697,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_418_892,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_362_735,(0,0,5):C.UVGC_360_709,(0,0,7):C.UVGC_418_894,(0,0,4):C.UVGC_478_952,(0,0,9):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_472 = CTVertex(name = 'V_472',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.b, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sbR] ], [ [P.g, P.sbR, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.sbR, P.suR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_385_842,(1,0,11):C.UVGC_385_843,(1,0,12):C.UVGC_365_769,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_480_956,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_385_845,(1,0,5):C.UVGC_385_847,(1,0,7):C.UVGC_480_957,(1,0,4):C.UVGC_480_958,(1,0,10):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_384_835,(0,0,11):C.UVGC_384_836,(0,0,12):C.UVGC_364_749,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_474_946,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_384_838,(0,0,5):C.UVGC_384_840,(0,0,7):C.UVGC_474_947,(0,0,4):C.UVGC_474_948,(0,0,10):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_473 = CTVertex(name = 'V_473',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.scL] ], [ [P.g, P.scL, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scL, P.suR] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_367_791,(1,0,12):C.UVGC_361_718,(1,0,13):C.UVGC_361_719,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_419_897,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_367_793,(1,0,5):C.UVGC_367_794,(1,0,7):C.UVGC_419_899,(1,0,4):C.UVGC_476_950,(1,0,11):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_366_786,(0,0,12):C.UVGC_360_698,(0,0,13):C.UVGC_360_699,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_418_892,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_366_788,(0,0,5):C.UVGC_366_789,(0,0,7):C.UVGC_418_894,(0,0,4):C.UVGC_478_952,(0,0,11):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_474 = CTVertex(name = 'V_474',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.c, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.scR] ], [ [P.g, P.scR, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.scR, P.suR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_385_844,(1,0,13):C.UVGC_365_770,(1,0,14):C.UVGC_365_771,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_480_956,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_385_846,(1,0,5):C.UVGC_385_848,(1,0,7):C.UVGC_480_957,(1,0,4):C.UVGC_480_958,(1,0,12):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_384_837,(0,0,13):C.UVGC_364_750,(0,0,14):C.UVGC_364_751,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_474_946,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_384_839,(0,0,5):C.UVGC_384_841,(0,0,7):C.UVGC_474_947,(0,0,4):C.UVGC_474_948,(0,0,12):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_475 = CTVertex(name = 'V_475',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sdL] ], [ [P.g, P.sdL, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdL, P.suR] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_387_852,(1,0,14):C.UVGC_361_720,(1,0,15):C.UVGC_361_721,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_419_897,(1,0,21):C.UVGC_361_727,(1,0,0):C.UVGC_387_853,(1,0,5):C.UVGC_387_854,(1,0,7):C.UVGC_419_899,(1,0,4):C.UVGC_476_950,(1,0,13):C.UVGC_361_731,(1,0,1):C.UVGC_363_744,(1,0,6):C.UVGC_361_732,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_386_849,(0,0,14):C.UVGC_360_700,(0,0,15):C.UVGC_360_701,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_418_892,(0,0,21):C.UVGC_360_707,(0,0,0):C.UVGC_386_850,(0,0,5):C.UVGC_386_851,(0,0,7):C.UVGC_418_894,(0,0,4):C.UVGC_478_952,(0,0,13):C.UVGC_360_711,(0,0,1):C.UVGC_362_738,(0,0,6):C.UVGC_360_712})

V_476 = CTVertex(name = 'V_476',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.d, P.go, P.u] ], [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.sdR] ], [ [P.g, P.sdR, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.sdR, P.suR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,2):C.UVGC_361_713,(1,0,3):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_389_858,(1,0,15):C.UVGC_365_772,(1,0,16):C.UVGC_365_773,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_480_956,(1,0,21):C.UVGC_365_778,(1,0,0):C.UVGC_389_859,(1,0,5):C.UVGC_389_860,(1,0,7):C.UVGC_480_957,(1,0,4):C.UVGC_480_958,(1,0,14):C.UVGC_361_731,(1,0,1):C.UVGC_365_783,(1,0,6):C.UVGC_365_784,(0,0,2):C.UVGC_360_693,(0,0,3):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_388_855,(0,0,15):C.UVGC_364_752,(0,0,16):C.UVGC_364_753,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_474_946,(0,0,21):C.UVGC_364_758,(0,0,0):C.UVGC_388_856,(0,0,5):C.UVGC_388_857,(0,0,7):C.UVGC_474_947,(0,0,4):C.UVGC_474_948,(0,0,14):C.UVGC_360_711,(0,0,1):C.UVGC_364_763,(0,0,6):C.UVGC_364_764})

V_477 = CTVertex(name = 'V_477',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.u] ], [ [P.go, P.u] ], [ [P.g, P.ssL] ], [ [P.g, P.ssL, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssL, P.suR] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_361_720,(1,0,14):C.UVGC_391_864,(1,0,16):C.UVGC_361_722,(1,0,17):C.UVGC_361_723,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_419_897,(1,0,21):C.UVGC_361_727,(1,0,5):C.UVGC_391_865,(1,0,7):C.UVGC_419_899,(1,0,2):C.UVGC_391_866,(1,0,4):C.UVGC_476_950,(1,0,15):C.UVGC_361_731,(1,0,6):C.UVGC_361_732,(1,0,3):C.UVGC_363_744,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_360_700,(0,0,14):C.UVGC_390_861,(0,0,16):C.UVGC_360_702,(0,0,17):C.UVGC_360_703,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_418_892,(0,0,21):C.UVGC_360_707,(0,0,5):C.UVGC_390_862,(0,0,7):C.UVGC_418_894,(0,0,2):C.UVGC_390_863,(0,0,4):C.UVGC_478_952,(0,0,15):C.UVGC_360_711,(0,0,6):C.UVGC_360_712,(0,0,3):C.UVGC_362_738})

V_478 = CTVertex(name = 'V_478',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.go, P.s, P.u] ], [ [P.go, P.u] ], [ [P.g, P.ssR] ], [ [P.g, P.ssR, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.ssR, P.suR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_365_771,(1,0,14):C.UVGC_365_772,(1,0,15):C.UVGC_393_870,(1,0,17):C.UVGC_365_774,(1,0,18):C.UVGC_365_775,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_480_956,(1,0,21):C.UVGC_365_778,(1,0,5):C.UVGC_393_871,(1,0,7):C.UVGC_480_957,(1,0,2):C.UVGC_393_872,(1,0,4):C.UVGC_480_958,(1,0,16):C.UVGC_361_731,(1,0,6):C.UVGC_365_784,(1,0,3):C.UVGC_365_783,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_364_751,(0,0,14):C.UVGC_364_752,(0,0,15):C.UVGC_392_867,(0,0,17):C.UVGC_364_754,(0,0,18):C.UVGC_364_755,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_474_946,(0,0,21):C.UVGC_364_758,(0,0,5):C.UVGC_392_868,(0,0,7):C.UVGC_474_947,(0,0,2):C.UVGC_392_869,(0,0,4):C.UVGC_474_948,(0,0,16):C.UVGC_360_711,(0,0,6):C.UVGC_364_764,(0,0,3):C.UVGC_364_763})

V_479 = CTVertex(name = 'V_479',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.go, P.t, P.u] ], [ [P.go, P.u] ], [ [P.g, P.stL] ], [ [P.g, P.stL, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stL, P.suR] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,8):C.UVGC_367_790,(1,0,9):C.UVGC_363_739,(1,0,10):C.UVGC_361_717,(1,0,11):C.UVGC_361_718,(1,0,12):C.UVGC_361_719,(1,0,13):C.UVGC_361_720,(1,0,14):C.UVGC_361_721,(1,0,15):C.UVGC_361_722,(1,0,16):C.UVGC_415_886,(1,0,18):C.UVGC_361_724,(1,0,19):C.UVGC_361_725,(1,0,20):C.UVGC_419_897,(1,0,21):C.UVGC_361_727,(1,0,5):C.UVGC_415_887,(1,0,7):C.UVGC_419_899,(1,0,2):C.UVGC_415_888,(1,0,4):C.UVGC_476_950,(1,0,17):C.UVGC_361_731,(1,0,6):C.UVGC_361_732,(1,0,3):C.UVGC_363_744,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,8):C.UVGC_366_785,(0,0,9):C.UVGC_362_733,(0,0,10):C.UVGC_360_697,(0,0,11):C.UVGC_360_698,(0,0,12):C.UVGC_360_699,(0,0,13):C.UVGC_360_700,(0,0,14):C.UVGC_360_701,(0,0,15):C.UVGC_360_702,(0,0,16):C.UVGC_414_883,(0,0,18):C.UVGC_360_704,(0,0,19):C.UVGC_360_705,(0,0,20):C.UVGC_418_892,(0,0,21):C.UVGC_360_707,(0,0,5):C.UVGC_414_884,(0,0,7):C.UVGC_418_894,(0,0,2):C.UVGC_414_885,(0,0,4):C.UVGC_478_952,(0,0,17):C.UVGC_360_711,(0,0,6):C.UVGC_360_712,(0,0,3):C.UVGC_362_738})

V_480 = CTVertex(name = 'V_480',
                 type = 'UV',
                 particles = [ P.stR__tilde__, P.stR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.go, P.t, P.u] ], [ [P.go, P.u] ], [ [P.g, P.stR] ], [ [P.g, P.stR, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.stR, P.suR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_365_765,(1,0,8):C.UVGC_371_805,(1,0,9):C.UVGC_365_767,(1,0,10):C.UVGC_385_843,(1,0,11):C.UVGC_365_769,(1,0,12):C.UVGC_365_770,(1,0,13):C.UVGC_365_771,(1,0,14):C.UVGC_365_772,(1,0,15):C.UVGC_365_773,(1,0,16):C.UVGC_365_774,(1,0,17):C.UVGC_395_876,(1,0,19):C.UVGC_365_776,(1,0,20):C.UVGC_480_956,(1,0,21):C.UVGC_365_778,(1,0,5):C.UVGC_395_877,(1,0,7):C.UVGC_480_957,(1,0,2):C.UVGC_395_878,(1,0,4):C.UVGC_480_958,(1,0,18):C.UVGC_361_731,(1,0,6):C.UVGC_365_784,(1,0,3):C.UVGC_365_783,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_364_745,(0,0,8):C.UVGC_370_801,(0,0,9):C.UVGC_364_747,(0,0,10):C.UVGC_384_836,(0,0,11):C.UVGC_364_749,(0,0,12):C.UVGC_364_750,(0,0,13):C.UVGC_364_751,(0,0,14):C.UVGC_364_752,(0,0,15):C.UVGC_364_753,(0,0,16):C.UVGC_364_754,(0,0,17):C.UVGC_394_873,(0,0,19):C.UVGC_364_756,(0,0,20):C.UVGC_474_946,(0,0,21):C.UVGC_364_758,(0,0,5):C.UVGC_394_874,(0,0,7):C.UVGC_474_947,(0,0,2):C.UVGC_394_875,(0,0,4):C.UVGC_474_948,(0,0,18):C.UVGC_360_711,(0,0,6):C.UVGC_364_764,(0,0,3):C.UVGC_364_763})

V_481 = CTVertex(name = 'V_481',
                 type = 'UV',
                 particles = [ P.suL__tilde__, P.suL, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.suL] ], [ [P.g, P.suL, P.suR] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suL, P.suR] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_361_713,(1,0,1):C.UVGC_361_714,(1,0,6):C.UVGC_367_790,(1,0,7):C.UVGC_363_739,(1,0,8):C.UVGC_361_717,(1,0,9):C.UVGC_361_718,(1,0,10):C.UVGC_361_719,(1,0,11):C.UVGC_361_720,(1,0,12):C.UVGC_361_721,(1,0,13):C.UVGC_361_722,(1,0,14):C.UVGC_361_723,(1,0,15):C.UVGC_361_724,(1,0,16):C.UVGC_419_896,(1,0,18):C.UVGC_419_897,(1,0,19):C.UVGC_361_727,(1,0,3):C.UVGC_419_898,(1,0,5):C.UVGC_419_899,(1,0,2):C.UVGC_419_900,(1,0,17):C.UVGC_361_731,(1,0,4):C.UVGC_361_732,(0,0,0):C.UVGC_360_693,(0,0,1):C.UVGC_360_694,(0,0,6):C.UVGC_366_785,(0,0,7):C.UVGC_362_733,(0,0,8):C.UVGC_360_697,(0,0,9):C.UVGC_360_698,(0,0,10):C.UVGC_360_699,(0,0,11):C.UVGC_360_700,(0,0,12):C.UVGC_360_701,(0,0,13):C.UVGC_360_702,(0,0,14):C.UVGC_360_703,(0,0,15):C.UVGC_360_704,(0,0,16):C.UVGC_418_891,(0,0,18):C.UVGC_418_892,(0,0,19):C.UVGC_360_707,(0,0,3):C.UVGC_418_893,(0,0,5):C.UVGC_418_894,(0,0,2):C.UVGC_418_895,(0,0,17):C.UVGC_360_711,(0,0,4):C.UVGC_360_712})

V_482 = CTVertex(name = 'V_482',
                 type = 'UV',
                 particles = [ P.suR__tilde__, P.suR__tilde__, P.suR, P.suR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.suR] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_162_268,(1,0,1):C.UVGC_162_269,(1,0,4):C.UVGC_168_294,(1,0,5):C.UVGC_162_271,(1,0,6):C.UVGC_162_272,(1,0,7):C.UVGC_162_273,(1,0,8):C.UVGC_162_274,(1,0,9):C.UVGC_162_275,(1,0,10):C.UVGC_162_276,(1,0,11):C.UVGC_162_277,(1,0,12):C.UVGC_162_278,(1,0,13):C.UVGC_162_279,(1,0,14):C.UVGC_162_280,(1,0,15):C.UVGC_329_564,(1,0,16):C.UVGC_162_282,(1,0,3):C.UVGC_329_565,(1,0,2):C.UVGC_329_566,(0,0,0):C.UVGC_162_268,(0,0,1):C.UVGC_162_269,(0,0,4):C.UVGC_168_294,(0,0,5):C.UVGC_162_271,(0,0,6):C.UVGC_162_272,(0,0,7):C.UVGC_162_273,(0,0,8):C.UVGC_162_274,(0,0,9):C.UVGC_162_275,(0,0,10):C.UVGC_162_276,(0,0,11):C.UVGC_162_277,(0,0,12):C.UVGC_162_278,(0,0,13):C.UVGC_162_279,(0,0,14):C.UVGC_162_280,(0,0,15):C.UVGC_329_564,(0,0,16):C.UVGC_162_282,(0,0,3):C.UVGC_329_565,(0,0,2):C.UVGC_329_566})

V_483 = CTVertex(name = 'V_483',
                 type = 'UV',
                 particles = [ P.g, P.scL__tilde__, P.scL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.go] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.scL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,3):C.UVGC_159_222,(0,0,4):C.UVGC_159_223,(0,0,5):C.UVGC_159_224,(0,0,6):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,2):C.UVGC_171_303,(0,0,7):C.UVGC_171_304})

V_484 = CTVertex(name = 'V_484',
                 type = 'UV',
                 particles = [ P.g, P.stL__tilde__, P.stL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.stL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,3):C.UVGC_159_223,(0,0,4):C.UVGC_159_224,(0,0,5):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,7):C.UVGC_284_506,(0,0,6):C.UVGC_284_507})

V_485 = CTVertex(name = 'V_485',
                 type = 'UV',
                 particles = [ P.g, P.suL__tilde__, P.suL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.suL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,3):C.UVGC_159_223,(0,0,4):C.UVGC_159_224,(0,0,5):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,7):C.UVGC_323_553,(0,0,6):C.UVGC_323_554})

V_486 = CTVertex(name = 'V_486',
                 type = 'UV',
                 particles = [ P.g, P.g, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.go] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.scL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,3):C.UVGC_161_247,(2,0,4):C.UVGC_161_248,(2,0,5):C.UVGC_161_249,(2,0,6):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,2):C.UVGC_173_305,(2,0,7):C.UVGC_173_306,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,3):C.UVGC_161_247,(1,0,4):C.UVGC_161_248,(1,0,5):C.UVGC_161_249,(1,0,6):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,2):C.UVGC_173_305,(1,0,7):C.UVGC_173_306,(0,0,4):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_487 = CTVertex(name = 'V_487',
                 type = 'UV',
                 particles = [ P.g, P.g, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.stL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,3):C.UVGC_161_248,(2,0,4):C.UVGC_161_249,(2,0,5):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,7):C.UVGC_287_510,(2,0,6):C.UVGC_287_511,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,3):C.UVGC_161_248,(1,0,4):C.UVGC_161_249,(1,0,5):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,7):C.UVGC_287_510,(1,0,6):C.UVGC_287_511,(0,0,3):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_488 = CTVertex(name = 'V_488',
                 type = 'UV',
                 particles = [ P.g, P.g, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.suL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,3):C.UVGC_161_248,(2,0,4):C.UVGC_161_249,(2,0,5):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,7):C.UVGC_326_557,(2,0,6):C.UVGC_326_558,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,3):C.UVGC_161_248,(1,0,4):C.UVGC_161_249,(1,0,5):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,7):C.UVGC_326_557,(1,0,6):C.UVGC_326_558,(0,0,3):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_489 = CTVertex(name = 'V_489',
                 type = 'UV',
                 particles = [ P.g, P.scR__tilde__, P.scR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.go] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.scR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,3):C.UVGC_159_222,(0,0,4):C.UVGC_159_223,(0,0,5):C.UVGC_159_224,(0,0,6):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,2):C.UVGC_177_315,(0,0,7):C.UVGC_177_316})

V_490 = CTVertex(name = 'V_490',
                 type = 'UV',
                 particles = [ P.g, P.stR__tilde__, P.stR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.stR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,3):C.UVGC_159_223,(0,0,4):C.UVGC_159_224,(0,0,5):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,7):C.UVGC_285_508,(0,0,6):C.UVGC_285_509})

V_491 = CTVertex(name = 'V_491',
                 type = 'UV',
                 particles = [ P.g, P.suR__tilde__, P.suR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.suR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,3):C.UVGC_159_223,(0,0,4):C.UVGC_159_224,(0,0,5):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,7):C.UVGC_324_555,(0,0,6):C.UVGC_324_556})

V_492 = CTVertex(name = 'V_492',
                 type = 'UV',
                 particles = [ P.g, P.g, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.go] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.scR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,3):C.UVGC_161_247,(2,0,4):C.UVGC_161_248,(2,0,5):C.UVGC_161_249,(2,0,6):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,2):C.UVGC_179_317,(2,0,7):C.UVGC_179_318,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,3):C.UVGC_161_247,(1,0,4):C.UVGC_161_248,(1,0,5):C.UVGC_161_249,(1,0,6):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,2):C.UVGC_179_317,(1,0,7):C.UVGC_179_318,(0,0,4):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_493 = CTVertex(name = 'V_493',
                 type = 'UV',
                 particles = [ P.g, P.g, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.t] ], [ [P.g, P.stR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,3):C.UVGC_161_248,(2,0,4):C.UVGC_161_249,(2,0,5):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,7):C.UVGC_288_512,(2,0,6):C.UVGC_288_513,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,3):C.UVGC_161_248,(1,0,4):C.UVGC_161_249,(1,0,5):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,7):C.UVGC_288_512,(1,0,6):C.UVGC_288_513,(0,0,3):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_494 = CTVertex(name = 'V_494',
                 type = 'UV',
                 particles = [ P.g, P.g, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.u] ], [ [P.g, P.suR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,3):C.UVGC_161_248,(2,0,4):C.UVGC_161_249,(2,0,5):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,7):C.UVGC_327_559,(2,0,6):C.UVGC_327_560,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,3):C.UVGC_161_248,(1,0,4):C.UVGC_161_249,(1,0,5):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,7):C.UVGC_327_559,(1,0,6):C.UVGC_327_560,(0,0,3):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_495 = CTVertex(name = 'V_495',
                 type = 'UV',
                 particles = [ P.g, P.sbL__tilde__, P.sbL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.go] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,2):C.UVGC_159_221,(0,0,3):C.UVGC_159_222,(0,0,4):C.UVGC_159_223,(0,0,5):C.UVGC_159_224,(0,0,6):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,1):C.UVGC_159_241,(0,0,7):C.UVGC_159_242})

V_496 = CTVertex(name = 'V_496',
                 type = 'UV',
                 particles = [ P.g, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sdL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,4):C.UVGC_159_223,(0,0,5):C.UVGC_159_224,(0,0,6):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,3):C.UVGC_183_327,(0,0,7):C.UVGC_183_328})

V_497 = CTVertex(name = 'V_497',
                 type = 'UV',
                 particles = [ P.g, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.ssL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,3):C.UVGC_159_223,(0,0,4):C.UVGC_159_224,(0,0,5):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,7):C.UVGC_240_439,(0,0,6):C.UVGC_240_440})

V_498 = CTVertex(name = 'V_498',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.go] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sbL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,2):C.UVGC_161_246,(2,0,3):C.UVGC_161_247,(2,0,4):C.UVGC_161_248,(2,0,5):C.UVGC_161_249,(2,0,6):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,1):C.UVGC_161_266,(2,0,7):C.UVGC_161_267,(1,0,0):C.UVGC_161_245,(1,0,2):C.UVGC_161_246,(1,0,3):C.UVGC_161_247,(1,0,4):C.UVGC_161_248,(1,0,5):C.UVGC_161_249,(1,0,6):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,1):C.UVGC_161_266,(1,0,7):C.UVGC_161_267,(0,0,4):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_499 = CTVertex(name = 'V_499',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sdL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,4):C.UVGC_161_248,(2,0,5):C.UVGC_161_249,(2,0,6):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,3):C.UVGC_185_329,(2,0,7):C.UVGC_185_330,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,4):C.UVGC_161_248,(1,0,5):C.UVGC_161_249,(1,0,6):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,3):C.UVGC_185_329,(1,0,7):C.UVGC_185_330,(0,0,4):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_500 = CTVertex(name = 'V_500',
                 type = 'UV',
                 particles = [ P.g, P.g, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.ssL] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,3):C.UVGC_161_248,(2,0,4):C.UVGC_161_249,(2,0,5):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,7):C.UVGC_243_443,(2,0,6):C.UVGC_243_444,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,3):C.UVGC_161_248,(1,0,4):C.UVGC_161_249,(1,0,5):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,7):C.UVGC_243_443,(1,0,6):C.UVGC_243_444,(0,0,3):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_501 = CTVertex(name = 'V_501',
                 type = 'UV',
                 particles = [ P.g, P.sbR__tilde__, P.sbR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.go] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sbR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,2):C.UVGC_159_221,(0,0,3):C.UVGC_159_222,(0,0,4):C.UVGC_159_223,(0,0,5):C.UVGC_159_224,(0,0,6):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,1):C.UVGC_165_290,(0,0,7):C.UVGC_165_291})

V_502 = CTVertex(name = 'V_502',
                 type = 'UV',
                 particles = [ P.g, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sdR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,4):C.UVGC_159_223,(0,0,5):C.UVGC_159_224,(0,0,6):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,3):C.UVGC_189_339,(0,0,7):C.UVGC_189_340})

V_503 = CTVertex(name = 'V_503',
                 type = 'UV',
                 particles = [ P.g, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.ssR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_159_220,(0,0,1):C.UVGC_159_221,(0,0,2):C.UVGC_159_222,(0,0,3):C.UVGC_159_223,(0,0,4):C.UVGC_159_224,(0,0,5):C.UVGC_159_225,(0,0,8):C.UVGC_159_226,(0,0,9):C.UVGC_159_227,(0,0,10):C.UVGC_159_228,(0,0,11):C.UVGC_159_229,(0,0,12):C.UVGC_159_230,(0,0,13):C.UVGC_159_231,(0,0,14):C.UVGC_159_232,(0,0,15):C.UVGC_159_233,(0,0,16):C.UVGC_159_234,(0,0,17):C.UVGC_159_235,(0,0,18):C.UVGC_159_236,(0,0,19):C.UVGC_159_237,(0,0,20):C.UVGC_159_238,(0,0,21):C.UVGC_159_239,(0,0,22):C.UVGC_159_240,(0,0,7):C.UVGC_241_441,(0,0,6):C.UVGC_241_442})

V_504 = CTVertex(name = 'V_504',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.go] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sbR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,2):C.UVGC_161_246,(2,0,3):C.UVGC_161_247,(2,0,4):C.UVGC_161_248,(2,0,5):C.UVGC_161_249,(2,0,6):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,1):C.UVGC_167_292,(2,0,7):C.UVGC_167_293,(1,0,0):C.UVGC_161_245,(1,0,2):C.UVGC_161_246,(1,0,3):C.UVGC_161_247,(1,0,4):C.UVGC_161_248,(1,0,5):C.UVGC_161_249,(1,0,6):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,1):C.UVGC_167_292,(1,0,7):C.UVGC_167_293,(0,0,4):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_505 = CTVertex(name = 'V_505',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.go] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.g, P.sdR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,4):C.UVGC_161_248,(2,0,5):C.UVGC_161_249,(2,0,6):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,3):C.UVGC_191_341,(2,0,7):C.UVGC_191_342,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,4):C.UVGC_161_248,(1,0,5):C.UVGC_161_249,(1,0,6):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,3):C.UVGC_191_341,(1,0,7):C.UVGC_191_342,(0,0,4):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_506 = CTVertex(name = 'V_506',
                 type = 'UV',
                 particles = [ P.g, P.g, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.s] ], [ [P.g, P.ssR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,0):C.UVGC_161_245,(2,0,1):C.UVGC_161_246,(2,0,2):C.UVGC_161_247,(2,0,3):C.UVGC_161_248,(2,0,4):C.UVGC_161_249,(2,0,5):C.UVGC_161_250,(2,0,8):C.UVGC_161_251,(2,0,9):C.UVGC_161_252,(2,0,10):C.UVGC_161_253,(2,0,11):C.UVGC_161_254,(2,0,12):C.UVGC_161_255,(2,0,13):C.UVGC_161_256,(2,0,14):C.UVGC_161_257,(2,0,15):C.UVGC_161_258,(2,0,16):C.UVGC_161_259,(2,0,17):C.UVGC_161_260,(2,0,18):C.UVGC_161_261,(2,0,19):C.UVGC_161_262,(2,0,20):C.UVGC_161_263,(2,0,21):C.UVGC_161_264,(2,0,22):C.UVGC_161_265,(2,0,7):C.UVGC_244_445,(2,0,6):C.UVGC_244_446,(1,0,0):C.UVGC_161_245,(1,0,1):C.UVGC_161_246,(1,0,2):C.UVGC_161_247,(1,0,3):C.UVGC_161_248,(1,0,4):C.UVGC_161_249,(1,0,5):C.UVGC_161_250,(1,0,8):C.UVGC_161_251,(1,0,9):C.UVGC_161_252,(1,0,10):C.UVGC_161_253,(1,0,11):C.UVGC_161_254,(1,0,12):C.UVGC_161_255,(1,0,13):C.UVGC_161_256,(1,0,14):C.UVGC_161_257,(1,0,15):C.UVGC_161_258,(1,0,16):C.UVGC_161_259,(1,0,17):C.UVGC_161_260,(1,0,18):C.UVGC_161_261,(1,0,19):C.UVGC_161_262,(1,0,20):C.UVGC_161_263,(1,0,21):C.UVGC_161_264,(1,0,22):C.UVGC_161_265,(1,0,7):C.UVGC_244_445,(1,0,6):C.UVGC_244_446,(0,0,3):C.UVGC_160_243,(0,0,7):C.UVGC_160_244})

V_507 = CTVertex(name = 'V_507',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.suL] ], [ [P.go, P.suR] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_119_196,(0,1,2):C.UVGC_308_534,(0,1,0):C.UVGC_308_535,(0,2,2):C.UVGC_310_538,(0,2,1):C.UVGC_310_539})

V_508 = CTVertex(name = 'V_508',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.go, P.scL] ], [ [P.go, P.scR] ] ],
                 couplings = {(0,0,0):C.UVGC_119_196,(0,1,0):C.UVGC_209_387,(0,1,1):C.UVGC_209_388,(0,2,0):C.UVGC_213_395,(0,2,2):C.UVGC_213_396})

V_509 = CTVertex(name = 'V_509',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,2):C.UVGC_119_196,(0,1,2):C.UVGC_258_462,(0,1,0):C.UVGC_258_463,(0,1,1):C.UVGC_258_464,(0,2,2):C.UVGC_260_468,(0,2,0):C.UVGC_260_469,(0,2,1):C.UVGC_260_470})

V_510 = CTVertex(name = 'V_510',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.suL] ], [ [P.go, P.suR] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,8):C.UVGC_118_195,(0,1,0):C.UVGC_203_354,(0,1,1):C.UVGC_203_355,(0,1,2):C.UVGC_203_356,(0,1,3):C.UVGC_203_357,(0,1,4):C.UVGC_203_358,(0,1,5):C.UVGC_203_359,(0,1,9):C.UVGC_203_360,(0,1,10):C.UVGC_203_361,(0,1,11):C.UVGC_203_362,(0,1,12):C.UVGC_203_363,(0,1,13):C.UVGC_203_364,(0,1,14):C.UVGC_203_365,(0,1,15):C.UVGC_203_366,(0,1,16):C.UVGC_203_367,(0,1,17):C.UVGC_203_368,(0,1,18):C.UVGC_203_369,(0,1,19):C.UVGC_203_370,(0,1,20):C.UVGC_203_371,(0,1,21):C.UVGC_203_372,(0,1,22):C.UVGC_203_373,(0,1,23):C.UVGC_203_374,(0,1,8):C.UVGC_311_540,(0,1,6):C.UVGC_311_541,(0,2,0):C.UVGC_203_354,(0,2,1):C.UVGC_203_355,(0,2,2):C.UVGC_203_356,(0,2,3):C.UVGC_203_357,(0,2,4):C.UVGC_203_358,(0,2,5):C.UVGC_203_359,(0,2,9):C.UVGC_203_360,(0,2,10):C.UVGC_203_361,(0,2,11):C.UVGC_203_362,(0,2,12):C.UVGC_203_363,(0,2,13):C.UVGC_203_364,(0,2,14):C.UVGC_203_365,(0,2,15):C.UVGC_203_366,(0,2,16):C.UVGC_203_367,(0,2,17):C.UVGC_203_368,(0,2,18):C.UVGC_203_369,(0,2,19):C.UVGC_203_370,(0,2,20):C.UVGC_203_371,(0,2,21):C.UVGC_203_372,(0,2,22):C.UVGC_203_373,(0,2,23):C.UVGC_203_374,(0,2,8):C.UVGC_312_542,(0,2,7):C.UVGC_312_543})

V_511 = CTVertex(name = 'V_511',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.scL] ], [ [P.go, P.scR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_118_195,(0,1,0):C.UVGC_203_354,(0,1,1):C.UVGC_203_355,(0,1,3):C.UVGC_203_356,(0,1,4):C.UVGC_203_357,(0,1,5):C.UVGC_203_358,(0,1,6):C.UVGC_203_359,(0,1,9):C.UVGC_203_360,(0,1,10):C.UVGC_203_361,(0,1,11):C.UVGC_203_362,(0,1,12):C.UVGC_203_363,(0,1,13):C.UVGC_203_364,(0,1,14):C.UVGC_203_365,(0,1,15):C.UVGC_203_366,(0,1,16):C.UVGC_203_367,(0,1,17):C.UVGC_203_368,(0,1,18):C.UVGC_203_369,(0,1,19):C.UVGC_203_370,(0,1,20):C.UVGC_203_371,(0,1,21):C.UVGC_203_372,(0,1,22):C.UVGC_203_373,(0,1,23):C.UVGC_203_374,(0,1,2):C.UVGC_211_391,(0,1,7):C.UVGC_211_392,(0,2,0):C.UVGC_203_354,(0,2,1):C.UVGC_203_355,(0,2,3):C.UVGC_203_356,(0,2,4):C.UVGC_203_357,(0,2,5):C.UVGC_203_358,(0,2,6):C.UVGC_203_359,(0,2,9):C.UVGC_203_360,(0,2,10):C.UVGC_203_361,(0,2,11):C.UVGC_203_362,(0,2,12):C.UVGC_203_363,(0,2,13):C.UVGC_203_364,(0,2,14):C.UVGC_203_365,(0,2,15):C.UVGC_203_366,(0,2,16):C.UVGC_203_367,(0,2,17):C.UVGC_203_368,(0,2,18):C.UVGC_203_369,(0,2,19):C.UVGC_203_370,(0,2,20):C.UVGC_203_371,(0,2,21):C.UVGC_203_372,(0,2,22):C.UVGC_203_373,(0,2,23):C.UVGC_203_374,(0,2,2):C.UVGC_215_399,(0,2,8):C.UVGC_215_400})

V_512 = CTVertex(name = 'V_512',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,8):C.UVGC_118_195,(0,1,0):C.UVGC_203_354,(0,1,1):C.UVGC_203_355,(0,1,2):C.UVGC_203_356,(0,1,3):C.UVGC_203_357,(0,1,4):C.UVGC_203_358,(0,1,5):C.UVGC_203_359,(0,1,9):C.UVGC_203_360,(0,1,10):C.UVGC_203_361,(0,1,11):C.UVGC_203_362,(0,1,12):C.UVGC_203_363,(0,1,13):C.UVGC_203_364,(0,1,14):C.UVGC_203_365,(0,1,15):C.UVGC_203_366,(0,1,16):C.UVGC_203_367,(0,1,17):C.UVGC_203_368,(0,1,18):C.UVGC_203_369,(0,1,19):C.UVGC_203_370,(0,1,20):C.UVGC_203_371,(0,1,21):C.UVGC_203_372,(0,1,22):C.UVGC_203_373,(0,1,23):C.UVGC_203_374,(0,1,8):C.UVGC_261_471,(0,1,6):C.UVGC_261_472,(0,1,7):C.UVGC_261_473,(0,2,0):C.UVGC_203_354,(0,2,1):C.UVGC_203_355,(0,2,2):C.UVGC_203_356,(0,2,3):C.UVGC_203_357,(0,2,4):C.UVGC_203_358,(0,2,5):C.UVGC_203_359,(0,2,9):C.UVGC_203_360,(0,2,10):C.UVGC_203_361,(0,2,11):C.UVGC_203_362,(0,2,12):C.UVGC_203_363,(0,2,13):C.UVGC_203_364,(0,2,14):C.UVGC_203_365,(0,2,15):C.UVGC_203_366,(0,2,16):C.UVGC_203_367,(0,2,17):C.UVGC_203_368,(0,2,18):C.UVGC_203_369,(0,2,19):C.UVGC_203_370,(0,2,20):C.UVGC_203_371,(0,2,21):C.UVGC_203_372,(0,2,22):C.UVGC_203_373,(0,2,23):C.UVGC_203_374,(0,2,8):C.UVGC_262_474,(0,2,6):C.UVGC_262_475,(0,2,7):C.UVGC_262_476})

V_513 = CTVertex(name = 'V_513',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.go, P.sdL] ], [ [P.go, P.suL] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_489_959,(0,0,4):C.UVGC_489_960,(0,0,2):C.UVGC_489_961,(0,0,3):C.UVGC_489_962,(0,0,1):C.UVGC_351_678})

V_514 = CTVertex(name = 'V_514',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.go, P.scL] ], [ [P.go, P.ssL] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_351_674,(0,0,4):C.UVGC_351_675,(0,0,2):C.UVGC_351_676,(0,0,3):C.UVGC_351_677,(0,0,1):C.UVGC_351_678})

V_515 = CTVertex(name = 'V_515',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.go, P.sbL] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_430_909,(0,0,5):C.UVGC_430_910,(0,0,2):C.UVGC_430_911,(0,0,3):C.UVGC_430_912,(0,0,4):C.UVGC_430_913,(0,0,1):C.UVGC_351_678})

V_516 = CTVertex(name = 'V_516',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.suL] ], [ [P.go, P.suR] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_316_544,(0,0,0):C.UVGC_316_545,(0,1,2):C.UVGC_317_546,(0,1,1):C.UVGC_317_547})

V_517 = CTVertex(name = 'V_517',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.go, P.scL] ], [ [P.go, P.scR] ] ],
                 couplings = {(0,0,0):C.UVGC_212_393,(0,0,1):C.UVGC_212_394,(0,1,0):C.UVGC_216_401,(0,1,2):C.UVGC_216_402})

V_518 = CTVertex(name = 'V_518',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,2):C.UVGC_266_480,(0,0,0):C.UVGC_266_481,(0,0,1):C.UVGC_266_482,(0,1,2):C.UVGC_267_483,(0,1,0):C.UVGC_267_484,(0,1,1):C.UVGC_267_485})

V_519 = CTVertex(name = 'V_519',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.go, P.sdL] ], [ [P.go, P.sdR] ] ],
                 couplings = {(0,0,0):C.UVGC_117_194,(0,1,0):C.UVGC_217_403,(0,1,1):C.UVGC_217_404,(0,2,0):C.UVGC_221_411,(0,2,2):C.UVGC_221_412})

V_520 = CTVertex(name = 'V_520',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.ssL] ], [ [P.go, P.ssR] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,2):C.UVGC_117_194,(0,1,2):C.UVGC_226_421,(0,1,0):C.UVGC_226_422,(0,2,2):C.UVGC_228_425,(0,2,1):C.UVGC_228_426})

V_521 = CTVertex(name = 'V_521',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.go, P.sbL] ], [ [P.go, P.sbR] ] ],
                 couplings = {(0,0,0):C.UVGC_117_194,(0,1,0):C.UVGC_201_350,(0,1,1):C.UVGC_201_351,(0,2,0):C.UVGC_205_379,(0,2,2):C.UVGC_205_380})

V_522 = CTVertex(name = 'V_522',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.sdL] ], [ [P.go, P.sdR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_118_195,(0,1,0):C.UVGC_203_354,(0,1,1):C.UVGC_203_355,(0,1,2):C.UVGC_203_356,(0,1,4):C.UVGC_203_357,(0,1,5):C.UVGC_203_358,(0,1,6):C.UVGC_203_359,(0,1,9):C.UVGC_203_360,(0,1,10):C.UVGC_203_361,(0,1,11):C.UVGC_203_362,(0,1,12):C.UVGC_203_363,(0,1,13):C.UVGC_203_364,(0,1,14):C.UVGC_203_365,(0,1,15):C.UVGC_203_366,(0,1,16):C.UVGC_203_367,(0,1,17):C.UVGC_203_368,(0,1,18):C.UVGC_203_369,(0,1,19):C.UVGC_203_370,(0,1,20):C.UVGC_203_371,(0,1,21):C.UVGC_203_372,(0,1,22):C.UVGC_203_373,(0,1,23):C.UVGC_203_374,(0,1,3):C.UVGC_219_407,(0,1,7):C.UVGC_219_408,(0,2,0):C.UVGC_203_354,(0,2,1):C.UVGC_203_355,(0,2,2):C.UVGC_203_356,(0,2,4):C.UVGC_203_357,(0,2,5):C.UVGC_203_358,(0,2,6):C.UVGC_203_359,(0,2,9):C.UVGC_203_360,(0,2,10):C.UVGC_203_361,(0,2,11):C.UVGC_203_362,(0,2,12):C.UVGC_203_363,(0,2,13):C.UVGC_203_364,(0,2,14):C.UVGC_203_365,(0,2,15):C.UVGC_203_366,(0,2,16):C.UVGC_203_367,(0,2,17):C.UVGC_203_368,(0,2,18):C.UVGC_203_369,(0,2,19):C.UVGC_203_370,(0,2,20):C.UVGC_203_371,(0,2,21):C.UVGC_203_372,(0,2,22):C.UVGC_203_373,(0,2,23):C.UVGC_203_374,(0,2,3):C.UVGC_223_415,(0,2,8):C.UVGC_223_416})

V_523 = CTVertex(name = 'V_523',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.ssL] ], [ [P.go, P.ssR] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,8):C.UVGC_118_195,(0,1,0):C.UVGC_203_354,(0,1,1):C.UVGC_203_355,(0,1,2):C.UVGC_203_356,(0,1,3):C.UVGC_203_357,(0,1,4):C.UVGC_203_358,(0,1,5):C.UVGC_203_359,(0,1,9):C.UVGC_203_360,(0,1,10):C.UVGC_203_361,(0,1,11):C.UVGC_203_362,(0,1,12):C.UVGC_203_363,(0,1,13):C.UVGC_203_364,(0,1,14):C.UVGC_203_365,(0,1,15):C.UVGC_203_366,(0,1,16):C.UVGC_203_367,(0,1,17):C.UVGC_203_368,(0,1,18):C.UVGC_203_369,(0,1,19):C.UVGC_203_370,(0,1,20):C.UVGC_203_371,(0,1,21):C.UVGC_203_372,(0,1,22):C.UVGC_203_373,(0,1,23):C.UVGC_203_374,(0,1,8):C.UVGC_229_427,(0,1,6):C.UVGC_229_428,(0,2,0):C.UVGC_203_354,(0,2,1):C.UVGC_203_355,(0,2,2):C.UVGC_203_356,(0,2,3):C.UVGC_203_357,(0,2,4):C.UVGC_203_358,(0,2,5):C.UVGC_203_359,(0,2,9):C.UVGC_203_360,(0,2,10):C.UVGC_203_361,(0,2,11):C.UVGC_203_362,(0,2,12):C.UVGC_203_363,(0,2,13):C.UVGC_203_364,(0,2,14):C.UVGC_203_365,(0,2,15):C.UVGC_203_366,(0,2,16):C.UVGC_203_367,(0,2,17):C.UVGC_203_368,(0,2,18):C.UVGC_203_369,(0,2,19):C.UVGC_203_370,(0,2,20):C.UVGC_203_371,(0,2,21):C.UVGC_203_372,(0,2,22):C.UVGC_203_373,(0,2,23):C.UVGC_203_374,(0,2,8):C.UVGC_230_429,(0,2,7):C.UVGC_230_430})

V_524 = CTVertex(name = 'V_524',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.go, P.sbL] ], [ [P.go, P.sbR] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_118_195,(0,1,0):C.UVGC_203_354,(0,1,2):C.UVGC_203_355,(0,1,3):C.UVGC_203_356,(0,1,4):C.UVGC_203_357,(0,1,5):C.UVGC_203_358,(0,1,6):C.UVGC_203_359,(0,1,9):C.UVGC_203_360,(0,1,10):C.UVGC_203_361,(0,1,11):C.UVGC_203_362,(0,1,12):C.UVGC_203_363,(0,1,13):C.UVGC_203_364,(0,1,14):C.UVGC_203_365,(0,1,15):C.UVGC_203_366,(0,1,16):C.UVGC_203_367,(0,1,17):C.UVGC_203_368,(0,1,18):C.UVGC_203_369,(0,1,19):C.UVGC_203_370,(0,1,20):C.UVGC_203_371,(0,1,21):C.UVGC_203_372,(0,1,22):C.UVGC_203_373,(0,1,23):C.UVGC_203_374,(0,1,1):C.UVGC_203_375,(0,1,7):C.UVGC_203_376,(0,2,0):C.UVGC_203_354,(0,2,2):C.UVGC_203_355,(0,2,3):C.UVGC_203_356,(0,2,4):C.UVGC_203_357,(0,2,5):C.UVGC_203_358,(0,2,6):C.UVGC_203_359,(0,2,9):C.UVGC_203_360,(0,2,10):C.UVGC_203_361,(0,2,11):C.UVGC_203_362,(0,2,12):C.UVGC_203_363,(0,2,13):C.UVGC_203_364,(0,2,14):C.UVGC_203_365,(0,2,15):C.UVGC_203_366,(0,2,16):C.UVGC_203_367,(0,2,17):C.UVGC_203_368,(0,2,18):C.UVGC_203_369,(0,2,19):C.UVGC_203_370,(0,2,20):C.UVGC_203_371,(0,2,21):C.UVGC_203_372,(0,2,22):C.UVGC_203_373,(0,2,23):C.UVGC_203_374,(0,2,1):C.UVGC_207_383,(0,2,8):C.UVGC_207_384})

V_525 = CTVertex(name = 'V_525',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.go, P.sdL] ], [ [P.go, P.suL] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_489_959,(0,0,4):C.UVGC_489_960,(0,0,2):C.UVGC_489_961,(0,0,3):C.UVGC_489_962,(0,0,1):C.UVGC_351_678})

V_526 = CTVertex(name = 'V_526',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.go, P.scL] ], [ [P.go, P.ssL] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_351_674,(0,0,4):C.UVGC_351_675,(0,0,2):C.UVGC_351_676,(0,0,3):C.UVGC_351_677,(0,0,1):C.UVGC_351_678})

V_527 = CTVertex(name = 'V_527',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.go, P.sbL] ], [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_430_909,(0,0,5):C.UVGC_430_910,(0,0,2):C.UVGC_430_911,(0,0,3):C.UVGC_430_912,(0,0,4):C.UVGC_430_913,(0,0,1):C.UVGC_351_678})

V_528 = CTVertex(name = 'V_528',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.go, P.sdL] ], [ [P.go, P.sdR] ] ],
                 couplings = {(0,0,0):C.UVGC_220_409,(0,0,1):C.UVGC_220_410,(0,1,0):C.UVGC_224_417,(0,1,2):C.UVGC_224_418})

V_529 = CTVertex(name = 'V_529',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.go, P.ssL] ], [ [P.go, P.ssR] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,2):C.UVGC_234_431,(0,0,0):C.UVGC_234_432,(0,1,2):C.UVGC_235_433,(0,1,1):C.UVGC_235_434})

V_530 = CTVertex(name = 'V_530',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.go, P.sbL] ], [ [P.go, P.sbR] ] ],
                 couplings = {(0,0,0):C.UVGC_204_377,(0,0,1):C.UVGC_204_378,(0,1,0):C.UVGC_208_385,(0,1,2):C.UVGC_208_386})

V_531 = CTVertex(name = 'V_531',
                 type = 'UV',
                 particles = [ P.go, P.go ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4, L.FF5, L.FF6 ],
                 loop_particles = [ [ [P.b, P.sbL] ], [ [P.b, P.sbR] ], [ [P.c, P.scL] ], [ [P.c, P.scR] ], [ [P.d, P.sdL] ], [ [P.d, P.sdR] ], [ [P.g, P.go] ], [ [P.s, P.ssL] ], [ [P.s, P.ssR] ], [ [P.stL, P.t] ], [ [P.stR, P.t] ], [ [P.suL, P.u] ], [ [P.suR, P.u] ] ],
                 couplings = {(0,2,0):C.UVGC_342_587,(0,2,1):C.UVGC_342_588,(0,2,2):C.UVGC_342_589,(0,2,3):C.UVGC_342_590,(0,2,4):C.UVGC_342_591,(0,2,5):C.UVGC_342_592,(0,2,6):C.UVGC_342_593,(0,2,7):C.UVGC_342_594,(0,2,8):C.UVGC_342_595,(0,2,9):C.UVGC_342_596,(0,2,10):C.UVGC_342_597,(0,2,11):C.UVGC_342_598,(0,2,12):C.UVGC_342_599,(0,4,0):C.UVGC_342_587,(0,4,1):C.UVGC_342_588,(0,4,2):C.UVGC_342_589,(0,4,3):C.UVGC_342_590,(0,4,4):C.UVGC_342_591,(0,4,5):C.UVGC_342_592,(0,4,6):C.UVGC_342_593,(0,4,7):C.UVGC_342_594,(0,4,8):C.UVGC_342_595,(0,4,9):C.UVGC_342_596,(0,4,10):C.UVGC_342_597,(0,4,11):C.UVGC_342_598,(0,4,12):C.UVGC_342_599,(0,3,6):C.UVGC_200_349,(0,5,6):C.UVGC_200_349,(0,1,0):C.UVGC_341_574,(0,1,1):C.UVGC_341_575,(0,1,2):C.UVGC_341_576,(0,1,3):C.UVGC_341_577,(0,1,4):C.UVGC_341_578,(0,1,5):C.UVGC_341_579,(0,1,6):C.UVGC_341_580,(0,1,7):C.UVGC_341_581,(0,1,8):C.UVGC_341_582,(0,1,9):C.UVGC_341_583,(0,1,10):C.UVGC_341_584,(0,1,11):C.UVGC_341_585,(0,1,12):C.UVGC_341_586,(0,0,0):C.UVGC_343_600,(0,0,1):C.UVGC_343_601,(0,0,2):C.UVGC_343_602,(0,0,3):C.UVGC_343_603,(0,0,4):C.UVGC_343_604,(0,0,5):C.UVGC_343_605,(0,0,6):C.UVGC_343_606,(0,0,7):C.UVGC_343_607,(0,0,8):C.UVGC_343_608,(0,0,9):C.UVGC_343_609,(0,0,10):C.UVGC_343_610,(0,0,11):C.UVGC_343_611,(0,0,12):C.UVGC_343_612})

V_532 = CTVertex(name = 'V_532',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF4, L.FF6 ],
                 loop_particles = [ [ [P.go, P.suL] ], [ [P.go, P.suR] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_116_193,(0,1,2):C.UVGC_307_532,(0,1,0):C.UVGC_307_533,(0,2,2):C.UVGC_309_536,(0,2,1):C.UVGC_309_537})

V_533 = CTVertex(name = 'V_533',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF4, L.FF6 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.go, P.scL] ], [ [P.go, P.scR] ] ],
                 couplings = {(0,0,0):C.UVGC_116_193,(0,1,0):C.UVGC_210_389,(0,1,1):C.UVGC_210_390,(0,2,0):C.UVGC_214_397,(0,2,2):C.UVGC_214_398})

V_534 = CTVertex(name = 'V_534',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF4, L.FF5, L.FF6 ],
                 loop_particles = [ [ [P.go, P.stL] ], [ [P.go, P.stR] ], [ [P.g, P.t] ] ],
                 couplings = {(0,1,2):C.UVGC_265_477,(0,1,0):C.UVGC_265_478,(0,1,1):C.UVGC_265_479,(0,3,2):C.UVGC_265_477,(0,3,0):C.UVGC_265_478,(0,3,1):C.UVGC_265_479,(0,2,2):C.UVGC_257_459,(0,2,0):C.UVGC_257_460,(0,2,1):C.UVGC_257_461,(0,4,2):C.UVGC_259_465,(0,4,0):C.UVGC_259_466,(0,4,1):C.UVGC_259_467,(0,0,2):C.UVGC_116_193})

V_535 = CTVertex(name = 'V_535',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF4, L.FF6 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.go, P.sdL] ], [ [P.go, P.sdR] ] ],
                 couplings = {(0,0,0):C.UVGC_116_193,(0,1,0):C.UVGC_218_405,(0,1,1):C.UVGC_218_406,(0,2,0):C.UVGC_222_413,(0,2,2):C.UVGC_222_414})

V_536 = CTVertex(name = 'V_536',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF4, L.FF6 ],
                 loop_particles = [ [ [P.go, P.ssL] ], [ [P.go, P.ssR] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,2):C.UVGC_116_193,(0,1,2):C.UVGC_225_419,(0,1,0):C.UVGC_225_420,(0,2,2):C.UVGC_227_423,(0,2,1):C.UVGC_227_424})

V_537 = CTVertex(name = 'V_537',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF4, L.FF6 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.go, P.sbL] ], [ [P.go, P.sbR] ] ],
                 couplings = {(0,0,0):C.UVGC_116_193,(0,1,0):C.UVGC_202_352,(0,1,1):C.UVGC_202_353,(0,2,0):C.UVGC_206_381,(0,2,2):C.UVGC_206_382})

V_538 = CTVertex(name = 'V_538',
                 type = 'UV',
                 particles = [ P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.u] ], [ [P.g, P.suL] ], [ [P.suL] ] ],
                 couplings = {(0,0,2):C.UVGC_330_567,(0,0,1):C.UVGC_330_568,(0,0,0):C.UVGC_330_569,(0,1,1):C.UVGC_318_548,(0,1,0):C.UVGC_318_549})

V_539 = CTVertex(name = 'V_539',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g, P.scL] ], [ [P.scL] ] ],
                 couplings = {(0,0,2):C.UVGC_175_310,(0,0,0):C.UVGC_175_311,(0,0,1):C.UVGC_175_312,(0,1,0):C.UVGC_170_301,(0,1,1):C.UVGC_170_302})

V_540 = CTVertex(name = 'V_540',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.t] ], [ [P.g, P.stL] ], [ [P.stL] ] ],
                 couplings = {(0,0,2):C.UVGC_292_521,(0,0,1):C.UVGC_292_522,(0,0,0):C.UVGC_292_523,(0,1,1):C.UVGC_280_502,(0,1,0):C.UVGC_280_503})

V_541 = CTVertex(name = 'V_541',
                 type = 'UV',
                 particles = [ P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.u] ], [ [P.g, P.suR] ], [ [P.suR] ] ],
                 couplings = {(0,0,2):C.UVGC_331_570,(0,0,1):C.UVGC_331_571,(0,0,0):C.UVGC_331_572,(0,1,1):C.UVGC_319_550,(0,1,0):C.UVGC_319_551})

V_542 = CTVertex(name = 'V_542',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.c, P.go] ], [ [P.g, P.scR] ], [ [P.scR] ] ],
                 couplings = {(0,0,2):C.UVGC_181_322,(0,0,0):C.UVGC_181_323,(0,0,1):C.UVGC_181_324,(0,1,0):C.UVGC_176_313,(0,1,1):C.UVGC_176_314})

V_543 = CTVertex(name = 'V_543',
                 type = 'UV',
                 particles = [ P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.t] ], [ [P.g, P.stR] ], [ [P.stR] ] ],
                 couplings = {(0,0,2):C.UVGC_293_524,(0,0,1):C.UVGC_293_525,(0,0,0):C.UVGC_293_526,(0,1,1):C.UVGC_281_504,(0,1,0):C.UVGC_281_505})

V_544 = CTVertex(name = 'V_544',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g, P.sdL] ], [ [P.sdL] ] ],
                 couplings = {(0,0,2):C.UVGC_187_334,(0,0,0):C.UVGC_187_335,(0,0,1):C.UVGC_187_336,(0,1,0):C.UVGC_182_325,(0,1,1):C.UVGC_182_326})

V_545 = CTVertex(name = 'V_545',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.g, P.ssL] ], [ [P.ssL] ] ],
                 couplings = {(0,0,2):C.UVGC_247_453,(0,0,1):C.UVGC_247_454,(0,0,0):C.UVGC_247_455,(0,1,1):C.UVGC_236_435,(0,1,0):C.UVGC_236_436})

V_546 = CTVertex(name = 'V_546',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g, P.sbL] ], [ [P.sbL] ] ],
                 couplings = {(0,0,2):C.UVGC_163_285,(0,0,0):C.UVGC_163_286,(0,0,1):C.UVGC_163_287,(0,1,0):C.UVGC_158_218,(0,1,1):C.UVGC_158_219})

V_547 = CTVertex(name = 'V_547',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.d, P.go] ], [ [P.g, P.sdR] ], [ [P.sdR] ] ],
                 couplings = {(0,0,2):C.UVGC_193_346,(0,0,0):C.UVGC_193_347,(0,0,1):C.UVGC_193_348,(0,1,0):C.UVGC_188_337,(0,1,1):C.UVGC_188_338})

V_548 = CTVertex(name = 'V_548',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.s] ], [ [P.g, P.ssR] ], [ [P.ssR] ] ],
                 couplings = {(0,0,2):C.UVGC_248_456,(0,0,1):C.UVGC_248_457,(0,0,0):C.UVGC_248_458,(0,1,1):C.UVGC_237_437,(0,1,0):C.UVGC_237_438})

V_549 = CTVertex(name = 'V_549',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.b, P.go] ], [ [P.g, P.sbR] ], [ [P.sbR] ] ],
                 couplings = {(0,0,2):C.UVGC_169_298,(0,0,0):C.UVGC_169_299,(0,0,1):C.UVGC_169_300,(0,1,0):C.UVGC_164_288,(0,1,1):C.UVGC_164_289})

V_550 = CTVertex(name = 'V_550',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.go] ], [ [P.s] ], [ [P.sbL] ], [ [P.sbR] ], [ [P.scL] ], [ [P.scR] ], [ [P.sdL] ], [ [P.sdR] ], [ [P.ssL] ], [ [P.ssR] ], [ [P.stL] ], [ [P.stR] ], [ [P.suL] ], [ [P.suR] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_106_49,(0,0,1):C.UVGC_106_50,(0,0,2):C.UVGC_106_51,(0,0,3):C.UVGC_106_52,(0,0,4):C.UVGC_106_53,(0,0,5):C.UVGC_106_54,(0,0,6):C.UVGC_106_55,(0,0,7):C.UVGC_106_56,(0,0,8):C.UVGC_106_57,(0,0,9):C.UVGC_106_58,(0,0,10):C.UVGC_106_59,(0,0,11):C.UVGC_106_60,(0,0,12):C.UVGC_106_61,(0,0,13):C.UVGC_106_62,(0,0,14):C.UVGC_106_63,(0,0,15):C.UVGC_106_64,(0,0,16):C.UVGC_106_65,(0,0,17):C.UVGC_106_66,(0,0,18):C.UVGC_106_67,(0,0,19):C.UVGC_106_68,(0,0,20):C.UVGC_106_69,(0,1,0):C.UVGC_107_70,(0,1,1):C.UVGC_107_71,(0,1,2):C.UVGC_107_72,(0,1,3):C.UVGC_107_73,(0,1,4):C.UVGC_107_74,(0,1,5):C.UVGC_107_75,(0,1,6):C.UVGC_107_76,(0,1,7):C.UVGC_107_77,(0,1,8):C.UVGC_107_78,(0,1,9):C.UVGC_107_79,(0,1,10):C.UVGC_107_80,(0,1,11):C.UVGC_107_81,(0,1,12):C.UVGC_107_82,(0,1,13):C.UVGC_107_83,(0,1,14):C.UVGC_107_84,(0,1,15):C.UVGC_107_85,(0,1,16):C.UVGC_107_86,(0,1,17):C.UVGC_107_87,(0,1,18):C.UVGC_107_88,(0,1,19):C.UVGC_107_89,(0,1,20):C.UVGC_107_90})

V_551 = CTVertex(name = 'V_551',
                 type = 'UV',
                 particles = [ P.go, P.go, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.sbL], [P.d, P.sdL], [P.s, P.ssL] ], [ [P.b, P.sbR], [P.d, P.sdR], [P.s, P.ssR] ], [ [P.c, P.scL], [P.stL, P.t], [P.suL, P.u] ], [ [P.c, P.scR], [P.stR, P.t], [P.suR, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_344_613,(0,0,1):C.UVGC_344_614,(0,0,2):C.UVGC_344_615,(0,0,3):C.UVGC_344_616})

V_552 = CTVertex(name = 'V_552',
                 type = 'UV',
                 particles = [ P.go, P.go, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.sbL], [P.d, P.sdL], [P.s, P.ssL] ], [ [P.b, P.sbR], [P.d, P.sdR], [P.s, P.ssR] ], [ [P.c, P.scL], [P.stL, P.t], [P.suL, P.u] ], [ [P.c, P.scR], [P.stR, P.t], [P.suR, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_346_651,(0,0,1):C.UVGC_346_652,(0,0,2):C.UVGC_346_653,(0,0,3):C.UVGC_346_654})

V_553 = CTVertex(name = 'V_553',
                 type = 'UV',
                 particles = [ P.a, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_133_207,(0,1,0):C.UVGC_320_552})

V_554 = CTVertex(name = 'V_554',
                 type = 'UV',
                 particles = [ P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_136_210,(0,1,0):C.UVGC_333_573})

V_555 = CTVertex(name = 'V_555',
                 type = 'UV',
                 particles = [ P.a, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_133_207})

V_556 = CTVertex(name = 'V_556',
                 type = 'UV',
                 particles = [ P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_136_210})

V_557 = CTVertex(name = 'V_557',
                 type = 'UV',
                 particles = [ P.a, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_133_207})

V_558 = CTVertex(name = 'V_558',
                 type = 'UV',
                 particles = [ P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_136_210})

V_559 = CTVertex(name = 'V_559',
                 type = 'UV',
                 particles = [ P.a, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_133_207})

V_560 = CTVertex(name = 'V_560',
                 type = 'UV',
                 particles = [ P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_137_211})

V_561 = CTVertex(name = 'V_561',
                 type = 'UV',
                 particles = [ P.a, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_133_207})

V_562 = CTVertex(name = 'V_562',
                 type = 'UV',
                 particles = [ P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_137_211})

V_563 = CTVertex(name = 'V_563',
                 type = 'UV',
                 particles = [ P.a, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_133_207})

V_564 = CTVertex(name = 'V_564',
                 type = 'UV',
                 particles = [ P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_137_211})

V_565 = CTVertex(name = 'V_565',
                 type = 'UV',
                 particles = [ P.W__plus__, P.sdL, P.suL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_354_681})

V_566 = CTVertex(name = 'V_566',
                 type = 'UV',
                 particles = [ P.W__minus__, P.sdL__tilde__, P.suL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_355_682})

V_567 = CTVertex(name = 'V_567',
                 type = 'UV',
                 particles = [ P.a, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_119_196})

V_568 = CTVertex(name = 'V_568',
                 type = 'UV',
                 particles = [ P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_122_199})

V_569 = CTVertex(name = 'V_569',
                 type = 'UV',
                 particles = [ P.W__plus__, P.scL__tilde__, P.ssL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_355_682})

V_570 = CTVertex(name = 'V_570',
                 type = 'UV',
                 particles = [ P.W__minus__, P.scL, P.ssL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_354_681})

V_571 = CTVertex(name = 'V_571',
                 type = 'UV',
                 particles = [ P.a, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_119_196})

V_572 = CTVertex(name = 'V_572',
                 type = 'UV',
                 particles = [ P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_122_199})

V_573 = CTVertex(name = 'V_573',
                 type = 'UV',
                 particles = [ P.W__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_354_681})

V_574 = CTVertex(name = 'V_574',
                 type = 'UV',
                 particles = [ P.W__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_355_682})

V_575 = CTVertex(name = 'V_575',
                 type = 'UV',
                 particles = [ P.a, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_119_196})

V_576 = CTVertex(name = 'V_576',
                 type = 'UV',
                 particles = [ P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_122_199})

V_577 = CTVertex(name = 'V_577',
                 type = 'UV',
                 particles = [ P.a, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_119_196})

V_578 = CTVertex(name = 'V_578',
                 type = 'UV',
                 particles = [ P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_123_200})

V_579 = CTVertex(name = 'V_579',
                 type = 'UV',
                 particles = [ P.a, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_119_196})

V_580 = CTVertex(name = 'V_580',
                 type = 'UV',
                 particles = [ P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_123_200})

V_581 = CTVertex(name = 'V_581',
                 type = 'UV',
                 particles = [ P.a, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_119_196})

V_582 = CTVertex(name = 'V_582',
                 type = 'UV',
                 particles = [ P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_123_200})

V_583 = CTVertex(name = 'V_583',
                 type = 'UV',
                 particles = [ P.H, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_305_530})

V_584 = CTVertex(name = 'V_584',
                 type = 'UV',
                 particles = [ P.H, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_303_528})

V_585 = CTVertex(name = 'V_585',
                 type = 'UV',
                 particles = [ P.G0, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_304_529})

V_586 = CTVertex(name = 'V_586',
                 type = 'UV',
                 particles = [ P.H, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_303_528})

V_587 = CTVertex(name = 'V_587',
                 type = 'UV',
                 particles = [ P.G0, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_302_527})

V_588 = CTVertex(name = 'V_588',
                 type = 'UV',
                 particles = [ P.H, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_305_530})

V_589 = CTVertex(name = 'V_589',
                 type = 'UV',
                 particles = [ P.G__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_450_929})

V_590 = CTVertex(name = 'V_590',
                 type = 'UV',
                 particles = [ P.G__plus__, P.sbL, P.stR__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_447_926})

V_591 = CTVertex(name = 'V_591',
                 type = 'UV',
                 particles = [ P.G__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_449_928})

V_592 = CTVertex(name = 'V_592',
                 type = 'UV',
                 particles = [ P.G__minus__, P.sbL__tilde__, P.stR ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_448_927})

V_593 = CTVertex(name = 'V_593',
                 type = 'UV',
                 particles = [ P.a, P.a, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_134_208})

V_594 = CTVertex(name = 'V_594',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_353_680})

V_595 = CTVertex(name = 'V_595',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_138_212})

V_596 = CTVertex(name = 'V_596',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_142_216})

V_597 = CTVertex(name = 'V_597',
                 type = 'UV',
                 particles = [ P.a, P.g, P.suL__tilde__, P.suL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_135_209})

V_598 = CTVertex(name = 'V_598',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.suL__tilde__, P.suL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_140_214})

V_599 = CTVertex(name = 'V_599',
                 type = 'UV',
                 particles = [ P.a, P.a, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_134_208})

V_600 = CTVertex(name = 'V_600',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_353_680})

V_601 = CTVertex(name = 'V_601',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_138_212})

V_602 = CTVertex(name = 'V_602',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_142_216})

V_603 = CTVertex(name = 'V_603',
                 type = 'UV',
                 particles = [ P.a, P.g, P.scL__tilde__, P.scL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_135_209})

V_604 = CTVertex(name = 'V_604',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.scL__tilde__, P.scL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_140_214})

V_605 = CTVertex(name = 'V_605',
                 type = 'UV',
                 particles = [ P.a, P.a, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_134_208})

V_606 = CTVertex(name = 'V_606',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_353_680})

V_607 = CTVertex(name = 'V_607',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_138_212})

V_608 = CTVertex(name = 'V_608',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_142_216})

V_609 = CTVertex(name = 'V_609',
                 type = 'UV',
                 particles = [ P.a, P.g, P.stL__tilde__, P.stL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_135_209})

V_610 = CTVertex(name = 'V_610',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.stL__tilde__, P.stL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_140_214})

V_611 = CTVertex(name = 'V_611',
                 type = 'UV',
                 particles = [ P.a, P.a, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_134_208})

V_612 = CTVertex(name = 'V_612',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_139_213})

V_613 = CTVertex(name = 'V_613',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_143_217})

V_614 = CTVertex(name = 'V_614',
                 type = 'UV',
                 particles = [ P.a, P.g, P.suR__tilde__, P.suR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_135_209})

V_615 = CTVertex(name = 'V_615',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.suR__tilde__, P.suR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_141_215})

V_616 = CTVertex(name = 'V_616',
                 type = 'UV',
                 particles = [ P.a, P.a, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_134_208})

V_617 = CTVertex(name = 'V_617',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_139_213})

V_618 = CTVertex(name = 'V_618',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_143_217})

V_619 = CTVertex(name = 'V_619',
                 type = 'UV',
                 particles = [ P.a, P.g, P.scR__tilde__, P.scR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_135_209})

V_620 = CTVertex(name = 'V_620',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.scR__tilde__, P.scR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_141_215})

V_621 = CTVertex(name = 'V_621',
                 type = 'UV',
                 particles = [ P.a, P.a, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_134_208})

V_622 = CTVertex(name = 'V_622',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_139_213})

V_623 = CTVertex(name = 'V_623',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_143_217})

V_624 = CTVertex(name = 'V_624',
                 type = 'UV',
                 particles = [ P.a, P.g, P.stR__tilde__, P.stR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_135_209})

V_625 = CTVertex(name = 'V_625',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.stR__tilde__, P.stR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_141_215})

V_626 = CTVertex(name = 'V_626',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.sdL, P.suL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_356_683})

V_627 = CTVertex(name = 'V_627',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.sdL, P.suL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_352_679})

V_628 = CTVertex(name = 'V_628',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.sdL, P.suL__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_357_684})

V_629 = CTVertex(name = 'V_629',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.sdL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_356_683})

V_630 = CTVertex(name = 'V_630',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.sdL__tilde__, P.suL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_352_679})

V_631 = CTVertex(name = 'V_631',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.sdL__tilde__, P.suL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_357_684})

V_632 = CTVertex(name = 'V_632',
                 type = 'UV',
                 particles = [ P.a, P.a, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_120_197})

V_633 = CTVertex(name = 'V_633',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_353_680})

V_634 = CTVertex(name = 'V_634',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_124_201})

V_635 = CTVertex(name = 'V_635',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_128_205})

V_636 = CTVertex(name = 'V_636',
                 type = 'UV',
                 particles = [ P.a, P.g, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_121_198})

V_637 = CTVertex(name = 'V_637',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_126_203})

V_638 = CTVertex(name = 'V_638',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.scL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_356_683})

V_639 = CTVertex(name = 'V_639',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.scL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_352_679})

V_640 = CTVertex(name = 'V_640',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.scL__tilde__, P.ssL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_357_684})

V_641 = CTVertex(name = 'V_641',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.scL, P.ssL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_356_683})

V_642 = CTVertex(name = 'V_642',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.scL, P.ssL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_352_679})

V_643 = CTVertex(name = 'V_643',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.scL, P.ssL__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_357_684})

V_644 = CTVertex(name = 'V_644',
                 type = 'UV',
                 particles = [ P.a, P.a, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_120_197})

V_645 = CTVertex(name = 'V_645',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.c, P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_353_680})

V_646 = CTVertex(name = 'V_646',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_124_201})

V_647 = CTVertex(name = 'V_647',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_128_205})

V_648 = CTVertex(name = 'V_648',
                 type = 'UV',
                 particles = [ P.a, P.g, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_121_198})

V_649 = CTVertex(name = 'V_649',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_126_203})

V_650 = CTVertex(name = 'V_650',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_356_683})

V_651 = CTVertex(name = 'V_651',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_352_679})

V_652 = CTVertex(name = 'V_652',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_357_684})

V_653 = CTVertex(name = 'V_653',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_356_683})

V_654 = CTVertex(name = 'V_654',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_352_679})

V_655 = CTVertex(name = 'V_655',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_357_684})

V_656 = CTVertex(name = 'V_656',
                 type = 'UV',
                 particles = [ P.a, P.a, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_120_197})

V_657 = CTVertex(name = 'V_657',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_353_680})

V_658 = CTVertex(name = 'V_658',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_124_201})

V_659 = CTVertex(name = 'V_659',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_128_205})

V_660 = CTVertex(name = 'V_660',
                 type = 'UV',
                 particles = [ P.a, P.g, P.sbL__tilde__, P.sbL ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_121_198})

V_661 = CTVertex(name = 'V_661',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.sbL__tilde__, P.sbL ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_126_203})

V_662 = CTVertex(name = 'V_662',
                 type = 'UV',
                 particles = [ P.a, P.a, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_120_197})

V_663 = CTVertex(name = 'V_663',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_125_202})

V_664 = CTVertex(name = 'V_664',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_129_206})

V_665 = CTVertex(name = 'V_665',
                 type = 'UV',
                 particles = [ P.a, P.g, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_121_198})

V_666 = CTVertex(name = 'V_666',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.d, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_127_204})

V_667 = CTVertex(name = 'V_667',
                 type = 'UV',
                 particles = [ P.a, P.a, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_120_197})

V_668 = CTVertex(name = 'V_668',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_125_202})

V_669 = CTVertex(name = 'V_669',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_129_206})

V_670 = CTVertex(name = 'V_670',
                 type = 'UV',
                 particles = [ P.a, P.g, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_121_198})

V_671 = CTVertex(name = 'V_671',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_127_204})

V_672 = CTVertex(name = 'V_672',
                 type = 'UV',
                 particles = [ P.a, P.a, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_120_197})

V_673 = CTVertex(name = 'V_673',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_125_202})

V_674 = CTVertex(name = 'V_674',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_129_206})

V_675 = CTVertex(name = 'V_675',
                 type = 'UV',
                 particles = [ P.a, P.g, P.sbR__tilde__, P.sbR ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_121_198})

V_676 = CTVertex(name = 'V_676',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.sbR__tilde__, P.sbR ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.go] ] ],
                 couplings = {(0,0,0):C.UVGC_127_204})

V_677 = CTVertex(name = 'V_677',
                 type = 'UV',
                 particles = [ P.H, P.H, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_306_531})

V_678 = CTVertex(name = 'V_678',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.stL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_306_531})

V_679 = CTVertex(name = 'V_679',
                 type = 'UV',
                 particles = [ P.H, P.H, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_306_531})

V_680 = CTVertex(name = 'V_680',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_306_531})

V_681 = CTVertex(name = 'V_681',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_306_531})

V_682 = CTVertex(name = 'V_682',
                 type = 'UV',
                 particles = [ P.G__plus__, P.H, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_454_932})

V_683 = CTVertex(name = 'V_683',
                 type = 'UV',
                 particles = [ P.G0, P.G__plus__, P.sbL, P.stL__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_453_931})

V_684 = CTVertex(name = 'V_684',
                 type = 'UV',
                 particles = [ P.G__minus__, P.H, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_452_930})

V_685 = CTVertex(name = 'V_685',
                 type = 'UV',
                 particles = [ P.G0, P.G__minus__, P.sbL__tilde__, P.stL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_453_931})

V_686 = CTVertex(name = 'V_686',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.sbL__tilde__, P.sbL ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b, P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_306_531})

V_687 = CTVertex(name = 'V_687',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_291_520,(0,1,0):C.UVGC_270_492})

V_688 = CTVertex(name = 'V_688',
                 type = 'UV',
                 particles = [ P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS3 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_291_520,(0,1,0):C.UVGC_270_492})

V_689 = CTVertex(name = 'V_689',
                 type = 'UV',
                 particles = [ P.g, P.stL__tilde__, P.stR ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_271_493})

V_690 = CTVertex(name = 'V_690',
                 type = 'UV',
                 particles = [ P.g, P.stL, P.stR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_272_494})

V_691 = CTVertex(name = 'V_691',
                 type = 'UV',
                 particles = [ P.g, P.g, P.stL__tilde__, P.stR ],
                 color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_279_501,(0,0,0):C.UVGC_279_501})

V_692 = CTVertex(name = 'V_692',
                 type = 'UV',
                 particles = [ P.g, P.g, P.stL, P.stR__tilde__ ],
                 color = [ 'T(1,-1,4)*T(2,3,-1)', 'T(1,3,-1)*T(2,-1,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_279_501,(0,0,0):C.UVGC_279_501})

V_693 = CTVertex(name = 'V_693',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stR, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_694 = CTVertex(name = 'V_694',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_695 = CTVertex(name = 'V_695',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stL__tilde__, P.stL, P.stR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_276_498,(0,0,0):C.UVGC_276_498})

V_696 = CTVertex(name = 'V_696',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stR, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_697 = CTVertex(name = 'V_697',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_698 = CTVertex(name = 'V_698',
                 type = 'UV',
                 particles = [ P.stL, P.stR__tilde__, P.suL__tilde__, P.suL ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_699 = CTVertex(name = 'V_699',
                 type = 'UV',
                 particles = [ P.scL__tilde__, P.scL, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_700 = CTVertex(name = 'V_700',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stL, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_276_498,(0,0,0):C.UVGC_276_498})

V_701 = CTVertex(name = 'V_701',
                 type = 'UV',
                 particles = [ P.stL, P.stR__tilde__, P.suR__tilde__, P.suR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_702 = CTVertex(name = 'V_702',
                 type = 'UV',
                 particles = [ P.scR__tilde__, P.scR, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_703 = CTVertex(name = 'V_703',
                 type = 'UV',
                 particles = [ P.stL__tilde__, P.stR__tilde__, P.stR, P.stR ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_275_497,(0,0,0):C.UVGC_275_497})

V_704 = CTVertex(name = 'V_704',
                 type = 'UV',
                 particles = [ P.stL, P.stR__tilde__, P.stR__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_275_497,(0,0,0):C.UVGC_275_497})

V_705 = CTVertex(name = 'V_705',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_706 = CTVertex(name = 'V_706',
                 type = 'UV',
                 particles = [ P.sdL__tilde__, P.sdL, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_707 = CTVertex(name = 'V_707',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_708 = CTVertex(name = 'V_708',
                 type = 'UV',
                 particles = [ P.ssL__tilde__, P.ssL, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_709 = CTVertex(name = 'V_709',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_710 = CTVertex(name = 'V_710',
                 type = 'UV',
                 particles = [ P.sbL__tilde__, P.sbL, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_278_500,(0,0,0):C.UVGC_273_495})

V_711 = CTVertex(name = 'V_711',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_712 = CTVertex(name = 'V_712',
                 type = 'UV',
                 particles = [ P.sdR__tilde__, P.sdR, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_713 = CTVertex(name = 'V_713',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_714 = CTVertex(name = 'V_714',
                 type = 'UV',
                 particles = [ P.ssR__tilde__, P.ssR, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_715 = CTVertex(name = 'V_715',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.stL__tilde__, P.stR ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_716 = CTVertex(name = 'V_716',
                 type = 'UV',
                 particles = [ P.sbR__tilde__, P.sbR, P.stL, P.stR__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.go, P.t] ] ],
                 couplings = {(1,0,0):C.UVGC_277_499,(0,0,0):C.UVGC_274_496})

V_717 = CTVertex(name = 'V_717',
                 type = 'UVloop',
                 particles = [ P.b__tilde__, P.go, P.sbL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_718 = CTVertex(name = 'V_718',
                 type = 'UVloop',
                 particles = [ P.go, P.b, P.sbR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_719 = CTVertex(name = 'V_719',
                 type = 'UVloop',
                 particles = [ P.c__tilde__, P.go, P.scL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_720 = CTVertex(name = 'V_720',
                 type = 'UVloop',
                 particles = [ P.go, P.c, P.scR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_721 = CTVertex(name = 'V_721',
                 type = 'UVloop',
                 particles = [ P.d__tilde__, P.go, P.sdL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_722 = CTVertex(name = 'V_722',
                 type = 'UVloop',
                 particles = [ P.go, P.d, P.sdR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_723 = CTVertex(name = 'V_723',
                 type = 'UVloop',
                 particles = [ P.s__tilde__, P.go, P.ssL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_724 = CTVertex(name = 'V_724',
                 type = 'UVloop',
                 particles = [ P.go, P.s, P.ssR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_725 = CTVertex(name = 'V_725',
                 type = 'UVloop',
                 particles = [ P.t__tilde__, P.go, P.stL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_726 = CTVertex(name = 'V_726',
                 type = 'UVloop',
                 particles = [ P.go, P.t, P.stR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_727 = CTVertex(name = 'V_727',
                 type = 'UVloop',
                 particles = [ P.u__tilde__, P.go, P.suL ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_728 = CTVertex(name = 'V_728',
                 type = 'UVloop',
                 particles = [ P.go, P.u, P.suR__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_729 = CTVertex(name = 'V_729',
                 type = 'UVloop',
                 particles = [ P.go, P.b, P.sbL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_730 = CTVertex(name = 'V_730',
                 type = 'UVloop',
                 particles = [ P.b__tilde__, P.go, P.sbR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_731 = CTVertex(name = 'V_731',
                 type = 'UVloop',
                 particles = [ P.go, P.c, P.scL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_732 = CTVertex(name = 'V_732',
                 type = 'UVloop',
                 particles = [ P.c__tilde__, P.go, P.scR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_733 = CTVertex(name = 'V_733',
                 type = 'UVloop',
                 particles = [ P.go, P.d, P.sdL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_734 = CTVertex(name = 'V_734',
                 type = 'UVloop',
                 particles = [ P.d__tilde__, P.go, P.sdR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_735 = CTVertex(name = 'V_735',
                 type = 'UVloop',
                 particles = [ P.go, P.s, P.ssL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_736 = CTVertex(name = 'V_736',
                 type = 'UVloop',
                 particles = [ P.s__tilde__, P.go, P.ssR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_737 = CTVertex(name = 'V_737',
                 type = 'UVloop',
                 particles = [ P.go, P.t, P.stL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_738 = CTVertex(name = 'V_738',
                 type = 'UVloop',
                 particles = [ P.t__tilde__, P.go, P.stR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_739 = CTVertex(name = 'V_739',
                 type = 'UVloop',
                 particles = [ P.go, P.u, P.suL__tilde__ ],
                 color = [ 'T(1,2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_525_4})

V_740 = CTVertex(name = 'V_740',
                 type = 'UVloop',
                 particles = [ P.u__tilde__, P.go, P.suR ],
                 color = [ 'T(2,3,1)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_531_5})

V_741 = CTVertex(name = 'V_741',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL__tilde__, P.sbL, P.sbL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_742 = CTVertex(name = 'V_742',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.sbR__tilde__, P.sbR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(0,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_522_1})

V_743 = CTVertex(name = 'V_743',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR__tilde__, P.sbR, P.sbR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_744 = CTVertex(name = 'V_744',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.scL__tilde__, P.scL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_745 = CTVertex(name = 'V_745',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.scL__tilde__, P.scL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_746 = CTVertex(name = 'V_746',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL__tilde__, P.scL, P.scL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_747 = CTVertex(name = 'V_747',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.scR__tilde__, P.scR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_748 = CTVertex(name = 'V_748',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.scR__tilde__, P.scR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_749 = CTVertex(name = 'V_749',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.scR__tilde__, P.scR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_750 = CTVertex(name = 'V_750',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR__tilde__, P.scR, P.scR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_751 = CTVertex(name = 'V_751',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_752 = CTVertex(name = 'V_752',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_523_2})

V_753 = CTVertex(name = 'V_753',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_754 = CTVertex(name = 'V_754',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.sdL__tilde__, P.sdL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_755 = CTVertex(name = 'V_755',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL__tilde__, P.sdL, P.sdL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_756 = CTVertex(name = 'V_756',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(0,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_522_1})

V_757 = CTVertex(name = 'V_757',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_758 = CTVertex(name = 'V_758',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_759 = CTVertex(name = 'V_759',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_760 = CTVertex(name = 'V_760',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL, P.sdR__tilde__, P.sdR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(0,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_522_1})

V_761 = CTVertex(name = 'V_761',
                 type = 'UVloop',
                 particles = [ P.sdR__tilde__, P.sdR__tilde__, P.sdR, P.sdR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_762 = CTVertex(name = 'V_762',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_763 = CTVertex(name = 'V_763',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_523_2})

V_764 = CTVertex(name = 'V_764',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_765 = CTVertex(name = 'V_765',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_766 = CTVertex(name = 'V_766',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_767 = CTVertex(name = 'V_767',
                 type = 'UVloop',
                 particles = [ P.sdR__tilde__, P.sdR, P.ssL__tilde__, P.ssL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_523_2})

V_768 = CTVertex(name = 'V_768',
                 type = 'UVloop',
                 particles = [ P.ssL__tilde__, P.ssL__tilde__, P.ssL, P.ssL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_769 = CTVertex(name = 'V_769',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(0,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_522_1})

V_770 = CTVertex(name = 'V_770',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_771 = CTVertex(name = 'V_771',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_772 = CTVertex(name = 'V_772',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_773 = CTVertex(name = 'V_773',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(0,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_522_1})

V_774 = CTVertex(name = 'V_774',
                 type = 'UVloop',
                 particles = [ P.sdR__tilde__, P.sdR, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_775 = CTVertex(name = 'V_775',
                 type = 'UVloop',
                 particles = [ P.ssL__tilde__, P.ssL, P.ssR__tilde__, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_523_2,(0,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_522_1})

V_776 = CTVertex(name = 'V_776',
                 type = 'UVloop',
                 particles = [ P.ssR__tilde__, P.ssR__tilde__, P.ssR, P.ssR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_777 = CTVertex(name = 'V_777',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_778 = CTVertex(name = 'V_778',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_779 = CTVertex(name = 'V_779',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_780 = CTVertex(name = 'V_780',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_781 = CTVertex(name = 'V_781',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_782 = CTVertex(name = 'V_782',
                 type = 'UVloop',
                 particles = [ P.sdR__tilde__, P.sdR, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_783 = CTVertex(name = 'V_783',
                 type = 'UVloop',
                 particles = [ P.ssL__tilde__, P.ssL, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_784 = CTVertex(name = 'V_784',
                 type = 'UVloop',
                 particles = [ P.ssR__tilde__, P.ssR, P.stL__tilde__, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_785 = CTVertex(name = 'V_785',
                 type = 'UVloop',
                 particles = [ P.stL__tilde__, P.stL__tilde__, P.stL, P.stL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_786 = CTVertex(name = 'V_786',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_787 = CTVertex(name = 'V_787',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_788 = CTVertex(name = 'V_788',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_789 = CTVertex(name = 'V_789',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_790 = CTVertex(name = 'V_790',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_791 = CTVertex(name = 'V_791',
                 type = 'UVloop',
                 particles = [ P.sdR__tilde__, P.sdR, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_792 = CTVertex(name = 'V_792',
                 type = 'UVloop',
                 particles = [ P.ssL__tilde__, P.ssL, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_793 = CTVertex(name = 'V_793',
                 type = 'UVloop',
                 particles = [ P.ssR__tilde__, P.ssR, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_794 = CTVertex(name = 'V_794',
                 type = 'UVloop',
                 particles = [ P.stL__tilde__, P.stL, P.stR__tilde__, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_795 = CTVertex(name = 'V_795',
                 type = 'UVloop',
                 particles = [ P.stR__tilde__, P.stR__tilde__, P.stR, P.stR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_796 = CTVertex(name = 'V_796',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_797 = CTVertex(name = 'V_797',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_798 = CTVertex(name = 'V_798',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_799 = CTVertex(name = 'V_799',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_800 = CTVertex(name = 'V_800',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_801 = CTVertex(name = 'V_801',
                 type = 'UVloop',
                 particles = [ P.sdR__tilde__, P.sdR, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_802 = CTVertex(name = 'V_802',
                 type = 'UVloop',
                 particles = [ P.ssL__tilde__, P.ssL, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_803 = CTVertex(name = 'V_803',
                 type = 'UVloop',
                 particles = [ P.ssR__tilde__, P.ssR, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_804 = CTVertex(name = 'V_804',
                 type = 'UVloop',
                 particles = [ P.stL__tilde__, P.stL, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_805 = CTVertex(name = 'V_805',
                 type = 'UVloop',
                 particles = [ P.stR__tilde__, P.stR, P.suL__tilde__, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_524_3,(1,0,0):C.UVloopGC_522_1,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_806 = CTVertex(name = 'V_806',
                 type = 'UVloop',
                 particles = [ P.suL__tilde__, P.suL__tilde__, P.suL, P.suL ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

V_807 = CTVertex(name = 'V_807',
                 type = 'UVloop',
                 particles = [ P.sbL__tilde__, P.sbL, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_808 = CTVertex(name = 'V_808',
                 type = 'UVloop',
                 particles = [ P.sbR__tilde__, P.sbR, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_809 = CTVertex(name = 'V_809',
                 type = 'UVloop',
                 particles = [ P.scL__tilde__, P.scL, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_810 = CTVertex(name = 'V_810',
                 type = 'UVloop',
                 particles = [ P.scR__tilde__, P.scR, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_811 = CTVertex(name = 'V_811',
                 type = 'UVloop',
                 particles = [ P.sdL__tilde__, P.sdL, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_812 = CTVertex(name = 'V_812',
                 type = 'UVloop',
                 particles = [ P.sdR__tilde__, P.sdR, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_813 = CTVertex(name = 'V_813',
                 type = 'UVloop',
                 particles = [ P.ssL__tilde__, P.ssL, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_814 = CTVertex(name = 'V_814',
                 type = 'UVloop',
                 particles = [ P.ssR__tilde__, P.ssR, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_815 = CTVertex(name = 'V_815',
                 type = 'UVloop',
                 particles = [ P.stL__tilde__, P.stL, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_816 = CTVertex(name = 'V_816',
                 type = 'UVloop',
                 particles = [ P.stR__tilde__, P.stR, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,3)*T(-3,2,-2)*T(-3,4,-1)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_522_1,(4,0,0):C.UVloopGC_522_1,(5,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_522_1,(2,0,0):C.UVloopGC_522_1})

V_817 = CTVertex(name = 'V_817',
                 type = 'UVloop',
                 particles = [ P.suL__tilde__, P.suL, P.suR__tilde__, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,3)*T(-3,2,-2)', 'T(-4,2,-1)*T(-4,4,-2)*T(-3,-2,3)*T(-3,-1,1)', 'T(-4,2,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,3)', 'T(-4,-2,3)*T(-4,-1,1)*T(-3,2,-1)*T(-3,4,-2)', 'T(-4,-2,3)*T(-4,2,-1)*T(-3,-1,1)*T(-3,4,-2)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(3,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_522_1,(0,0,0):C.UVloopGC_524_3,(2,0,0):C.UVloopGC_522_1,(1,0,0):C.UVloopGC_522_1})

V_818 = CTVertex(name = 'V_818',
                 type = 'UVloop',
                 particles = [ P.suR__tilde__, P.suR__tilde__, P.suR, P.suR ],
                 color = [ 'T(-4,-2,1)*T(-4,-1,2)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,3,-1)*T(-3,-1,2)*T(-3,4,-2)', 'T(-4,-2,1)*T(-4,4,-1)*T(-3,-1,2)*T(-3,3,-2)', 'T(-4,-2,2)*T(-4,-1,1)*T(-3,3,-1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,3,-1)*T(-3,-1,1)*T(-3,4,-2)', 'T(-4,-2,2)*T(-4,4,-1)*T(-3,-1,1)*T(-3,3,-2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-1)*T(-4,4,-2)*T(-3,-2,2)*T(-3,-1,1)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,1)*T(-3,-1,2)', 'T(-4,3,-2)*T(-4,4,-1)*T(-3,-2,2)*T(-3,-1,1)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [],
                 couplings = {(0,0,0):C.UVloopGC_523_2,(3,0,0):C.UVloopGC_523_2,(1,0,0):C.UVloopGC_523_2,(4,0,0):C.UVloopGC_523_2,(2,0,0):C.UVloopGC_523_2,(5,0,0):C.UVloopGC_523_2,(8,0,0):C.UVloopGC_522_1,(9,0,0):C.UVloopGC_522_1,(6,0,0):C.UVloopGC_522_1,(7,0,0):C.UVloopGC_522_1})

