# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Wed 27 Jul 2022 19:05:58


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
               couplings = {(0,0,0):C.R2GC_359_179,(0,1,0):C.R2GC_360_180})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_401_216})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_405_217,(0,1,0):C.R2GC_412_224})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.x__tilde__, P.x, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.x] ] ],
               couplings = {(0,0,0):C.R2GC_447_256,(0,1,0):C.R2GC_448_257})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.y__tilde__, P.y, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.y] ] ],
               couplings = {(0,0,0):C.R2GC_488_297,(0,1,0):C.R2GC_489_298})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_478_288,(0,0,1):C.R2GC_478_289})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_295_138,(2,1,1):C.R2GC_295_139,(0,1,0):C.R2GC_295_138,(0,1,1):C.R2GC_295_139,(4,1,0):C.R2GC_293_134,(4,1,1):C.R2GC_293_135,(3,1,0):C.R2GC_293_134,(3,1,1):C.R2GC_293_135,(8,1,0):C.R2GC_294_136,(8,1,1):C.R2GC_294_137,(6,1,0):C.R2GC_298_143,(6,1,1):C.R2GC_484_296,(7,1,0):C.R2GC_299_145,(7,1,1):C.R2GC_483_295,(5,1,0):C.R2GC_293_134,(5,1,1):C.R2GC_293_135,(1,1,0):C.R2GC_293_134,(1,1,1):C.R2GC_293_135,(11,0,0):C.R2GC_297_141,(11,0,1):C.R2GC_297_142,(10,0,0):C.R2GC_297_141,(10,0,1):C.R2GC_297_142,(9,0,1):C.R2GC_296_140,(0,2,0):C.R2GC_295_138,(0,2,1):C.R2GC_295_139,(2,2,0):C.R2GC_295_138,(2,2,1):C.R2GC_295_139,(5,2,0):C.R2GC_293_134,(5,2,1):C.R2GC_293_135,(1,2,0):C.R2GC_293_134,(1,2,1):C.R2GC_293_135,(7,2,0):C.R2GC_299_145,(7,2,1):C.R2GC_299_146,(4,2,0):C.R2GC_293_134,(4,2,1):C.R2GC_293_135,(3,2,0):C.R2GC_293_134,(3,2,1):C.R2GC_293_135,(8,2,0):C.R2GC_294_136,(8,2,1):C.R2GC_482_294,(6,2,0):C.R2GC_480_291,(6,2,1):C.R2GC_480_292,(0,3,0):C.R2GC_295_138,(0,3,1):C.R2GC_295_139,(2,3,0):C.R2GC_295_138,(2,3,1):C.R2GC_295_139,(5,3,0):C.R2GC_293_134,(5,3,1):C.R2GC_293_135,(1,3,0):C.R2GC_293_134,(1,3,1):C.R2GC_293_135,(7,3,0):C.R2GC_481_293,(7,3,1):C.R2GC_295_139,(4,3,0):C.R2GC_293_134,(4,3,1):C.R2GC_293_135,(3,3,0):C.R2GC_293_134,(3,3,1):C.R2GC_293_135,(8,3,0):C.R2GC_294_136,(8,3,1):C.R2GC_479_290,(6,3,0):C.R2GC_298_143,(6,3,1):C.R2GC_298_144})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_301_148})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_309_152})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_336_161})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_338_162})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_318_155,(0,1,0):C.R2GC_319_156})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_324_157,(0,1,0):C.R2GC_325_158})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_304_150,(0,1,0):C.R2GC_305_151})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_334_159,(0,1,0):C.R2GC_335_160})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_312_153,(0,1,0):C.R2GC_313_154})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_388_205,(0,1,0):C.R2GC_387_204})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_356_176,(0,1,0):C.R2GC_353_173})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_357_177,(0,1,0):C.R2GC_354_174})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_358_178,(0,1,0):C.R2GC_355_175})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_424_236,(0,1,0):C.R2GC_421_233})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_425_237,(0,1,0):C.R2GC_422_234})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_426_238,(0,1,0):C.R2GC_423_235})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_364_184,(0,1,0):C.R2GC_361_181})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_365_185,(0,1,0):C.R2GC_362_182})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_366_186,(0,1,0):C.R2GC_363_183})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_409_221,(0,1,0):C.R2GC_406_218})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_410_222,(0,1,0):C.R2GC_407_219})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_411_223,(0,1,0):C.R2GC_408_220})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_491_300,(0,1,0):C.R2GC_490_299})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_414_226,(0,1,0):C.R2GC_413_225})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_450_259,(0,1,0):C.R2GC_449_258})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_369_189,(0,1,0):C.R2GC_367_187})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_370_190,(0,1,0):C.R2GC_368_188})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_390_207,(0,1,0):C.R2GC_389_206})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_347_170,(0,1,0):C.R2GC_346_169})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_343_166,(0,1,0):C.R2GC_342_165})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_392_209,(0,1,0):C.R2GC_391_208})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_418_230,(0,1,0):C.R2GC_415_227})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_419_231,(0,1,0):C.R2GC_416_228})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_420_232,(0,1,0):C.R2GC_417_229})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_454_263,(0,1,0):C.R2GC_451_260})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_455_264,(0,1,0):C.R2GC_452_261})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_456_265,(0,1,0):C.R2GC_453_262})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_495_304,(0,1,0):C.R2GC_492_301})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_496_305,(0,1,0):C.R2GC_493_302})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_497_306,(0,1,0):C.R2GC_494_303})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_458_267,(0,1,0):C.R2GC_457_266})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_499_308,(0,1,0):C.R2GC_498_307})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_462_271,(0,1,0):C.R2GC_459_268})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_463_272,(0,1,0):C.R2GC_460_269})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_464_273,(0,1,0):C.R2GC_461_270})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_503_312,(0,1,0):C.R2GC_500_309})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_504_313,(0,1,0):C.R2GC_501_310})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_505_314,(0,1,0):C.R2GC_502_311})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_490_299,(0,1,0):C.R2GC_491_300})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_413_225,(0,1,0):C.R2GC_414_226})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_449_258,(0,1,0):C.R2GC_450_259})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_457_266,(0,1,0):C.R2GC_458_267})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_498_307,(0,1,0):C.R2GC_499_308})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_361_181,(0,1,0):C.R2GC_364_184})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_362_182,(0,1,0):C.R2GC_365_185})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_363_183,(0,1,0):C.R2GC_366_186})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_406_218,(0,1,0):C.R2GC_409_221})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_407_219,(0,1,0):C.R2GC_410_222})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_408_220,(0,1,0):C.R2GC_411_223})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_367_187,(0,1,0):C.R2GC_369_189})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_368_188,(0,1,0):C.R2GC_370_190})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_389_206,(0,1,0):C.R2GC_390_207})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_346_169,(0,1,0):C.R2GC_347_170})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_342_165,(0,1,0):C.R2GC_343_166})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_391_208,(0,1,0):C.R2GC_392_209})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_415_227,(0,1,0):C.R2GC_418_230})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_416_228,(0,1,0):C.R2GC_419_231})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_417_229,(0,1,0):C.R2GC_420_232})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_451_260,(0,1,0):C.R2GC_454_263})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_452_261,(0,1,0):C.R2GC_455_264})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_453_262,(0,1,0):C.R2GC_456_265})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_492_301,(0,1,0):C.R2GC_495_304})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_493_302,(0,1,0):C.R2GC_496_305})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_494_303,(0,1,0):C.R2GC_497_306})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_459_268,(0,1,0):C.R2GC_462_271})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_460_269,(0,1,0):C.R2GC_463_272})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_461_270,(0,1,0):C.R2GC_464_273})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_500_309,(0,1,0):C.R2GC_503_312})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_501_310,(0,1,0):C.R2GC_504_313})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_502_311,(0,1,0):C.R2GC_505_314})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_353_173,(0,1,0):C.R2GC_356_176})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_354_174,(0,1,0):C.R2GC_357_177})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_355_175,(0,1,0):C.R2GC_358_178})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_421_233,(0,1,0):C.R2GC_424_236})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_422_234,(0,1,0):C.R2GC_425_237})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_423_235,(0,1,0):C.R2GC_426_238})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_303_149})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_303_149})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_303_149})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_303_149})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_428_240,(0,1,0):C.R2GC_434_246})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_429_241,(0,1,0):C.R2GC_435_247})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_430_242,(0,1,0):C.R2GC_436_248})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_468_277,(0,1,0):C.R2GC_471_280})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_469_278,(0,1,0):C.R2GC_472_281})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_470_279,(0,1,0):C.R2GC_473_282})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_372_192,(0,1,0):C.R2GC_377_197})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_373_193,(0,1,0):C.R2GC_378_198})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_397_214,(0,1,0):C.R2GC_398_215})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_509_318,(0,1,0):C.R2GC_512_321})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_510_319,(0,1,0):C.R2GC_513_322})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_511_320,(0,1,0):C.R2GC_514_323})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_374_194,(0,1,0):C.R2GC_379_199})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_375_195,(0,1,0):C.R2GC_380_200})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_376_196,(0,1,0):C.R2GC_381_201})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_431_243,(0,1,0):C.R2GC_437_249})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_432_244,(0,1,0):C.R2GC_438_250})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_433_245,(0,1,0):C.R2GC_439_251})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_507_316,(0,1,0):C.R2GC_508_317})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_440_252,(0,1,0):C.R2GC_441_253})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_466_275,(0,1,0):C.R2GC_467_276})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_507_316,(0,1,0):C.R2GC_508_317})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_440_252,(0,1,0):C.R2GC_441_253})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_466_275,(0,1,0):C.R2GC_467_276})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_428_240,(0,1,0):C.R2GC_434_246})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_429_241,(0,1,0):C.R2GC_435_247})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_430_242,(0,1,0):C.R2GC_436_248})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_468_277,(0,1,0):C.R2GC_471_280})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_469_278,(0,1,0):C.R2GC_472_281})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_470_279,(0,1,0):C.R2GC_473_282})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_372_192,(0,1,0):C.R2GC_377_197})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_373_193,(0,1,0):C.R2GC_378_198})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_397_214,(0,1,0):C.R2GC_398_215})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_509_318,(0,1,0):C.R2GC_512_321})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_510_319,(0,1,0):C.R2GC_513_322})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_511_320,(0,1,0):C.R2GC_514_323})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_382_202,(0,1,0):C.R2GC_383_203})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_442_254,(0,1,0):C.R2GC_443_255})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_474_283,(0,1,0):C.R2GC_475_284})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_515_324,(0,1,0):C.R2GC_516_325})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_374_194,(0,1,0):C.R2GC_379_199})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_375_195,(0,1,0):C.R2GC_380_200})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_376_196,(0,1,0):C.R2GC_381_201})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_431_243,(0,1,0):C.R2GC_437_249})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_432_244,(0,1,0):C.R2GC_438_250})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_433_245,(0,1,0):C.R2GC_439_251})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_309_152})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_309_152})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_309_152})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_301_148})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_301_148})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_301_148})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_303_149})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_303_149})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_303_149})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_303_149})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_303_149})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_303_149})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_348_171})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_349_172})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_345_168})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_341_164})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_344_167})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_340_163})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_394_211})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_395_212})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_396_213})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_348_171})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_341_164})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_394_211})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_349_172})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_344_167})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_395_212})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_345_168})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_340_163})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_396_213})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_270_41,(0,1,0):C.R2GC_257_2})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_270_41,(0,1,0):C.R2GC_257_2})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_270_41,(0,1,0):C.R2GC_257_2})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_269_40,(0,1,0):C.R2GC_256_1})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_269_40,(0,1,0):C.R2GC_256_1})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_269_40,(0,1,0):C.R2GC_256_1})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_300_147})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_300_147})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_393_210,(0,2,0):C.R2GC_393_210,(0,1,0):C.R2GC_300_147,(0,3,0):C.R2GC_300_147})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_300_147})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_300_147})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_300_147})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_465_274,(0,2,0):C.R2GC_465_274,(0,1,0):C.R2GC_300_147,(0,3,0):C.R2GC_300_147})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_427_239,(0,2,0):C.R2GC_427_239,(0,1,0):C.R2GC_300_147,(0,3,0):C.R2GC_300_147})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_371_191,(0,2,0):C.R2GC_371_191,(0,1,0):C.R2GC_300_147,(0,3,0):C.R2GC_300_147})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_506_315,(0,2,0):C.R2GC_506_315,(0,1,0):C.R2GC_300_147,(0,3,0):C.R2GC_300_147})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_477_287,(0,1,0):C.R2GC_265_17,(0,1,3):C.R2GC_265_18,(0,1,4):C.R2GC_265_19,(0,1,5):C.R2GC_265_20,(0,1,6):C.R2GC_265_21,(0,2,1):C.R2GC_476_285,(0,2,2):C.R2GC_476_286})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_261_3})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_264_12,(0,0,1):C.R2GC_264_13,(0,0,2):C.R2GC_264_14,(0,0,3):C.R2GC_264_15,(0,0,4):C.R2GC_264_16})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.u] ], [ [P.b, P.y] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.c, P.x] ], [ [P.d, P.t] ], [ [P.d, P.tp] ], [ [P.d, P.u] ], [ [P.d, P.y] ], [ [P.s, P.t] ], [ [P.s, P.tp] ], [ [P.s, P.u] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_280_110,(0,0,6):C.R2GC_280_111,(0,0,7):C.R2GC_280_112,(0,0,8):C.R2GC_280_113,(0,0,9):C.R2GC_280_114,(0,0,1):C.R2GC_280_115,(0,0,2):C.R2GC_280_116,(0,0,3):C.R2GC_280_117,(0,0,4):C.R2GC_280_118,(0,0,5):C.R2GC_280_119,(0,0,10):C.R2GC_280_120,(0,0,11):C.R2GC_280_121,(0,0,12):C.R2GC_280_122,(0,0,13):C.R2GC_280_123,(0,0,14):C.R2GC_280_124,(0,0,15):C.R2GC_280_125,(0,0,16):C.R2GC_280_126,(0,0,17):C.R2GC_280_127,(0,0,18):C.R2GC_280_128,(0,0,19):C.R2GC_280_129,(0,0,20):C.R2GC_280_130,(0,0,22):C.R2GC_280_131,(0,0,21):C.R2GC_280_132,(0,0,23):C.R2GC_280_133,(0,1,0):C.R2GC_280_110,(0,1,6):C.R2GC_280_111,(0,1,7):C.R2GC_280_112,(0,1,8):C.R2GC_280_113,(0,1,9):C.R2GC_280_114,(0,1,1):C.R2GC_280_115,(0,1,2):C.R2GC_280_116,(0,1,3):C.R2GC_280_117,(0,1,4):C.R2GC_280_118,(0,1,5):C.R2GC_280_119,(0,1,10):C.R2GC_280_120,(0,1,11):C.R2GC_280_121,(0,1,12):C.R2GC_280_122,(0,1,13):C.R2GC_280_123,(0,1,14):C.R2GC_280_124,(0,1,15):C.R2GC_280_125,(0,1,16):C.R2GC_280_126,(0,1,17):C.R2GC_280_127,(0,1,18):C.R2GC_280_128,(0,1,19):C.R2GC_280_129,(0,1,20):C.R2GC_280_130,(0,1,22):C.R2GC_280_131,(0,1,21):C.R2GC_280_132,(0,1,23):C.R2GC_280_133,(0,2,0):C.R2GC_280_110,(0,2,6):C.R2GC_280_111,(0,2,7):C.R2GC_280_112,(0,2,8):C.R2GC_280_113,(0,2,9):C.R2GC_280_114,(0,2,1):C.R2GC_280_115,(0,2,2):C.R2GC_280_116,(0,2,3):C.R2GC_280_117,(0,2,4):C.R2GC_280_118,(0,2,5):C.R2GC_280_119,(0,2,10):C.R2GC_280_120,(0,2,11):C.R2GC_280_121,(0,2,12):C.R2GC_280_122,(0,2,13):C.R2GC_280_123,(0,2,14):C.R2GC_280_124,(0,2,15):C.R2GC_280_125,(0,2,16):C.R2GC_280_126,(0,2,17):C.R2GC_280_127,(0,2,18):C.R2GC_280_128,(0,2,19):C.R2GC_280_129,(0,2,20):C.R2GC_280_130,(0,2,22):C.R2GC_280_131,(0,2,21):C.R2GC_280_132,(0,2,23):C.R2GC_280_133})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b, P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_277_72,(0,0,0):C.R2GC_277_73,(0,0,6):C.R2GC_277_74,(0,0,7):C.R2GC_277_75,(0,0,10):C.R2GC_277_76,(0,0,11):C.R2GC_277_77,(0,0,1):C.R2GC_277_78,(0,0,3):C.R2GC_277_79,(0,0,4):C.R2GC_277_80,(0,0,5):C.R2GC_277_81,(0,0,9):C.R2GC_277_82,(0,0,8):C.R2GC_277_83,(0,1,2):C.R2GC_277_72,(0,1,0):C.R2GC_277_73,(0,1,6):C.R2GC_277_74,(0,1,7):C.R2GC_277_75,(0,1,10):C.R2GC_277_76,(0,1,11):C.R2GC_277_77,(0,1,1):C.R2GC_277_78,(0,1,3):C.R2GC_277_79,(0,1,4):C.R2GC_277_80,(0,1,5):C.R2GC_277_81,(0,1,9):C.R2GC_277_82,(0,1,8):C.R2GC_277_83,(0,2,2):C.R2GC_277_72,(0,2,0):C.R2GC_277_73,(0,2,6):C.R2GC_277_74,(0,2,7):C.R2GC_277_75,(0,2,10):C.R2GC_277_76,(0,2,11):C.R2GC_277_77,(0,2,1):C.R2GC_277_78,(0,2,3):C.R2GC_277_79,(0,2,4):C.R2GC_277_80,(0,2,5):C.R2GC_277_81,(0,2,9):C.R2GC_277_82,(0,2,8):C.R2GC_277_83})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_266_22,(0,0,0):C.R2GC_266_23,(0,0,2):C.R2GC_266_24,(0,0,3):C.R2GC_266_25,(0,0,4):C.R2GC_266_26,(0,0,5):C.R2GC_266_27,(0,1,1):C.R2GC_266_22,(0,1,0):C.R2GC_266_23,(0,1,2):C.R2GC_266_24,(0,1,3):C.R2GC_266_25,(0,1,4):C.R2GC_266_26,(0,1,5):C.R2GC_266_27,(0,2,1):C.R2GC_266_22,(0,2,0):C.R2GC_266_23,(0,2,2):C.R2GC_266_24,(0,2,3):C.R2GC_266_25,(0,2,4):C.R2GC_266_26,(0,2,5):C.R2GC_266_27})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_262_4,(0,0,1):C.R2GC_262_5,(0,0,2):C.R2GC_262_6,(0,0,3):C.R2GC_262_7,(0,1,0):C.R2GC_262_4,(0,1,1):C.R2GC_262_5,(0,1,2):C.R2GC_262_6,(0,1,3):C.R2GC_262_7,(0,2,0):C.R2GC_262_4,(0,2,1):C.R2GC_262_5,(0,2,2):C.R2GC_262_6,(0,2,3):C.R2GC_262_7})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(1,0,1):C.R2GC_268_34,(1,0,0):C.R2GC_268_35,(1,0,2):C.R2GC_268_36,(1,0,3):C.R2GC_268_37,(1,0,4):C.R2GC_268_38,(1,0,5):C.R2GC_268_39,(0,1,1):C.R2GC_267_28,(0,1,0):C.R2GC_267_29,(0,1,2):C.R2GC_267_30,(0,1,3):C.R2GC_267_31,(0,1,4):C.R2GC_267_32,(0,1,5):C.R2GC_267_33,(0,2,1):C.R2GC_267_28,(0,2,0):C.R2GC_267_29,(0,2,2):C.R2GC_267_30,(0,2,3):C.R2GC_267_31,(0,2,4):C.R2GC_267_32,(0,2,5):C.R2GC_267_33,(0,3,1):C.R2GC_267_28,(0,3,0):C.R2GC_267_29,(0,3,2):C.R2GC_267_30,(0,3,3):C.R2GC_267_31,(0,3,4):C.R2GC_267_32,(0,3,5):C.R2GC_267_33})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_263_8,(0,0,1):C.R2GC_263_9,(0,0,2):C.R2GC_263_10,(0,0,3):C.R2GC_263_11,(0,1,0):C.R2GC_263_8,(0,1,1):C.R2GC_263_9,(0,1,2):C.R2GC_263_10,(0,1,3):C.R2GC_263_11,(0,2,0):C.R2GC_263_8,(0,2,1):C.R2GC_263_9,(0,2,2):C.R2GC_263_10,(0,2,3):C.R2GC_263_11})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,4):C.R2GC_276_65,(0,0,0):C.R2GC_276_66,(0,0,1):C.R2GC_276_67,(0,0,2):C.R2GC_276_68,(0,0,3):C.R2GC_276_69,(0,0,6):C.R2GC_276_70,(0,0,5):C.R2GC_276_71})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,4):C.R2GC_275_58,(0,0,0):C.R2GC_275_59,(0,0,1):C.R2GC_275_60,(0,0,2):C.R2GC_275_61,(0,0,3):C.R2GC_275_62,(0,0,6):C.R2GC_275_63,(0,0,5):C.R2GC_275_64})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c] ], [ [P.c, P.tp] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_274_42,(0,0,1):C.R2GC_274_43,(0,0,5):C.R2GC_274_44,(0,0,7):C.R2GC_274_45,(0,0,8):C.R2GC_274_46,(0,0,9):C.R2GC_274_47,(0,0,10):C.R2GC_274_48,(0,0,13):C.R2GC_274_49,(0,0,14):C.R2GC_274_50,(0,0,15):C.R2GC_274_51,(0,0,2):C.R2GC_274_52,(0,0,3):C.R2GC_274_53,(0,0,4):C.R2GC_274_54,(0,0,6):C.R2GC_274_55,(0,0,12):C.R2GC_274_56,(0,0,11):C.R2GC_274_57})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus__, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.y] ], [ [P.c, P.s] ], [ [P.c, P.x] ], [ [P.d, P.tp] ], [ [P.d, P.u] ], [ [P.d, P.y] ], [ [P.s, P.tp] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,5):C.R2GC_279_92,(0,0,6):C.R2GC_279_93,(0,0,7):C.R2GC_279_94,(0,0,0):C.R2GC_279_95,(0,0,1):C.R2GC_279_96,(0,0,2):C.R2GC_279_97,(0,0,3):C.R2GC_279_98,(0,0,4):C.R2GC_279_99,(0,0,8):C.R2GC_279_100,(0,0,9):C.R2GC_279_101,(0,0,10):C.R2GC_279_102,(0,0,11):C.R2GC_279_103,(0,0,12):C.R2GC_279_104,(0,0,13):C.R2GC_279_105,(0,0,14):C.R2GC_279_106,(0,0,16):C.R2GC_279_107,(0,0,15):C.R2GC_279_108,(0,0,17):C.R2GC_279_109})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus____minus__, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.x] ], [ [P.b, P.x] ], [ [P.c, P.y] ], [ [P.d, P.x] ], [ [P.s, P.x] ], [ [P.tp, P.y] ], [ [P.t, P.y] ], [ [P.u, P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_278_84,(0,0,0):C.R2GC_278_85,(0,0,2):C.R2GC_278_86,(0,0,3):C.R2GC_278_87,(0,0,4):C.R2GC_278_88,(0,0,6):C.R2GC_278_89,(0,0,5):C.R2GC_278_90,(0,0,7):C.R2GC_278_91})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_359_84,(0,1,0):C.UVGC_360_85})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_401_184})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_405_188,(0,1,0):C.UVGC_412_207})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_447_298,(0,1,0):C.UVGC_448_299})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_488_431,(0,1,0):C.UVGC_489_432})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,1):C.UVGC_478_387,(0,1,0):C.UVGC_478_388,(0,1,4):C.UVGC_478_389,(0,1,5):C.UVGC_478_390,(0,1,6):C.UVGC_478_391,(0,1,7):C.UVGC_478_392,(0,2,2):C.UVGC_281_1,(0,0,3):C.UVGC_282_2})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(2,1,3):C.UVGC_294_9,(2,1,4):C.UVGC_294_8,(0,1,3):C.UVGC_294_9,(0,1,4):C.UVGC_294_8,(4,1,3):C.UVGC_293_6,(4,1,4):C.UVGC_293_7,(3,1,3):C.UVGC_293_6,(3,1,4):C.UVGC_293_7,(8,1,3):C.UVGC_294_8,(8,1,4):C.UVGC_294_9,(6,1,2):C.UVGC_483_418,(6,1,0):C.UVGC_483_419,(6,1,3):C.UVGC_484_426,(6,1,4):C.UVGC_484_427,(6,1,5):C.UVGC_483_422,(6,1,6):C.UVGC_483_423,(6,1,7):C.UVGC_483_424,(6,1,8):C.UVGC_483_425,(7,1,2):C.UVGC_483_418,(7,1,0):C.UVGC_483_419,(7,1,3):C.UVGC_483_420,(7,1,4):C.UVGC_483_421,(7,1,5):C.UVGC_483_422,(7,1,6):C.UVGC_483_423,(7,1,7):C.UVGC_483_424,(7,1,8):C.UVGC_483_425,(5,1,3):C.UVGC_293_6,(5,1,4):C.UVGC_293_7,(1,1,3):C.UVGC_293_6,(1,1,4):C.UVGC_293_7,(11,0,3):C.UVGC_297_12,(11,0,4):C.UVGC_297_13,(10,0,3):C.UVGC_297_12,(10,0,4):C.UVGC_297_13,(9,0,3):C.UVGC_296_10,(9,0,4):C.UVGC_296_11,(0,2,3):C.UVGC_294_9,(0,2,4):C.UVGC_294_8,(2,2,3):C.UVGC_294_9,(2,2,4):C.UVGC_294_8,(5,2,3):C.UVGC_293_6,(5,2,4):C.UVGC_293_7,(1,2,3):C.UVGC_293_6,(1,2,4):C.UVGC_293_7,(7,2,1):C.UVGC_298_14,(7,2,3):C.UVGC_299_16,(7,2,4):C.UVGC_299_17,(4,2,3):C.UVGC_293_6,(4,2,4):C.UVGC_293_7,(3,2,3):C.UVGC_293_6,(3,2,4):C.UVGC_293_7,(8,2,2):C.UVGC_482_410,(8,2,0):C.UVGC_482_411,(8,2,3):C.UVGC_482_412,(8,2,4):C.UVGC_482_413,(8,2,5):C.UVGC_482_414,(8,2,6):C.UVGC_482_415,(8,2,7):C.UVGC_482_416,(8,2,8):C.UVGC_482_417,(6,2,0):C.UVGC_480_401,(6,2,3):C.UVGC_480_402,(6,2,4):C.UVGC_480_403,(6,2,5):C.UVGC_480_404,(6,2,6):C.UVGC_480_405,(6,2,7):C.UVGC_480_406,(6,2,8):C.UVGC_480_407,(0,3,3):C.UVGC_294_9,(0,3,4):C.UVGC_294_8,(2,3,3):C.UVGC_294_9,(2,3,4):C.UVGC_294_8,(5,3,3):C.UVGC_293_6,(5,3,4):C.UVGC_293_7,(1,3,3):C.UVGC_293_6,(1,3,4):C.UVGC_293_7,(7,3,0):C.UVGC_480_401,(7,3,3):C.UVGC_481_408,(7,3,4):C.UVGC_481_409,(7,3,5):C.UVGC_480_404,(7,3,6):C.UVGC_480_405,(7,3,7):C.UVGC_480_406,(7,3,8):C.UVGC_480_407,(4,3,3):C.UVGC_293_6,(4,3,4):C.UVGC_293_7,(3,3,3):C.UVGC_293_6,(3,3,4):C.UVGC_293_7,(8,3,2):C.UVGC_479_393,(8,3,0):C.UVGC_479_394,(8,3,3):C.UVGC_479_395,(8,3,4):C.UVGC_479_396,(8,3,5):C.UVGC_479_397,(8,3,6):C.UVGC_479_398,(8,3,7):C.UVGC_479_399,(8,3,8):C.UVGC_479_400,(6,3,1):C.UVGC_298_14,(6,3,3):C.UVGC_298_15,(6,3,4):C.UVGC_296_10})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_301_19,(0,1,0):C.UVGC_351_64})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_309_32,(0,1,0):C.UVGC_403_186})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_336_41,(0,1,0):C.UVGC_445_296})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_338_42,(0,1,0):C.UVGC_486_429})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_318_35,(0,1,0):C.UVGC_319_36})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_324_37,(0,1,0):C.UVGC_325_38})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_304_30,(0,1,0):C.UVGC_305_31})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_334_39,(0,1,0):C.UVGC_335_40})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_312_33,(0,1,0):C.UVGC_313_34})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_388_153,(0,1,0):C.UVGC_387_152})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_356_75,(0,0,2):C.UVGC_356_76,(0,0,0):C.UVGC_356_77,(0,1,1):C.UVGC_353_66,(0,1,2):C.UVGC_353_67,(0,1,0):C.UVGC_353_68})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_357_78,(0,0,2):C.UVGC_357_79,(0,0,1):C.UVGC_357_80,(0,1,0):C.UVGC_354_69,(0,1,2):C.UVGC_354_70,(0,1,1):C.UVGC_354_71})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_358_81,(0,0,2):C.UVGC_358_82,(0,0,0):C.UVGC_358_83,(0,1,1):C.UVGC_355_72,(0,1,2):C.UVGC_355_73,(0,1,0):C.UVGC_355_74})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_424_241,(0,0,2):C.UVGC_424_242,(0,0,1):C.UVGC_424_243,(0,1,0):C.UVGC_421_232,(0,1,2):C.UVGC_421_233,(0,1,1):C.UVGC_421_234})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_425_244,(0,0,2):C.UVGC_425_245,(0,0,1):C.UVGC_425_246,(0,1,0):C.UVGC_422_235,(0,1,2):C.UVGC_422_236,(0,1,1):C.UVGC_422_237})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_426_247,(0,0,1):C.UVGC_426_248,(0,0,2):C.UVGC_426_249,(0,1,0):C.UVGC_423_238,(0,1,1):C.UVGC_423_239,(0,1,2):C.UVGC_423_240})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_364_95,(0,0,2):C.UVGC_364_96,(0,0,0):C.UVGC_364_97,(0,1,1):C.UVGC_361_86,(0,1,2):C.UVGC_361_87,(0,1,0):C.UVGC_361_88})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_365_98,(0,0,2):C.UVGC_365_99,(0,0,1):C.UVGC_365_100,(0,1,0):C.UVGC_362_89,(0,1,2):C.UVGC_362_90,(0,1,1):C.UVGC_362_91})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_366_101,(0,0,2):C.UVGC_366_102,(0,0,0):C.UVGC_366_103,(0,1,1):C.UVGC_363_92,(0,1,2):C.UVGC_363_93,(0,1,0):C.UVGC_363_94})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_409_198,(0,0,2):C.UVGC_409_199,(0,0,1):C.UVGC_409_200,(0,1,0):C.UVGC_406_189,(0,1,2):C.UVGC_406_190,(0,1,1):C.UVGC_406_191})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_410_201,(0,0,2):C.UVGC_410_202,(0,0,1):C.UVGC_410_203,(0,1,0):C.UVGC_407_192,(0,1,2):C.UVGC_407_193,(0,1,1):C.UVGC_407_194})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_411_204,(0,0,1):C.UVGC_411_205,(0,0,2):C.UVGC_411_206,(0,1,0):C.UVGC_408_195,(0,1,1):C.UVGC_408_196,(0,1,2):C.UVGC_408_197})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_491_436,(0,0,2):C.UVGC_491_437,(0,0,1):C.UVGC_491_438,(0,1,0):C.UVGC_490_433,(0,1,2):C.UVGC_490_434,(0,1,1):C.UVGC_490_435})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_414_211,(0,0,2):C.UVGC_414_212,(0,0,1):C.UVGC_414_213,(0,1,0):C.UVGC_413_208,(0,1,2):C.UVGC_413_209,(0,1,1):C.UVGC_413_210})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_450_303,(0,0,2):C.UVGC_450_304,(0,0,1):C.UVGC_450_305,(0,1,0):C.UVGC_449_300,(0,1,2):C.UVGC_449_301,(0,1,1):C.UVGC_449_302})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_369_110,(0,0,2):C.UVGC_369_111,(0,0,1):C.UVGC_369_112,(0,1,0):C.UVGC_367_104,(0,1,2):C.UVGC_367_105,(0,1,1):C.UVGC_367_106})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_370_113,(0,0,2):C.UVGC_370_114,(0,0,0):C.UVGC_370_115,(0,1,1):C.UVGC_368_107,(0,1,2):C.UVGC_368_108,(0,1,0):C.UVGC_368_109})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_390_157,(0,0,2):C.UVGC_390_158,(0,0,1):C.UVGC_390_159,(0,1,0):C.UVGC_389_154,(0,1,2):C.UVGC_389_155,(0,1,1):C.UVGC_389_156})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_347_57,(0,0,1):C.UVGC_347_58,(0,1,0):C.UVGC_346_55,(0,1,1):C.UVGC_346_56})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_343_49,(0,0,1):C.UVGC_343_50,(0,1,0):C.UVGC_342_47,(0,1,1):C.UVGC_342_48})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_392_163,(0,0,2):C.UVGC_392_164,(0,0,1):C.UVGC_392_165,(0,1,0):C.UVGC_391_160,(0,1,2):C.UVGC_391_161,(0,1,1):C.UVGC_391_162})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_418_223,(0,0,2):C.UVGC_418_224,(0,0,1):C.UVGC_418_225,(0,1,0):C.UVGC_415_214,(0,1,2):C.UVGC_415_215,(0,1,1):C.UVGC_415_216})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_419_226,(0,0,2):C.UVGC_419_227,(0,0,1):C.UVGC_419_228,(0,1,0):C.UVGC_416_217,(0,1,2):C.UVGC_416_218,(0,1,1):C.UVGC_416_219})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_420_229,(0,0,2):C.UVGC_420_230,(0,0,1):C.UVGC_420_231,(0,1,0):C.UVGC_417_220,(0,1,2):C.UVGC_417_221,(0,1,1):C.UVGC_417_222})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_454_315,(0,0,2):C.UVGC_454_316,(0,0,1):C.UVGC_454_317,(0,1,0):C.UVGC_451_306,(0,1,2):C.UVGC_451_307,(0,1,1):C.UVGC_451_308})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_455_318,(0,0,2):C.UVGC_455_319,(0,0,1):C.UVGC_455_320,(0,1,0):C.UVGC_452_309,(0,1,2):C.UVGC_452_310,(0,1,1):C.UVGC_452_311})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_456_321,(0,0,2):C.UVGC_456_322,(0,0,1):C.UVGC_456_323,(0,1,0):C.UVGC_453_312,(0,1,2):C.UVGC_453_313,(0,1,1):C.UVGC_453_314})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_495_448,(0,0,2):C.UVGC_495_449,(0,0,1):C.UVGC_495_450,(0,1,0):C.UVGC_492_439,(0,1,2):C.UVGC_492_440,(0,1,1):C.UVGC_492_441})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_496_451,(0,0,2):C.UVGC_496_452,(0,0,1):C.UVGC_496_453,(0,1,0):C.UVGC_493_442,(0,1,2):C.UVGC_493_443,(0,1,1):C.UVGC_493_444})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_497_454,(0,0,2):C.UVGC_497_455,(0,0,1):C.UVGC_497_456,(0,1,0):C.UVGC_494_445,(0,1,2):C.UVGC_494_446,(0,1,1):C.UVGC_494_447})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_458_327,(0,0,2):C.UVGC_458_328,(0,0,1):C.UVGC_458_329,(0,1,0):C.UVGC_457_324,(0,1,2):C.UVGC_457_325,(0,1,1):C.UVGC_457_326})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_499_460,(0,0,2):C.UVGC_499_461,(0,0,1):C.UVGC_499_462,(0,1,0):C.UVGC_498_457,(0,1,2):C.UVGC_498_458,(0,1,1):C.UVGC_498_459})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_462_339,(0,0,2):C.UVGC_462_340,(0,0,1):C.UVGC_462_341,(0,1,0):C.UVGC_459_330,(0,1,2):C.UVGC_459_331,(0,1,1):C.UVGC_459_332})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_463_342,(0,0,2):C.UVGC_463_343,(0,0,1):C.UVGC_463_344,(0,1,0):C.UVGC_460_333,(0,1,2):C.UVGC_460_334,(0,1,1):C.UVGC_460_335})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_464_345,(0,0,2):C.UVGC_464_346,(0,0,1):C.UVGC_464_347,(0,1,0):C.UVGC_461_336,(0,1,2):C.UVGC_461_337,(0,1,1):C.UVGC_461_338})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_503_472,(0,0,2):C.UVGC_503_473,(0,0,1):C.UVGC_503_474,(0,1,0):C.UVGC_500_463,(0,1,2):C.UVGC_500_464,(0,1,1):C.UVGC_500_465})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_504_475,(0,0,2):C.UVGC_504_476,(0,0,1):C.UVGC_504_477,(0,1,0):C.UVGC_501_466,(0,1,2):C.UVGC_501_467,(0,1,1):C.UVGC_501_468})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_505_478,(0,0,2):C.UVGC_505_479,(0,0,1):C.UVGC_505_480,(0,1,0):C.UVGC_502_469,(0,1,2):C.UVGC_502_470,(0,1,1):C.UVGC_502_471})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_490_433,(0,0,2):C.UVGC_490_434,(0,0,1):C.UVGC_490_435,(0,1,0):C.UVGC_491_436,(0,1,2):C.UVGC_491_437,(0,1,1):C.UVGC_491_438})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_413_208,(0,0,2):C.UVGC_413_209,(0,0,1):C.UVGC_413_210,(0,1,0):C.UVGC_414_211,(0,1,2):C.UVGC_414_212,(0,1,1):C.UVGC_414_213})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_449_300,(0,0,2):C.UVGC_449_301,(0,0,1):C.UVGC_449_302,(0,1,0):C.UVGC_450_303,(0,1,2):C.UVGC_450_304,(0,1,1):C.UVGC_450_305})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_457_324,(0,0,2):C.UVGC_457_325,(0,0,1):C.UVGC_457_326,(0,1,0):C.UVGC_458_327,(0,1,2):C.UVGC_458_328,(0,1,1):C.UVGC_458_329})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_498_457,(0,0,2):C.UVGC_498_458,(0,0,1):C.UVGC_498_459,(0,1,0):C.UVGC_499_460,(0,1,2):C.UVGC_499_461,(0,1,1):C.UVGC_499_462})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_361_86,(0,0,2):C.UVGC_361_87,(0,0,0):C.UVGC_361_88,(0,1,1):C.UVGC_364_95,(0,1,2):C.UVGC_364_96,(0,1,0):C.UVGC_364_97})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_362_89,(0,0,2):C.UVGC_362_90,(0,0,1):C.UVGC_362_91,(0,1,0):C.UVGC_365_98,(0,1,2):C.UVGC_365_99,(0,1,1):C.UVGC_365_100})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_363_92,(0,0,2):C.UVGC_363_93,(0,0,0):C.UVGC_363_94,(0,1,1):C.UVGC_366_101,(0,1,2):C.UVGC_366_102,(0,1,0):C.UVGC_366_103})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_406_189,(0,0,2):C.UVGC_406_190,(0,0,1):C.UVGC_406_191,(0,1,0):C.UVGC_409_198,(0,1,2):C.UVGC_409_199,(0,1,1):C.UVGC_409_200})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_407_192,(0,0,2):C.UVGC_407_193,(0,0,1):C.UVGC_407_194,(0,1,0):C.UVGC_410_201,(0,1,2):C.UVGC_410_202,(0,1,1):C.UVGC_410_203})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_408_195,(0,0,1):C.UVGC_408_196,(0,0,2):C.UVGC_408_197,(0,1,0):C.UVGC_411_204,(0,1,1):C.UVGC_411_205,(0,1,2):C.UVGC_411_206})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_367_104,(0,0,2):C.UVGC_367_105,(0,0,1):C.UVGC_367_106,(0,1,0):C.UVGC_369_110,(0,1,2):C.UVGC_369_111,(0,1,1):C.UVGC_369_112})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_368_107,(0,0,2):C.UVGC_368_108,(0,0,0):C.UVGC_368_109,(0,1,1):C.UVGC_370_113,(0,1,2):C.UVGC_370_114,(0,1,0):C.UVGC_370_115})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_389_154,(0,0,2):C.UVGC_389_155,(0,0,1):C.UVGC_389_156,(0,1,0):C.UVGC_390_157,(0,1,2):C.UVGC_390_158,(0,1,1):C.UVGC_390_159})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_346_55,(0,0,1):C.UVGC_346_56,(0,1,0):C.UVGC_347_57,(0,1,1):C.UVGC_347_58})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_342_47,(0,0,1):C.UVGC_342_48,(0,1,0):C.UVGC_343_49,(0,1,1):C.UVGC_343_50})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_391_160,(0,0,2):C.UVGC_391_161,(0,0,1):C.UVGC_391_162,(0,1,0):C.UVGC_392_163,(0,1,2):C.UVGC_392_164,(0,1,1):C.UVGC_392_165})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_415_214,(0,0,2):C.UVGC_415_215,(0,0,1):C.UVGC_415_216,(0,1,0):C.UVGC_418_223,(0,1,2):C.UVGC_418_224,(0,1,1):C.UVGC_418_225})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_416_217,(0,0,2):C.UVGC_416_218,(0,0,1):C.UVGC_416_219,(0,1,0):C.UVGC_419_226,(0,1,2):C.UVGC_419_227,(0,1,1):C.UVGC_419_228})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_417_220,(0,0,2):C.UVGC_417_221,(0,0,1):C.UVGC_417_222,(0,1,0):C.UVGC_420_229,(0,1,2):C.UVGC_420_230,(0,1,1):C.UVGC_420_231})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_451_306,(0,0,2):C.UVGC_451_307,(0,0,1):C.UVGC_451_308,(0,1,0):C.UVGC_454_315,(0,1,2):C.UVGC_454_316,(0,1,1):C.UVGC_454_317})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_452_309,(0,0,2):C.UVGC_452_310,(0,0,1):C.UVGC_452_311,(0,1,0):C.UVGC_455_318,(0,1,2):C.UVGC_455_319,(0,1,1):C.UVGC_455_320})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_453_312,(0,0,2):C.UVGC_453_313,(0,0,1):C.UVGC_453_314,(0,1,0):C.UVGC_456_321,(0,1,2):C.UVGC_456_322,(0,1,1):C.UVGC_456_323})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_492_439,(0,0,2):C.UVGC_492_440,(0,0,1):C.UVGC_492_441,(0,1,0):C.UVGC_495_448,(0,1,2):C.UVGC_495_449,(0,1,1):C.UVGC_495_450})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_493_442,(0,0,2):C.UVGC_493_443,(0,0,1):C.UVGC_493_444,(0,1,0):C.UVGC_496_451,(0,1,2):C.UVGC_496_452,(0,1,1):C.UVGC_496_453})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_494_445,(0,0,2):C.UVGC_494_446,(0,0,1):C.UVGC_494_447,(0,1,0):C.UVGC_497_454,(0,1,2):C.UVGC_497_455,(0,1,1):C.UVGC_497_456})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_459_330,(0,0,2):C.UVGC_459_331,(0,0,1):C.UVGC_459_332,(0,1,0):C.UVGC_462_339,(0,1,2):C.UVGC_462_340,(0,1,1):C.UVGC_462_341})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_460_333,(0,0,2):C.UVGC_460_334,(0,0,1):C.UVGC_460_335,(0,1,0):C.UVGC_463_342,(0,1,2):C.UVGC_463_343,(0,1,1):C.UVGC_463_344})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_461_336,(0,0,2):C.UVGC_461_337,(0,0,1):C.UVGC_461_338,(0,1,0):C.UVGC_464_345,(0,1,2):C.UVGC_464_346,(0,1,1):C.UVGC_464_347})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_500_463,(0,0,2):C.UVGC_500_464,(0,0,1):C.UVGC_500_465,(0,1,0):C.UVGC_503_472,(0,1,2):C.UVGC_503_473,(0,1,1):C.UVGC_503_474})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_501_466,(0,0,2):C.UVGC_501_467,(0,0,1):C.UVGC_501_468,(0,1,0):C.UVGC_504_475,(0,1,2):C.UVGC_504_476,(0,1,1):C.UVGC_504_477})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_502_469,(0,0,2):C.UVGC_502_470,(0,0,1):C.UVGC_502_471,(0,1,0):C.UVGC_505_478,(0,1,2):C.UVGC_505_479,(0,1,1):C.UVGC_505_480})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_353_66,(0,0,2):C.UVGC_353_67,(0,0,0):C.UVGC_353_68,(0,1,1):C.UVGC_356_75,(0,1,2):C.UVGC_356_76,(0,1,0):C.UVGC_356_77})

V_292 = CTVertex(name = 'V_292',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_354_69,(0,0,2):C.UVGC_354_70,(0,0,1):C.UVGC_354_71,(0,1,0):C.UVGC_357_78,(0,1,2):C.UVGC_357_79,(0,1,1):C.UVGC_357_80})

V_293 = CTVertex(name = 'V_293',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_355_72,(0,0,2):C.UVGC_355_73,(0,0,0):C.UVGC_355_74,(0,1,1):C.UVGC_358_81,(0,1,2):C.UVGC_358_82,(0,1,0):C.UVGC_358_83})

V_294 = CTVertex(name = 'V_294',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_421_232,(0,0,2):C.UVGC_421_233,(0,0,1):C.UVGC_421_234,(0,1,0):C.UVGC_424_241,(0,1,2):C.UVGC_424_242,(0,1,1):C.UVGC_424_243})

V_295 = CTVertex(name = 'V_295',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_422_235,(0,0,2):C.UVGC_422_236,(0,0,1):C.UVGC_422_237,(0,1,0):C.UVGC_425_244,(0,1,2):C.UVGC_425_245,(0,1,1):C.UVGC_425_246})

V_296 = CTVertex(name = 'V_296',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_423_238,(0,0,1):C.UVGC_423_239,(0,0,2):C.UVGC_423_240,(0,1,0):C.UVGC_426_247,(0,1,1):C.UVGC_426_248,(0,1,2):C.UVGC_426_249})

V_297 = CTVertex(name = 'V_297',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,2):C.UVGC_302_22,(0,1,3):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,4):C.UVGC_404_187})

V_298 = CTVertex(name = 'V_298',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.bp, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,3):C.UVGC_302_22,(0,1,4):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,2):C.UVGC_352_65})

V_299 = CTVertex(name = 'V_299',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.x] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,2):C.UVGC_302_22,(0,1,3):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,4):C.UVGC_446_297})

V_300 = CTVertex(name = 'V_300',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.y] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,2):C.UVGC_302_22,(0,1,3):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,4):C.UVGC_487_430})

V_301 = CTVertex(name = 'V_301',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_428_251,(0,0,2):C.UVGC_428_252,(0,0,1):C.UVGC_428_253,(0,1,0):C.UVGC_434_269,(0,1,2):C.UVGC_434_270,(0,1,1):C.UVGC_434_271})

V_302 = CTVertex(name = 'V_302',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_429_254,(0,0,2):C.UVGC_429_255,(0,0,1):C.UVGC_429_256,(0,1,0):C.UVGC_435_272,(0,1,2):C.UVGC_435_273,(0,1,1):C.UVGC_435_274})

V_303 = CTVertex(name = 'V_303',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_430_257,(0,0,2):C.UVGC_430_258,(0,0,1):C.UVGC_430_259,(0,1,0):C.UVGC_436_275,(0,1,2):C.UVGC_436_276,(0,1,1):C.UVGC_436_277})

V_304 = CTVertex(name = 'V_304',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_468_355,(0,0,2):C.UVGC_468_356,(0,0,1):C.UVGC_468_357,(0,1,0):C.UVGC_471_364,(0,1,2):C.UVGC_471_365,(0,1,1):C.UVGC_471_366})

V_305 = CTVertex(name = 'V_305',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_469_358,(0,0,2):C.UVGC_469_359,(0,0,1):C.UVGC_469_360,(0,1,0):C.UVGC_472_367,(0,1,2):C.UVGC_472_368,(0,1,1):C.UVGC_472_369})

V_306 = CTVertex(name = 'V_306',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_470_361,(0,0,2):C.UVGC_470_362,(0,0,1):C.UVGC_470_363,(0,1,0):C.UVGC_473_370,(0,1,2):C.UVGC_473_371,(0,1,1):C.UVGC_473_372})

V_307 = CTVertex(name = 'V_307',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_372_117,(0,0,2):C.UVGC_372_118,(0,0,1):C.UVGC_372_119,(0,1,0):C.UVGC_377_132,(0,1,2):C.UVGC_377_133,(0,1,1):C.UVGC_377_134})

V_308 = CTVertex(name = 'V_308',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_373_120,(0,0,2):C.UVGC_373_121,(0,0,0):C.UVGC_373_122,(0,1,1):C.UVGC_378_135,(0,1,2):C.UVGC_378_136,(0,1,0):C.UVGC_378_137})

V_309 = CTVertex(name = 'V_309',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_397_176,(0,0,2):C.UVGC_397_177,(0,0,1):C.UVGC_397_178,(0,1,0):C.UVGC_398_179,(0,1,2):C.UVGC_398_180,(0,1,1):C.UVGC_398_181})

V_310 = CTVertex(name = 'V_310',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_509_488,(0,0,2):C.UVGC_509_489,(0,0,1):C.UVGC_509_490,(0,1,0):C.UVGC_512_497,(0,1,2):C.UVGC_512_498,(0,1,1):C.UVGC_512_499})

V_311 = CTVertex(name = 'V_311',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_510_491,(0,0,2):C.UVGC_510_492,(0,0,1):C.UVGC_510_493,(0,1,0):C.UVGC_513_500,(0,1,2):C.UVGC_513_501,(0,1,1):C.UVGC_513_502})

V_312 = CTVertex(name = 'V_312',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_511_494,(0,0,2):C.UVGC_511_495,(0,0,1):C.UVGC_511_496,(0,1,0):C.UVGC_514_503,(0,1,2):C.UVGC_514_504,(0,1,1):C.UVGC_514_505})

V_313 = CTVertex(name = 'V_313',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_374_123,(0,0,2):C.UVGC_374_124,(0,0,0):C.UVGC_374_125,(0,1,1):C.UVGC_379_138,(0,1,2):C.UVGC_379_139,(0,1,0):C.UVGC_379_140})

V_314 = CTVertex(name = 'V_314',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_375_126,(0,0,2):C.UVGC_375_127,(0,0,1):C.UVGC_375_128,(0,1,0):C.UVGC_380_141,(0,1,2):C.UVGC_380_142,(0,1,1):C.UVGC_380_143})

V_315 = CTVertex(name = 'V_315',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_376_129,(0,0,2):C.UVGC_376_130,(0,0,0):C.UVGC_376_131,(0,1,1):C.UVGC_381_144,(0,1,2):C.UVGC_381_145,(0,1,0):C.UVGC_381_146})

V_316 = CTVertex(name = 'V_316',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_431_260,(0,0,2):C.UVGC_431_261,(0,0,1):C.UVGC_431_262,(0,1,0):C.UVGC_437_278,(0,1,2):C.UVGC_437_279,(0,1,1):C.UVGC_437_280})

V_317 = CTVertex(name = 'V_317',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_432_263,(0,0,2):C.UVGC_432_264,(0,0,1):C.UVGC_432_265,(0,1,0):C.UVGC_438_281,(0,1,2):C.UVGC_438_282,(0,1,1):C.UVGC_438_283})

V_318 = CTVertex(name = 'V_318',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_433_266,(0,0,1):C.UVGC_433_267,(0,0,2):C.UVGC_433_268,(0,1,0):C.UVGC_439_284,(0,1,1):C.UVGC_439_285,(0,1,2):C.UVGC_439_286})

V_319 = CTVertex(name = 'V_319',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_507_482,(0,0,2):C.UVGC_507_483,(0,0,1):C.UVGC_507_484,(0,1,0):C.UVGC_508_485,(0,1,2):C.UVGC_508_486,(0,1,1):C.UVGC_508_487})

V_320 = CTVertex(name = 'V_320',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_440_287,(0,0,2):C.UVGC_440_288,(0,0,1):C.UVGC_440_289,(0,1,0):C.UVGC_441_290,(0,1,2):C.UVGC_441_291,(0,1,1):C.UVGC_441_292})

V_321 = CTVertex(name = 'V_321',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_466_349,(0,0,2):C.UVGC_466_350,(0,0,1):C.UVGC_466_351,(0,1,0):C.UVGC_467_352,(0,1,2):C.UVGC_467_353,(0,1,1):C.UVGC_467_354})

V_322 = CTVertex(name = 'V_322',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_507_482,(0,0,2):C.UVGC_507_483,(0,0,1):C.UVGC_507_484,(0,1,0):C.UVGC_508_485,(0,1,2):C.UVGC_508_486,(0,1,1):C.UVGC_508_487})

V_323 = CTVertex(name = 'V_323',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_440_287,(0,0,2):C.UVGC_440_288,(0,0,1):C.UVGC_440_289,(0,1,0):C.UVGC_441_290,(0,1,2):C.UVGC_441_291,(0,1,1):C.UVGC_441_292})

V_324 = CTVertex(name = 'V_324',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_466_349,(0,0,2):C.UVGC_466_350,(0,0,1):C.UVGC_466_351,(0,1,0):C.UVGC_467_352,(0,1,2):C.UVGC_467_353,(0,1,1):C.UVGC_467_354})

V_325 = CTVertex(name = 'V_325',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_428_251,(0,0,2):C.UVGC_428_252,(0,0,1):C.UVGC_428_253,(0,1,0):C.UVGC_434_269,(0,1,2):C.UVGC_434_270,(0,1,1):C.UVGC_434_271})

V_326 = CTVertex(name = 'V_326',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_429_254,(0,0,2):C.UVGC_429_255,(0,0,1):C.UVGC_429_256,(0,1,0):C.UVGC_435_272,(0,1,2):C.UVGC_435_273,(0,1,1):C.UVGC_435_274})

V_327 = CTVertex(name = 'V_327',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_430_257,(0,0,2):C.UVGC_430_258,(0,0,1):C.UVGC_430_259,(0,1,0):C.UVGC_436_275,(0,1,2):C.UVGC_436_276,(0,1,1):C.UVGC_436_277})

V_328 = CTVertex(name = 'V_328',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_468_355,(0,0,2):C.UVGC_468_356,(0,0,1):C.UVGC_468_357,(0,1,0):C.UVGC_471_364,(0,1,2):C.UVGC_471_365,(0,1,1):C.UVGC_471_366})

V_329 = CTVertex(name = 'V_329',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_469_358,(0,0,2):C.UVGC_469_359,(0,0,1):C.UVGC_469_360,(0,1,0):C.UVGC_472_367,(0,1,2):C.UVGC_472_368,(0,1,1):C.UVGC_472_369})

V_330 = CTVertex(name = 'V_330',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_470_361,(0,0,2):C.UVGC_470_362,(0,0,1):C.UVGC_470_363,(0,1,0):C.UVGC_473_370,(0,1,2):C.UVGC_473_371,(0,1,1):C.UVGC_473_372})

V_331 = CTVertex(name = 'V_331',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_372_117,(0,0,2):C.UVGC_372_118,(0,0,1):C.UVGC_372_119,(0,1,0):C.UVGC_377_132,(0,1,2):C.UVGC_377_133,(0,1,1):C.UVGC_377_134})

V_332 = CTVertex(name = 'V_332',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_373_120,(0,0,2):C.UVGC_373_121,(0,0,0):C.UVGC_373_122,(0,1,1):C.UVGC_378_135,(0,1,2):C.UVGC_378_136,(0,1,0):C.UVGC_378_137})

V_333 = CTVertex(name = 'V_333',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_397_176,(0,0,2):C.UVGC_397_177,(0,0,1):C.UVGC_397_178,(0,1,0):C.UVGC_398_179,(0,1,2):C.UVGC_398_180,(0,1,1):C.UVGC_398_181})

V_334 = CTVertex(name = 'V_334',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_509_488,(0,0,2):C.UVGC_509_489,(0,0,1):C.UVGC_509_490,(0,1,0):C.UVGC_512_497,(0,1,2):C.UVGC_512_498,(0,1,1):C.UVGC_512_499})

V_335 = CTVertex(name = 'V_335',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_510_491,(0,0,2):C.UVGC_510_492,(0,0,1):C.UVGC_510_493,(0,1,0):C.UVGC_513_500,(0,1,2):C.UVGC_513_501,(0,1,1):C.UVGC_513_502})

V_336 = CTVertex(name = 'V_336',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_511_494,(0,0,2):C.UVGC_511_495,(0,0,1):C.UVGC_511_496,(0,1,0):C.UVGC_514_503,(0,1,2):C.UVGC_514_504,(0,1,1):C.UVGC_514_505})

V_337 = CTVertex(name = 'V_337',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_382_147,(0,1,0):C.UVGC_383_148})

V_338 = CTVertex(name = 'V_338',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_442_293,(0,1,0):C.UVGC_443_294})

V_339 = CTVertex(name = 'V_339',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_474_373,(0,1,0):C.UVGC_475_374})

V_340 = CTVertex(name = 'V_340',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_515_506,(0,1,0):C.UVGC_516_507})

V_341 = CTVertex(name = 'V_341',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_374_123,(0,0,2):C.UVGC_374_124,(0,0,0):C.UVGC_374_125,(0,1,1):C.UVGC_379_138,(0,1,2):C.UVGC_379_139,(0,1,0):C.UVGC_379_140})

V_342 = CTVertex(name = 'V_342',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_375_126,(0,0,2):C.UVGC_375_127,(0,0,1):C.UVGC_375_128,(0,1,0):C.UVGC_380_141,(0,1,2):C.UVGC_380_142,(0,1,1):C.UVGC_380_143})

V_343 = CTVertex(name = 'V_343',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_376_129,(0,0,2):C.UVGC_376_130,(0,0,0):C.UVGC_376_131,(0,1,1):C.UVGC_381_144,(0,1,2):C.UVGC_381_145,(0,1,0):C.UVGC_381_146})

V_344 = CTVertex(name = 'V_344',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_431_260,(0,0,2):C.UVGC_431_261,(0,0,1):C.UVGC_431_262,(0,1,0):C.UVGC_437_278,(0,1,2):C.UVGC_437_279,(0,1,1):C.UVGC_437_280})

V_345 = CTVertex(name = 'V_345',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_432_263,(0,0,2):C.UVGC_432_264,(0,0,1):C.UVGC_432_265,(0,1,0):C.UVGC_438_281,(0,1,2):C.UVGC_438_282,(0,1,1):C.UVGC_438_283})

V_346 = CTVertex(name = 'V_346',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_433_266,(0,0,1):C.UVGC_433_267,(0,0,2):C.UVGC_433_268,(0,1,0):C.UVGC_439_284,(0,1,1):C.UVGC_439_285,(0,1,2):C.UVGC_439_286})

V_347 = CTVertex(name = 'V_347',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_309_32,(0,1,0):C.UVGC_286_5,(0,2,0):C.UVGC_286_5})

V_348 = CTVertex(name = 'V_348',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_309_32,(0,1,0):C.UVGC_286_5,(0,2,0):C.UVGC_286_5})

V_349 = CTVertex(name = 'V_349',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_309_32,(0,1,0):C.UVGC_385_150,(0,2,0):C.UVGC_385_150})

V_350 = CTVertex(name = 'V_350',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_301_19,(0,1,0):C.UVGC_284_4,(0,2,0):C.UVGC_284_4})

V_351 = CTVertex(name = 'V_351',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_301_19,(0,1,0):C.UVGC_284_4,(0,2,0):C.UVGC_284_4})

V_352 = CTVertex(name = 'V_352',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_301_19,(0,1,0):C.UVGC_284_4,(0,2,0):C.UVGC_284_4})

V_353 = CTVertex(name = 'V_353',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,2):C.UVGC_302_22,(0,1,3):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,4):C.UVGC_302_28,(0,2,1):C.UVGC_302_20,(0,2,0):C.UVGC_302_21,(0,2,2):C.UVGC_302_22,(0,2,3):C.UVGC_302_23,(0,2,5):C.UVGC_302_24,(0,2,6):C.UVGC_302_25,(0,2,7):C.UVGC_302_26,(0,2,8):C.UVGC_302_27,(0,2,4):C.UVGC_302_28})

V_354 = CTVertex(name = 'V_354',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,3):C.UVGC_302_22,(0,1,4):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,2):C.UVGC_302_28,(0,2,1):C.UVGC_302_20,(0,2,0):C.UVGC_302_21,(0,2,3):C.UVGC_302_22,(0,2,4):C.UVGC_302_23,(0,2,5):C.UVGC_302_24,(0,2,6):C.UVGC_302_25,(0,2,7):C.UVGC_302_26,(0,2,8):C.UVGC_302_27,(0,2,2):C.UVGC_302_28})

V_355 = CTVertex(name = 'V_355',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,2):C.UVGC_302_22,(0,1,3):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,4):C.UVGC_386_151,(0,2,1):C.UVGC_302_20,(0,2,0):C.UVGC_302_21,(0,2,2):C.UVGC_302_22,(0,2,3):C.UVGC_302_23,(0,2,5):C.UVGC_302_24,(0,2,6):C.UVGC_302_25,(0,2,7):C.UVGC_302_26,(0,2,8):C.UVGC_302_27,(0,2,4):C.UVGC_386_151})

V_356 = CTVertex(name = 'V_356',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,3):C.UVGC_302_22,(0,1,4):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,2):C.UVGC_302_28,(0,2,1):C.UVGC_302_20,(0,2,0):C.UVGC_302_21,(0,2,3):C.UVGC_302_22,(0,2,4):C.UVGC_302_23,(0,2,5):C.UVGC_302_24,(0,2,6):C.UVGC_302_25,(0,2,7):C.UVGC_302_26,(0,2,8):C.UVGC_302_27,(0,2,2):C.UVGC_302_28})

V_357 = CTVertex(name = 'V_357',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,2):C.UVGC_302_22,(0,1,3):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,4):C.UVGC_302_28,(0,2,1):C.UVGC_302_20,(0,2,0):C.UVGC_302_21,(0,2,2):C.UVGC_302_22,(0,2,3):C.UVGC_302_23,(0,2,5):C.UVGC_302_24,(0,2,6):C.UVGC_302_25,(0,2,7):C.UVGC_302_26,(0,2,8):C.UVGC_302_27,(0,2,4):C.UVGC_302_28})

V_358 = CTVertex(name = 'V_358',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_303_29,(0,1,1):C.UVGC_302_20,(0,1,0):C.UVGC_302_21,(0,1,3):C.UVGC_302_22,(0,1,4):C.UVGC_302_23,(0,1,5):C.UVGC_302_24,(0,1,6):C.UVGC_302_25,(0,1,7):C.UVGC_302_26,(0,1,8):C.UVGC_302_27,(0,1,2):C.UVGC_302_28,(0,2,1):C.UVGC_302_20,(0,2,0):C.UVGC_302_21,(0,2,3):C.UVGC_302_22,(0,2,4):C.UVGC_302_23,(0,2,5):C.UVGC_302_24,(0,2,6):C.UVGC_302_25,(0,2,7):C.UVGC_302_26,(0,2,8):C.UVGC_302_27,(0,2,2):C.UVGC_302_28})

V_359 = CTVertex(name = 'V_359',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_348_59,(0,0,1):C.UVGC_348_60})

V_360 = CTVertex(name = 'V_360',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_349_61,(0,0,1):C.UVGC_349_62})

V_361 = CTVertex(name = 'V_361',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_345_53,(0,0,1):C.UVGC_345_54})

V_362 = CTVertex(name = 'V_362',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_341_45,(0,0,0):C.UVGC_341_46})

V_363 = CTVertex(name = 'V_363',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_344_51,(0,0,1):C.UVGC_344_52})

V_364 = CTVertex(name = 'V_364',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_340_43,(0,0,0):C.UVGC_340_44})

V_365 = CTVertex(name = 'V_365',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_394_167,(0,0,2):C.UVGC_394_168,(0,0,1):C.UVGC_394_169})

V_366 = CTVertex(name = 'V_366',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_395_170,(0,0,2):C.UVGC_395_171,(0,0,1):C.UVGC_395_172})

V_367 = CTVertex(name = 'V_367',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_396_173,(0,0,2):C.UVGC_396_174,(0,0,1):C.UVGC_396_175})

V_368 = CTVertex(name = 'V_368',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_348_59,(0,0,1):C.UVGC_348_60})

V_369 = CTVertex(name = 'V_369',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_341_45,(0,0,0):C.UVGC_341_46})

V_370 = CTVertex(name = 'V_370',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_394_167,(0,0,2):C.UVGC_394_168,(0,0,1):C.UVGC_394_169})

V_371 = CTVertex(name = 'V_371',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_349_61,(0,0,1):C.UVGC_349_62})

V_372 = CTVertex(name = 'V_372',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_344_51,(0,0,1):C.UVGC_344_52})

V_373 = CTVertex(name = 'V_373',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_395_170,(0,0,2):C.UVGC_395_171,(0,0,1):C.UVGC_395_172})

V_374 = CTVertex(name = 'V_374',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_345_53,(0,0,1):C.UVGC_345_54})

V_375 = CTVertex(name = 'V_375',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_340_43,(0,0,0):C.UVGC_340_44})

V_376 = CTVertex(name = 'V_376',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_396_173,(0,0,2):C.UVGC_396_174,(0,0,1):C.UVGC_396_175})

V_377 = CTVertex(name = 'V_377',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_399_182,(0,1,0):C.UVGC_400_183})

V_378 = CTVertex(name = 'V_378',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_300_18,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_379 = CTVertex(name = 'V_379',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_300_18,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_380 = CTVertex(name = 'V_380',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_393_166,(0,2,0):C.UVGC_393_166,(0,1,0):C.UVGC_384_149,(0,3,0):C.UVGC_384_149})

V_381 = CTVertex(name = 'V_381',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_300_18,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_382 = CTVertex(name = 'V_382',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_300_18,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_383 = CTVertex(name = 'V_383',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_300_18,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_384 = CTVertex(name = 'V_384',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_465_348,(0,2,0):C.UVGC_465_348,(0,1,0):C.UVGC_444_295,(0,3,0):C.UVGC_444_295})

V_385 = CTVertex(name = 'V_385',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_427_250,(0,2,0):C.UVGC_427_250,(0,1,0):C.UVGC_402_185,(0,3,0):C.UVGC_402_185})

V_386 = CTVertex(name = 'V_386',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_371_116,(0,2,0):C.UVGC_371_116,(0,1,0):C.UVGC_350_63,(0,3,0):C.UVGC_350_63})

V_387 = CTVertex(name = 'V_387',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_506_481,(0,2,0):C.UVGC_506_481,(0,1,0):C.UVGC_485_428,(0,3,0):C.UVGC_485_428})

V_388 = CTVertex(name = 'V_388',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_477_380,(0,0,1):C.UVGC_477_381,(0,0,2):C.UVGC_477_382,(0,0,3):C.UVGC_477_383,(0,0,4):C.UVGC_477_384,(0,0,5):C.UVGC_477_385,(0,0,6):C.UVGC_477_386,(0,1,0):C.UVGC_476_375,(0,1,3):C.UVGC_476_376,(0,1,4):C.UVGC_476_377,(0,1,5):C.UVGC_476_378,(0,1,6):C.UVGC_476_379})

