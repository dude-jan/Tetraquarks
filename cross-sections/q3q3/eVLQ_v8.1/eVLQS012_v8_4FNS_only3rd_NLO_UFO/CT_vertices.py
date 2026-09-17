# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Thu 28 Jul 2022 08:33:21


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_256_127})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_262_130,(0,1,0):C.R2GC_263_131})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_288_151})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_292_152,(0,1,0):C.R2GC_295_155})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.x__tilde__, P.x, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.x] ] ],
               couplings = {(0,0,0):C.R2GC_314_171,(0,1,0):C.R2GC_315_172})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.y__tilde__, P.y, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.y] ] ],
               couplings = {(0,0,0):C.R2GC_342_197,(0,1,0):C.R2GC_343_198})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_332_188,(0,0,1):C.R2GC_332_189})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_215_105,(2,1,1):C.R2GC_215_106,(0,1,0):C.R2GC_215_105,(0,1,1):C.R2GC_215_106,(4,1,0):C.R2GC_213_101,(4,1,1):C.R2GC_213_102,(3,1,0):C.R2GC_213_101,(3,1,1):C.R2GC_213_102,(8,1,0):C.R2GC_214_103,(8,1,1):C.R2GC_214_104,(6,1,0):C.R2GC_218_110,(6,1,1):C.R2GC_338_196,(7,1,0):C.R2GC_219_112,(7,1,1):C.R2GC_337_195,(5,1,0):C.R2GC_213_101,(5,1,1):C.R2GC_213_102,(1,1,0):C.R2GC_213_101,(1,1,1):C.R2GC_213_102,(11,0,0):C.R2GC_217_108,(11,0,1):C.R2GC_217_109,(10,0,0):C.R2GC_217_108,(10,0,1):C.R2GC_217_109,(9,0,1):C.R2GC_216_107,(0,2,0):C.R2GC_215_105,(0,2,1):C.R2GC_215_106,(2,2,0):C.R2GC_215_105,(2,2,1):C.R2GC_215_106,(5,2,0):C.R2GC_213_101,(5,2,1):C.R2GC_213_102,(1,2,0):C.R2GC_213_101,(1,2,1):C.R2GC_213_102,(7,2,0):C.R2GC_219_112,(7,2,1):C.R2GC_219_113,(4,2,0):C.R2GC_213_101,(4,2,1):C.R2GC_213_102,(3,2,0):C.R2GC_213_101,(3,2,1):C.R2GC_213_102,(8,2,0):C.R2GC_214_103,(8,2,1):C.R2GC_336_194,(6,2,0):C.R2GC_334_191,(6,2,1):C.R2GC_334_192,(0,3,0):C.R2GC_215_105,(0,3,1):C.R2GC_215_106,(2,3,0):C.R2GC_215_105,(2,3,1):C.R2GC_215_106,(5,3,0):C.R2GC_213_101,(5,3,1):C.R2GC_213_102,(1,3,0):C.R2GC_213_101,(1,3,1):C.R2GC_213_102,(7,3,0):C.R2GC_335_193,(7,3,1):C.R2GC_215_106,(4,3,0):C.R2GC_213_101,(4,3,1):C.R2GC_213_102,(3,3,0):C.R2GC_213_101,(3,3,1):C.R2GC_213_102,(8,3,0):C.R2GC_214_103,(8,3,1):C.R2GC_333_190,(6,3,0):C.R2GC_218_110,(6,3,1):C.R2GC_218_111})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_220_114})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_173_3})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_238_116})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_240_117})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_250_123,(0,1,0):C.R2GC_249_122})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_275_140,(0,1,0):C.R2GC_274_139})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_261_129,(0,1,0):C.R2GC_260_128})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_301_161,(0,1,0):C.R2GC_300_160})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_265_133,(0,1,0):C.R2GC_264_132})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_294_154,(0,1,0):C.R2GC_293_153})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_345_200,(0,1,0):C.R2GC_344_199})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_297_157,(0,1,0):C.R2GC_296_156})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_317_174,(0,1,0):C.R2GC_316_173})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_277_142,(0,1,0):C.R2GC_276_141})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_279_144,(0,1,0):C.R2GC_278_143})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_299_159,(0,1,0):C.R2GC_298_158})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_319_176,(0,1,0):C.R2GC_318_175})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_347_202,(0,1,0):C.R2GC_346_201})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_321_178,(0,1,0):C.R2GC_320_177})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_349_204,(0,1,0):C.R2GC_348_203})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_323_180,(0,1,0):C.R2GC_322_179})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_351_206,(0,1,0):C.R2GC_350_205})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_344_199,(0,1,0):C.R2GC_345_200})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_296_156,(0,1,0):C.R2GC_297_157})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_316_173,(0,1,0):C.R2GC_317_174})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_320_177,(0,1,0):C.R2GC_321_178})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_348_203,(0,1,0):C.R2GC_349_204})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_264_132,(0,1,0):C.R2GC_265_133})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_293_153,(0,1,0):C.R2GC_294_154})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_276_141,(0,1,0):C.R2GC_277_142})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_278_143,(0,1,0):C.R2GC_279_144})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_298_158,(0,1,0):C.R2GC_299_159})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_318_175,(0,1,0):C.R2GC_319_176})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_346_201,(0,1,0):C.R2GC_347_202})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_322_179,(0,1,0):C.R2GC_323_180})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_350_205,(0,1,0):C.R2GC_351_206})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_260_128,(0,1,0):C.R2GC_261_129})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_300_160,(0,1,0):C.R2GC_301_161})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_303_163,(0,1,0):C.R2GC_305_165})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_327_184,(0,1,0):C.R2GC_328_185})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_284_149,(0,1,0):C.R2GC_285_150})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_355_210,(0,1,0):C.R2GC_356_211})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_267_135,(0,1,0):C.R2GC_268_136})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_304_164,(0,1,0):C.R2GC_306_166})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_353_208,(0,1,0):C.R2GC_354_209})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_307_167,(0,1,0):C.R2GC_308_168})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_325_182,(0,1,0):C.R2GC_326_183})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_353_208,(0,1,0):C.R2GC_354_209})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_307_167,(0,1,0):C.R2GC_308_168})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_325_182,(0,1,0):C.R2GC_326_183})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_303_163,(0,1,0):C.R2GC_305_165})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_327_184,(0,1,0):C.R2GC_328_185})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_284_149,(0,1,0):C.R2GC_285_150})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_355_210,(0,1,0):C.R2GC_356_211})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_269_137,(0,1,0):C.R2GC_270_138})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_309_169,(0,1,0):C.R2GC_310_170})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_329_186,(0,1,0):C.R2GC_330_187})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_357_212,(0,1,0):C.R2GC_358_213})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_267_135,(0,1,0):C.R2GC_268_136})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_304_164,(0,1,0):C.R2GC_306_166})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_173_3})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_173_3})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_173_3})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_220_114})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_220_114})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_220_114})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_221_115})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_244_120})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_245_121})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_252_125})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_242_118})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_243_119})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_253_126})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_281_146})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_282_147})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_283_148})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_244_120})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_242_118})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_281_146})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_245_121})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_243_119})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_282_147})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_252_125})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_253_126})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_283_148})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_193_48,(0,1,0):C.R2GC_174_4})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_193_48,(0,1,0):C.R2GC_174_4})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_193_48,(0,1,0):C.R2GC_174_4})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_176_5,(0,1,0):C.R2GC_177_6})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_176_5,(0,1,0):C.R2GC_177_6})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_176_5,(0,1,0):C.R2GC_177_6})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_172_2})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_172_2})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_280_145,(0,1,0):C.R2GC_172_2})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_172_2})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_172_2})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_251_124,(0,1,0):C.R2GC_172_2})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_324_181,(0,1,0):C.R2GC_172_2})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_302_162,(0,1,0):C.R2GC_172_2})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_266_134,(0,1,0):C.R2GC_172_2})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_352_207,(0,1,0):C.R2GC_172_2})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV2, L.VV3, L.VV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,2,3):C.R2GC_171_1,(0,0,0):C.R2GC_189_24,(0,0,1):C.R2GC_189_25,(0,0,4):C.R2GC_189_26,(0,0,5):C.R2GC_189_27,(0,0,6):C.R2GC_189_28,(0,0,7):C.R2GC_189_29,(0,1,2):C.R2GC_185_9})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_184_7,(0,0,1):C.R2GC_184_8})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_188_18,(0,0,1):C.R2GC_188_19,(0,0,2):C.R2GC_188_20,(0,0,3):C.R2GC_188_21,(0,0,4):C.R2GC_188_22,(0,0,5):C.R2GC_188_23})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.u] ], [ [P.b, P.y] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ], [ [P.tp, P.x] ], [ [P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_201_85,(0,0,4):C.R2GC_201_86,(0,0,5):C.R2GC_201_87,(0,0,6):C.R2GC_201_88,(0,0,7):C.R2GC_201_89,(0,0,1):C.R2GC_201_90,(0,0,2):C.R2GC_201_91,(0,0,3):C.R2GC_201_92,(0,0,8):C.R2GC_201_93,(0,0,9):C.R2GC_201_94,(0,0,10):C.R2GC_201_95,(0,0,11):C.R2GC_201_96,(0,0,12):C.R2GC_201_97,(0,0,13):C.R2GC_201_98,(0,0,15):C.R2GC_201_99,(0,0,14):C.R2GC_201_100})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b, P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_197_65,(0,0,0):C.R2GC_197_66,(0,0,3):C.R2GC_197_67,(0,0,4):C.R2GC_197_68,(0,0,6):C.R2GC_197_69,(0,0,7):C.R2GC_197_70,(0,0,1):C.R2GC_197_71,(0,0,5):C.R2GC_197_72})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_190_30,(0,0,0):C.R2GC_190_31,(0,0,2):C.R2GC_190_32,(0,0,3):C.R2GC_190_33,(0,0,4):C.R2GC_190_34,(0,0,5):C.R2GC_190_35})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_186_10,(0,0,1):C.R2GC_186_11,(0,0,2):C.R2GC_186_12,(0,0,3):C.R2GC_186_13})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV10 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(1,0,1):C.R2GC_192_42,(1,0,0):C.R2GC_192_43,(1,0,2):C.R2GC_192_44,(1,0,3):C.R2GC_192_45,(1,0,4):C.R2GC_192_46,(1,0,5):C.R2GC_192_47,(0,1,1):C.R2GC_191_36,(0,1,0):C.R2GC_191_37,(0,1,2):C.R2GC_191_38,(0,1,3):C.R2GC_191_39,(0,1,4):C.R2GC_191_40,(0,1,5):C.R2GC_191_41})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_187_14,(0,0,1):C.R2GC_187_15,(0,0,2):C.R2GC_187_16,(0,0,3):C.R2GC_187_17})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.t] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_196_61,(0,0,2):C.R2GC_196_62,(0,0,1):C.R2GC_196_63,(0,0,3):C.R2GC_196_64})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.t] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_195_57,(0,0,2):C.R2GC_195_58,(0,0,1):C.R2GC_195_59,(0,0,3):C.R2GC_195_60})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_194_49,(0,0,1):C.R2GC_194_50,(0,0,3):C.R2GC_194_51,(0,0,4):C.R2GC_194_52,(0,0,6):C.R2GC_194_53,(0,0,7):C.R2GC_194_54,(0,0,2):C.R2GC_194_55,(0,0,5):C.R2GC_194_56})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus__, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ] ],
                 couplings = {(0,0,3):C.R2GC_200_77,(0,0,4):C.R2GC_200_78,(0,0,5):C.R2GC_200_79,(0,0,0):C.R2GC_200_80,(0,0,1):C.R2GC_200_81,(0,0,2):C.R2GC_200_82,(0,0,7):C.R2GC_200_83,(0,0,6):C.R2GC_200_84})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus____minus__, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.x] ], [ [P.b, P.x] ], [ [P.tp, P.y] ], [ [P.t, P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_199_73,(0,0,0):C.R2GC_199_74,(0,0,3):C.R2GC_199_75,(0,0,2):C.R2GC_199_76})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_256_56})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_262_66,(0,1,0):C.UVGC_263_67})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_288_118})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_292_122,(0,1,0):C.UVGC_295_129})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_314_172,(0,1,0):C.UVGC_315_173})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_342_268,(0,1,0):C.UVGC_343_269})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,0):C.UVGC_332_219,(0,1,1):C.UVGC_332_220,(0,1,2):C.UVGC_332_221,(0,1,5):C.UVGC_332_222,(0,1,6):C.UVGC_332_223,(0,1,7):C.UVGC_332_224,(0,1,8):C.UVGC_332_225,(0,2,3):C.UVGC_202_1,(0,0,4):C.UVGC_203_2})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(2,1,4):C.UVGC_214_11,(2,1,5):C.UVGC_214_10,(0,1,4):C.UVGC_214_11,(0,1,5):C.UVGC_214_10,(4,1,4):C.UVGC_213_8,(4,1,5):C.UVGC_213_9,(3,1,4):C.UVGC_213_8,(3,1,5):C.UVGC_213_9,(8,1,4):C.UVGC_214_10,(8,1,5):C.UVGC_214_11,(6,1,0):C.UVGC_337_254,(6,1,1):C.UVGC_337_255,(6,1,3):C.UVGC_337_256,(6,1,4):C.UVGC_338_263,(6,1,5):C.UVGC_338_264,(6,1,6):C.UVGC_337_259,(6,1,7):C.UVGC_337_260,(6,1,8):C.UVGC_337_261,(6,1,9):C.UVGC_337_262,(7,1,0):C.UVGC_337_254,(7,1,1):C.UVGC_337_255,(7,1,3):C.UVGC_337_256,(7,1,4):C.UVGC_337_257,(7,1,5):C.UVGC_337_258,(7,1,6):C.UVGC_337_259,(7,1,7):C.UVGC_337_260,(7,1,8):C.UVGC_337_261,(7,1,9):C.UVGC_337_262,(5,1,4):C.UVGC_213_8,(5,1,5):C.UVGC_213_9,(1,1,4):C.UVGC_213_8,(1,1,5):C.UVGC_213_9,(11,0,4):C.UVGC_217_14,(11,0,5):C.UVGC_217_15,(10,0,4):C.UVGC_217_14,(10,0,5):C.UVGC_217_15,(9,0,4):C.UVGC_216_12,(9,0,5):C.UVGC_216_13,(0,2,4):C.UVGC_214_11,(0,2,5):C.UVGC_214_10,(2,2,4):C.UVGC_214_11,(2,2,5):C.UVGC_214_10,(5,2,4):C.UVGC_213_8,(5,2,5):C.UVGC_213_9,(1,2,4):C.UVGC_213_8,(1,2,5):C.UVGC_213_9,(7,2,2):C.UVGC_218_16,(7,2,4):C.UVGC_219_18,(7,2,5):C.UVGC_219_19,(4,2,4):C.UVGC_213_8,(4,2,5):C.UVGC_213_9,(3,2,4):C.UVGC_213_8,(3,2,5):C.UVGC_213_9,(8,2,0):C.UVGC_336_245,(8,2,1):C.UVGC_336_246,(8,2,3):C.UVGC_336_247,(8,2,4):C.UVGC_336_248,(8,2,5):C.UVGC_336_249,(8,2,6):C.UVGC_336_250,(8,2,7):C.UVGC_336_251,(8,2,8):C.UVGC_336_252,(8,2,9):C.UVGC_336_253,(6,2,0):C.UVGC_334_235,(6,2,1):C.UVGC_334_236,(6,2,4):C.UVGC_334_237,(6,2,5):C.UVGC_334_238,(6,2,6):C.UVGC_334_239,(6,2,7):C.UVGC_334_240,(6,2,8):C.UVGC_334_241,(6,2,9):C.UVGC_334_242,(0,3,4):C.UVGC_214_11,(0,3,5):C.UVGC_214_10,(2,3,4):C.UVGC_214_11,(2,3,5):C.UVGC_214_10,(5,3,4):C.UVGC_213_8,(5,3,5):C.UVGC_213_9,(1,3,4):C.UVGC_213_8,(1,3,5):C.UVGC_213_9,(7,3,0):C.UVGC_334_235,(7,3,1):C.UVGC_334_236,(7,3,4):C.UVGC_335_243,(7,3,5):C.UVGC_335_244,(7,3,6):C.UVGC_334_239,(7,3,7):C.UVGC_334_240,(7,3,8):C.UVGC_334_241,(7,3,9):C.UVGC_334_242,(4,3,4):C.UVGC_213_8,(4,3,5):C.UVGC_213_9,(3,3,4):C.UVGC_213_8,(3,3,5):C.UVGC_213_9,(8,3,0):C.UVGC_333_226,(8,3,1):C.UVGC_333_227,(8,3,3):C.UVGC_333_228,(8,3,4):C.UVGC_333_229,(8,3,5):C.UVGC_333_230,(8,3,6):C.UVGC_333_231,(8,3,7):C.UVGC_333_232,(8,3,8):C.UVGC_333_233,(8,3,9):C.UVGC_333_234,(6,3,2):C.UVGC_218_16,(6,3,4):C.UVGC_218_17,(6,3,5):C.UVGC_216_12})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_220_20,(0,1,0):C.UVGC_258_58})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_205_4,(0,1,0):C.UVGC_290_120})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_238_32,(0,1,0):C.UVGC_312_170,(0,2,0):C.UVGC_312_170})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_240_33,(0,1,0):C.UVGC_340_266,(0,2,0):C.UVGC_340_266})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_250_46,(0,1,0):C.UVGC_249_45})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_275_87,(0,1,0):C.UVGC_274_86})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_261_63,(0,0,2):C.UVGC_261_64,(0,0,0):C.UVGC_261_65,(0,1,1):C.UVGC_260_60,(0,1,2):C.UVGC_260_61,(0,1,0):C.UVGC_260_62})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_301_145,(0,0,1):C.UVGC_301_146,(0,0,2):C.UVGC_301_147,(0,1,0):C.UVGC_300_142,(0,1,1):C.UVGC_300_143,(0,1,2):C.UVGC_300_144})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_265_71,(0,0,2):C.UVGC_265_72,(0,0,0):C.UVGC_265_73,(0,1,1):C.UVGC_264_68,(0,1,2):C.UVGC_264_69,(0,1,0):C.UVGC_264_70})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_294_126,(0,0,1):C.UVGC_294_127,(0,0,2):C.UVGC_294_128,(0,1,0):C.UVGC_293_123,(0,1,1):C.UVGC_293_124,(0,1,2):C.UVGC_293_125})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_345_273,(0,0,2):C.UVGC_345_274,(0,0,1):C.UVGC_345_275,(0,1,0):C.UVGC_344_270,(0,1,2):C.UVGC_344_271,(0,1,1):C.UVGC_344_272})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_297_133,(0,0,2):C.UVGC_297_134,(0,0,1):C.UVGC_297_135,(0,1,0):C.UVGC_296_130,(0,1,2):C.UVGC_296_131,(0,1,1):C.UVGC_296_132})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_317_177,(0,0,2):C.UVGC_317_178,(0,0,1):C.UVGC_317_179,(0,1,0):C.UVGC_316_174,(0,1,2):C.UVGC_316_175,(0,1,1):C.UVGC_316_176})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_277_91,(0,0,2):C.UVGC_277_92,(0,0,1):C.UVGC_277_93,(0,1,0):C.UVGC_276_88,(0,1,2):C.UVGC_276_89,(0,1,1):C.UVGC_276_90})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_279_97,(0,0,2):C.UVGC_279_98,(0,0,1):C.UVGC_279_99,(0,1,0):C.UVGC_278_94,(0,1,2):C.UVGC_278_95,(0,1,1):C.UVGC_278_96})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_299_139,(0,0,2):C.UVGC_299_140,(0,0,1):C.UVGC_299_141,(0,1,0):C.UVGC_298_136,(0,1,2):C.UVGC_298_137,(0,1,1):C.UVGC_298_138})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_319_183,(0,0,2):C.UVGC_319_184,(0,0,1):C.UVGC_319_185,(0,1,0):C.UVGC_318_180,(0,1,2):C.UVGC_318_181,(0,1,1):C.UVGC_318_182})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_347_279,(0,0,2):C.UVGC_347_280,(0,0,1):C.UVGC_347_281,(0,1,0):C.UVGC_346_276,(0,1,2):C.UVGC_346_277,(0,1,1):C.UVGC_346_278})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_321_189,(0,0,2):C.UVGC_321_190,(0,0,1):C.UVGC_321_191,(0,1,0):C.UVGC_320_186,(0,1,2):C.UVGC_320_187,(0,1,1):C.UVGC_320_188})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_349_285,(0,0,2):C.UVGC_349_286,(0,0,1):C.UVGC_349_287,(0,1,0):C.UVGC_348_282,(0,1,2):C.UVGC_348_283,(0,1,1):C.UVGC_348_284})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_323_195,(0,0,2):C.UVGC_323_196,(0,0,1):C.UVGC_323_197,(0,1,0):C.UVGC_322_192,(0,1,2):C.UVGC_322_193,(0,1,1):C.UVGC_322_194})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_351_291,(0,0,2):C.UVGC_351_292,(0,0,1):C.UVGC_351_293,(0,1,0):C.UVGC_350_288,(0,1,2):C.UVGC_350_289,(0,1,1):C.UVGC_350_290})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_344_270,(0,0,2):C.UVGC_344_271,(0,0,1):C.UVGC_344_272,(0,1,0):C.UVGC_345_273,(0,1,2):C.UVGC_345_274,(0,1,1):C.UVGC_345_275})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_296_130,(0,0,2):C.UVGC_296_131,(0,0,1):C.UVGC_296_132,(0,1,0):C.UVGC_297_133,(0,1,2):C.UVGC_297_134,(0,1,1):C.UVGC_297_135})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_316_174,(0,0,2):C.UVGC_316_175,(0,0,1):C.UVGC_316_176,(0,1,0):C.UVGC_317_177,(0,1,2):C.UVGC_317_178,(0,1,1):C.UVGC_317_179})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_320_186,(0,0,2):C.UVGC_320_187,(0,0,1):C.UVGC_320_188,(0,1,0):C.UVGC_321_189,(0,1,2):C.UVGC_321_190,(0,1,1):C.UVGC_321_191})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_348_282,(0,0,2):C.UVGC_348_283,(0,0,1):C.UVGC_348_284,(0,1,0):C.UVGC_349_285,(0,1,2):C.UVGC_349_286,(0,1,1):C.UVGC_349_287})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_264_68,(0,0,2):C.UVGC_264_69,(0,0,0):C.UVGC_264_70,(0,1,1):C.UVGC_265_71,(0,1,2):C.UVGC_265_72,(0,1,0):C.UVGC_265_73})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_293_123,(0,0,1):C.UVGC_293_124,(0,0,2):C.UVGC_293_125,(0,1,0):C.UVGC_294_126,(0,1,1):C.UVGC_294_127,(0,1,2):C.UVGC_294_128})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_276_88,(0,0,2):C.UVGC_276_89,(0,0,1):C.UVGC_276_90,(0,1,0):C.UVGC_277_91,(0,1,2):C.UVGC_277_92,(0,1,1):C.UVGC_277_93})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_278_94,(0,0,2):C.UVGC_278_95,(0,0,1):C.UVGC_278_96,(0,1,0):C.UVGC_279_97,(0,1,2):C.UVGC_279_98,(0,1,1):C.UVGC_279_99})

V_172 = CTVertex(name = 'V_172',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_298_136,(0,0,2):C.UVGC_298_137,(0,0,1):C.UVGC_298_138,(0,1,0):C.UVGC_299_139,(0,1,2):C.UVGC_299_140,(0,1,1):C.UVGC_299_141})

V_173 = CTVertex(name = 'V_173',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_318_180,(0,0,2):C.UVGC_318_181,(0,0,1):C.UVGC_318_182,(0,1,0):C.UVGC_319_183,(0,1,2):C.UVGC_319_184,(0,1,1):C.UVGC_319_185})

V_174 = CTVertex(name = 'V_174',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_346_276,(0,0,2):C.UVGC_346_277,(0,0,1):C.UVGC_346_278,(0,1,0):C.UVGC_347_279,(0,1,2):C.UVGC_347_280,(0,1,1):C.UVGC_347_281})

V_175 = CTVertex(name = 'V_175',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_322_192,(0,0,2):C.UVGC_322_193,(0,0,1):C.UVGC_322_194,(0,1,0):C.UVGC_323_195,(0,1,2):C.UVGC_323_196,(0,1,1):C.UVGC_323_197})

V_176 = CTVertex(name = 'V_176',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_350_288,(0,0,2):C.UVGC_350_289,(0,0,1):C.UVGC_350_290,(0,1,0):C.UVGC_351_291,(0,1,2):C.UVGC_351_292,(0,1,1):C.UVGC_351_293})

V_177 = CTVertex(name = 'V_177',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_260_60,(0,0,2):C.UVGC_260_61,(0,0,0):C.UVGC_260_62,(0,1,1):C.UVGC_261_63,(0,1,2):C.UVGC_261_64,(0,1,0):C.UVGC_261_65})

V_178 = CTVertex(name = 'V_178',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_300_142,(0,0,1):C.UVGC_300_143,(0,0,2):C.UVGC_300_144,(0,1,0):C.UVGC_301_145,(0,1,1):C.UVGC_301_146,(0,1,2):C.UVGC_301_147})

V_179 = CTVertex(name = 'V_179',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,3):C.UVGC_224_25,(0,1,4):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,5):C.UVGC_291_121})

V_180 = CTVertex(name = 'V_180',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.bp, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,3):C.UVGC_224_24,(0,1,4):C.UVGC_224_25,(0,1,5):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,2):C.UVGC_259_59})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.x] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,3):C.UVGC_224_25,(0,1,4):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,5):C.UVGC_313_171})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.y] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,3):C.UVGC_224_25,(0,1,4):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,5):C.UVGC_341_267})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_303_149,(0,0,2):C.UVGC_303_150,(0,0,1):C.UVGC_303_151,(0,1,0):C.UVGC_305_155,(0,1,2):C.UVGC_305_156,(0,1,1):C.UVGC_305_157})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_327_205,(0,0,2):C.UVGC_327_206,(0,0,1):C.UVGC_327_207,(0,1,0):C.UVGC_328_208,(0,1,2):C.UVGC_328_209,(0,1,1):C.UVGC_328_210})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_284_110,(0,0,2):C.UVGC_284_111,(0,0,1):C.UVGC_284_112,(0,1,0):C.UVGC_285_113,(0,1,2):C.UVGC_285_114,(0,1,1):C.UVGC_285_115})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_355_301,(0,0,2):C.UVGC_355_302,(0,0,1):C.UVGC_355_303,(0,1,0):C.UVGC_356_304,(0,1,2):C.UVGC_356_305,(0,1,1):C.UVGC_356_306})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_267_75,(0,0,2):C.UVGC_267_76,(0,0,0):C.UVGC_267_77,(0,1,1):C.UVGC_268_78,(0,1,2):C.UVGC_268_79,(0,1,0):C.UVGC_268_80})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_304_152,(0,0,1):C.UVGC_304_153,(0,0,2):C.UVGC_304_154,(0,1,0):C.UVGC_306_158,(0,1,1):C.UVGC_306_159,(0,1,2):C.UVGC_306_160})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_353_295,(0,0,2):C.UVGC_353_296,(0,0,1):C.UVGC_353_297,(0,1,0):C.UVGC_354_298,(0,1,2):C.UVGC_354_299,(0,1,1):C.UVGC_354_300})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_307_161,(0,0,2):C.UVGC_307_162,(0,0,1):C.UVGC_307_163,(0,1,0):C.UVGC_308_164,(0,1,2):C.UVGC_308_165,(0,1,1):C.UVGC_308_166})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_325_199,(0,0,2):C.UVGC_325_200,(0,0,1):C.UVGC_325_201,(0,1,0):C.UVGC_326_202,(0,1,2):C.UVGC_326_203,(0,1,1):C.UVGC_326_204})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_353_295,(0,0,2):C.UVGC_353_296,(0,0,1):C.UVGC_353_297,(0,1,0):C.UVGC_354_298,(0,1,2):C.UVGC_354_299,(0,1,1):C.UVGC_354_300})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_307_161,(0,0,2):C.UVGC_307_162,(0,0,1):C.UVGC_307_163,(0,1,0):C.UVGC_308_164,(0,1,2):C.UVGC_308_165,(0,1,1):C.UVGC_308_166})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_325_199,(0,0,2):C.UVGC_325_200,(0,0,1):C.UVGC_325_201,(0,1,0):C.UVGC_326_202,(0,1,2):C.UVGC_326_203,(0,1,1):C.UVGC_326_204})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_303_149,(0,0,2):C.UVGC_303_150,(0,0,1):C.UVGC_303_151,(0,1,0):C.UVGC_305_155,(0,1,2):C.UVGC_305_156,(0,1,1):C.UVGC_305_157})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_327_205,(0,0,2):C.UVGC_327_206,(0,0,1):C.UVGC_327_207,(0,1,0):C.UVGC_328_208,(0,1,2):C.UVGC_328_209,(0,1,1):C.UVGC_328_210})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_284_110,(0,0,2):C.UVGC_284_111,(0,0,1):C.UVGC_284_112,(0,1,0):C.UVGC_285_113,(0,1,2):C.UVGC_285_114,(0,1,1):C.UVGC_285_115})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_355_301,(0,0,2):C.UVGC_355_302,(0,0,1):C.UVGC_355_303,(0,1,0):C.UVGC_356_304,(0,1,2):C.UVGC_356_305,(0,1,1):C.UVGC_356_306})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_269_81,(0,1,0):C.UVGC_270_82})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_309_167,(0,1,0):C.UVGC_310_168})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_329_211,(0,1,0):C.UVGC_330_212})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_357_307,(0,1,0):C.UVGC_358_308})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_267_75,(0,0,2):C.UVGC_267_76,(0,0,0):C.UVGC_267_77,(0,1,1):C.UVGC_268_78,(0,1,2):C.UVGC_268_79,(0,1,0):C.UVGC_268_80})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_304_152,(0,0,1):C.UVGC_304_153,(0,0,2):C.UVGC_304_154,(0,1,0):C.UVGC_306_158,(0,1,1):C.UVGC_306_159,(0,1,2):C.UVGC_306_160})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_205_4})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_205_4})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_205_4,(0,1,0):C.UVGC_272_84,(0,2,0):C.UVGC_272_84})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_220_20,(0,1,0):C.UVGC_207_5,(0,2,0):C.UVGC_207_5})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_220_20,(0,1,0):C.UVGC_207_5,(0,2,0):C.UVGC_207_5})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_220_20,(0,1,0):C.UVGC_247_43,(0,2,0):C.UVGC_247_43})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,3):C.UVGC_224_25,(0,1,4):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,5):C.UVGC_224_31,(0,2,0):C.UVGC_224_22,(0,2,1):C.UVGC_224_23,(0,2,2):C.UVGC_224_24,(0,2,3):C.UVGC_224_25,(0,2,4):C.UVGC_224_26,(0,2,6):C.UVGC_224_27,(0,2,7):C.UVGC_224_28,(0,2,8):C.UVGC_224_29,(0,2,9):C.UVGC_224_30,(0,2,5):C.UVGC_224_31})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,4):C.UVGC_224_25,(0,1,5):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,3):C.UVGC_224_31,(0,2,0):C.UVGC_224_22,(0,2,1):C.UVGC_224_23,(0,2,2):C.UVGC_224_24,(0,2,4):C.UVGC_224_25,(0,2,5):C.UVGC_224_26,(0,2,6):C.UVGC_224_27,(0,2,7):C.UVGC_224_28,(0,2,8):C.UVGC_224_29,(0,2,9):C.UVGC_224_30,(0,2,3):C.UVGC_224_31})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,3):C.UVGC_224_25,(0,1,4):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,5):C.UVGC_273_85,(0,2,0):C.UVGC_224_22,(0,2,1):C.UVGC_224_23,(0,2,2):C.UVGC_224_24,(0,2,3):C.UVGC_224_25,(0,2,4):C.UVGC_224_26,(0,2,6):C.UVGC_224_27,(0,2,7):C.UVGC_224_28,(0,2,8):C.UVGC_224_29,(0,2,9):C.UVGC_224_30,(0,2,5):C.UVGC_273_85})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,4):C.UVGC_224_25,(0,1,5):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,3):C.UVGC_224_31,(0,2,0):C.UVGC_224_22,(0,2,1):C.UVGC_224_23,(0,2,2):C.UVGC_224_24,(0,2,4):C.UVGC_224_25,(0,2,5):C.UVGC_224_26,(0,2,6):C.UVGC_224_27,(0,2,7):C.UVGC_224_28,(0,2,8):C.UVGC_224_29,(0,2,9):C.UVGC_224_30,(0,2,3):C.UVGC_224_31})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,2):C.UVGC_224_24,(0,1,3):C.UVGC_224_25,(0,1,4):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,5):C.UVGC_224_31,(0,2,0):C.UVGC_224_22,(0,2,1):C.UVGC_224_23,(0,2,2):C.UVGC_224_24,(0,2,3):C.UVGC_224_25,(0,2,4):C.UVGC_224_26,(0,2,6):C.UVGC_224_27,(0,2,7):C.UVGC_224_28,(0,2,8):C.UVGC_224_29,(0,2,9):C.UVGC_224_30,(0,2,5):C.UVGC_224_31})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_221_21,(0,1,0):C.UVGC_224_22,(0,1,1):C.UVGC_224_23,(0,1,3):C.UVGC_224_24,(0,1,4):C.UVGC_224_25,(0,1,5):C.UVGC_224_26,(0,1,6):C.UVGC_224_27,(0,1,7):C.UVGC_224_28,(0,1,8):C.UVGC_224_29,(0,1,9):C.UVGC_224_30,(0,1,2):C.UVGC_248_44,(0,2,0):C.UVGC_224_22,(0,2,1):C.UVGC_224_23,(0,2,3):C.UVGC_224_24,(0,2,4):C.UVGC_224_25,(0,2,5):C.UVGC_224_26,(0,2,6):C.UVGC_224_27,(0,2,7):C.UVGC_224_28,(0,2,8):C.UVGC_224_29,(0,2,9):C.UVGC_224_30,(0,2,2):C.UVGC_248_44})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_244_38,(0,0,1):C.UVGC_244_39})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_245_40,(0,0,1):C.UVGC_245_41})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_252_48,(0,0,2):C.UVGC_252_49,(0,0,1):C.UVGC_252_50})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_242_34,(0,0,0):C.UVGC_242_35})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_243_36,(0,0,1):C.UVGC_243_37})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_253_51,(0,0,2):C.UVGC_253_52,(0,0,0):C.UVGC_253_53})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_281_101,(0,0,2):C.UVGC_281_102,(0,0,1):C.UVGC_281_103})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_282_104,(0,0,2):C.UVGC_282_105,(0,0,1):C.UVGC_282_106})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_283_107,(0,0,2):C.UVGC_283_108,(0,0,1):C.UVGC_283_109})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_244_38,(0,0,1):C.UVGC_244_39})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_242_34,(0,0,0):C.UVGC_242_35})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_281_101,(0,0,2):C.UVGC_281_102,(0,0,1):C.UVGC_281_103})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_245_40,(0,0,1):C.UVGC_245_41})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_243_36,(0,0,1):C.UVGC_243_37})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_282_104,(0,0,2):C.UVGC_282_105,(0,0,1):C.UVGC_282_106})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_252_48,(0,0,2):C.UVGC_252_49,(0,0,1):C.UVGC_252_50})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_253_51,(0,0,2):C.UVGC_253_52,(0,0,0):C.UVGC_253_53})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_283_107,(0,0,2):C.UVGC_283_108,(0,0,1):C.UVGC_283_109})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_286_116,(0,1,0):C.UVGC_287_117})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_254_54,(0,1,0):C.UVGC_255_55})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_204_3})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_204_3})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_280_100,(0,1,0):C.UVGC_271_83})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_204_3})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_204_3})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_251_47,(0,1,0):C.UVGC_246_42})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_324_198,(0,1,0):C.UVGC_311_169})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_302_148,(0,1,0):C.UVGC_289_119})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_266_74,(0,1,0):C.UVGC_257_57})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_352_294,(0,1,0):C.UVGC_339_265})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,0):C.UVGC_331_213,(0,1,1):C.UVGC_331_214,(0,1,4):C.UVGC_331_215,(0,1,5):C.UVGC_331_216,(0,1,6):C.UVGC_331_217,(0,1,7):C.UVGC_331_218,(0,0,2):C.UVGC_212_6,(0,0,3):C.UVGC_212_7})

