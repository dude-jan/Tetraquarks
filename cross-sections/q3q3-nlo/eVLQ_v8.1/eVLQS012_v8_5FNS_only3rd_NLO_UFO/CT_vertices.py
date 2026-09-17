# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Thu 28 Jul 2022 09:55:34


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_263_125,(0,1,0):C.R2GC_264_126})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_289_146})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_293_147,(0,1,0):C.R2GC_296_150})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.x__tilde__, P.x, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.x] ] ],
               couplings = {(0,0,0):C.R2GC_315_166,(0,1,0):C.R2GC_316_167})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.y__tilde__, P.y, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.y] ] ],
               couplings = {(0,0,0):C.R2GC_343_192,(0,1,0):C.R2GC_344_193})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_333_183,(0,0,1):C.R2GC_333_184})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_220_101,(2,0,1):C.R2GC_220_102,(0,0,0):C.R2GC_220_101,(0,0,1):C.R2GC_220_102,(4,0,0):C.R2GC_218_97,(4,0,1):C.R2GC_218_98,(3,0,0):C.R2GC_218_97,(3,0,1):C.R2GC_218_98,(8,0,0):C.R2GC_219_99,(8,0,1):C.R2GC_219_100,(6,0,0):C.R2GC_223_106,(6,0,1):C.R2GC_339_191,(7,0,0):C.R2GC_224_108,(7,0,1):C.R2GC_338_190,(5,0,0):C.R2GC_218_97,(5,0,1):C.R2GC_218_98,(1,0,0):C.R2GC_218_97,(1,0,1):C.R2GC_218_98,(11,3,0):C.R2GC_222_104,(11,3,1):C.R2GC_222_105,(10,3,0):C.R2GC_222_104,(10,3,1):C.R2GC_222_105,(9,3,1):C.R2GC_221_103,(0,1,0):C.R2GC_220_101,(0,1,1):C.R2GC_220_102,(2,1,0):C.R2GC_220_101,(2,1,1):C.R2GC_220_102,(5,1,0):C.R2GC_218_97,(5,1,1):C.R2GC_218_98,(1,1,0):C.R2GC_218_97,(1,1,1):C.R2GC_218_98,(7,1,0):C.R2GC_224_108,(7,1,1):C.R2GC_224_109,(4,1,0):C.R2GC_218_97,(4,1,1):C.R2GC_218_98,(3,1,0):C.R2GC_218_97,(3,1,1):C.R2GC_218_98,(8,1,0):C.R2GC_219_99,(8,1,1):C.R2GC_337_189,(6,1,0):C.R2GC_335_186,(6,1,1):C.R2GC_335_187,(0,2,0):C.R2GC_220_101,(0,2,1):C.R2GC_220_102,(2,2,0):C.R2GC_220_101,(2,2,1):C.R2GC_220_102,(5,2,0):C.R2GC_218_97,(5,2,1):C.R2GC_218_98,(1,2,0):C.R2GC_218_97,(1,2,1):C.R2GC_218_98,(7,2,0):C.R2GC_336_188,(7,2,1):C.R2GC_220_102,(4,2,0):C.R2GC_218_97,(4,2,1):C.R2GC_218_98,(3,2,0):C.R2GC_218_97,(3,2,1):C.R2GC_218_98,(8,2,0):C.R2GC_219_99,(8,2,1):C.R2GC_334_185,(6,2,0):C.R2GC_223_106,(6,2,1):C.R2GC_223_107})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_225_110})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_232_114})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_248_115})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_250_116})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_228_112,(0,1,0):C.R2GC_229_113})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_276_135,(0,1,0):C.R2GC_275_134})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_262_124,(0,1,0):C.R2GC_261_123})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_302_156,(0,1,0):C.R2GC_301_155})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_266_128,(0,1,0):C.R2GC_265_127})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_295_149,(0,1,0):C.R2GC_294_148})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_346_195,(0,1,0):C.R2GC_345_194})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_298_152,(0,1,0):C.R2GC_297_151})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_318_169,(0,1,0):C.R2GC_317_168})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_278_137,(0,1,0):C.R2GC_277_136})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_280_139,(0,1,0):C.R2GC_279_138})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_300_154,(0,1,0):C.R2GC_299_153})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_320_171,(0,1,0):C.R2GC_319_170})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_348_197,(0,1,0):C.R2GC_347_196})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_322_173,(0,1,0):C.R2GC_321_172})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_350_199,(0,1,0):C.R2GC_349_198})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_324_175,(0,1,0):C.R2GC_323_174})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_352_201,(0,1,0):C.R2GC_351_200})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_345_194,(0,1,0):C.R2GC_346_195})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_297_151,(0,1,0):C.R2GC_298_152})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_317_168,(0,1,0):C.R2GC_318_169})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_321_172,(0,1,0):C.R2GC_322_173})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_349_198,(0,1,0):C.R2GC_350_199})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_265_127,(0,1,0):C.R2GC_266_128})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_294_148,(0,1,0):C.R2GC_295_149})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_277_136,(0,1,0):C.R2GC_278_137})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_279_138,(0,1,0):C.R2GC_280_139})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_299_153,(0,1,0):C.R2GC_300_154})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_319_170,(0,1,0):C.R2GC_320_171})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_347_196,(0,1,0):C.R2GC_348_197})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_323_174,(0,1,0):C.R2GC_324_175})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_351_200,(0,1,0):C.R2GC_352_201})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_261_123,(0,1,0):C.R2GC_262_124})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_301_155,(0,1,0):C.R2GC_302_156})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_304_158,(0,1,0):C.R2GC_306_160})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_328_179,(0,1,0):C.R2GC_329_180})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_285_144,(0,1,0):C.R2GC_286_145})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_356_205,(0,1,0):C.R2GC_357_206})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_268_130,(0,1,0):C.R2GC_269_131})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_305_159,(0,1,0):C.R2GC_307_161})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_354_203,(0,1,0):C.R2GC_355_204})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_308_162,(0,1,0):C.R2GC_309_163})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_326_177,(0,1,0):C.R2GC_327_178})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_354_203,(0,1,0):C.R2GC_355_204})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_308_162,(0,1,0):C.R2GC_309_163})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_326_177,(0,1,0):C.R2GC_327_178})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_304_158,(0,1,0):C.R2GC_306_160})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_328_179,(0,1,0):C.R2GC_329_180})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_285_144,(0,1,0):C.R2GC_286_145})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_356_205,(0,1,0):C.R2GC_357_206})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_270_132,(0,1,0):C.R2GC_271_133})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_310_164,(0,1,0):C.R2GC_311_165})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_330_181,(0,1,0):C.R2GC_331_182})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_358_207,(0,1,0):C.R2GC_359_208})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_268_130,(0,1,0):C.R2GC_269_131})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_305_159,(0,1,0):C.R2GC_307_161})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_232_114})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_232_114})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_232_114})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_225_110})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_225_110})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_225_110})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_227_111})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_256_121})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_257_122})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_255_120})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_253_118})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_254_119})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_252_117})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_282_141})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_283_142})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_284_143})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_256_121})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_253_118})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_282_141})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_257_122})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_254_119})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_283_142})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_255_120})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_252_117})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_284_143})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_195_45,(0,1,0):C.R2GC_178_5})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_195_45,(0,1,0):C.R2GC_178_5})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_195_45,(0,1,0):C.R2GC_178_5})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_196_46,(0,1,0):C.R2GC_180_6})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_175_3,(0,1,0):C.R2GC_176_4})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_175_3,(0,1,0):C.R2GC_176_4})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_174_2})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_174_2})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_281_140,(0,1,0):C.R2GC_174_2})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_174_2})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_174_2})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_174_2})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_325_176,(0,1,0):C.R2GC_174_2})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_303_157,(0,1,0):C.R2GC_174_2})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_267_129,(0,1,0):C.R2GC_174_2})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_353_202,(0,1,0):C.R2GC_174_2})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV2, L.VV3, L.VV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,2,2):C.R2GC_173_1,(0,0,0):C.R2GC_191_22,(0,0,3):C.R2GC_191_23,(0,0,4):C.R2GC_191_24,(0,0,5):C.R2GC_191_25,(0,0,6):C.R2GC_191_26,(0,1,1):C.R2GC_187_8})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_186_7})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_190_17,(0,0,1):C.R2GC_190_18,(0,0,2):C.R2GC_190_19,(0,0,3):C.R2GC_190_20,(0,0,4):C.R2GC_190_21})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV9 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.u] ], [ [P.b, P.y] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ], [ [P.tp, P.x] ], [ [P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_204_81,(0,0,4):C.R2GC_204_82,(0,0,5):C.R2GC_204_83,(0,0,6):C.R2GC_204_84,(0,0,7):C.R2GC_204_85,(0,0,1):C.R2GC_204_86,(0,0,2):C.R2GC_204_87,(0,0,3):C.R2GC_204_88,(0,0,8):C.R2GC_204_89,(0,0,9):C.R2GC_204_90,(0,0,10):C.R2GC_204_91,(0,0,11):C.R2GC_204_92,(0,0,12):C.R2GC_204_93,(0,0,13):C.R2GC_204_94,(0,0,15):C.R2GC_204_95,(0,0,14):C.R2GC_204_96})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV9 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b, P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_200_61,(0,0,0):C.R2GC_200_62,(0,0,3):C.R2GC_200_63,(0,0,4):C.R2GC_200_64,(0,0,6):C.R2GC_200_65,(0,0,7):C.R2GC_200_66,(0,0,1):C.R2GC_200_67,(0,0,5):C.R2GC_200_68})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV9 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_192_27,(0,0,0):C.R2GC_192_28,(0,0,2):C.R2GC_192_29,(0,0,3):C.R2GC_192_30,(0,0,4):C.R2GC_192_31,(0,0,5):C.R2GC_192_32})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV9 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_188_9,(0,0,1):C.R2GC_188_10,(0,0,2):C.R2GC_188_11,(0,0,3):C.R2GC_188_12})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV9 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(1,0,1):C.R2GC_194_39,(1,0,0):C.R2GC_194_40,(1,0,2):C.R2GC_194_41,(1,0,3):C.R2GC_194_42,(1,0,4):C.R2GC_194_43,(1,0,5):C.R2GC_194_44,(0,1,1):C.R2GC_193_33,(0,1,0):C.R2GC_193_34,(0,1,2):C.R2GC_193_35,(0,1,3):C.R2GC_193_36,(0,1,4):C.R2GC_193_37,(0,1,5):C.R2GC_193_38})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV9 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_189_13,(0,0,1):C.R2GC_189_14,(0,0,2):C.R2GC_189_15,(0,0,3):C.R2GC_189_16})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.bp] ], [ [P.t] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,1):C.R2GC_199_58,(0,0,0):C.R2GC_199_59,(0,0,2):C.R2GC_199_60})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.bp] ], [ [P.t] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,1):C.R2GC_198_55,(0,0,0):C.R2GC_198_56,(0,0,2):C.R2GC_198_57})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_197_47,(0,0,1):C.R2GC_197_48,(0,0,3):C.R2GC_197_49,(0,0,4):C.R2GC_197_50,(0,0,6):C.R2GC_197_51,(0,0,7):C.R2GC_197_52,(0,0,2):C.R2GC_197_53,(0,0,5):C.R2GC_197_54})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus__, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ] ],
                 couplings = {(0,0,3):C.R2GC_203_73,(0,0,4):C.R2GC_203_74,(0,0,5):C.R2GC_203_75,(0,0,0):C.R2GC_203_76,(0,0,1):C.R2GC_203_77,(0,0,2):C.R2GC_203_78,(0,0,7):C.R2GC_203_79,(0,0,6):C.R2GC_203_80})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus____minus__, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.x] ], [ [P.b, P.x] ], [ [P.tp, P.y] ], [ [P.t, P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_202_69,(0,0,0):C.R2GC_202_70,(0,0,3):C.R2GC_202_71,(0,0,2):C.R2GC_202_72})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_263_57,(0,1,0):C.UVGC_264_58})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_289_109})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_293_113,(0,1,0):C.UVGC_296_120})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_315_163,(0,1,0):C.UVGC_316_164})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_343_253,(0,1,0):C.UVGC_344_254})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,1):C.UVGC_333_209,(0,1,0):C.UVGC_333_210,(0,1,4):C.UVGC_333_211,(0,1,5):C.UVGC_333_212,(0,1,6):C.UVGC_333_213,(0,1,7):C.UVGC_333_214,(0,2,2):C.UVGC_205_1,(0,0,3):C.UVGC_206_2})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(2,0,3):C.UVGC_219_11,(2,0,4):C.UVGC_219_10,(0,0,3):C.UVGC_219_11,(0,0,4):C.UVGC_219_10,(4,0,3):C.UVGC_218_8,(4,0,4):C.UVGC_218_9,(3,0,3):C.UVGC_218_8,(3,0,4):C.UVGC_218_9,(8,0,3):C.UVGC_219_10,(8,0,4):C.UVGC_219_11,(6,0,2):C.UVGC_338_240,(6,0,0):C.UVGC_338_241,(6,0,3):C.UVGC_339_248,(6,0,4):C.UVGC_339_249,(6,0,5):C.UVGC_338_244,(6,0,6):C.UVGC_338_245,(6,0,7):C.UVGC_338_246,(6,0,8):C.UVGC_338_247,(7,0,2):C.UVGC_338_240,(7,0,0):C.UVGC_338_241,(7,0,3):C.UVGC_338_242,(7,0,4):C.UVGC_338_243,(7,0,5):C.UVGC_338_244,(7,0,6):C.UVGC_338_245,(7,0,7):C.UVGC_338_246,(7,0,8):C.UVGC_338_247,(5,0,3):C.UVGC_218_8,(5,0,4):C.UVGC_218_9,(1,0,3):C.UVGC_218_8,(1,0,4):C.UVGC_218_9,(11,3,3):C.UVGC_222_14,(11,3,4):C.UVGC_222_15,(10,3,3):C.UVGC_222_14,(10,3,4):C.UVGC_222_15,(9,3,3):C.UVGC_221_12,(9,3,4):C.UVGC_221_13,(0,1,3):C.UVGC_219_11,(0,1,4):C.UVGC_219_10,(2,1,3):C.UVGC_219_11,(2,1,4):C.UVGC_219_10,(5,1,3):C.UVGC_218_8,(5,1,4):C.UVGC_218_9,(1,1,3):C.UVGC_218_8,(1,1,4):C.UVGC_218_9,(7,1,1):C.UVGC_223_16,(7,1,3):C.UVGC_224_18,(7,1,4):C.UVGC_224_19,(4,1,3):C.UVGC_218_8,(4,1,4):C.UVGC_218_9,(3,1,3):C.UVGC_218_8,(3,1,4):C.UVGC_218_9,(8,1,2):C.UVGC_337_232,(8,1,0):C.UVGC_337_233,(8,1,3):C.UVGC_337_234,(8,1,4):C.UVGC_337_235,(8,1,5):C.UVGC_337_236,(8,1,6):C.UVGC_337_237,(8,1,7):C.UVGC_337_238,(8,1,8):C.UVGC_337_239,(6,1,0):C.UVGC_335_223,(6,1,3):C.UVGC_335_224,(6,1,4):C.UVGC_335_225,(6,1,5):C.UVGC_335_226,(6,1,6):C.UVGC_335_227,(6,1,7):C.UVGC_335_228,(6,1,8):C.UVGC_335_229,(0,2,3):C.UVGC_219_11,(0,2,4):C.UVGC_219_10,(2,2,3):C.UVGC_219_11,(2,2,4):C.UVGC_219_10,(5,2,3):C.UVGC_218_8,(5,2,4):C.UVGC_218_9,(1,2,3):C.UVGC_218_8,(1,2,4):C.UVGC_218_9,(7,2,0):C.UVGC_335_223,(7,2,3):C.UVGC_336_230,(7,2,4):C.UVGC_336_231,(7,2,5):C.UVGC_335_226,(7,2,6):C.UVGC_335_227,(7,2,7):C.UVGC_335_228,(7,2,8):C.UVGC_335_229,(4,2,3):C.UVGC_218_8,(4,2,4):C.UVGC_218_9,(3,2,3):C.UVGC_218_8,(3,2,4):C.UVGC_218_9,(8,2,2):C.UVGC_334_215,(8,2,0):C.UVGC_334_216,(8,2,3):C.UVGC_334_217,(8,2,4):C.UVGC_334_218,(8,2,5):C.UVGC_334_219,(8,2,6):C.UVGC_334_220,(8,2,7):C.UVGC_334_221,(8,2,8):C.UVGC_334_222,(6,2,1):C.UVGC_223_16,(6,2,3):C.UVGC_223_17,(6,2,4):C.UVGC_221_12})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_225_20,(0,1,0):C.UVGC_259_49})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_232_33,(0,1,0):C.UVGC_291_111})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_248_34,(0,1,0):C.UVGC_313_161,(0,2,0):C.UVGC_313_161})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_250_35,(0,1,0):C.UVGC_341_251,(0,2,0):C.UVGC_341_251})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_228_31,(0,1,0):C.UVGC_229_32})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_276_78,(0,1,0):C.UVGC_275_77})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_262_54,(0,0,2):C.UVGC_262_55,(0,0,0):C.UVGC_262_56,(0,1,1):C.UVGC_261_51,(0,1,2):C.UVGC_261_52,(0,1,0):C.UVGC_261_53})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_302_136,(0,0,1):C.UVGC_302_137,(0,0,2):C.UVGC_302_138,(0,1,0):C.UVGC_301_133,(0,1,1):C.UVGC_301_134,(0,1,2):C.UVGC_301_135})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_266_62,(0,0,2):C.UVGC_266_63,(0,0,0):C.UVGC_266_64,(0,1,1):C.UVGC_265_59,(0,1,2):C.UVGC_265_60,(0,1,0):C.UVGC_265_61})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_295_117,(0,0,1):C.UVGC_295_118,(0,0,2):C.UVGC_295_119,(0,1,0):C.UVGC_294_114,(0,1,1):C.UVGC_294_115,(0,1,2):C.UVGC_294_116})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_346_258,(0,0,2):C.UVGC_346_259,(0,0,1):C.UVGC_346_260,(0,1,0):C.UVGC_345_255,(0,1,2):C.UVGC_345_256,(0,1,1):C.UVGC_345_257})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_298_124,(0,0,2):C.UVGC_298_125,(0,0,1):C.UVGC_298_126,(0,1,0):C.UVGC_297_121,(0,1,2):C.UVGC_297_122,(0,1,1):C.UVGC_297_123})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_318_168,(0,0,2):C.UVGC_318_169,(0,0,1):C.UVGC_318_170,(0,1,0):C.UVGC_317_165,(0,1,2):C.UVGC_317_166,(0,1,1):C.UVGC_317_167})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_278_82,(0,0,2):C.UVGC_278_83,(0,0,1):C.UVGC_278_84,(0,1,0):C.UVGC_277_79,(0,1,2):C.UVGC_277_80,(0,1,1):C.UVGC_277_81})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_280_88,(0,0,2):C.UVGC_280_89,(0,0,1):C.UVGC_280_90,(0,1,0):C.UVGC_279_85,(0,1,2):C.UVGC_279_86,(0,1,1):C.UVGC_279_87})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_300_130,(0,0,2):C.UVGC_300_131,(0,0,1):C.UVGC_300_132,(0,1,0):C.UVGC_299_127,(0,1,2):C.UVGC_299_128,(0,1,1):C.UVGC_299_129})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_320_174,(0,0,2):C.UVGC_320_175,(0,0,1):C.UVGC_320_176,(0,1,0):C.UVGC_319_171,(0,1,2):C.UVGC_319_172,(0,1,1):C.UVGC_319_173})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_348_264,(0,0,2):C.UVGC_348_265,(0,0,1):C.UVGC_348_266,(0,1,0):C.UVGC_347_261,(0,1,2):C.UVGC_347_262,(0,1,1):C.UVGC_347_263})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_322_180,(0,0,2):C.UVGC_322_181,(0,0,1):C.UVGC_322_182,(0,1,0):C.UVGC_321_177,(0,1,2):C.UVGC_321_178,(0,1,1):C.UVGC_321_179})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_350_270,(0,0,2):C.UVGC_350_271,(0,0,1):C.UVGC_350_272,(0,1,0):C.UVGC_349_267,(0,1,2):C.UVGC_349_268,(0,1,1):C.UVGC_349_269})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_324_186,(0,0,2):C.UVGC_324_187,(0,0,1):C.UVGC_324_188,(0,1,0):C.UVGC_323_183,(0,1,2):C.UVGC_323_184,(0,1,1):C.UVGC_323_185})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_352_276,(0,0,2):C.UVGC_352_277,(0,0,1):C.UVGC_352_278,(0,1,0):C.UVGC_351_273,(0,1,2):C.UVGC_351_274,(0,1,1):C.UVGC_351_275})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_345_255,(0,0,2):C.UVGC_345_256,(0,0,1):C.UVGC_345_257,(0,1,0):C.UVGC_346_258,(0,1,2):C.UVGC_346_259,(0,1,1):C.UVGC_346_260})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_297_121,(0,0,2):C.UVGC_297_122,(0,0,1):C.UVGC_297_123,(0,1,0):C.UVGC_298_124,(0,1,2):C.UVGC_298_125,(0,1,1):C.UVGC_298_126})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_317_165,(0,0,2):C.UVGC_317_166,(0,0,1):C.UVGC_317_167,(0,1,0):C.UVGC_318_168,(0,1,2):C.UVGC_318_169,(0,1,1):C.UVGC_318_170})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_321_177,(0,0,2):C.UVGC_321_178,(0,0,1):C.UVGC_321_179,(0,1,0):C.UVGC_322_180,(0,1,2):C.UVGC_322_181,(0,1,1):C.UVGC_322_182})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_349_267,(0,0,2):C.UVGC_349_268,(0,0,1):C.UVGC_349_269,(0,1,0):C.UVGC_350_270,(0,1,2):C.UVGC_350_271,(0,1,1):C.UVGC_350_272})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_265_59,(0,0,2):C.UVGC_265_60,(0,0,0):C.UVGC_265_61,(0,1,1):C.UVGC_266_62,(0,1,2):C.UVGC_266_63,(0,1,0):C.UVGC_266_64})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_294_114,(0,0,1):C.UVGC_294_115,(0,0,2):C.UVGC_294_116,(0,1,0):C.UVGC_295_117,(0,1,1):C.UVGC_295_118,(0,1,2):C.UVGC_295_119})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_277_79,(0,0,2):C.UVGC_277_80,(0,0,1):C.UVGC_277_81,(0,1,0):C.UVGC_278_82,(0,1,2):C.UVGC_278_83,(0,1,1):C.UVGC_278_84})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_279_85,(0,0,2):C.UVGC_279_86,(0,0,1):C.UVGC_279_87,(0,1,0):C.UVGC_280_88,(0,1,2):C.UVGC_280_89,(0,1,1):C.UVGC_280_90})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_299_127,(0,0,2):C.UVGC_299_128,(0,0,1):C.UVGC_299_129,(0,1,0):C.UVGC_300_130,(0,1,2):C.UVGC_300_131,(0,1,1):C.UVGC_300_132})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_319_171,(0,0,2):C.UVGC_319_172,(0,0,1):C.UVGC_319_173,(0,1,0):C.UVGC_320_174,(0,1,2):C.UVGC_320_175,(0,1,1):C.UVGC_320_176})

V_172 = CTVertex(name = 'V_172',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_347_261,(0,0,2):C.UVGC_347_262,(0,0,1):C.UVGC_347_263,(0,1,0):C.UVGC_348_264,(0,1,2):C.UVGC_348_265,(0,1,1):C.UVGC_348_266})

V_173 = CTVertex(name = 'V_173',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_323_183,(0,0,2):C.UVGC_323_184,(0,0,1):C.UVGC_323_185,(0,1,0):C.UVGC_324_186,(0,1,2):C.UVGC_324_187,(0,1,1):C.UVGC_324_188})

V_174 = CTVertex(name = 'V_174',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_351_273,(0,0,2):C.UVGC_351_274,(0,0,1):C.UVGC_351_275,(0,1,0):C.UVGC_352_276,(0,1,2):C.UVGC_352_277,(0,1,1):C.UVGC_352_278})

V_175 = CTVertex(name = 'V_175',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_261_51,(0,0,2):C.UVGC_261_52,(0,0,0):C.UVGC_261_53,(0,1,1):C.UVGC_262_54,(0,1,2):C.UVGC_262_55,(0,1,0):C.UVGC_262_56})

V_176 = CTVertex(name = 'V_176',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_301_133,(0,0,1):C.UVGC_301_134,(0,0,2):C.UVGC_301_135,(0,1,0):C.UVGC_302_136,(0,1,1):C.UVGC_302_137,(0,1,2):C.UVGC_302_138})

V_177 = CTVertex(name = 'V_177',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,2):C.UVGC_226_23,(0,1,3):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,4):C.UVGC_292_112})

V_178 = CTVertex(name = 'V_178',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.bp, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,3):C.UVGC_226_23,(0,1,4):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,2):C.UVGC_260_50})

V_179 = CTVertex(name = 'V_179',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.x] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,2):C.UVGC_226_23,(0,1,3):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,4):C.UVGC_314_162})

V_180 = CTVertex(name = 'V_180',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.y] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,2):C.UVGC_226_23,(0,1,3):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,4):C.UVGC_342_252})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_304_140,(0,0,2):C.UVGC_304_141,(0,0,1):C.UVGC_304_142,(0,1,0):C.UVGC_306_146,(0,1,2):C.UVGC_306_147,(0,1,1):C.UVGC_306_148})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_328_196,(0,0,2):C.UVGC_328_197,(0,0,1):C.UVGC_328_198,(0,1,0):C.UVGC_329_199,(0,1,2):C.UVGC_329_200,(0,1,1):C.UVGC_329_201})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_285_101,(0,0,2):C.UVGC_285_102,(0,0,1):C.UVGC_285_103,(0,1,0):C.UVGC_286_104,(0,1,2):C.UVGC_286_105,(0,1,1):C.UVGC_286_106})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_356_286,(0,0,2):C.UVGC_356_287,(0,0,1):C.UVGC_356_288,(0,1,0):C.UVGC_357_289,(0,1,2):C.UVGC_357_290,(0,1,1):C.UVGC_357_291})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_268_66,(0,0,2):C.UVGC_268_67,(0,0,0):C.UVGC_268_68,(0,1,1):C.UVGC_269_69,(0,1,2):C.UVGC_269_70,(0,1,0):C.UVGC_269_71})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_305_143,(0,0,1):C.UVGC_305_144,(0,0,2):C.UVGC_305_145,(0,1,0):C.UVGC_307_149,(0,1,1):C.UVGC_307_150,(0,1,2):C.UVGC_307_151})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_354_280,(0,0,2):C.UVGC_354_281,(0,0,1):C.UVGC_354_282,(0,1,0):C.UVGC_355_283,(0,1,2):C.UVGC_355_284,(0,1,1):C.UVGC_355_285})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_308_152,(0,0,2):C.UVGC_308_153,(0,0,1):C.UVGC_308_154,(0,1,0):C.UVGC_309_155,(0,1,2):C.UVGC_309_156,(0,1,1):C.UVGC_309_157})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_326_190,(0,0,2):C.UVGC_326_191,(0,0,1):C.UVGC_326_192,(0,1,0):C.UVGC_327_193,(0,1,2):C.UVGC_327_194,(0,1,1):C.UVGC_327_195})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_354_280,(0,0,2):C.UVGC_354_281,(0,0,1):C.UVGC_354_282,(0,1,0):C.UVGC_355_283,(0,1,2):C.UVGC_355_284,(0,1,1):C.UVGC_355_285})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_308_152,(0,0,2):C.UVGC_308_153,(0,0,1):C.UVGC_308_154,(0,1,0):C.UVGC_309_155,(0,1,2):C.UVGC_309_156,(0,1,1):C.UVGC_309_157})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_326_190,(0,0,2):C.UVGC_326_191,(0,0,1):C.UVGC_326_192,(0,1,0):C.UVGC_327_193,(0,1,2):C.UVGC_327_194,(0,1,1):C.UVGC_327_195})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_304_140,(0,0,2):C.UVGC_304_141,(0,0,1):C.UVGC_304_142,(0,1,0):C.UVGC_306_146,(0,1,2):C.UVGC_306_147,(0,1,1):C.UVGC_306_148})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_328_196,(0,0,2):C.UVGC_328_197,(0,0,1):C.UVGC_328_198,(0,1,0):C.UVGC_329_199,(0,1,2):C.UVGC_329_200,(0,1,1):C.UVGC_329_201})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_285_101,(0,0,2):C.UVGC_285_102,(0,0,1):C.UVGC_285_103,(0,1,0):C.UVGC_286_104,(0,1,2):C.UVGC_286_105,(0,1,1):C.UVGC_286_106})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_356_286,(0,0,2):C.UVGC_356_287,(0,0,1):C.UVGC_356_288,(0,1,0):C.UVGC_357_289,(0,1,2):C.UVGC_357_290,(0,1,1):C.UVGC_357_291})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_270_72,(0,1,0):C.UVGC_271_73})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_310_158,(0,1,0):C.UVGC_311_159})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_330_202,(0,1,0):C.UVGC_331_203})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_358_292,(0,1,0):C.UVGC_359_293})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_268_66,(0,0,2):C.UVGC_268_67,(0,0,0):C.UVGC_268_68,(0,1,1):C.UVGC_269_69,(0,1,2):C.UVGC_269_70,(0,1,0):C.UVGC_269_71})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_305_143,(0,0,1):C.UVGC_305_144,(0,0,2):C.UVGC_305_145,(0,1,0):C.UVGC_307_149,(0,1,1):C.UVGC_307_150,(0,1,2):C.UVGC_307_151})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_232_33,(0,1,0):C.UVGC_210_5,(0,2,0):C.UVGC_210_5})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_232_33,(0,1,0):C.UVGC_210_5,(0,2,0):C.UVGC_210_5})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_232_33,(0,1,0):C.UVGC_273_75,(0,2,0):C.UVGC_273_75})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_225_20,(0,1,0):C.UVGC_208_4,(0,2,0):C.UVGC_208_4})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_225_20,(0,1,0):C.UVGC_208_4,(0,2,0):C.UVGC_208_4})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_225_20,(0,1,0):C.UVGC_208_4,(0,2,0):C.UVGC_208_4})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,2):C.UVGC_226_23,(0,1,3):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,4):C.UVGC_226_29,(0,2,1):C.UVGC_226_21,(0,2,0):C.UVGC_226_22,(0,2,2):C.UVGC_226_23,(0,2,3):C.UVGC_226_24,(0,2,5):C.UVGC_226_25,(0,2,6):C.UVGC_226_26,(0,2,7):C.UVGC_226_27,(0,2,8):C.UVGC_226_28,(0,2,4):C.UVGC_226_29})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,3):C.UVGC_226_23,(0,1,4):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,2):C.UVGC_226_29,(0,2,1):C.UVGC_226_21,(0,2,0):C.UVGC_226_22,(0,2,3):C.UVGC_226_23,(0,2,4):C.UVGC_226_24,(0,2,5):C.UVGC_226_25,(0,2,6):C.UVGC_226_26,(0,2,7):C.UVGC_226_27,(0,2,8):C.UVGC_226_28,(0,2,2):C.UVGC_226_29})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,2):C.UVGC_226_23,(0,1,3):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,4):C.UVGC_274_76,(0,2,1):C.UVGC_226_21,(0,2,0):C.UVGC_226_22,(0,2,2):C.UVGC_226_23,(0,2,3):C.UVGC_226_24,(0,2,5):C.UVGC_226_25,(0,2,6):C.UVGC_226_26,(0,2,7):C.UVGC_226_27,(0,2,8):C.UVGC_226_28,(0,2,4):C.UVGC_274_76})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,3):C.UVGC_226_23,(0,1,4):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,2):C.UVGC_226_29,(0,2,1):C.UVGC_226_21,(0,2,0):C.UVGC_226_22,(0,2,3):C.UVGC_226_23,(0,2,4):C.UVGC_226_24,(0,2,5):C.UVGC_226_25,(0,2,6):C.UVGC_226_26,(0,2,7):C.UVGC_226_27,(0,2,8):C.UVGC_226_28,(0,2,2):C.UVGC_226_29})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,2):C.UVGC_226_23,(0,1,3):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,4):C.UVGC_226_29,(0,2,1):C.UVGC_226_21,(0,2,0):C.UVGC_226_22,(0,2,2):C.UVGC_226_23,(0,2,3):C.UVGC_226_24,(0,2,5):C.UVGC_226_25,(0,2,6):C.UVGC_226_26,(0,2,7):C.UVGC_226_27,(0,2,8):C.UVGC_226_28,(0,2,4):C.UVGC_226_29})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_227_30,(0,1,1):C.UVGC_226_21,(0,1,0):C.UVGC_226_22,(0,1,3):C.UVGC_226_23,(0,1,4):C.UVGC_226_24,(0,1,5):C.UVGC_226_25,(0,1,6):C.UVGC_226_26,(0,1,7):C.UVGC_226_27,(0,1,8):C.UVGC_226_28,(0,1,2):C.UVGC_226_29,(0,2,1):C.UVGC_226_21,(0,2,0):C.UVGC_226_22,(0,2,3):C.UVGC_226_23,(0,2,4):C.UVGC_226_24,(0,2,5):C.UVGC_226_25,(0,2,6):C.UVGC_226_26,(0,2,7):C.UVGC_226_27,(0,2,8):C.UVGC_226_28,(0,2,2):C.UVGC_226_29})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_256_44,(0,0,1):C.UVGC_256_45})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_257_46,(0,0,1):C.UVGC_257_47})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_255_42,(0,0,1):C.UVGC_255_43})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_253_38,(0,0,0):C.UVGC_253_39})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_254_40,(0,0,1):C.UVGC_254_41})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_252_36,(0,0,0):C.UVGC_252_37})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_282_92,(0,0,2):C.UVGC_282_93,(0,0,1):C.UVGC_282_94})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_283_95,(0,0,2):C.UVGC_283_96,(0,0,1):C.UVGC_283_97})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_284_98,(0,0,2):C.UVGC_284_99,(0,0,1):C.UVGC_284_100})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_256_44,(0,0,1):C.UVGC_256_45})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_253_38,(0,0,0):C.UVGC_253_39})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_282_92,(0,0,2):C.UVGC_282_93,(0,0,1):C.UVGC_282_94})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_257_46,(0,0,1):C.UVGC_257_47})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_254_40,(0,0,1):C.UVGC_254_41})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_283_95,(0,0,2):C.UVGC_283_96,(0,0,1):C.UVGC_283_97})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_255_42,(0,0,1):C.UVGC_255_43})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_252_36,(0,0,0):C.UVGC_252_37})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_284_98,(0,0,2):C.UVGC_284_99,(0,0,1):C.UVGC_284_100})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_287_107,(0,1,0):C.UVGC_288_108})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_207_3})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_207_3})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_281_91,(0,1,0):C.UVGC_272_74})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_207_3})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_207_3})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_207_3})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_325_189,(0,1,0):C.UVGC_312_160})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_303_139,(0,1,0):C.UVGC_290_110})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_267_65,(0,1,0):C.UVGC_258_48})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_353_279,(0,1,0):C.UVGC_340_250})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,0):C.UVGC_332_204,(0,1,3):C.UVGC_332_205,(0,1,4):C.UVGC_332_206,(0,1,5):C.UVGC_332_207,(0,1,6):C.UVGC_332_208,(0,0,1):C.UVGC_217_6,(0,0,2):C.UVGC_217_7})

