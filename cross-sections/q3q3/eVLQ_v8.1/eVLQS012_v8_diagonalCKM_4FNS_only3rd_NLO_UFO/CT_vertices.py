# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Thu 28 Jul 2022 11:36:59


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
               couplings = {(0,0,0):C.R2GC_245_116})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_251_119,(0,1,0):C.R2GC_252_120})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_275_137})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_279_138,(0,1,0):C.R2GC_282_141})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.x__tilde__, P.x, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.x] ] ],
               couplings = {(0,0,0):C.R2GC_301_157,(0,1,0):C.R2GC_302_158})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.y__tilde__, P.y, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.y] ] ],
               couplings = {(0,0,0):C.R2GC_329_183,(0,1,0):C.R2GC_330_184})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_319_174,(0,0,1):C.R2GC_319_175})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_206_96,(2,1,1):C.R2GC_206_97,(0,1,0):C.R2GC_206_96,(0,1,1):C.R2GC_206_97,(4,1,0):C.R2GC_204_92,(4,1,1):C.R2GC_204_93,(3,1,0):C.R2GC_204_92,(3,1,1):C.R2GC_204_93,(8,1,0):C.R2GC_205_94,(8,1,1):C.R2GC_205_95,(6,1,0):C.R2GC_209_101,(6,1,1):C.R2GC_325_182,(7,1,0):C.R2GC_210_103,(7,1,1):C.R2GC_324_181,(5,1,0):C.R2GC_204_92,(5,1,1):C.R2GC_204_93,(1,1,0):C.R2GC_204_92,(1,1,1):C.R2GC_204_93,(11,0,0):C.R2GC_208_99,(11,0,1):C.R2GC_208_100,(10,0,0):C.R2GC_208_99,(10,0,1):C.R2GC_208_100,(9,0,1):C.R2GC_207_98,(0,2,0):C.R2GC_206_96,(0,2,1):C.R2GC_206_97,(2,2,0):C.R2GC_206_96,(2,2,1):C.R2GC_206_97,(5,2,0):C.R2GC_204_92,(5,2,1):C.R2GC_204_93,(1,2,0):C.R2GC_204_92,(1,2,1):C.R2GC_204_93,(7,2,0):C.R2GC_210_103,(7,2,1):C.R2GC_210_104,(4,2,0):C.R2GC_204_92,(4,2,1):C.R2GC_204_93,(3,2,0):C.R2GC_204_92,(3,2,1):C.R2GC_204_93,(8,2,0):C.R2GC_205_94,(8,2,1):C.R2GC_323_180,(6,2,0):C.R2GC_321_177,(6,2,1):C.R2GC_321_178,(0,3,0):C.R2GC_206_96,(0,3,1):C.R2GC_206_97,(2,3,0):C.R2GC_206_96,(2,3,1):C.R2GC_206_97,(5,3,0):C.R2GC_204_92,(5,3,1):C.R2GC_204_93,(1,3,0):C.R2GC_204_92,(1,3,1):C.R2GC_204_93,(7,3,0):C.R2GC_322_179,(7,3,1):C.R2GC_206_97,(4,3,0):C.R2GC_204_92,(4,3,1):C.R2GC_204_93,(3,3,0):C.R2GC_204_92,(3,3,1):C.R2GC_204_93,(8,3,0):C.R2GC_205_94,(8,3,1):C.R2GC_320_176,(6,3,0):C.R2GC_209_101,(6,3,1):C.R2GC_209_102})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_211_105})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_215_107})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_231_108})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_233_109})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_241_112,(0,1,0):C.R2GC_240_111})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_264_129,(0,1,0):C.R2GC_263_128})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_250_118,(0,1,0):C.R2GC_249_117})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_288_147,(0,1,0):C.R2GC_287_146})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_254_122,(0,1,0):C.R2GC_253_121})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_281_140,(0,1,0):C.R2GC_280_139})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_332_186,(0,1,0):C.R2GC_331_185})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_284_143,(0,1,0):C.R2GC_283_142})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_304_160,(0,1,0):C.R2GC_303_159})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_266_131,(0,1,0):C.R2GC_265_130})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_268_133,(0,1,0):C.R2GC_267_132})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_286_145,(0,1,0):C.R2GC_285_144})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_306_162,(0,1,0):C.R2GC_305_161})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_334_188,(0,1,0):C.R2GC_333_187})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_308_164,(0,1,0):C.R2GC_307_163})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_336_190,(0,1,0):C.R2GC_335_189})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_310_166,(0,1,0):C.R2GC_309_165})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_338_192,(0,1,0):C.R2GC_337_191})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_331_185,(0,1,0):C.R2GC_332_186})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_283_142,(0,1,0):C.R2GC_284_143})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_303_159,(0,1,0):C.R2GC_304_160})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_307_163,(0,1,0):C.R2GC_308_164})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_335_189,(0,1,0):C.R2GC_336_190})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_253_121,(0,1,0):C.R2GC_254_122})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_280_139,(0,1,0):C.R2GC_281_140})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_265_130,(0,1,0):C.R2GC_266_131})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_267_132,(0,1,0):C.R2GC_268_133})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_285_144,(0,1,0):C.R2GC_286_145})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_305_161,(0,1,0):C.R2GC_306_162})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_333_187,(0,1,0):C.R2GC_334_188})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_309_165,(0,1,0):C.R2GC_310_166})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_337_191,(0,1,0):C.R2GC_338_192})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_249_117,(0,1,0):C.R2GC_250_118})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_287_146,(0,1,0):C.R2GC_288_147})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_290_149,(0,1,0):C.R2GC_292_151})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_314_170,(0,1,0):C.R2GC_315_171})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_271_135,(0,1,0):C.R2GC_272_136})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_342_196,(0,1,0):C.R2GC_343_197})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_256_124,(0,1,0):C.R2GC_257_125})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_291_150,(0,1,0):C.R2GC_293_152})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_340_194,(0,1,0):C.R2GC_341_195})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_294_153,(0,1,0):C.R2GC_295_154})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_312_168,(0,1,0):C.R2GC_313_169})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_340_194,(0,1,0):C.R2GC_341_195})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_294_153,(0,1,0):C.R2GC_295_154})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_312_168,(0,1,0):C.R2GC_313_169})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_290_149,(0,1,0):C.R2GC_292_151})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_314_170,(0,1,0):C.R2GC_315_171})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_271_135,(0,1,0):C.R2GC_272_136})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_342_196,(0,1,0):C.R2GC_343_197})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_258_126,(0,1,0):C.R2GC_259_127})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_296_155,(0,1,0):C.R2GC_297_156})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_316_172,(0,1,0):C.R2GC_317_173})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_344_198,(0,1,0):C.R2GC_345_199})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_256_124,(0,1,0):C.R2GC_257_125})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_291_150,(0,1,0):C.R2GC_293_152})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_215_107})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_215_107})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_215_107})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_211_105})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_211_105})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_211_105})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_212_106})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_235_110})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_235_110})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_235_110})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_235_110})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_235_110})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_235_110})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_182_46,(0,1,0):C.R2GC_166_3})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_182_46,(0,1,0):C.R2GC_166_3})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_182_46,(0,1,0):C.R2GC_166_3})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_183_47,(0,1,0):C.R2GC_168_4})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_183_47,(0,1,0):C.R2GC_168_4})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_243_114,(0,1,0):C.R2GC_244_115})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_165_2})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_165_2})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_269_134,(0,1,0):C.R2GC_165_2})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_165_2})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_165_2})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_242_113,(0,1,0):C.R2GC_165_2})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_311_167,(0,1,0):C.R2GC_165_2})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_289_148,(0,1,0):C.R2GC_165_2})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_255_123,(0,1,0):C.R2GC_165_2})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_339_193,(0,1,0):C.R2GC_165_2})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV2, L.VV3, L.VV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,2,3):C.R2GC_164_1,(0,0,0):C.R2GC_178_22,(0,0,1):C.R2GC_178_23,(0,0,4):C.R2GC_178_24,(0,0,5):C.R2GC_178_25,(0,0,6):C.R2GC_178_26,(0,0,7):C.R2GC_178_27,(0,1,2):C.R2GC_174_7})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_173_5,(0,0,1):C.R2GC_173_6})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_177_16,(0,0,1):C.R2GC_177_17,(0,0,2):C.R2GC_177_18,(0,0,3):C.R2GC_177_19,(0,0,4):C.R2GC_177_20,(0,0,5):C.R2GC_177_21})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.y] ], [ [P.b, P.tp] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.b, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ] ],
                 couplings = {(0,0,4):C.R2GC_192_84,(0,0,3):C.R2GC_192_85,(0,0,5):C.R2GC_192_86,(0,0,0):C.R2GC_192_87,(0,0,1):C.R2GC_192_88,(0,0,2):C.R2GC_192_89,(0,0,7):C.R2GC_192_90,(0,0,6):C.R2GC_192_91})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b, P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_188_64,(0,0,0):C.R2GC_188_65,(0,0,3):C.R2GC_188_66,(0,0,4):C.R2GC_188_67,(0,0,6):C.R2GC_188_68,(0,0,7):C.R2GC_188_69,(0,0,1):C.R2GC_188_70,(0,0,5):C.R2GC_188_71})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_179_28,(0,0,0):C.R2GC_179_29,(0,0,2):C.R2GC_179_30,(0,0,3):C.R2GC_179_31,(0,0,4):C.R2GC_179_32,(0,0,5):C.R2GC_179_33})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_175_8,(0,0,1):C.R2GC_175_9,(0,0,2):C.R2GC_175_10,(0,0,3):C.R2GC_175_11})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV10 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(1,0,1):C.R2GC_181_40,(1,0,0):C.R2GC_181_41,(1,0,2):C.R2GC_181_42,(1,0,3):C.R2GC_181_43,(1,0,4):C.R2GC_181_44,(1,0,5):C.R2GC_181_45,(0,1,1):C.R2GC_180_34,(0,1,0):C.R2GC_180_35,(0,1,2):C.R2GC_180_36,(0,1,3):C.R2GC_180_37,(0,1,4):C.R2GC_180_38,(0,1,5):C.R2GC_180_39})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_176_12,(0,0,1):C.R2GC_176_13,(0,0,2):C.R2GC_176_14,(0,0,3):C.R2GC_176_15})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.t] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_187_60,(0,0,2):C.R2GC_187_61,(0,0,1):C.R2GC_187_62,(0,0,3):C.R2GC_187_63})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.t] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_186_56,(0,0,2):C.R2GC_186_57,(0,0,1):C.R2GC_186_58,(0,0,3):C.R2GC_186_59})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_185_48,(0,0,1):C.R2GC_185_49,(0,0,3):C.R2GC_185_50,(0,0,4):C.R2GC_185_51,(0,0,6):C.R2GC_185_52,(0,0,7):C.R2GC_185_53,(0,0,2):C.R2GC_185_54,(0,0,5):C.R2GC_185_55})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus__, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ] ],
                 couplings = {(0,0,3):C.R2GC_191_76,(0,0,4):C.R2GC_191_77,(0,0,5):C.R2GC_191_78,(0,0,0):C.R2GC_191_79,(0,0,1):C.R2GC_191_80,(0,0,2):C.R2GC_191_81,(0,0,7):C.R2GC_191_82,(0,0,6):C.R2GC_191_83})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus____minus__, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.x] ], [ [P.b, P.x] ], [ [P.tp, P.y] ], [ [P.t, P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_190_72,(0,0,0):C.R2GC_190_73,(0,0,3):C.R2GC_190_74,(0,0,2):C.R2GC_190_75})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_245_45})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_251_55,(0,1,0):C.UVGC_252_56})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_275_100})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_279_104,(0,1,0):C.UVGC_282_111})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_301_154,(0,1,0):C.UVGC_302_155})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_329_250,(0,1,0):C.UVGC_330_251})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,0):C.UVGC_319_201,(0,1,1):C.UVGC_319_202,(0,1,2):C.UVGC_319_203,(0,1,5):C.UVGC_319_204,(0,1,6):C.UVGC_319_205,(0,1,7):C.UVGC_319_206,(0,1,8):C.UVGC_319_207,(0,2,3):C.UVGC_193_1,(0,0,4):C.UVGC_194_2})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(2,1,4):C.UVGC_205_11,(2,1,5):C.UVGC_205_10,(0,1,4):C.UVGC_205_11,(0,1,5):C.UVGC_205_10,(4,1,4):C.UVGC_204_8,(4,1,5):C.UVGC_204_9,(3,1,4):C.UVGC_204_8,(3,1,5):C.UVGC_204_9,(8,1,4):C.UVGC_205_10,(8,1,5):C.UVGC_205_11,(6,1,0):C.UVGC_324_236,(6,1,1):C.UVGC_324_237,(6,1,3):C.UVGC_324_238,(6,1,4):C.UVGC_325_245,(6,1,5):C.UVGC_325_246,(6,1,6):C.UVGC_324_241,(6,1,7):C.UVGC_324_242,(6,1,8):C.UVGC_324_243,(6,1,9):C.UVGC_324_244,(7,1,0):C.UVGC_324_236,(7,1,1):C.UVGC_324_237,(7,1,3):C.UVGC_324_238,(7,1,4):C.UVGC_324_239,(7,1,5):C.UVGC_324_240,(7,1,6):C.UVGC_324_241,(7,1,7):C.UVGC_324_242,(7,1,8):C.UVGC_324_243,(7,1,9):C.UVGC_324_244,(5,1,4):C.UVGC_204_8,(5,1,5):C.UVGC_204_9,(1,1,4):C.UVGC_204_8,(1,1,5):C.UVGC_204_9,(11,0,4):C.UVGC_208_14,(11,0,5):C.UVGC_208_15,(10,0,4):C.UVGC_208_14,(10,0,5):C.UVGC_208_15,(9,0,4):C.UVGC_207_12,(9,0,5):C.UVGC_207_13,(0,2,4):C.UVGC_205_11,(0,2,5):C.UVGC_205_10,(2,2,4):C.UVGC_205_11,(2,2,5):C.UVGC_205_10,(5,2,4):C.UVGC_204_8,(5,2,5):C.UVGC_204_9,(1,2,4):C.UVGC_204_8,(1,2,5):C.UVGC_204_9,(7,2,2):C.UVGC_209_16,(7,2,4):C.UVGC_210_18,(7,2,5):C.UVGC_210_19,(4,2,4):C.UVGC_204_8,(4,2,5):C.UVGC_204_9,(3,2,4):C.UVGC_204_8,(3,2,5):C.UVGC_204_9,(8,2,0):C.UVGC_323_227,(8,2,1):C.UVGC_323_228,(8,2,3):C.UVGC_323_229,(8,2,4):C.UVGC_323_230,(8,2,5):C.UVGC_323_231,(8,2,6):C.UVGC_323_232,(8,2,7):C.UVGC_323_233,(8,2,8):C.UVGC_323_234,(8,2,9):C.UVGC_323_235,(6,2,0):C.UVGC_321_217,(6,2,1):C.UVGC_321_218,(6,2,4):C.UVGC_321_219,(6,2,5):C.UVGC_321_220,(6,2,6):C.UVGC_321_221,(6,2,7):C.UVGC_321_222,(6,2,8):C.UVGC_321_223,(6,2,9):C.UVGC_321_224,(0,3,4):C.UVGC_205_11,(0,3,5):C.UVGC_205_10,(2,3,4):C.UVGC_205_11,(2,3,5):C.UVGC_205_10,(5,3,4):C.UVGC_204_8,(5,3,5):C.UVGC_204_9,(1,3,4):C.UVGC_204_8,(1,3,5):C.UVGC_204_9,(7,3,0):C.UVGC_321_217,(7,3,1):C.UVGC_321_218,(7,3,4):C.UVGC_322_225,(7,3,5):C.UVGC_322_226,(7,3,6):C.UVGC_321_221,(7,3,7):C.UVGC_321_222,(7,3,8):C.UVGC_321_223,(7,3,9):C.UVGC_321_224,(4,3,4):C.UVGC_204_8,(4,3,5):C.UVGC_204_9,(3,3,4):C.UVGC_204_8,(3,3,5):C.UVGC_204_9,(8,3,0):C.UVGC_320_208,(8,3,1):C.UVGC_320_209,(8,3,3):C.UVGC_320_210,(8,3,4):C.UVGC_320_211,(8,3,5):C.UVGC_320_212,(8,3,6):C.UVGC_320_213,(8,3,7):C.UVGC_320_214,(8,3,8):C.UVGC_320_215,(8,3,9):C.UVGC_320_216,(6,3,2):C.UVGC_209_16,(6,3,4):C.UVGC_209_17,(6,3,5):C.UVGC_207_12})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_211_20,(0,1,0):C.UVGC_247_47,(0,2,0):C.UVGC_247_47})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_215_22,(0,1,0):C.UVGC_277_102,(0,2,0):C.UVGC_277_102})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_231_33,(0,1,0):C.UVGC_299_152,(0,2,0):C.UVGC_299_152})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_233_34,(0,1,0):C.UVGC_327_248,(0,2,0):C.UVGC_327_248})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_241_41,(0,1,0):C.UVGC_240_40})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_264_76,(0,1,0):C.UVGC_263_75})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_250_52,(0,0,2):C.UVGC_250_53,(0,0,0):C.UVGC_250_54,(0,1,1):C.UVGC_249_49,(0,1,2):C.UVGC_249_50,(0,1,0):C.UVGC_249_51})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_288_127,(0,0,1):C.UVGC_288_128,(0,0,2):C.UVGC_288_129,(0,1,0):C.UVGC_287_124,(0,1,1):C.UVGC_287_125,(0,1,2):C.UVGC_287_126})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_254_60,(0,0,2):C.UVGC_254_61,(0,0,0):C.UVGC_254_62,(0,1,1):C.UVGC_253_57,(0,1,2):C.UVGC_253_58,(0,1,0):C.UVGC_253_59})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_281_108,(0,0,1):C.UVGC_281_109,(0,0,2):C.UVGC_281_110,(0,1,0):C.UVGC_280_105,(0,1,1):C.UVGC_280_106,(0,1,2):C.UVGC_280_107})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_332_255,(0,0,2):C.UVGC_332_256,(0,0,1):C.UVGC_332_257,(0,1,0):C.UVGC_331_252,(0,1,2):C.UVGC_331_253,(0,1,1):C.UVGC_331_254})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_284_115,(0,0,2):C.UVGC_284_116,(0,0,1):C.UVGC_284_117,(0,1,0):C.UVGC_283_112,(0,1,2):C.UVGC_283_113,(0,1,1):C.UVGC_283_114})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_304_159,(0,0,2):C.UVGC_304_160,(0,0,1):C.UVGC_304_161,(0,1,0):C.UVGC_303_156,(0,1,2):C.UVGC_303_157,(0,1,1):C.UVGC_303_158})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_266_80,(0,0,2):C.UVGC_266_81,(0,0,1):C.UVGC_266_82,(0,1,0):C.UVGC_265_77,(0,1,2):C.UVGC_265_78,(0,1,1):C.UVGC_265_79})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_268_86,(0,0,2):C.UVGC_268_87,(0,0,1):C.UVGC_268_88,(0,1,0):C.UVGC_267_83,(0,1,2):C.UVGC_267_84,(0,1,1):C.UVGC_267_85})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_286_121,(0,0,2):C.UVGC_286_122,(0,0,1):C.UVGC_286_123,(0,1,0):C.UVGC_285_118,(0,1,2):C.UVGC_285_119,(0,1,1):C.UVGC_285_120})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_306_165,(0,0,2):C.UVGC_306_166,(0,0,1):C.UVGC_306_167,(0,1,0):C.UVGC_305_162,(0,1,2):C.UVGC_305_163,(0,1,1):C.UVGC_305_164})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_334_261,(0,0,2):C.UVGC_334_262,(0,0,1):C.UVGC_334_263,(0,1,0):C.UVGC_333_258,(0,1,2):C.UVGC_333_259,(0,1,1):C.UVGC_333_260})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_308_171,(0,0,2):C.UVGC_308_172,(0,0,1):C.UVGC_308_173,(0,1,0):C.UVGC_307_168,(0,1,2):C.UVGC_307_169,(0,1,1):C.UVGC_307_170})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_336_267,(0,0,2):C.UVGC_336_268,(0,0,1):C.UVGC_336_269,(0,1,0):C.UVGC_335_264,(0,1,2):C.UVGC_335_265,(0,1,1):C.UVGC_335_266})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_310_177,(0,0,2):C.UVGC_310_178,(0,0,1):C.UVGC_310_179,(0,1,0):C.UVGC_309_174,(0,1,2):C.UVGC_309_175,(0,1,1):C.UVGC_309_176})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_338_273,(0,0,2):C.UVGC_338_274,(0,0,1):C.UVGC_338_275,(0,1,0):C.UVGC_337_270,(0,1,2):C.UVGC_337_271,(0,1,1):C.UVGC_337_272})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_331_252,(0,0,2):C.UVGC_331_253,(0,0,1):C.UVGC_331_254,(0,1,0):C.UVGC_332_255,(0,1,2):C.UVGC_332_256,(0,1,1):C.UVGC_332_257})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_283_112,(0,0,2):C.UVGC_283_113,(0,0,1):C.UVGC_283_114,(0,1,0):C.UVGC_284_115,(0,1,2):C.UVGC_284_116,(0,1,1):C.UVGC_284_117})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_303_156,(0,0,2):C.UVGC_303_157,(0,0,1):C.UVGC_303_158,(0,1,0):C.UVGC_304_159,(0,1,2):C.UVGC_304_160,(0,1,1):C.UVGC_304_161})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_307_168,(0,0,2):C.UVGC_307_169,(0,0,1):C.UVGC_307_170,(0,1,0):C.UVGC_308_171,(0,1,2):C.UVGC_308_172,(0,1,1):C.UVGC_308_173})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_335_264,(0,0,2):C.UVGC_335_265,(0,0,1):C.UVGC_335_266,(0,1,0):C.UVGC_336_267,(0,1,2):C.UVGC_336_268,(0,1,1):C.UVGC_336_269})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_253_57,(0,0,2):C.UVGC_253_58,(0,0,0):C.UVGC_253_59,(0,1,1):C.UVGC_254_60,(0,1,2):C.UVGC_254_61,(0,1,0):C.UVGC_254_62})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_280_105,(0,0,1):C.UVGC_280_106,(0,0,2):C.UVGC_280_107,(0,1,0):C.UVGC_281_108,(0,1,1):C.UVGC_281_109,(0,1,2):C.UVGC_281_110})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_265_77,(0,0,2):C.UVGC_265_78,(0,0,1):C.UVGC_265_79,(0,1,0):C.UVGC_266_80,(0,1,2):C.UVGC_266_81,(0,1,1):C.UVGC_266_82})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_267_83,(0,0,2):C.UVGC_267_84,(0,0,1):C.UVGC_267_85,(0,1,0):C.UVGC_268_86,(0,1,2):C.UVGC_268_87,(0,1,1):C.UVGC_268_88})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_285_118,(0,0,2):C.UVGC_285_119,(0,0,1):C.UVGC_285_120,(0,1,0):C.UVGC_286_121,(0,1,2):C.UVGC_286_122,(0,1,1):C.UVGC_286_123})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_305_162,(0,0,2):C.UVGC_305_163,(0,0,1):C.UVGC_305_164,(0,1,0):C.UVGC_306_165,(0,1,2):C.UVGC_306_166,(0,1,1):C.UVGC_306_167})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_333_258,(0,0,2):C.UVGC_333_259,(0,0,1):C.UVGC_333_260,(0,1,0):C.UVGC_334_261,(0,1,2):C.UVGC_334_262,(0,1,1):C.UVGC_334_263})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_309_174,(0,0,2):C.UVGC_309_175,(0,0,1):C.UVGC_309_176,(0,1,0):C.UVGC_310_177,(0,1,2):C.UVGC_310_178,(0,1,1):C.UVGC_310_179})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_337_270,(0,0,2):C.UVGC_337_271,(0,0,1):C.UVGC_337_272,(0,1,0):C.UVGC_338_273,(0,1,2):C.UVGC_338_274,(0,1,1):C.UVGC_338_275})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_249_49,(0,0,2):C.UVGC_249_50,(0,0,0):C.UVGC_249_51,(0,1,1):C.UVGC_250_52,(0,1,2):C.UVGC_250_53,(0,1,0):C.UVGC_250_54})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_287_124,(0,0,1):C.UVGC_287_125,(0,0,2):C.UVGC_287_126,(0,1,0):C.UVGC_288_127,(0,1,1):C.UVGC_288_128,(0,1,2):C.UVGC_288_129})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,3):C.UVGC_216_26,(0,1,4):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,5):C.UVGC_278_103})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.bp, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,3):C.UVGC_216_25,(0,1,4):C.UVGC_216_26,(0,1,5):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,2):C.UVGC_248_48})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.x] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,3):C.UVGC_216_26,(0,1,4):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,5):C.UVGC_300_153})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.y] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,3):C.UVGC_216_26,(0,1,4):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,5):C.UVGC_328_249})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_290_131,(0,0,2):C.UVGC_290_132,(0,0,1):C.UVGC_290_133,(0,1,0):C.UVGC_292_137,(0,1,2):C.UVGC_292_138,(0,1,1):C.UVGC_292_139})

V_172 = CTVertex(name = 'V_172',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_314_187,(0,0,2):C.UVGC_314_188,(0,0,1):C.UVGC_314_189,(0,1,0):C.UVGC_315_190,(0,1,2):C.UVGC_315_191,(0,1,1):C.UVGC_315_192})

V_173 = CTVertex(name = 'V_173',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_271_92,(0,0,2):C.UVGC_271_93,(0,0,1):C.UVGC_271_94,(0,1,0):C.UVGC_272_95,(0,1,2):C.UVGC_272_96,(0,1,1):C.UVGC_272_97})

V_174 = CTVertex(name = 'V_174',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_342_283,(0,0,2):C.UVGC_342_284,(0,0,1):C.UVGC_342_285,(0,1,0):C.UVGC_343_286,(0,1,2):C.UVGC_343_287,(0,1,1):C.UVGC_343_288})

V_175 = CTVertex(name = 'V_175',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_256_64,(0,0,2):C.UVGC_256_65,(0,0,0):C.UVGC_256_66,(0,1,1):C.UVGC_257_67,(0,1,2):C.UVGC_257_68,(0,1,0):C.UVGC_257_69})

V_176 = CTVertex(name = 'V_176',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_291_134,(0,0,1):C.UVGC_291_135,(0,0,2):C.UVGC_291_136,(0,1,0):C.UVGC_293_140,(0,1,1):C.UVGC_293_141,(0,1,2):C.UVGC_293_142})

V_177 = CTVertex(name = 'V_177',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_340_277,(0,0,2):C.UVGC_340_278,(0,0,1):C.UVGC_340_279,(0,1,0):C.UVGC_341_280,(0,1,2):C.UVGC_341_281,(0,1,1):C.UVGC_341_282})

V_178 = CTVertex(name = 'V_178',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_294_143,(0,0,2):C.UVGC_294_144,(0,0,1):C.UVGC_294_145,(0,1,0):C.UVGC_295_146,(0,1,2):C.UVGC_295_147,(0,1,1):C.UVGC_295_148})

V_179 = CTVertex(name = 'V_179',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_312_181,(0,0,2):C.UVGC_312_182,(0,0,1):C.UVGC_312_183,(0,1,0):C.UVGC_313_184,(0,1,2):C.UVGC_313_185,(0,1,1):C.UVGC_313_186})

V_180 = CTVertex(name = 'V_180',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_340_277,(0,0,2):C.UVGC_340_278,(0,0,1):C.UVGC_340_279,(0,1,0):C.UVGC_341_280,(0,1,2):C.UVGC_341_281,(0,1,1):C.UVGC_341_282})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_294_143,(0,0,2):C.UVGC_294_144,(0,0,1):C.UVGC_294_145,(0,1,0):C.UVGC_295_146,(0,1,2):C.UVGC_295_147,(0,1,1):C.UVGC_295_148})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_312_181,(0,0,2):C.UVGC_312_182,(0,0,1):C.UVGC_312_183,(0,1,0):C.UVGC_313_184,(0,1,2):C.UVGC_313_185,(0,1,1):C.UVGC_313_186})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_290_131,(0,0,2):C.UVGC_290_132,(0,0,1):C.UVGC_290_133,(0,1,0):C.UVGC_292_137,(0,1,2):C.UVGC_292_138,(0,1,1):C.UVGC_292_139})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_314_187,(0,0,2):C.UVGC_314_188,(0,0,1):C.UVGC_314_189,(0,1,0):C.UVGC_315_190,(0,1,2):C.UVGC_315_191,(0,1,1):C.UVGC_315_192})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_271_92,(0,0,2):C.UVGC_271_93,(0,0,1):C.UVGC_271_94,(0,1,0):C.UVGC_272_95,(0,1,2):C.UVGC_272_96,(0,1,1):C.UVGC_272_97})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_342_283,(0,0,2):C.UVGC_342_284,(0,0,1):C.UVGC_342_285,(0,1,0):C.UVGC_343_286,(0,1,2):C.UVGC_343_287,(0,1,1):C.UVGC_343_288})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_258_70,(0,1,0):C.UVGC_259_71})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_296_149,(0,1,0):C.UVGC_297_150})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_316_193,(0,1,0):C.UVGC_317_194})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_344_289,(0,1,0):C.UVGC_345_290})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_256_64,(0,0,2):C.UVGC_256_65,(0,0,0):C.UVGC_256_66,(0,1,1):C.UVGC_257_67,(0,1,2):C.UVGC_257_68,(0,1,0):C.UVGC_257_69})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_291_134,(0,0,1):C.UVGC_291_135,(0,0,2):C.UVGC_291_136,(0,1,0):C.UVGC_293_140,(0,1,1):C.UVGC_293_141,(0,1,2):C.UVGC_293_142})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_215_22,(0,1,0):C.UVGC_196_4,(0,2,0):C.UVGC_196_4})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_215_22,(0,1,0):C.UVGC_196_4,(0,2,0):C.UVGC_196_4})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_215_22,(0,1,0):C.UVGC_261_73,(0,2,0):C.UVGC_261_73})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_211_20,(0,1,0):C.UVGC_198_5,(0,2,0):C.UVGC_198_5})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_211_20,(0,1,0):C.UVGC_198_5,(0,2,0):C.UVGC_198_5})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_211_20,(0,1,0):C.UVGC_238_38,(0,2,0):C.UVGC_238_38})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,3):C.UVGC_216_26,(0,1,4):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,5):C.UVGC_216_32,(0,2,0):C.UVGC_216_23,(0,2,1):C.UVGC_216_24,(0,2,2):C.UVGC_216_25,(0,2,3):C.UVGC_216_26,(0,2,4):C.UVGC_216_27,(0,2,6):C.UVGC_216_28,(0,2,7):C.UVGC_216_29,(0,2,8):C.UVGC_216_30,(0,2,9):C.UVGC_216_31,(0,2,5):C.UVGC_216_32})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,4):C.UVGC_216_26,(0,1,5):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,3):C.UVGC_216_32,(0,2,0):C.UVGC_216_23,(0,2,1):C.UVGC_216_24,(0,2,2):C.UVGC_216_25,(0,2,4):C.UVGC_216_26,(0,2,5):C.UVGC_216_27,(0,2,6):C.UVGC_216_28,(0,2,7):C.UVGC_216_29,(0,2,8):C.UVGC_216_30,(0,2,9):C.UVGC_216_31,(0,2,3):C.UVGC_216_32})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,3):C.UVGC_216_26,(0,1,4):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,5):C.UVGC_262_74,(0,2,0):C.UVGC_216_23,(0,2,1):C.UVGC_216_24,(0,2,2):C.UVGC_216_25,(0,2,3):C.UVGC_216_26,(0,2,4):C.UVGC_216_27,(0,2,6):C.UVGC_216_28,(0,2,7):C.UVGC_216_29,(0,2,8):C.UVGC_216_30,(0,2,9):C.UVGC_216_31,(0,2,5):C.UVGC_262_74})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,4):C.UVGC_216_26,(0,1,5):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,3):C.UVGC_216_32,(0,2,0):C.UVGC_216_23,(0,2,1):C.UVGC_216_24,(0,2,2):C.UVGC_216_25,(0,2,4):C.UVGC_216_26,(0,2,5):C.UVGC_216_27,(0,2,6):C.UVGC_216_28,(0,2,7):C.UVGC_216_29,(0,2,8):C.UVGC_216_30,(0,2,9):C.UVGC_216_31,(0,2,3):C.UVGC_216_32})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,2):C.UVGC_216_25,(0,1,3):C.UVGC_216_26,(0,1,4):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,5):C.UVGC_216_32,(0,2,0):C.UVGC_216_23,(0,2,1):C.UVGC_216_24,(0,2,2):C.UVGC_216_25,(0,2,3):C.UVGC_216_26,(0,2,4):C.UVGC_216_27,(0,2,6):C.UVGC_216_28,(0,2,7):C.UVGC_216_29,(0,2,8):C.UVGC_216_30,(0,2,9):C.UVGC_216_31,(0,2,5):C.UVGC_216_32})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_212_21,(0,1,0):C.UVGC_216_23,(0,1,1):C.UVGC_216_24,(0,1,3):C.UVGC_216_25,(0,1,4):C.UVGC_216_26,(0,1,5):C.UVGC_216_27,(0,1,6):C.UVGC_216_28,(0,1,7):C.UVGC_216_29,(0,1,8):C.UVGC_216_30,(0,1,9):C.UVGC_216_31,(0,1,2):C.UVGC_239_39,(0,2,0):C.UVGC_216_23,(0,2,1):C.UVGC_216_24,(0,2,3):C.UVGC_216_25,(0,2,4):C.UVGC_216_26,(0,2,5):C.UVGC_216_27,(0,2,6):C.UVGC_216_28,(0,2,7):C.UVGC_216_29,(0,2,8):C.UVGC_216_30,(0,2,9):C.UVGC_216_31,(0,2,2):C.UVGC_239_39})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_235_35,(0,0,1):C.UVGC_235_36})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_235_35,(0,0,1):C.UVGC_235_36})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_270_90,(0,0,2):C.UVGC_270_91,(0,0,1):C.UVGC_235_36})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_235_35,(0,0,1):C.UVGC_235_36})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_235_35,(0,0,1):C.UVGC_235_36})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_270_90,(0,0,2):C.UVGC_270_91,(0,0,1):C.UVGC_235_36})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_273_98,(0,1,0):C.UVGC_274_99})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_243_43,(0,1,0):C.UVGC_244_44})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_195_3})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_195_3})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_269_89,(0,1,0):C.UVGC_260_72})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_195_3})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_195_3})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_242_42,(0,1,0):C.UVGC_237_37})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_311_180,(0,1,0):C.UVGC_298_151})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_289_130,(0,1,0):C.UVGC_276_101})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_255_63,(0,1,0):C.UVGC_246_46})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_339_276,(0,1,0):C.UVGC_326_247})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,0):C.UVGC_318_195,(0,1,1):C.UVGC_318_196,(0,1,4):C.UVGC_318_197,(0,1,5):C.UVGC_318_198,(0,1,6):C.UVGC_318_199,(0,1,7):C.UVGC_318_200,(0,0,2):C.UVGC_203_6,(0,0,3):C.UVGC_203_7})

