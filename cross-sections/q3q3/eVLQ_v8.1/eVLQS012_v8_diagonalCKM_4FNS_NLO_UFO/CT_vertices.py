# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Thu 28 Jul 2022 08:06:42


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
               couplings = {(0,0,0):C.R2GC_339_166})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_349_173,(0,1,0):C.R2GC_350_174})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_389_207})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_393_208,(0,1,0):C.R2GC_400_215})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.x__tilde__, P.x, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.x] ] ],
               couplings = {(0,0,0):C.R2GC_435_247,(0,1,0):C.R2GC_436_248})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.y__tilde__, P.y, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.y] ] ],
               couplings = {(0,0,0):C.R2GC_476_288,(0,1,0):C.R2GC_477_289})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_466_279,(0,0,1):C.R2GC_466_280})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_284_135,(2,1,1):C.R2GC_284_136,(0,1,0):C.R2GC_284_135,(0,1,1):C.R2GC_284_136,(4,1,0):C.R2GC_282_131,(4,1,1):C.R2GC_282_132,(3,1,0):C.R2GC_282_131,(3,1,1):C.R2GC_282_132,(8,1,0):C.R2GC_283_133,(8,1,1):C.R2GC_283_134,(6,1,0):C.R2GC_287_140,(6,1,1):C.R2GC_472_287,(7,1,0):C.R2GC_288_142,(7,1,1):C.R2GC_471_286,(5,1,0):C.R2GC_282_131,(5,1,1):C.R2GC_282_132,(1,1,0):C.R2GC_282_131,(1,1,1):C.R2GC_282_132,(11,0,0):C.R2GC_286_138,(11,0,1):C.R2GC_286_139,(10,0,0):C.R2GC_286_138,(10,0,1):C.R2GC_286_139,(9,0,1):C.R2GC_285_137,(0,2,0):C.R2GC_284_135,(0,2,1):C.R2GC_284_136,(2,2,0):C.R2GC_284_135,(2,2,1):C.R2GC_284_136,(5,2,0):C.R2GC_282_131,(5,2,1):C.R2GC_282_132,(1,2,0):C.R2GC_282_131,(1,2,1):C.R2GC_282_132,(7,2,0):C.R2GC_288_142,(7,2,1):C.R2GC_288_143,(4,2,0):C.R2GC_282_131,(4,2,1):C.R2GC_282_132,(3,2,0):C.R2GC_282_131,(3,2,1):C.R2GC_282_132,(8,2,0):C.R2GC_283_133,(8,2,1):C.R2GC_470_285,(6,2,0):C.R2GC_468_282,(6,2,1):C.R2GC_468_283,(0,3,0):C.R2GC_284_135,(0,3,1):C.R2GC_284_136,(2,3,0):C.R2GC_284_135,(2,3,1):C.R2GC_284_136,(5,3,0):C.R2GC_282_131,(5,3,1):C.R2GC_282_132,(1,3,0):C.R2GC_282_131,(1,3,1):C.R2GC_282_132,(7,3,0):C.R2GC_469_284,(7,3,1):C.R2GC_284_136,(4,3,0):C.R2GC_282_131,(4,3,1):C.R2GC_282_132,(3,3,0):C.R2GC_282_131,(3,3,1):C.R2GC_282_132,(8,3,0):C.R2GC_283_133,(8,3,1):C.R2GC_467_281,(6,3,0):C.R2GC_287_140,(6,3,1):C.R2GC_287_141})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_289_144})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_294_147})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_321_156})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_323_157})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_303_150,(0,1,0):C.R2GC_304_151})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_309_152,(0,1,0):C.R2GC_310_153})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_334_163,(0,1,0):C.R2GC_335_164})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_319_154,(0,1,0):C.R2GC_320_155})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_297_148,(0,1,0):C.R2GC_298_149})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_378_199,(0,1,0):C.R2GC_377_198})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_346_170,(0,1,0):C.R2GC_343_167})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_347_171,(0,1,0):C.R2GC_344_168})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_348_172,(0,1,0):C.R2GC_345_169})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_412_227,(0,1,0):C.R2GC_409_224})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_413_228,(0,1,0):C.R2GC_410_225})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_414_229,(0,1,0):C.R2GC_411_226})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_354_178,(0,1,0):C.R2GC_351_175})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_355_179,(0,1,0):C.R2GC_352_176})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_356_180,(0,1,0):C.R2GC_353_177})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_397_212,(0,1,0):C.R2GC_394_209})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_398_213,(0,1,0):C.R2GC_395_210})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_399_214,(0,1,0):C.R2GC_396_211})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_479_291,(0,1,0):C.R2GC_478_290})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_402_217,(0,1,0):C.R2GC_401_216})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_438_250,(0,1,0):C.R2GC_437_249})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_359_183,(0,1,0):C.R2GC_357_181})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_360_184,(0,1,0):C.R2GC_358_182})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_380_201,(0,1,0):C.R2GC_379_200})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_329_162,(0,1,0):C.R2GC_328_161})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_326_159,(0,1,0):C.R2GC_325_158})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_382_203,(0,1,0):C.R2GC_381_202})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_406_221,(0,1,0):C.R2GC_403_218})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_407_222,(0,1,0):C.R2GC_404_219})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_408_223,(0,1,0):C.R2GC_405_220})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_442_254,(0,1,0):C.R2GC_439_251})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_443_255,(0,1,0):C.R2GC_440_252})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_444_256,(0,1,0):C.R2GC_441_253})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_483_295,(0,1,0):C.R2GC_480_292})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_484_296,(0,1,0):C.R2GC_481_293})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_485_297,(0,1,0):C.R2GC_482_294})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_446_258,(0,1,0):C.R2GC_445_257})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_487_299,(0,1,0):C.R2GC_486_298})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_450_262,(0,1,0):C.R2GC_447_259})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_451_263,(0,1,0):C.R2GC_448_260})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_452_264,(0,1,0):C.R2GC_449_261})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_491_303,(0,1,0):C.R2GC_488_300})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_492_304,(0,1,0):C.R2GC_489_301})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_493_305,(0,1,0):C.R2GC_490_302})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_478_290,(0,1,0):C.R2GC_479_291})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_401_216,(0,1,0):C.R2GC_402_217})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_437_249,(0,1,0):C.R2GC_438_250})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_445_257,(0,1,0):C.R2GC_446_258})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_486_298,(0,1,0):C.R2GC_487_299})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_351_175,(0,1,0):C.R2GC_354_178})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_352_176,(0,1,0):C.R2GC_355_179})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_353_177,(0,1,0):C.R2GC_356_180})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_394_209,(0,1,0):C.R2GC_397_212})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_395_210,(0,1,0):C.R2GC_398_213})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_396_211,(0,1,0):C.R2GC_399_214})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_357_181,(0,1,0):C.R2GC_359_183})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_358_182,(0,1,0):C.R2GC_360_184})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_379_200,(0,1,0):C.R2GC_380_201})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_328_161,(0,1,0):C.R2GC_329_162})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_325_158,(0,1,0):C.R2GC_326_159})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_381_202,(0,1,0):C.R2GC_382_203})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_403_218,(0,1,0):C.R2GC_406_221})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_404_219,(0,1,0):C.R2GC_407_222})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_405_220,(0,1,0):C.R2GC_408_223})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_439_251,(0,1,0):C.R2GC_442_254})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_440_252,(0,1,0):C.R2GC_443_255})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_441_253,(0,1,0):C.R2GC_444_256})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_480_292,(0,1,0):C.R2GC_483_295})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_481_293,(0,1,0):C.R2GC_484_296})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_482_294,(0,1,0):C.R2GC_485_297})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_447_259,(0,1,0):C.R2GC_450_262})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_448_260,(0,1,0):C.R2GC_451_263})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_449_261,(0,1,0):C.R2GC_452_264})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_488_300,(0,1,0):C.R2GC_491_303})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_489_301,(0,1,0):C.R2GC_492_304})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_490_302,(0,1,0):C.R2GC_493_305})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_343_167,(0,1,0):C.R2GC_346_170})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_344_168,(0,1,0):C.R2GC_347_171})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_345_169,(0,1,0):C.R2GC_348_172})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_409_224,(0,1,0):C.R2GC_412_227})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_410_225,(0,1,0):C.R2GC_413_228})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_411_226,(0,1,0):C.R2GC_414_229})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_290_145})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_290_145})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_290_145})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_290_145})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_416_231,(0,1,0):C.R2GC_422_237})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_417_232,(0,1,0):C.R2GC_423_238})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_418_233,(0,1,0):C.R2GC_424_239})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_456_268,(0,1,0):C.R2GC_459_271})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_457_269,(0,1,0):C.R2GC_460_272})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_458_270,(0,1,0):C.R2GC_461_273})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_362_186,(0,1,0):C.R2GC_367_191})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_363_187,(0,1,0):C.R2GC_368_192})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_385_205,(0,1,0):C.R2GC_386_206})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_497_309,(0,1,0):C.R2GC_500_312})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_498_310,(0,1,0):C.R2GC_501_313})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_499_311,(0,1,0):C.R2GC_502_314})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_364_188,(0,1,0):C.R2GC_369_193})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_365_189,(0,1,0):C.R2GC_370_194})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_366_190,(0,1,0):C.R2GC_371_195})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_419_234,(0,1,0):C.R2GC_425_240})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_420_235,(0,1,0):C.R2GC_426_241})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_421_236,(0,1,0):C.R2GC_427_242})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_495_307,(0,1,0):C.R2GC_496_308})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_428_243,(0,1,0):C.R2GC_429_244})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_454_266,(0,1,0):C.R2GC_455_267})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_495_307,(0,1,0):C.R2GC_496_308})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_428_243,(0,1,0):C.R2GC_429_244})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_454_266,(0,1,0):C.R2GC_455_267})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_416_231,(0,1,0):C.R2GC_422_237})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_417_232,(0,1,0):C.R2GC_423_238})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_418_233,(0,1,0):C.R2GC_424_239})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_456_268,(0,1,0):C.R2GC_459_271})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_457_269,(0,1,0):C.R2GC_460_272})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_458_270,(0,1,0):C.R2GC_461_273})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_362_186,(0,1,0):C.R2GC_367_191})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_363_187,(0,1,0):C.R2GC_368_192})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_385_205,(0,1,0):C.R2GC_386_206})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_497_309,(0,1,0):C.R2GC_500_312})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_498_310,(0,1,0):C.R2GC_501_313})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_499_311,(0,1,0):C.R2GC_502_314})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_372_196,(0,1,0):C.R2GC_373_197})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_430_245,(0,1,0):C.R2GC_431_246})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_462_274,(0,1,0):C.R2GC_463_275})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_503_315,(0,1,0):C.R2GC_504_316})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_364_188,(0,1,0):C.R2GC_369_193})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_365_189,(0,1,0):C.R2GC_370_194})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_366_190,(0,1,0):C.R2GC_371_195})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_419_234,(0,1,0):C.R2GC_425_240})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_420_235,(0,1,0):C.R2GC_426_241})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_421_236,(0,1,0):C.R2GC_427_242})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_294_147})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_294_147})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_294_147})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_289_144})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_289_144})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_289_144})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_290_145})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_290_145})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_290_145})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_290_145})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_290_145})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_290_145})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_327_160})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_327_160})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_327_160})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_327_160})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_327_160})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_327_160})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_261_43,(0,1,0):C.R2GC_249_1})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_261_43,(0,1,0):C.R2GC_249_1})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_261_43,(0,1,0):C.R2GC_249_1})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_262_44,(0,1,0):C.R2GC_250_2})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_262_44,(0,1,0):C.R2GC_250_2})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_262_44,(0,1,0):C.R2GC_250_2})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_293_146})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_293_146})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_383_204,(0,2,0):C.R2GC_383_204,(0,1,0):C.R2GC_293_146,(0,3,0):C.R2GC_293_146})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_293_146})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_293_146})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_336_165,(0,2,0):C.R2GC_336_165,(0,1,0):C.R2GC_293_146,(0,3,0):C.R2GC_293_146})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_453_265,(0,2,0):C.R2GC_453_265,(0,1,0):C.R2GC_293_146,(0,3,0):C.R2GC_293_146})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_415_230,(0,2,0):C.R2GC_415_230,(0,1,0):C.R2GC_293_146,(0,3,0):C.R2GC_293_146})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_361_185,(0,2,0):C.R2GC_361_185,(0,1,0):C.R2GC_293_146,(0,3,0):C.R2GC_293_146})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_494_306,(0,2,0):C.R2GC_494_306,(0,1,0):C.R2GC_293_146,(0,3,0):C.R2GC_293_146})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.R2GC_465_278,(0,1,0):C.R2GC_257_19,(0,1,1):C.R2GC_257_20,(0,1,4):C.R2GC_257_21,(0,1,5):C.R2GC_257_22,(0,1,6):C.R2GC_257_23,(0,1,7):C.R2GC_257_24,(0,2,2):C.R2GC_464_276,(0,2,3):C.R2GC_464_277})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_253_3,(0,0,1):C.R2GC_253_4})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_256_13,(0,0,1):C.R2GC_256_14,(0,0,2):C.R2GC_256_15,(0,0,3):C.R2GC_256_16,(0,0,4):C.R2GC_256_17,(0,0,5):C.R2GC_256_18})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.tp] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.b, P.y] ], [ [P.c, P.x] ], [ [P.d, P.tp] ], [ [P.d, P.y] ], [ [P.s, P.tp] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,6):C.R2GC_271_115,(0,0,5):C.R2GC_271_116,(0,0,7):C.R2GC_271_117,(0,0,0):C.R2GC_271_118,(0,0,1):C.R2GC_271_119,(0,0,2):C.R2GC_271_120,(0,0,3):C.R2GC_271_121,(0,0,4):C.R2GC_271_122,(0,0,8):C.R2GC_271_123,(0,0,9):C.R2GC_271_124,(0,0,10):C.R2GC_271_125,(0,0,11):C.R2GC_271_126,(0,0,12):C.R2GC_271_127,(0,0,14):C.R2GC_271_128,(0,0,13):C.R2GC_271_129,(0,0,15):C.R2GC_271_130,(0,1,6):C.R2GC_271_115,(0,1,5):C.R2GC_271_116,(0,1,7):C.R2GC_271_117,(0,1,0):C.R2GC_271_118,(0,1,1):C.R2GC_271_119,(0,1,2):C.R2GC_271_120,(0,1,3):C.R2GC_271_121,(0,1,4):C.R2GC_271_122,(0,1,8):C.R2GC_271_123,(0,1,9):C.R2GC_271_124,(0,1,10):C.R2GC_271_125,(0,1,11):C.R2GC_271_126,(0,1,12):C.R2GC_271_127,(0,1,14):C.R2GC_271_128,(0,1,13):C.R2GC_271_129,(0,1,15):C.R2GC_271_130,(0,2,6):C.R2GC_271_115,(0,2,5):C.R2GC_271_116,(0,2,7):C.R2GC_271_117,(0,2,0):C.R2GC_271_118,(0,2,1):C.R2GC_271_119,(0,2,2):C.R2GC_271_120,(0,2,3):C.R2GC_271_121,(0,2,4):C.R2GC_271_122,(0,2,8):C.R2GC_271_123,(0,2,9):C.R2GC_271_124,(0,2,10):C.R2GC_271_125,(0,2,11):C.R2GC_271_126,(0,2,12):C.R2GC_271_127,(0,2,14):C.R2GC_271_128,(0,2,13):C.R2GC_271_129,(0,2,15):C.R2GC_271_130})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b, P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_268_77,(0,0,0):C.R2GC_268_78,(0,0,6):C.R2GC_268_79,(0,0,7):C.R2GC_268_80,(0,0,10):C.R2GC_268_81,(0,0,11):C.R2GC_268_82,(0,0,1):C.R2GC_268_83,(0,0,3):C.R2GC_268_84,(0,0,4):C.R2GC_268_85,(0,0,5):C.R2GC_268_86,(0,0,9):C.R2GC_268_87,(0,0,8):C.R2GC_268_88,(0,1,2):C.R2GC_268_77,(0,1,0):C.R2GC_268_78,(0,1,6):C.R2GC_268_79,(0,1,7):C.R2GC_268_80,(0,1,10):C.R2GC_268_81,(0,1,11):C.R2GC_268_82,(0,1,1):C.R2GC_268_83,(0,1,3):C.R2GC_268_84,(0,1,4):C.R2GC_268_85,(0,1,5):C.R2GC_268_86,(0,1,9):C.R2GC_268_87,(0,1,8):C.R2GC_268_88,(0,2,2):C.R2GC_268_77,(0,2,0):C.R2GC_268_78,(0,2,6):C.R2GC_268_79,(0,2,7):C.R2GC_268_80,(0,2,10):C.R2GC_268_81,(0,2,11):C.R2GC_268_82,(0,2,1):C.R2GC_268_83,(0,2,3):C.R2GC_268_84,(0,2,4):C.R2GC_268_85,(0,2,5):C.R2GC_268_86,(0,2,9):C.R2GC_268_87,(0,2,8):C.R2GC_268_88})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_258_25,(0,0,0):C.R2GC_258_26,(0,0,2):C.R2GC_258_27,(0,0,3):C.R2GC_258_28,(0,0,4):C.R2GC_258_29,(0,0,5):C.R2GC_258_30,(0,1,1):C.R2GC_258_25,(0,1,0):C.R2GC_258_26,(0,1,2):C.R2GC_258_27,(0,1,3):C.R2GC_258_28,(0,1,4):C.R2GC_258_29,(0,1,5):C.R2GC_258_30,(0,2,1):C.R2GC_258_25,(0,2,0):C.R2GC_258_26,(0,2,2):C.R2GC_258_27,(0,2,3):C.R2GC_258_28,(0,2,4):C.R2GC_258_29,(0,2,5):C.R2GC_258_30})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_254_5,(0,0,1):C.R2GC_254_6,(0,0,2):C.R2GC_254_7,(0,0,3):C.R2GC_254_8,(0,1,0):C.R2GC_254_5,(0,1,1):C.R2GC_254_6,(0,1,2):C.R2GC_254_7,(0,1,3):C.R2GC_254_8,(0,2,0):C.R2GC_254_5,(0,2,1):C.R2GC_254_6,(0,2,2):C.R2GC_254_7,(0,2,3):C.R2GC_254_8})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(1,0,1):C.R2GC_260_37,(1,0,0):C.R2GC_260_38,(1,0,2):C.R2GC_260_39,(1,0,3):C.R2GC_260_40,(1,0,4):C.R2GC_260_41,(1,0,5):C.R2GC_260_42,(0,1,1):C.R2GC_259_31,(0,1,0):C.R2GC_259_32,(0,1,2):C.R2GC_259_33,(0,1,3):C.R2GC_259_34,(0,1,4):C.R2GC_259_35,(0,1,5):C.R2GC_259_36,(0,2,1):C.R2GC_259_31,(0,2,0):C.R2GC_259_32,(0,2,2):C.R2GC_259_33,(0,2,3):C.R2GC_259_34,(0,2,4):C.R2GC_259_35,(0,2,5):C.R2GC_259_36,(0,3,1):C.R2GC_259_31,(0,3,0):C.R2GC_259_32,(0,3,2):C.R2GC_259_33,(0,3,3):C.R2GC_259_34,(0,3,4):C.R2GC_259_35,(0,3,5):C.R2GC_259_36})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_255_9,(0,0,1):C.R2GC_255_10,(0,0,2):C.R2GC_255_11,(0,0,3):C.R2GC_255_12,(0,1,0):C.R2GC_255_9,(0,1,1):C.R2GC_255_10,(0,1,2):C.R2GC_255_11,(0,1,3):C.R2GC_255_12,(0,2,0):C.R2GC_255_9,(0,2,1):C.R2GC_255_10,(0,2,2):C.R2GC_255_11,(0,2,3):C.R2GC_255_12})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_267_69,(0,0,5):C.R2GC_267_70,(0,0,1):C.R2GC_267_71,(0,0,2):C.R2GC_267_72,(0,0,3):C.R2GC_267_73,(0,0,4):C.R2GC_267_74,(0,0,7):C.R2GC_267_75,(0,0,6):C.R2GC_267_76})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_266_61,(0,0,5):C.R2GC_266_62,(0,0,1):C.R2GC_266_63,(0,0,2):C.R2GC_266_64,(0,0,3):C.R2GC_266_65,(0,0,4):C.R2GC_266_66,(0,0,7):C.R2GC_266_67,(0,0,6):C.R2GC_266_68})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c] ], [ [P.c, P.tp] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_265_45,(0,0,1):C.R2GC_265_46,(0,0,5):C.R2GC_265_47,(0,0,7):C.R2GC_265_48,(0,0,8):C.R2GC_265_49,(0,0,9):C.R2GC_265_50,(0,0,10):C.R2GC_265_51,(0,0,13):C.R2GC_265_52,(0,0,14):C.R2GC_265_53,(0,0,15):C.R2GC_265_54,(0,0,2):C.R2GC_265_55,(0,0,3):C.R2GC_265_56,(0,0,4):C.R2GC_265_57,(0,0,6):C.R2GC_265_58,(0,0,12):C.R2GC_265_59,(0,0,11):C.R2GC_265_60})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus__, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.y] ], [ [P.c, P.s] ], [ [P.c, P.x] ], [ [P.d, P.tp] ], [ [P.d, P.u] ], [ [P.d, P.y] ], [ [P.s, P.tp] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,5):C.R2GC_270_97,(0,0,6):C.R2GC_270_98,(0,0,7):C.R2GC_270_99,(0,0,0):C.R2GC_270_100,(0,0,1):C.R2GC_270_101,(0,0,2):C.R2GC_270_102,(0,0,3):C.R2GC_270_103,(0,0,4):C.R2GC_270_104,(0,0,8):C.R2GC_270_105,(0,0,9):C.R2GC_270_106,(0,0,10):C.R2GC_270_107,(0,0,11):C.R2GC_270_108,(0,0,12):C.R2GC_270_109,(0,0,13):C.R2GC_270_110,(0,0,14):C.R2GC_270_111,(0,0,16):C.R2GC_270_112,(0,0,15):C.R2GC_270_113,(0,0,17):C.R2GC_270_114})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus____minus__, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.x] ], [ [P.b, P.x] ], [ [P.c, P.y] ], [ [P.d, P.x] ], [ [P.s, P.x] ], [ [P.tp, P.y] ], [ [P.t, P.y] ], [ [P.u, P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_269_89,(0,0,0):C.R2GC_269_90,(0,0,2):C.R2GC_269_91,(0,0,3):C.R2GC_269_92,(0,0,4):C.R2GC_269_93,(0,0,6):C.R2GC_269_94,(0,0,5):C.R2GC_269_95,(0,0,7):C.R2GC_269_96})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_339_60})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_349_82,(0,1,0):C.UVGC_350_83})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_389_175})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_393_179,(0,1,0):C.UVGC_400_198})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_435_289,(0,1,0):C.UVGC_436_290})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_476_429,(0,1,0):C.UVGC_477_430})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,0):C.UVGC_466_380,(0,1,1):C.UVGC_466_381,(0,1,2):C.UVGC_466_382,(0,1,5):C.UVGC_466_383,(0,1,6):C.UVGC_466_384,(0,1,7):C.UVGC_466_385,(0,1,8):C.UVGC_466_386,(0,2,3):C.UVGC_272_1,(0,0,4):C.UVGC_273_2})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(2,1,4):C.UVGC_283_9,(2,1,5):C.UVGC_283_8,(0,1,4):C.UVGC_283_9,(0,1,5):C.UVGC_283_8,(4,1,4):C.UVGC_282_6,(4,1,5):C.UVGC_282_7,(3,1,4):C.UVGC_282_6,(3,1,5):C.UVGC_282_7,(8,1,4):C.UVGC_283_8,(8,1,5):C.UVGC_283_9,(6,1,0):C.UVGC_471_415,(6,1,1):C.UVGC_471_416,(6,1,3):C.UVGC_471_417,(6,1,4):C.UVGC_472_424,(6,1,5):C.UVGC_472_425,(6,1,6):C.UVGC_471_420,(6,1,7):C.UVGC_471_421,(6,1,8):C.UVGC_471_422,(6,1,9):C.UVGC_471_423,(7,1,0):C.UVGC_471_415,(7,1,1):C.UVGC_471_416,(7,1,3):C.UVGC_471_417,(7,1,4):C.UVGC_471_418,(7,1,5):C.UVGC_471_419,(7,1,6):C.UVGC_471_420,(7,1,7):C.UVGC_471_421,(7,1,8):C.UVGC_471_422,(7,1,9):C.UVGC_471_423,(5,1,4):C.UVGC_282_6,(5,1,5):C.UVGC_282_7,(1,1,4):C.UVGC_282_6,(1,1,5):C.UVGC_282_7,(11,0,4):C.UVGC_286_12,(11,0,5):C.UVGC_286_13,(10,0,4):C.UVGC_286_12,(10,0,5):C.UVGC_286_13,(9,0,4):C.UVGC_285_10,(9,0,5):C.UVGC_285_11,(0,2,4):C.UVGC_283_9,(0,2,5):C.UVGC_283_8,(2,2,4):C.UVGC_283_9,(2,2,5):C.UVGC_283_8,(5,2,4):C.UVGC_282_6,(5,2,5):C.UVGC_282_7,(1,2,4):C.UVGC_282_6,(1,2,5):C.UVGC_282_7,(7,2,2):C.UVGC_287_14,(7,2,4):C.UVGC_288_16,(7,2,5):C.UVGC_288_17,(4,2,4):C.UVGC_282_6,(4,2,5):C.UVGC_282_7,(3,2,4):C.UVGC_282_6,(3,2,5):C.UVGC_282_7,(8,2,0):C.UVGC_470_406,(8,2,1):C.UVGC_470_407,(8,2,3):C.UVGC_470_408,(8,2,4):C.UVGC_470_409,(8,2,5):C.UVGC_470_410,(8,2,6):C.UVGC_470_411,(8,2,7):C.UVGC_470_412,(8,2,8):C.UVGC_470_413,(8,2,9):C.UVGC_470_414,(6,2,0):C.UVGC_468_396,(6,2,1):C.UVGC_468_397,(6,2,4):C.UVGC_468_398,(6,2,5):C.UVGC_468_399,(6,2,6):C.UVGC_468_400,(6,2,7):C.UVGC_468_401,(6,2,8):C.UVGC_468_402,(6,2,9):C.UVGC_468_403,(0,3,4):C.UVGC_283_9,(0,3,5):C.UVGC_283_8,(2,3,4):C.UVGC_283_9,(2,3,5):C.UVGC_283_8,(5,3,4):C.UVGC_282_6,(5,3,5):C.UVGC_282_7,(1,3,4):C.UVGC_282_6,(1,3,5):C.UVGC_282_7,(7,3,0):C.UVGC_468_396,(7,3,1):C.UVGC_468_397,(7,3,4):C.UVGC_469_404,(7,3,5):C.UVGC_469_405,(7,3,6):C.UVGC_468_400,(7,3,7):C.UVGC_468_401,(7,3,8):C.UVGC_468_402,(7,3,9):C.UVGC_468_403,(4,3,4):C.UVGC_282_6,(4,3,5):C.UVGC_282_7,(3,3,4):C.UVGC_282_6,(3,3,5):C.UVGC_282_7,(8,3,0):C.UVGC_467_387,(8,3,1):C.UVGC_467_388,(8,3,3):C.UVGC_467_389,(8,3,4):C.UVGC_467_390,(8,3,5):C.UVGC_467_391,(8,3,6):C.UVGC_467_392,(8,3,7):C.UVGC_467_393,(8,3,8):C.UVGC_467_394,(8,3,9):C.UVGC_467_395,(6,3,2):C.UVGC_287_14,(6,3,4):C.UVGC_287_15,(6,3,5):C.UVGC_285_10})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_289_18,(0,1,0):C.UVGC_341_62})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_294_21,(0,1,0):C.UVGC_391_177})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_321_40,(0,1,0):C.UVGC_433_287})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_323_41,(0,1,0):C.UVGC_474_427})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_303_34,(0,1,0):C.UVGC_304_35})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_309_36,(0,1,0):C.UVGC_310_37})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_334_55,(0,1,0):C.UVGC_335_56})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_319_38,(0,1,0):C.UVGC_320_39})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_297_32,(0,1,0):C.UVGC_298_33})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_378_151,(0,1,0):C.UVGC_377_150})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_346_73,(0,0,2):C.UVGC_346_74,(0,0,0):C.UVGC_346_75,(0,1,1):C.UVGC_343_64,(0,1,2):C.UVGC_343_65,(0,1,0):C.UVGC_343_66})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_347_76,(0,0,2):C.UVGC_347_77,(0,0,1):C.UVGC_347_78,(0,1,0):C.UVGC_344_67,(0,1,2):C.UVGC_344_68,(0,1,1):C.UVGC_344_69})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_348_79,(0,0,2):C.UVGC_348_80,(0,0,0):C.UVGC_348_81,(0,1,1):C.UVGC_345_70,(0,1,2):C.UVGC_345_71,(0,1,0):C.UVGC_345_72})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_412_232,(0,0,2):C.UVGC_412_233,(0,0,1):C.UVGC_412_234,(0,1,0):C.UVGC_409_223,(0,1,2):C.UVGC_409_224,(0,1,1):C.UVGC_409_225})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_413_235,(0,0,2):C.UVGC_413_236,(0,0,1):C.UVGC_413_237,(0,1,0):C.UVGC_410_226,(0,1,2):C.UVGC_410_227,(0,1,1):C.UVGC_410_228})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_414_238,(0,0,1):C.UVGC_414_239,(0,0,2):C.UVGC_414_240,(0,1,0):C.UVGC_411_229,(0,1,1):C.UVGC_411_230,(0,1,2):C.UVGC_411_231})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_354_93,(0,0,2):C.UVGC_354_94,(0,0,0):C.UVGC_354_95,(0,1,1):C.UVGC_351_84,(0,1,2):C.UVGC_351_85,(0,1,0):C.UVGC_351_86})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_355_96,(0,0,2):C.UVGC_355_97,(0,0,1):C.UVGC_355_98,(0,1,0):C.UVGC_352_87,(0,1,2):C.UVGC_352_88,(0,1,1):C.UVGC_352_89})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_356_99,(0,0,2):C.UVGC_356_100,(0,0,0):C.UVGC_356_101,(0,1,1):C.UVGC_353_90,(0,1,2):C.UVGC_353_91,(0,1,0):C.UVGC_353_92})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_397_189,(0,0,2):C.UVGC_397_190,(0,0,1):C.UVGC_397_191,(0,1,0):C.UVGC_394_180,(0,1,2):C.UVGC_394_181,(0,1,1):C.UVGC_394_182})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_398_192,(0,0,2):C.UVGC_398_193,(0,0,1):C.UVGC_398_194,(0,1,0):C.UVGC_395_183,(0,1,2):C.UVGC_395_184,(0,1,1):C.UVGC_395_185})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_399_195,(0,0,1):C.UVGC_399_196,(0,0,2):C.UVGC_399_197,(0,1,0):C.UVGC_396_186,(0,1,1):C.UVGC_396_187,(0,1,2):C.UVGC_396_188})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_479_434,(0,0,2):C.UVGC_479_435,(0,0,1):C.UVGC_479_436,(0,1,0):C.UVGC_478_431,(0,1,2):C.UVGC_478_432,(0,1,1):C.UVGC_478_433})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_402_202,(0,0,2):C.UVGC_402_203,(0,0,1):C.UVGC_402_204,(0,1,0):C.UVGC_401_199,(0,1,2):C.UVGC_401_200,(0,1,1):C.UVGC_401_201})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_438_294,(0,0,2):C.UVGC_438_295,(0,0,1):C.UVGC_438_296,(0,1,0):C.UVGC_437_291,(0,1,2):C.UVGC_437_292,(0,1,1):C.UVGC_437_293})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_359_108,(0,0,2):C.UVGC_359_109,(0,0,1):C.UVGC_359_110,(0,1,0):C.UVGC_357_102,(0,1,2):C.UVGC_357_103,(0,1,1):C.UVGC_357_104})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_360_111,(0,0,2):C.UVGC_360_112,(0,0,0):C.UVGC_360_113,(0,1,1):C.UVGC_358_105,(0,1,2):C.UVGC_358_106,(0,1,0):C.UVGC_358_107})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_380_155,(0,0,2):C.UVGC_380_156,(0,0,1):C.UVGC_380_157,(0,1,0):C.UVGC_379_152,(0,1,2):C.UVGC_379_153,(0,1,1):C.UVGC_379_154})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_329_50,(0,0,1):C.UVGC_329_51,(0,1,0):C.UVGC_328_48,(0,1,1):C.UVGC_328_49})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_326_44,(0,0,1):C.UVGC_326_45,(0,1,0):C.UVGC_325_42,(0,1,1):C.UVGC_325_43})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_382_161,(0,0,2):C.UVGC_382_162,(0,0,1):C.UVGC_382_163,(0,1,0):C.UVGC_381_158,(0,1,2):C.UVGC_381_159,(0,1,1):C.UVGC_381_160})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_406_214,(0,0,2):C.UVGC_406_215,(0,0,1):C.UVGC_406_216,(0,1,0):C.UVGC_403_205,(0,1,2):C.UVGC_403_206,(0,1,1):C.UVGC_403_207})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_407_217,(0,0,2):C.UVGC_407_218,(0,0,1):C.UVGC_407_219,(0,1,0):C.UVGC_404_208,(0,1,2):C.UVGC_404_209,(0,1,1):C.UVGC_404_210})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_408_220,(0,0,2):C.UVGC_408_221,(0,0,1):C.UVGC_408_222,(0,1,0):C.UVGC_405_211,(0,1,2):C.UVGC_405_212,(0,1,1):C.UVGC_405_213})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_442_306,(0,0,2):C.UVGC_442_307,(0,0,1):C.UVGC_442_308,(0,1,0):C.UVGC_439_297,(0,1,2):C.UVGC_439_298,(0,1,1):C.UVGC_439_299})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_443_309,(0,0,2):C.UVGC_443_310,(0,0,1):C.UVGC_443_311,(0,1,0):C.UVGC_440_300,(0,1,2):C.UVGC_440_301,(0,1,1):C.UVGC_440_302})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_444_312,(0,0,2):C.UVGC_444_313,(0,0,1):C.UVGC_444_314,(0,1,0):C.UVGC_441_303,(0,1,2):C.UVGC_441_304,(0,1,1):C.UVGC_441_305})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_483_446,(0,0,2):C.UVGC_483_447,(0,0,1):C.UVGC_483_448,(0,1,0):C.UVGC_480_437,(0,1,2):C.UVGC_480_438,(0,1,1):C.UVGC_480_439})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_484_449,(0,0,2):C.UVGC_484_450,(0,0,1):C.UVGC_484_451,(0,1,0):C.UVGC_481_440,(0,1,2):C.UVGC_481_441,(0,1,1):C.UVGC_481_442})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_485_452,(0,0,2):C.UVGC_485_453,(0,0,1):C.UVGC_485_454,(0,1,0):C.UVGC_482_443,(0,1,2):C.UVGC_482_444,(0,1,1):C.UVGC_482_445})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_446_318,(0,0,2):C.UVGC_446_319,(0,0,1):C.UVGC_446_320,(0,1,0):C.UVGC_445_315,(0,1,2):C.UVGC_445_316,(0,1,1):C.UVGC_445_317})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_487_458,(0,0,2):C.UVGC_487_459,(0,0,1):C.UVGC_487_460,(0,1,0):C.UVGC_486_455,(0,1,2):C.UVGC_486_456,(0,1,1):C.UVGC_486_457})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_450_330,(0,0,2):C.UVGC_450_331,(0,0,1):C.UVGC_450_332,(0,1,0):C.UVGC_447_321,(0,1,2):C.UVGC_447_322,(0,1,1):C.UVGC_447_323})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_451_333,(0,0,2):C.UVGC_451_334,(0,0,1):C.UVGC_451_335,(0,1,0):C.UVGC_448_324,(0,1,2):C.UVGC_448_325,(0,1,1):C.UVGC_448_326})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_452_336,(0,0,2):C.UVGC_452_337,(0,0,1):C.UVGC_452_338,(0,1,0):C.UVGC_449_327,(0,1,2):C.UVGC_449_328,(0,1,1):C.UVGC_449_329})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_491_470,(0,0,2):C.UVGC_491_471,(0,0,1):C.UVGC_491_472,(0,1,0):C.UVGC_488_461,(0,1,2):C.UVGC_488_462,(0,1,1):C.UVGC_488_463})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_492_473,(0,0,2):C.UVGC_492_474,(0,0,1):C.UVGC_492_475,(0,1,0):C.UVGC_489_464,(0,1,2):C.UVGC_489_465,(0,1,1):C.UVGC_489_466})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_493_476,(0,0,2):C.UVGC_493_477,(0,0,1):C.UVGC_493_478,(0,1,0):C.UVGC_490_467,(0,1,2):C.UVGC_490_468,(0,1,1):C.UVGC_490_469})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_478_431,(0,0,2):C.UVGC_478_432,(0,0,1):C.UVGC_478_433,(0,1,0):C.UVGC_479_434,(0,1,2):C.UVGC_479_435,(0,1,1):C.UVGC_479_436})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_401_199,(0,0,2):C.UVGC_401_200,(0,0,1):C.UVGC_401_201,(0,1,0):C.UVGC_402_202,(0,1,2):C.UVGC_402_203,(0,1,1):C.UVGC_402_204})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_437_291,(0,0,2):C.UVGC_437_292,(0,0,1):C.UVGC_437_293,(0,1,0):C.UVGC_438_294,(0,1,2):C.UVGC_438_295,(0,1,1):C.UVGC_438_296})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_445_315,(0,0,2):C.UVGC_445_316,(0,0,1):C.UVGC_445_317,(0,1,0):C.UVGC_446_318,(0,1,2):C.UVGC_446_319,(0,1,1):C.UVGC_446_320})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_486_455,(0,0,2):C.UVGC_486_456,(0,0,1):C.UVGC_486_457,(0,1,0):C.UVGC_487_458,(0,1,2):C.UVGC_487_459,(0,1,1):C.UVGC_487_460})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_351_84,(0,0,2):C.UVGC_351_85,(0,0,0):C.UVGC_351_86,(0,1,1):C.UVGC_354_93,(0,1,2):C.UVGC_354_94,(0,1,0):C.UVGC_354_95})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_352_87,(0,0,2):C.UVGC_352_88,(0,0,1):C.UVGC_352_89,(0,1,0):C.UVGC_355_96,(0,1,2):C.UVGC_355_97,(0,1,1):C.UVGC_355_98})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_353_90,(0,0,2):C.UVGC_353_91,(0,0,0):C.UVGC_353_92,(0,1,1):C.UVGC_356_99,(0,1,2):C.UVGC_356_100,(0,1,0):C.UVGC_356_101})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_394_180,(0,0,2):C.UVGC_394_181,(0,0,1):C.UVGC_394_182,(0,1,0):C.UVGC_397_189,(0,1,2):C.UVGC_397_190,(0,1,1):C.UVGC_397_191})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_395_183,(0,0,2):C.UVGC_395_184,(0,0,1):C.UVGC_395_185,(0,1,0):C.UVGC_398_192,(0,1,2):C.UVGC_398_193,(0,1,1):C.UVGC_398_194})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_396_186,(0,0,1):C.UVGC_396_187,(0,0,2):C.UVGC_396_188,(0,1,0):C.UVGC_399_195,(0,1,1):C.UVGC_399_196,(0,1,2):C.UVGC_399_197})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_357_102,(0,0,2):C.UVGC_357_103,(0,0,1):C.UVGC_357_104,(0,1,0):C.UVGC_359_108,(0,1,2):C.UVGC_359_109,(0,1,1):C.UVGC_359_110})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_358_105,(0,0,2):C.UVGC_358_106,(0,0,0):C.UVGC_358_107,(0,1,1):C.UVGC_360_111,(0,1,2):C.UVGC_360_112,(0,1,0):C.UVGC_360_113})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_379_152,(0,0,2):C.UVGC_379_153,(0,0,1):C.UVGC_379_154,(0,1,0):C.UVGC_380_155,(0,1,2):C.UVGC_380_156,(0,1,1):C.UVGC_380_157})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_328_48,(0,0,1):C.UVGC_328_49,(0,1,0):C.UVGC_329_50,(0,1,1):C.UVGC_329_51})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_325_42,(0,0,1):C.UVGC_325_43,(0,1,0):C.UVGC_326_44,(0,1,1):C.UVGC_326_45})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_381_158,(0,0,2):C.UVGC_381_159,(0,0,1):C.UVGC_381_160,(0,1,0):C.UVGC_382_161,(0,1,2):C.UVGC_382_162,(0,1,1):C.UVGC_382_163})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_403_205,(0,0,2):C.UVGC_403_206,(0,0,1):C.UVGC_403_207,(0,1,0):C.UVGC_406_214,(0,1,2):C.UVGC_406_215,(0,1,1):C.UVGC_406_216})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_404_208,(0,0,2):C.UVGC_404_209,(0,0,1):C.UVGC_404_210,(0,1,0):C.UVGC_407_217,(0,1,2):C.UVGC_407_218,(0,1,1):C.UVGC_407_219})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_405_211,(0,0,2):C.UVGC_405_212,(0,0,1):C.UVGC_405_213,(0,1,0):C.UVGC_408_220,(0,1,2):C.UVGC_408_221,(0,1,1):C.UVGC_408_222})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_439_297,(0,0,2):C.UVGC_439_298,(0,0,1):C.UVGC_439_299,(0,1,0):C.UVGC_442_306,(0,1,2):C.UVGC_442_307,(0,1,1):C.UVGC_442_308})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_440_300,(0,0,2):C.UVGC_440_301,(0,0,1):C.UVGC_440_302,(0,1,0):C.UVGC_443_309,(0,1,2):C.UVGC_443_310,(0,1,1):C.UVGC_443_311})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_441_303,(0,0,2):C.UVGC_441_304,(0,0,1):C.UVGC_441_305,(0,1,0):C.UVGC_444_312,(0,1,2):C.UVGC_444_313,(0,1,1):C.UVGC_444_314})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_480_437,(0,0,2):C.UVGC_480_438,(0,0,1):C.UVGC_480_439,(0,1,0):C.UVGC_483_446,(0,1,2):C.UVGC_483_447,(0,1,1):C.UVGC_483_448})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_481_440,(0,0,2):C.UVGC_481_441,(0,0,1):C.UVGC_481_442,(0,1,0):C.UVGC_484_449,(0,1,2):C.UVGC_484_450,(0,1,1):C.UVGC_484_451})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_482_443,(0,0,2):C.UVGC_482_444,(0,0,1):C.UVGC_482_445,(0,1,0):C.UVGC_485_452,(0,1,2):C.UVGC_485_453,(0,1,1):C.UVGC_485_454})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_447_321,(0,0,2):C.UVGC_447_322,(0,0,1):C.UVGC_447_323,(0,1,0):C.UVGC_450_330,(0,1,2):C.UVGC_450_331,(0,1,1):C.UVGC_450_332})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_448_324,(0,0,2):C.UVGC_448_325,(0,0,1):C.UVGC_448_326,(0,1,0):C.UVGC_451_333,(0,1,2):C.UVGC_451_334,(0,1,1):C.UVGC_451_335})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_449_327,(0,0,2):C.UVGC_449_328,(0,0,1):C.UVGC_449_329,(0,1,0):C.UVGC_452_336,(0,1,2):C.UVGC_452_337,(0,1,1):C.UVGC_452_338})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_488_461,(0,0,2):C.UVGC_488_462,(0,0,1):C.UVGC_488_463,(0,1,0):C.UVGC_491_470,(0,1,2):C.UVGC_491_471,(0,1,1):C.UVGC_491_472})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_489_464,(0,0,2):C.UVGC_489_465,(0,0,1):C.UVGC_489_466,(0,1,0):C.UVGC_492_473,(0,1,2):C.UVGC_492_474,(0,1,1):C.UVGC_492_475})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_490_467,(0,0,2):C.UVGC_490_468,(0,0,1):C.UVGC_490_469,(0,1,0):C.UVGC_493_476,(0,1,2):C.UVGC_493_477,(0,1,1):C.UVGC_493_478})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_343_64,(0,0,2):C.UVGC_343_65,(0,0,0):C.UVGC_343_66,(0,1,1):C.UVGC_346_73,(0,1,2):C.UVGC_346_74,(0,1,0):C.UVGC_346_75})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_344_67,(0,0,2):C.UVGC_344_68,(0,0,1):C.UVGC_344_69,(0,1,0):C.UVGC_347_76,(0,1,2):C.UVGC_347_77,(0,1,1):C.UVGC_347_78})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_345_70,(0,0,2):C.UVGC_345_71,(0,0,0):C.UVGC_345_72,(0,1,1):C.UVGC_348_79,(0,1,2):C.UVGC_348_80,(0,1,0):C.UVGC_348_81})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_409_223,(0,0,2):C.UVGC_409_224,(0,0,1):C.UVGC_409_225,(0,1,0):C.UVGC_412_232,(0,1,2):C.UVGC_412_233,(0,1,1):C.UVGC_412_234})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_410_226,(0,0,2):C.UVGC_410_227,(0,0,1):C.UVGC_410_228,(0,1,0):C.UVGC_413_235,(0,1,2):C.UVGC_413_236,(0,1,1):C.UVGC_413_237})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_411_229,(0,0,1):C.UVGC_411_230,(0,0,2):C.UVGC_411_231,(0,1,0):C.UVGC_414_238,(0,1,1):C.UVGC_414_239,(0,1,2):C.UVGC_414_240})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,3):C.UVGC_295_25,(0,1,4):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,5):C.UVGC_392_178})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.bp, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,3):C.UVGC_295_24,(0,1,4):C.UVGC_295_25,(0,1,5):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,2):C.UVGC_342_63})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.x] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,3):C.UVGC_295_25,(0,1,4):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,5):C.UVGC_434_288})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.y] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,3):C.UVGC_295_25,(0,1,4):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,5):C.UVGC_475_428})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_416_242,(0,0,2):C.UVGC_416_243,(0,0,1):C.UVGC_416_244,(0,1,0):C.UVGC_422_260,(0,1,2):C.UVGC_422_261,(0,1,1):C.UVGC_422_262})

V_292 = CTVertex(name = 'V_292',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_417_245,(0,0,2):C.UVGC_417_246,(0,0,1):C.UVGC_417_247,(0,1,0):C.UVGC_423_263,(0,1,2):C.UVGC_423_264,(0,1,1):C.UVGC_423_265})

V_293 = CTVertex(name = 'V_293',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_418_248,(0,0,2):C.UVGC_418_249,(0,0,1):C.UVGC_418_250,(0,1,0):C.UVGC_424_266,(0,1,2):C.UVGC_424_267,(0,1,1):C.UVGC_424_268})

V_294 = CTVertex(name = 'V_294',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_456_346,(0,0,2):C.UVGC_456_347,(0,0,1):C.UVGC_456_348,(0,1,0):C.UVGC_459_355,(0,1,2):C.UVGC_459_356,(0,1,1):C.UVGC_459_357})

V_295 = CTVertex(name = 'V_295',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_457_349,(0,0,2):C.UVGC_457_350,(0,0,1):C.UVGC_457_351,(0,1,0):C.UVGC_460_358,(0,1,2):C.UVGC_460_359,(0,1,1):C.UVGC_460_360})

V_296 = CTVertex(name = 'V_296',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_458_352,(0,0,2):C.UVGC_458_353,(0,0,1):C.UVGC_458_354,(0,1,0):C.UVGC_461_361,(0,1,2):C.UVGC_461_362,(0,1,1):C.UVGC_461_363})

V_297 = CTVertex(name = 'V_297',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_362_115,(0,0,2):C.UVGC_362_116,(0,0,1):C.UVGC_362_117,(0,1,0):C.UVGC_367_130,(0,1,2):C.UVGC_367_131,(0,1,1):C.UVGC_367_132})

V_298 = CTVertex(name = 'V_298',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_363_118,(0,0,2):C.UVGC_363_119,(0,0,0):C.UVGC_363_120,(0,1,1):C.UVGC_368_133,(0,1,2):C.UVGC_368_134,(0,1,0):C.UVGC_368_135})

V_299 = CTVertex(name = 'V_299',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_385_167,(0,0,2):C.UVGC_385_168,(0,0,1):C.UVGC_385_169,(0,1,0):C.UVGC_386_170,(0,1,2):C.UVGC_386_171,(0,1,1):C.UVGC_386_172})

V_300 = CTVertex(name = 'V_300',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_497_486,(0,0,2):C.UVGC_497_487,(0,0,1):C.UVGC_497_488,(0,1,0):C.UVGC_500_495,(0,1,2):C.UVGC_500_496,(0,1,1):C.UVGC_500_497})

V_301 = CTVertex(name = 'V_301',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_498_489,(0,0,2):C.UVGC_498_490,(0,0,1):C.UVGC_498_491,(0,1,0):C.UVGC_501_498,(0,1,2):C.UVGC_501_499,(0,1,1):C.UVGC_501_500})

V_302 = CTVertex(name = 'V_302',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_499_492,(0,0,2):C.UVGC_499_493,(0,0,1):C.UVGC_499_494,(0,1,0):C.UVGC_502_501,(0,1,2):C.UVGC_502_502,(0,1,1):C.UVGC_502_503})

V_303 = CTVertex(name = 'V_303',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_364_121,(0,0,2):C.UVGC_364_122,(0,0,0):C.UVGC_364_123,(0,1,1):C.UVGC_369_136,(0,1,2):C.UVGC_369_137,(0,1,0):C.UVGC_369_138})

V_304 = CTVertex(name = 'V_304',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_365_124,(0,0,2):C.UVGC_365_125,(0,0,1):C.UVGC_365_126,(0,1,0):C.UVGC_370_139,(0,1,2):C.UVGC_370_140,(0,1,1):C.UVGC_370_141})

V_305 = CTVertex(name = 'V_305',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_366_127,(0,0,2):C.UVGC_366_128,(0,0,0):C.UVGC_366_129,(0,1,1):C.UVGC_371_142,(0,1,2):C.UVGC_371_143,(0,1,0):C.UVGC_371_144})

V_306 = CTVertex(name = 'V_306',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_419_251,(0,0,2):C.UVGC_419_252,(0,0,1):C.UVGC_419_253,(0,1,0):C.UVGC_425_269,(0,1,2):C.UVGC_425_270,(0,1,1):C.UVGC_425_271})

V_307 = CTVertex(name = 'V_307',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_420_254,(0,0,2):C.UVGC_420_255,(0,0,1):C.UVGC_420_256,(0,1,0):C.UVGC_426_272,(0,1,2):C.UVGC_426_273,(0,1,1):C.UVGC_426_274})

V_308 = CTVertex(name = 'V_308',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_421_257,(0,0,1):C.UVGC_421_258,(0,0,2):C.UVGC_421_259,(0,1,0):C.UVGC_427_275,(0,1,1):C.UVGC_427_276,(0,1,2):C.UVGC_427_277})

V_309 = CTVertex(name = 'V_309',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_495_480,(0,0,2):C.UVGC_495_481,(0,0,1):C.UVGC_495_482,(0,1,0):C.UVGC_496_483,(0,1,2):C.UVGC_496_484,(0,1,1):C.UVGC_496_485})

V_310 = CTVertex(name = 'V_310',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_428_278,(0,0,2):C.UVGC_428_279,(0,0,1):C.UVGC_428_280,(0,1,0):C.UVGC_429_281,(0,1,2):C.UVGC_429_282,(0,1,1):C.UVGC_429_283})

V_311 = CTVertex(name = 'V_311',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_454_340,(0,0,2):C.UVGC_454_341,(0,0,1):C.UVGC_454_342,(0,1,0):C.UVGC_455_343,(0,1,2):C.UVGC_455_344,(0,1,1):C.UVGC_455_345})

V_312 = CTVertex(name = 'V_312',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_495_480,(0,0,2):C.UVGC_495_481,(0,0,1):C.UVGC_495_482,(0,1,0):C.UVGC_496_483,(0,1,2):C.UVGC_496_484,(0,1,1):C.UVGC_496_485})

V_313 = CTVertex(name = 'V_313',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_428_278,(0,0,2):C.UVGC_428_279,(0,0,1):C.UVGC_428_280,(0,1,0):C.UVGC_429_281,(0,1,2):C.UVGC_429_282,(0,1,1):C.UVGC_429_283})

V_314 = CTVertex(name = 'V_314',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_454_340,(0,0,2):C.UVGC_454_341,(0,0,1):C.UVGC_454_342,(0,1,0):C.UVGC_455_343,(0,1,2):C.UVGC_455_344,(0,1,1):C.UVGC_455_345})

V_315 = CTVertex(name = 'V_315',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_416_242,(0,0,2):C.UVGC_416_243,(0,0,1):C.UVGC_416_244,(0,1,0):C.UVGC_422_260,(0,1,2):C.UVGC_422_261,(0,1,1):C.UVGC_422_262})

V_316 = CTVertex(name = 'V_316',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_417_245,(0,0,2):C.UVGC_417_246,(0,0,1):C.UVGC_417_247,(0,1,0):C.UVGC_423_263,(0,1,2):C.UVGC_423_264,(0,1,1):C.UVGC_423_265})

V_317 = CTVertex(name = 'V_317',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_418_248,(0,0,2):C.UVGC_418_249,(0,0,1):C.UVGC_418_250,(0,1,0):C.UVGC_424_266,(0,1,2):C.UVGC_424_267,(0,1,1):C.UVGC_424_268})

V_318 = CTVertex(name = 'V_318',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_456_346,(0,0,2):C.UVGC_456_347,(0,0,1):C.UVGC_456_348,(0,1,0):C.UVGC_459_355,(0,1,2):C.UVGC_459_356,(0,1,1):C.UVGC_459_357})

V_319 = CTVertex(name = 'V_319',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_457_349,(0,0,2):C.UVGC_457_350,(0,0,1):C.UVGC_457_351,(0,1,0):C.UVGC_460_358,(0,1,2):C.UVGC_460_359,(0,1,1):C.UVGC_460_360})

V_320 = CTVertex(name = 'V_320',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_458_352,(0,0,2):C.UVGC_458_353,(0,0,1):C.UVGC_458_354,(0,1,0):C.UVGC_461_361,(0,1,2):C.UVGC_461_362,(0,1,1):C.UVGC_461_363})

V_321 = CTVertex(name = 'V_321',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_362_115,(0,0,2):C.UVGC_362_116,(0,0,1):C.UVGC_362_117,(0,1,0):C.UVGC_367_130,(0,1,2):C.UVGC_367_131,(0,1,1):C.UVGC_367_132})

V_322 = CTVertex(name = 'V_322',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_363_118,(0,0,2):C.UVGC_363_119,(0,0,0):C.UVGC_363_120,(0,1,1):C.UVGC_368_133,(0,1,2):C.UVGC_368_134,(0,1,0):C.UVGC_368_135})

V_323 = CTVertex(name = 'V_323',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_385_167,(0,0,2):C.UVGC_385_168,(0,0,1):C.UVGC_385_169,(0,1,0):C.UVGC_386_170,(0,1,2):C.UVGC_386_171,(0,1,1):C.UVGC_386_172})

V_324 = CTVertex(name = 'V_324',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_497_486,(0,0,2):C.UVGC_497_487,(0,0,1):C.UVGC_497_488,(0,1,0):C.UVGC_500_495,(0,1,2):C.UVGC_500_496,(0,1,1):C.UVGC_500_497})

V_325 = CTVertex(name = 'V_325',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_498_489,(0,0,2):C.UVGC_498_490,(0,0,1):C.UVGC_498_491,(0,1,0):C.UVGC_501_498,(0,1,2):C.UVGC_501_499,(0,1,1):C.UVGC_501_500})

V_326 = CTVertex(name = 'V_326',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_499_492,(0,0,2):C.UVGC_499_493,(0,0,1):C.UVGC_499_494,(0,1,0):C.UVGC_502_501,(0,1,2):C.UVGC_502_502,(0,1,1):C.UVGC_502_503})

V_327 = CTVertex(name = 'V_327',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_372_145,(0,1,0):C.UVGC_373_146})

V_328 = CTVertex(name = 'V_328',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_430_284,(0,1,0):C.UVGC_431_285})

V_329 = CTVertex(name = 'V_329',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_462_364,(0,1,0):C.UVGC_463_365})

V_330 = CTVertex(name = 'V_330',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_503_504,(0,1,0):C.UVGC_504_505})

V_331 = CTVertex(name = 'V_331',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_364_121,(0,0,2):C.UVGC_364_122,(0,0,0):C.UVGC_364_123,(0,1,1):C.UVGC_369_136,(0,1,2):C.UVGC_369_137,(0,1,0):C.UVGC_369_138})

V_332 = CTVertex(name = 'V_332',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_365_124,(0,0,2):C.UVGC_365_125,(0,0,1):C.UVGC_365_126,(0,1,0):C.UVGC_370_139,(0,1,2):C.UVGC_370_140,(0,1,1):C.UVGC_370_141})

V_333 = CTVertex(name = 'V_333',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_366_127,(0,0,2):C.UVGC_366_128,(0,0,0):C.UVGC_366_129,(0,1,1):C.UVGC_371_142,(0,1,2):C.UVGC_371_143,(0,1,0):C.UVGC_371_144})

V_334 = CTVertex(name = 'V_334',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_419_251,(0,0,2):C.UVGC_419_252,(0,0,1):C.UVGC_419_253,(0,1,0):C.UVGC_425_269,(0,1,2):C.UVGC_425_270,(0,1,1):C.UVGC_425_271})

V_335 = CTVertex(name = 'V_335',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_420_254,(0,0,2):C.UVGC_420_255,(0,0,1):C.UVGC_420_256,(0,1,0):C.UVGC_426_272,(0,1,2):C.UVGC_426_273,(0,1,1):C.UVGC_426_274})

V_336 = CTVertex(name = 'V_336',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_421_257,(0,0,1):C.UVGC_421_258,(0,0,2):C.UVGC_421_259,(0,1,0):C.UVGC_427_275,(0,1,1):C.UVGC_427_276,(0,1,2):C.UVGC_427_277})

V_337 = CTVertex(name = 'V_337',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_294_21,(0,1,0):C.UVGC_275_4,(0,2,0):C.UVGC_275_4})

V_338 = CTVertex(name = 'V_338',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_294_21,(0,1,0):C.UVGC_275_4,(0,2,0):C.UVGC_275_4})

V_339 = CTVertex(name = 'V_339',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_294_21,(0,1,0):C.UVGC_375_148,(0,2,0):C.UVGC_375_148})

V_340 = CTVertex(name = 'V_340',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_289_18,(0,1,0):C.UVGC_277_5,(0,2,0):C.UVGC_277_5})

V_341 = CTVertex(name = 'V_341',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_289_18,(0,1,0):C.UVGC_277_5,(0,2,0):C.UVGC_277_5})

V_342 = CTVertex(name = 'V_342',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_289_18,(0,1,0):C.UVGC_332_53,(0,2,0):C.UVGC_332_53})

V_343 = CTVertex(name = 'V_343',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,3):C.UVGC_295_25,(0,1,4):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,5):C.UVGC_295_31,(0,2,0):C.UVGC_295_22,(0,2,1):C.UVGC_295_23,(0,2,2):C.UVGC_295_24,(0,2,3):C.UVGC_295_25,(0,2,4):C.UVGC_295_26,(0,2,6):C.UVGC_295_27,(0,2,7):C.UVGC_295_28,(0,2,8):C.UVGC_295_29,(0,2,9):C.UVGC_295_30,(0,2,5):C.UVGC_295_31})

V_344 = CTVertex(name = 'V_344',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,4):C.UVGC_295_25,(0,1,5):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,3):C.UVGC_295_31,(0,2,0):C.UVGC_295_22,(0,2,1):C.UVGC_295_23,(0,2,2):C.UVGC_295_24,(0,2,4):C.UVGC_295_25,(0,2,5):C.UVGC_295_26,(0,2,6):C.UVGC_295_27,(0,2,7):C.UVGC_295_28,(0,2,8):C.UVGC_295_29,(0,2,9):C.UVGC_295_30,(0,2,3):C.UVGC_295_31})

V_345 = CTVertex(name = 'V_345',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,3):C.UVGC_295_25,(0,1,4):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,5):C.UVGC_376_149,(0,2,0):C.UVGC_295_22,(0,2,1):C.UVGC_295_23,(0,2,2):C.UVGC_295_24,(0,2,3):C.UVGC_295_25,(0,2,4):C.UVGC_295_26,(0,2,6):C.UVGC_295_27,(0,2,7):C.UVGC_295_28,(0,2,8):C.UVGC_295_29,(0,2,9):C.UVGC_295_30,(0,2,5):C.UVGC_376_149})

V_346 = CTVertex(name = 'V_346',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,4):C.UVGC_295_25,(0,1,5):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,3):C.UVGC_295_31,(0,2,0):C.UVGC_295_22,(0,2,1):C.UVGC_295_23,(0,2,2):C.UVGC_295_24,(0,2,4):C.UVGC_295_25,(0,2,5):C.UVGC_295_26,(0,2,6):C.UVGC_295_27,(0,2,7):C.UVGC_295_28,(0,2,8):C.UVGC_295_29,(0,2,9):C.UVGC_295_30,(0,2,3):C.UVGC_295_31})

V_347 = CTVertex(name = 'V_347',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,2):C.UVGC_295_24,(0,1,3):C.UVGC_295_25,(0,1,4):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,5):C.UVGC_295_31,(0,2,0):C.UVGC_295_22,(0,2,1):C.UVGC_295_23,(0,2,2):C.UVGC_295_24,(0,2,3):C.UVGC_295_25,(0,2,4):C.UVGC_295_26,(0,2,6):C.UVGC_295_27,(0,2,7):C.UVGC_295_28,(0,2,8):C.UVGC_295_29,(0,2,9):C.UVGC_295_30,(0,2,5):C.UVGC_295_31})

V_348 = CTVertex(name = 'V_348',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_290_19,(0,1,0):C.UVGC_295_22,(0,1,1):C.UVGC_295_23,(0,1,3):C.UVGC_295_24,(0,1,4):C.UVGC_295_25,(0,1,5):C.UVGC_295_26,(0,1,6):C.UVGC_295_27,(0,1,7):C.UVGC_295_28,(0,1,8):C.UVGC_295_29,(0,1,9):C.UVGC_295_30,(0,1,2):C.UVGC_333_54,(0,2,0):C.UVGC_295_22,(0,2,1):C.UVGC_295_23,(0,2,3):C.UVGC_295_24,(0,2,4):C.UVGC_295_25,(0,2,5):C.UVGC_295_26,(0,2,6):C.UVGC_295_27,(0,2,7):C.UVGC_295_28,(0,2,8):C.UVGC_295_29,(0,2,9):C.UVGC_295_30,(0,2,2):C.UVGC_333_54})

V_349 = CTVertex(name = 'V_349',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_327_46,(0,0,1):C.UVGC_327_47})

V_350 = CTVertex(name = 'V_350',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_327_46,(0,0,1):C.UVGC_327_47})

V_351 = CTVertex(name = 'V_351',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_384_165,(0,0,2):C.UVGC_384_166,(0,0,1):C.UVGC_327_47})

V_352 = CTVertex(name = 'V_352',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_327_46,(0,0,1):C.UVGC_327_47})

V_353 = CTVertex(name = 'V_353',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_327_46,(0,0,1):C.UVGC_327_47})

V_354 = CTVertex(name = 'V_354',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_384_165,(0,0,2):C.UVGC_384_166,(0,0,1):C.UVGC_327_47})

V_355 = CTVertex(name = 'V_355',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_387_173,(0,1,0):C.UVGC_388_174})

V_356 = CTVertex(name = 'V_356',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_337_58,(0,1,0):C.UVGC_338_59})

V_357 = CTVertex(name = 'V_357',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_293_20,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_358 = CTVertex(name = 'V_358',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_293_20,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_359 = CTVertex(name = 'V_359',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_383_164,(0,2,0):C.UVGC_383_164,(0,1,0):C.UVGC_374_147,(0,3,0):C.UVGC_374_147})

V_360 = CTVertex(name = 'V_360',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_293_20,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_361 = CTVertex(name = 'V_361',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_293_20,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_362 = CTVertex(name = 'V_362',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_336_57,(0,2,0):C.UVGC_336_57,(0,1,0):C.UVGC_331_52,(0,3,0):C.UVGC_331_52})

V_363 = CTVertex(name = 'V_363',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_453_339,(0,2,0):C.UVGC_453_339,(0,1,0):C.UVGC_432_286,(0,3,0):C.UVGC_432_286})

V_364 = CTVertex(name = 'V_364',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_415_241,(0,2,0):C.UVGC_415_241,(0,1,0):C.UVGC_390_176,(0,3,0):C.UVGC_390_176})

V_365 = CTVertex(name = 'V_365',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_361_114,(0,2,0):C.UVGC_361_114,(0,1,0):C.UVGC_340_61,(0,3,0):C.UVGC_340_61})

V_366 = CTVertex(name = 'V_366',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_494_479,(0,2,0):C.UVGC_494_479,(0,1,0):C.UVGC_473_426,(0,3,0):C.UVGC_473_426})

V_367 = CTVertex(name = 'V_367',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_465_372,(0,0,1):C.UVGC_465_373,(0,0,2):C.UVGC_465_374,(0,0,3):C.UVGC_465_375,(0,0,4):C.UVGC_465_376,(0,0,5):C.UVGC_465_377,(0,0,6):C.UVGC_465_378,(0,0,7):C.UVGC_465_379,(0,1,0):C.UVGC_464_366,(0,1,1):C.UVGC_464_367,(0,1,4):C.UVGC_464_368,(0,1,5):C.UVGC_464_369,(0,1,6):C.UVGC_464_370,(0,1,7):C.UVGC_464_371})

