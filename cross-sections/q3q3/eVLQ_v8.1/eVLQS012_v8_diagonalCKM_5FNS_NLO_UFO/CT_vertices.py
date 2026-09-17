# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Thu 28 Jul 2022 07:39:47


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
               couplings = {(0,0,0):C.R2GC_346_166,(0,1,0):C.R2GC_347_167})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_386_200})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_390_201,(0,1,0):C.R2GC_397_208})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.x__tilde__, P.x, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.x] ] ],
               couplings = {(0,0,0):C.R2GC_432_240,(0,1,0):C.R2GC_433_241})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.y__tilde__, P.y, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.y] ] ],
               couplings = {(0,0,0):C.R2GC_473_281,(0,1,0):C.R2GC_474_282})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_463_272,(0,0,1):C.R2GC_463_273})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_286_130,(2,1,1):C.R2GC_286_131,(0,1,0):C.R2GC_286_130,(0,1,1):C.R2GC_286_131,(4,1,0):C.R2GC_284_126,(4,1,1):C.R2GC_284_127,(3,1,0):C.R2GC_284_126,(3,1,1):C.R2GC_284_127,(8,1,0):C.R2GC_285_128,(8,1,1):C.R2GC_285_129,(6,1,0):C.R2GC_289_135,(6,1,1):C.R2GC_469_280,(7,1,0):C.R2GC_290_137,(7,1,1):C.R2GC_468_279,(5,1,0):C.R2GC_284_126,(5,1,1):C.R2GC_284_127,(1,1,0):C.R2GC_284_126,(1,1,1):C.R2GC_284_127,(11,0,0):C.R2GC_288_133,(11,0,1):C.R2GC_288_134,(10,0,0):C.R2GC_288_133,(10,0,1):C.R2GC_288_134,(9,0,1):C.R2GC_287_132,(0,2,0):C.R2GC_286_130,(0,2,1):C.R2GC_286_131,(2,2,0):C.R2GC_286_130,(2,2,1):C.R2GC_286_131,(5,2,0):C.R2GC_284_126,(5,2,1):C.R2GC_284_127,(1,2,0):C.R2GC_284_126,(1,2,1):C.R2GC_284_127,(7,2,0):C.R2GC_290_137,(7,2,1):C.R2GC_290_138,(4,2,0):C.R2GC_284_126,(4,2,1):C.R2GC_284_127,(3,2,0):C.R2GC_284_126,(3,2,1):C.R2GC_284_127,(8,2,0):C.R2GC_285_128,(8,2,1):C.R2GC_467_278,(6,2,0):C.R2GC_465_275,(6,2,1):C.R2GC_465_276,(0,3,0):C.R2GC_286_130,(0,3,1):C.R2GC_286_131,(2,3,0):C.R2GC_286_130,(2,3,1):C.R2GC_286_131,(5,3,0):C.R2GC_284_126,(5,3,1):C.R2GC_284_127,(1,3,0):C.R2GC_284_126,(1,3,1):C.R2GC_284_127,(7,3,0):C.R2GC_466_277,(7,3,1):C.R2GC_286_131,(4,3,0):C.R2GC_284_126,(4,3,1):C.R2GC_284_127,(3,3,0):C.R2GC_284_126,(3,3,1):C.R2GC_284_127,(8,3,0):C.R2GC_285_128,(8,3,1):C.R2GC_464_274,(6,3,0):C.R2GC_289_135,(6,3,1):C.R2GC_289_136})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_292_140})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_300_144})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_327_153})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_329_154})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_309_147,(0,1,0):C.R2GC_310_148})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_315_149,(0,1,0):C.R2GC_316_150})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_295_142,(0,1,0):C.R2GC_296_143})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_325_151,(0,1,0):C.R2GC_326_152})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_303_145,(0,1,0):C.R2GC_304_146})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_375_192,(0,1,0):C.R2GC_374_191})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_343_163,(0,1,0):C.R2GC_340_160})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_344_164,(0,1,0):C.R2GC_341_161})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_345_165,(0,1,0):C.R2GC_342_162})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_409_220,(0,1,0):C.R2GC_406_217})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_410_221,(0,1,0):C.R2GC_407_218})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_411_222,(0,1,0):C.R2GC_408_219})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_351_171,(0,1,0):C.R2GC_348_168})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_352_172,(0,1,0):C.R2GC_349_169})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_353_173,(0,1,0):C.R2GC_350_170})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_394_205,(0,1,0):C.R2GC_391_202})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_395_206,(0,1,0):C.R2GC_392_203})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_396_207,(0,1,0):C.R2GC_393_204})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_476_284,(0,1,0):C.R2GC_475_283})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_399_210,(0,1,0):C.R2GC_398_209})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_435_243,(0,1,0):C.R2GC_434_242})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_356_176,(0,1,0):C.R2GC_354_174})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_357_177,(0,1,0):C.R2GC_355_175})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_377_194,(0,1,0):C.R2GC_376_193})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_335_159,(0,1,0):C.R2GC_334_158})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_332_156,(0,1,0):C.R2GC_331_155})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_379_196,(0,1,0):C.R2GC_378_195})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_403_214,(0,1,0):C.R2GC_400_211})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_404_215,(0,1,0):C.R2GC_401_212})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_405_216,(0,1,0):C.R2GC_402_213})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_439_247,(0,1,0):C.R2GC_436_244})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_440_248,(0,1,0):C.R2GC_437_245})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_441_249,(0,1,0):C.R2GC_438_246})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_480_288,(0,1,0):C.R2GC_477_285})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_481_289,(0,1,0):C.R2GC_478_286})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_482_290,(0,1,0):C.R2GC_479_287})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_443_251,(0,1,0):C.R2GC_442_250})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_484_292,(0,1,0):C.R2GC_483_291})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_447_255,(0,1,0):C.R2GC_444_252})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_448_256,(0,1,0):C.R2GC_445_253})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_449_257,(0,1,0):C.R2GC_446_254})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_488_296,(0,1,0):C.R2GC_485_293})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_489_297,(0,1,0):C.R2GC_486_294})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_490_298,(0,1,0):C.R2GC_487_295})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_475_283,(0,1,0):C.R2GC_476_284})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_398_209,(0,1,0):C.R2GC_399_210})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_434_242,(0,1,0):C.R2GC_435_243})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_442_250,(0,1,0):C.R2GC_443_251})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_483_291,(0,1,0):C.R2GC_484_292})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_348_168,(0,1,0):C.R2GC_351_171})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_349_169,(0,1,0):C.R2GC_352_172})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_350_170,(0,1,0):C.R2GC_353_173})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_391_202,(0,1,0):C.R2GC_394_205})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_392_203,(0,1,0):C.R2GC_395_206})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_393_204,(0,1,0):C.R2GC_396_207})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_354_174,(0,1,0):C.R2GC_356_176})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_355_175,(0,1,0):C.R2GC_357_177})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_376_193,(0,1,0):C.R2GC_377_194})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_334_158,(0,1,0):C.R2GC_335_159})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_331_155,(0,1,0):C.R2GC_332_156})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_378_195,(0,1,0):C.R2GC_379_196})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_400_211,(0,1,0):C.R2GC_403_214})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_401_212,(0,1,0):C.R2GC_404_215})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_402_213,(0,1,0):C.R2GC_405_216})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_436_244,(0,1,0):C.R2GC_439_247})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_437_245,(0,1,0):C.R2GC_440_248})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_438_246,(0,1,0):C.R2GC_441_249})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_477_285,(0,1,0):C.R2GC_480_288})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_478_286,(0,1,0):C.R2GC_481_289})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_479_287,(0,1,0):C.R2GC_482_290})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_444_252,(0,1,0):C.R2GC_447_255})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_445_253,(0,1,0):C.R2GC_448_256})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_446_254,(0,1,0):C.R2GC_449_257})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_485_293,(0,1,0):C.R2GC_488_296})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_486_294,(0,1,0):C.R2GC_489_297})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_487_295,(0,1,0):C.R2GC_490_298})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_340_160,(0,1,0):C.R2GC_343_163})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_341_161,(0,1,0):C.R2GC_344_164})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_342_162,(0,1,0):C.R2GC_345_165})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_406_217,(0,1,0):C.R2GC_409_220})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_407_218,(0,1,0):C.R2GC_410_221})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_408_219,(0,1,0):C.R2GC_411_222})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_294_141})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_294_141})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_294_141})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_294_141})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_413_224,(0,1,0):C.R2GC_419_230})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_414_225,(0,1,0):C.R2GC_420_231})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_415_226,(0,1,0):C.R2GC_421_232})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_453_261,(0,1,0):C.R2GC_456_264})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_454_262,(0,1,0):C.R2GC_457_265})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_455_263,(0,1,0):C.R2GC_458_266})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_359_179,(0,1,0):C.R2GC_364_184})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_360_180,(0,1,0):C.R2GC_365_185})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_382_198,(0,1,0):C.R2GC_383_199})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_494_302,(0,1,0):C.R2GC_497_305})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_495_303,(0,1,0):C.R2GC_498_306})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_496_304,(0,1,0):C.R2GC_499_307})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_361_181,(0,1,0):C.R2GC_366_186})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_362_182,(0,1,0):C.R2GC_367_187})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_363_183,(0,1,0):C.R2GC_368_188})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_416_227,(0,1,0):C.R2GC_422_233})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_417_228,(0,1,0):C.R2GC_423_234})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_418_229,(0,1,0):C.R2GC_424_235})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_492_300,(0,1,0):C.R2GC_493_301})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_425_236,(0,1,0):C.R2GC_426_237})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_451_259,(0,1,0):C.R2GC_452_260})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_492_300,(0,1,0):C.R2GC_493_301})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_425_236,(0,1,0):C.R2GC_426_237})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_451_259,(0,1,0):C.R2GC_452_260})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_413_224,(0,1,0):C.R2GC_419_230})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_414_225,(0,1,0):C.R2GC_420_231})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_415_226,(0,1,0):C.R2GC_421_232})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_453_261,(0,1,0):C.R2GC_456_264})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_454_262,(0,1,0):C.R2GC_457_265})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_455_263,(0,1,0):C.R2GC_458_266})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_359_179,(0,1,0):C.R2GC_364_184})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_360_180,(0,1,0):C.R2GC_365_185})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_382_198,(0,1,0):C.R2GC_383_199})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_494_302,(0,1,0):C.R2GC_497_305})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_495_303,(0,1,0):C.R2GC_498_306})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_496_304,(0,1,0):C.R2GC_499_307})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_369_189,(0,1,0):C.R2GC_370_190})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_427_238,(0,1,0):C.R2GC_428_239})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_459_267,(0,1,0):C.R2GC_460_268})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_500_308,(0,1,0):C.R2GC_501_309})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_361_181,(0,1,0):C.R2GC_366_186})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_362_182,(0,1,0):C.R2GC_367_187})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_363_183,(0,1,0):C.R2GC_368_188})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_416_227,(0,1,0):C.R2GC_422_233})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_417_228,(0,1,0):C.R2GC_423_234})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_418_229,(0,1,0):C.R2GC_424_235})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_300_144})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_300_144})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_300_144})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_292_140})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_292_140})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_292_140})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_294_141})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_294_141})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_294_141})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_294_141})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_294_141})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_294_141})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_333_157})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_333_157})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_333_157})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_333_157})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_333_157})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_333_157})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_261_41,(0,1,0):C.R2GC_248_2})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_261_41,(0,1,0):C.R2GC_248_2})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_261_41,(0,1,0):C.R2GC_248_2})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_260_40,(0,1,0):C.R2GC_247_1})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_260_40,(0,1,0):C.R2GC_247_1})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_260_40,(0,1,0):C.R2GC_247_1})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_291_139})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_291_139})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_380_197,(0,2,0):C.R2GC_380_197,(0,1,0):C.R2GC_291_139,(0,3,0):C.R2GC_291_139})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_291_139})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_291_139})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_291_139})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_450_258,(0,2,0):C.R2GC_450_258,(0,1,0):C.R2GC_291_139,(0,3,0):C.R2GC_291_139})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_412_223,(0,2,0):C.R2GC_412_223,(0,1,0):C.R2GC_291_139,(0,3,0):C.R2GC_291_139})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_358_178,(0,2,0):C.R2GC_358_178,(0,1,0):C.R2GC_291_139,(0,3,0):C.R2GC_291_139})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_491_299,(0,2,0):C.R2GC_491_299,(0,1,0):C.R2GC_291_139,(0,3,0):C.R2GC_291_139})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_462_271,(0,1,0):C.R2GC_256_17,(0,1,3):C.R2GC_256_18,(0,1,4):C.R2GC_256_19,(0,1,5):C.R2GC_256_20,(0,1,6):C.R2GC_256_21,(0,2,1):C.R2GC_461_269,(0,2,2):C.R2GC_461_270})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_252_3})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_255_12,(0,0,1):C.R2GC_255_13,(0,0,2):C.R2GC_255_14,(0,0,3):C.R2GC_255_15,(0,0,4):C.R2GC_255_16})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.tp] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.b, P.y] ], [ [P.c, P.x] ], [ [P.d, P.tp] ], [ [P.d, P.y] ], [ [P.s, P.tp] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,6):C.R2GC_271_110,(0,0,5):C.R2GC_271_111,(0,0,7):C.R2GC_271_112,(0,0,0):C.R2GC_271_113,(0,0,1):C.R2GC_271_114,(0,0,2):C.R2GC_271_115,(0,0,3):C.R2GC_271_116,(0,0,4):C.R2GC_271_117,(0,0,8):C.R2GC_271_118,(0,0,9):C.R2GC_271_119,(0,0,10):C.R2GC_271_120,(0,0,11):C.R2GC_271_121,(0,0,12):C.R2GC_271_122,(0,0,14):C.R2GC_271_123,(0,0,13):C.R2GC_271_124,(0,0,15):C.R2GC_271_125,(0,1,6):C.R2GC_271_110,(0,1,5):C.R2GC_271_111,(0,1,7):C.R2GC_271_112,(0,1,0):C.R2GC_271_113,(0,1,1):C.R2GC_271_114,(0,1,2):C.R2GC_271_115,(0,1,3):C.R2GC_271_116,(0,1,4):C.R2GC_271_117,(0,1,8):C.R2GC_271_118,(0,1,9):C.R2GC_271_119,(0,1,10):C.R2GC_271_120,(0,1,11):C.R2GC_271_121,(0,1,12):C.R2GC_271_122,(0,1,14):C.R2GC_271_123,(0,1,13):C.R2GC_271_124,(0,1,15):C.R2GC_271_125,(0,2,6):C.R2GC_271_110,(0,2,5):C.R2GC_271_111,(0,2,7):C.R2GC_271_112,(0,2,0):C.R2GC_271_113,(0,2,1):C.R2GC_271_114,(0,2,2):C.R2GC_271_115,(0,2,3):C.R2GC_271_116,(0,2,4):C.R2GC_271_117,(0,2,8):C.R2GC_271_118,(0,2,9):C.R2GC_271_119,(0,2,10):C.R2GC_271_120,(0,2,11):C.R2GC_271_121,(0,2,12):C.R2GC_271_122,(0,2,14):C.R2GC_271_123,(0,2,13):C.R2GC_271_124,(0,2,15):C.R2GC_271_125})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b, P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_268_72,(0,0,0):C.R2GC_268_73,(0,0,6):C.R2GC_268_74,(0,0,7):C.R2GC_268_75,(0,0,10):C.R2GC_268_76,(0,0,11):C.R2GC_268_77,(0,0,1):C.R2GC_268_78,(0,0,3):C.R2GC_268_79,(0,0,4):C.R2GC_268_80,(0,0,5):C.R2GC_268_81,(0,0,9):C.R2GC_268_82,(0,0,8):C.R2GC_268_83,(0,1,2):C.R2GC_268_72,(0,1,0):C.R2GC_268_73,(0,1,6):C.R2GC_268_74,(0,1,7):C.R2GC_268_75,(0,1,10):C.R2GC_268_76,(0,1,11):C.R2GC_268_77,(0,1,1):C.R2GC_268_78,(0,1,3):C.R2GC_268_79,(0,1,4):C.R2GC_268_80,(0,1,5):C.R2GC_268_81,(0,1,9):C.R2GC_268_82,(0,1,8):C.R2GC_268_83,(0,2,2):C.R2GC_268_72,(0,2,0):C.R2GC_268_73,(0,2,6):C.R2GC_268_74,(0,2,7):C.R2GC_268_75,(0,2,10):C.R2GC_268_76,(0,2,11):C.R2GC_268_77,(0,2,1):C.R2GC_268_78,(0,2,3):C.R2GC_268_79,(0,2,4):C.R2GC_268_80,(0,2,5):C.R2GC_268_81,(0,2,9):C.R2GC_268_82,(0,2,8):C.R2GC_268_83})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_257_22,(0,0,0):C.R2GC_257_23,(0,0,2):C.R2GC_257_24,(0,0,3):C.R2GC_257_25,(0,0,4):C.R2GC_257_26,(0,0,5):C.R2GC_257_27,(0,1,1):C.R2GC_257_22,(0,1,0):C.R2GC_257_23,(0,1,2):C.R2GC_257_24,(0,1,3):C.R2GC_257_25,(0,1,4):C.R2GC_257_26,(0,1,5):C.R2GC_257_27,(0,2,1):C.R2GC_257_22,(0,2,0):C.R2GC_257_23,(0,2,2):C.R2GC_257_24,(0,2,3):C.R2GC_257_25,(0,2,4):C.R2GC_257_26,(0,2,5):C.R2GC_257_27})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_253_4,(0,0,1):C.R2GC_253_5,(0,0,2):C.R2GC_253_6,(0,0,3):C.R2GC_253_7,(0,1,0):C.R2GC_253_4,(0,1,1):C.R2GC_253_5,(0,1,2):C.R2GC_253_6,(0,1,3):C.R2GC_253_7,(0,2,0):C.R2GC_253_4,(0,2,1):C.R2GC_253_5,(0,2,2):C.R2GC_253_6,(0,2,3):C.R2GC_253_7})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(1,0,1):C.R2GC_259_34,(1,0,0):C.R2GC_259_35,(1,0,2):C.R2GC_259_36,(1,0,3):C.R2GC_259_37,(1,0,4):C.R2GC_259_38,(1,0,5):C.R2GC_259_39,(0,1,1):C.R2GC_258_28,(0,1,0):C.R2GC_258_29,(0,1,2):C.R2GC_258_30,(0,1,3):C.R2GC_258_31,(0,1,4):C.R2GC_258_32,(0,1,5):C.R2GC_258_33,(0,2,1):C.R2GC_258_28,(0,2,0):C.R2GC_258_29,(0,2,2):C.R2GC_258_30,(0,2,3):C.R2GC_258_31,(0,2,4):C.R2GC_258_32,(0,2,5):C.R2GC_258_33,(0,3,1):C.R2GC_258_28,(0,3,0):C.R2GC_258_29,(0,3,2):C.R2GC_258_30,(0,3,3):C.R2GC_258_31,(0,3,4):C.R2GC_258_32,(0,3,5):C.R2GC_258_33})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_254_8,(0,0,1):C.R2GC_254_9,(0,0,2):C.R2GC_254_10,(0,0,3):C.R2GC_254_11,(0,1,0):C.R2GC_254_8,(0,1,1):C.R2GC_254_9,(0,1,2):C.R2GC_254_10,(0,1,3):C.R2GC_254_11,(0,2,0):C.R2GC_254_8,(0,2,1):C.R2GC_254_9,(0,2,2):C.R2GC_254_10,(0,2,3):C.R2GC_254_11})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,4):C.R2GC_267_65,(0,0,0):C.R2GC_267_66,(0,0,1):C.R2GC_267_67,(0,0,2):C.R2GC_267_68,(0,0,3):C.R2GC_267_69,(0,0,6):C.R2GC_267_70,(0,0,5):C.R2GC_267_71})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,4):C.R2GC_266_58,(0,0,0):C.R2GC_266_59,(0,0,1):C.R2GC_266_60,(0,0,2):C.R2GC_266_61,(0,0,3):C.R2GC_266_62,(0,0,6):C.R2GC_266_63,(0,0,5):C.R2GC_266_64})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c] ], [ [P.c, P.tp] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_265_42,(0,0,1):C.R2GC_265_43,(0,0,5):C.R2GC_265_44,(0,0,7):C.R2GC_265_45,(0,0,8):C.R2GC_265_46,(0,0,9):C.R2GC_265_47,(0,0,10):C.R2GC_265_48,(0,0,13):C.R2GC_265_49,(0,0,14):C.R2GC_265_50,(0,0,15):C.R2GC_265_51,(0,0,2):C.R2GC_265_52,(0,0,3):C.R2GC_265_53,(0,0,4):C.R2GC_265_54,(0,0,6):C.R2GC_265_55,(0,0,12):C.R2GC_265_56,(0,0,11):C.R2GC_265_57})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus__, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.y] ], [ [P.c, P.s] ], [ [P.c, P.x] ], [ [P.d, P.tp] ], [ [P.d, P.u] ], [ [P.d, P.y] ], [ [P.s, P.tp] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,5):C.R2GC_270_92,(0,0,6):C.R2GC_270_93,(0,0,7):C.R2GC_270_94,(0,0,0):C.R2GC_270_95,(0,0,1):C.R2GC_270_96,(0,0,2):C.R2GC_270_97,(0,0,3):C.R2GC_270_98,(0,0,4):C.R2GC_270_99,(0,0,8):C.R2GC_270_100,(0,0,9):C.R2GC_270_101,(0,0,10):C.R2GC_270_102,(0,0,11):C.R2GC_270_103,(0,0,12):C.R2GC_270_104,(0,0,13):C.R2GC_270_105,(0,0,14):C.R2GC_270_106,(0,0,16):C.R2GC_270_107,(0,0,15):C.R2GC_270_108,(0,0,17):C.R2GC_270_109})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus____minus__, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.x] ], [ [P.b, P.x] ], [ [P.c, P.y] ], [ [P.d, P.x] ], [ [P.s, P.x] ], [ [P.tp, P.y] ], [ [P.t, P.y] ], [ [P.u, P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_269_84,(0,0,0):C.R2GC_269_85,(0,0,2):C.R2GC_269_86,(0,0,3):C.R2GC_269_87,(0,0,4):C.R2GC_269_88,(0,0,6):C.R2GC_269_89,(0,0,5):C.R2GC_269_90,(0,0,7):C.R2GC_269_91})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_346_74,(0,1,0):C.UVGC_347_75})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_386_166})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_390_170,(0,1,0):C.UVGC_397_189})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_432_280,(0,1,0):C.UVGC_433_281})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_473_413,(0,1,0):C.UVGC_474_414})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,1):C.UVGC_463_369,(0,1,0):C.UVGC_463_370,(0,1,4):C.UVGC_463_371,(0,1,5):C.UVGC_463_372,(0,1,6):C.UVGC_463_373,(0,1,7):C.UVGC_463_374,(0,2,2):C.UVGC_272_1,(0,0,3):C.UVGC_273_2})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(2,1,3):C.UVGC_285_9,(2,1,4):C.UVGC_285_8,(0,1,3):C.UVGC_285_9,(0,1,4):C.UVGC_285_8,(4,1,3):C.UVGC_284_6,(4,1,4):C.UVGC_284_7,(3,1,3):C.UVGC_284_6,(3,1,4):C.UVGC_284_7,(8,1,3):C.UVGC_285_8,(8,1,4):C.UVGC_285_9,(6,1,2):C.UVGC_468_400,(6,1,0):C.UVGC_468_401,(6,1,3):C.UVGC_469_408,(6,1,4):C.UVGC_469_409,(6,1,5):C.UVGC_468_404,(6,1,6):C.UVGC_468_405,(6,1,7):C.UVGC_468_406,(6,1,8):C.UVGC_468_407,(7,1,2):C.UVGC_468_400,(7,1,0):C.UVGC_468_401,(7,1,3):C.UVGC_468_402,(7,1,4):C.UVGC_468_403,(7,1,5):C.UVGC_468_404,(7,1,6):C.UVGC_468_405,(7,1,7):C.UVGC_468_406,(7,1,8):C.UVGC_468_407,(5,1,3):C.UVGC_284_6,(5,1,4):C.UVGC_284_7,(1,1,3):C.UVGC_284_6,(1,1,4):C.UVGC_284_7,(11,0,3):C.UVGC_288_12,(11,0,4):C.UVGC_288_13,(10,0,3):C.UVGC_288_12,(10,0,4):C.UVGC_288_13,(9,0,3):C.UVGC_287_10,(9,0,4):C.UVGC_287_11,(0,2,3):C.UVGC_285_9,(0,2,4):C.UVGC_285_8,(2,2,3):C.UVGC_285_9,(2,2,4):C.UVGC_285_8,(5,2,3):C.UVGC_284_6,(5,2,4):C.UVGC_284_7,(1,2,3):C.UVGC_284_6,(1,2,4):C.UVGC_284_7,(7,2,1):C.UVGC_289_14,(7,2,3):C.UVGC_290_16,(7,2,4):C.UVGC_290_17,(4,2,3):C.UVGC_284_6,(4,2,4):C.UVGC_284_7,(3,2,3):C.UVGC_284_6,(3,2,4):C.UVGC_284_7,(8,2,2):C.UVGC_467_392,(8,2,0):C.UVGC_467_393,(8,2,3):C.UVGC_467_394,(8,2,4):C.UVGC_467_395,(8,2,5):C.UVGC_467_396,(8,2,6):C.UVGC_467_397,(8,2,7):C.UVGC_467_398,(8,2,8):C.UVGC_467_399,(6,2,0):C.UVGC_465_383,(6,2,3):C.UVGC_465_384,(6,2,4):C.UVGC_465_385,(6,2,5):C.UVGC_465_386,(6,2,6):C.UVGC_465_387,(6,2,7):C.UVGC_465_388,(6,2,8):C.UVGC_465_389,(0,3,3):C.UVGC_285_9,(0,3,4):C.UVGC_285_8,(2,3,3):C.UVGC_285_9,(2,3,4):C.UVGC_285_8,(5,3,3):C.UVGC_284_6,(5,3,4):C.UVGC_284_7,(1,3,3):C.UVGC_284_6,(1,3,4):C.UVGC_284_7,(7,3,0):C.UVGC_465_383,(7,3,3):C.UVGC_466_390,(7,3,4):C.UVGC_466_391,(7,3,5):C.UVGC_465_386,(7,3,6):C.UVGC_465_387,(7,3,7):C.UVGC_465_388,(7,3,8):C.UVGC_465_389,(4,3,3):C.UVGC_284_6,(4,3,4):C.UVGC_284_7,(3,3,3):C.UVGC_284_6,(3,3,4):C.UVGC_284_7,(8,3,2):C.UVGC_464_375,(8,3,0):C.UVGC_464_376,(8,3,3):C.UVGC_464_377,(8,3,4):C.UVGC_464_378,(8,3,5):C.UVGC_464_379,(8,3,6):C.UVGC_464_380,(8,3,7):C.UVGC_464_381,(8,3,8):C.UVGC_464_382,(6,3,1):C.UVGC_289_14,(6,3,3):C.UVGC_289_15,(6,3,4):C.UVGC_287_10})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_292_19,(0,1,0):C.UVGC_338_54})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_300_32,(0,1,0):C.UVGC_388_168})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_327_41,(0,1,0):C.UVGC_430_278})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_329_42,(0,1,0):C.UVGC_471_411})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_309_35,(0,1,0):C.UVGC_310_36})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_315_37,(0,1,0):C.UVGC_316_38})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_295_30,(0,1,0):C.UVGC_296_31})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_325_39,(0,1,0):C.UVGC_326_40})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_303_33,(0,1,0):C.UVGC_304_34})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_375_143,(0,1,0):C.UVGC_374_142})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_343_65,(0,0,2):C.UVGC_343_66,(0,0,0):C.UVGC_343_67,(0,1,1):C.UVGC_340_56,(0,1,2):C.UVGC_340_57,(0,1,0):C.UVGC_340_58})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_344_68,(0,0,2):C.UVGC_344_69,(0,0,1):C.UVGC_344_70,(0,1,0):C.UVGC_341_59,(0,1,2):C.UVGC_341_60,(0,1,1):C.UVGC_341_61})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_345_71,(0,0,2):C.UVGC_345_72,(0,0,0):C.UVGC_345_73,(0,1,1):C.UVGC_342_62,(0,1,2):C.UVGC_342_63,(0,1,0):C.UVGC_342_64})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_409_223,(0,0,2):C.UVGC_409_224,(0,0,1):C.UVGC_409_225,(0,1,0):C.UVGC_406_214,(0,1,2):C.UVGC_406_215,(0,1,1):C.UVGC_406_216})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_410_226,(0,0,2):C.UVGC_410_227,(0,0,1):C.UVGC_410_228,(0,1,0):C.UVGC_407_217,(0,1,2):C.UVGC_407_218,(0,1,1):C.UVGC_407_219})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_411_229,(0,0,1):C.UVGC_411_230,(0,0,2):C.UVGC_411_231,(0,1,0):C.UVGC_408_220,(0,1,1):C.UVGC_408_221,(0,1,2):C.UVGC_408_222})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_351_85,(0,0,2):C.UVGC_351_86,(0,0,0):C.UVGC_351_87,(0,1,1):C.UVGC_348_76,(0,1,2):C.UVGC_348_77,(0,1,0):C.UVGC_348_78})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_352_88,(0,0,2):C.UVGC_352_89,(0,0,1):C.UVGC_352_90,(0,1,0):C.UVGC_349_79,(0,1,2):C.UVGC_349_80,(0,1,1):C.UVGC_349_81})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_353_91,(0,0,2):C.UVGC_353_92,(0,0,0):C.UVGC_353_93,(0,1,1):C.UVGC_350_82,(0,1,2):C.UVGC_350_83,(0,1,0):C.UVGC_350_84})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_394_180,(0,0,2):C.UVGC_394_181,(0,0,1):C.UVGC_394_182,(0,1,0):C.UVGC_391_171,(0,1,2):C.UVGC_391_172,(0,1,1):C.UVGC_391_173})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_395_183,(0,0,2):C.UVGC_395_184,(0,0,1):C.UVGC_395_185,(0,1,0):C.UVGC_392_174,(0,1,2):C.UVGC_392_175,(0,1,1):C.UVGC_392_176})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_396_186,(0,0,1):C.UVGC_396_187,(0,0,2):C.UVGC_396_188,(0,1,0):C.UVGC_393_177,(0,1,1):C.UVGC_393_178,(0,1,2):C.UVGC_393_179})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_476_418,(0,0,2):C.UVGC_476_419,(0,0,1):C.UVGC_476_420,(0,1,0):C.UVGC_475_415,(0,1,2):C.UVGC_475_416,(0,1,1):C.UVGC_475_417})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_399_193,(0,0,2):C.UVGC_399_194,(0,0,1):C.UVGC_399_195,(0,1,0):C.UVGC_398_190,(0,1,2):C.UVGC_398_191,(0,1,1):C.UVGC_398_192})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_435_285,(0,0,2):C.UVGC_435_286,(0,0,1):C.UVGC_435_287,(0,1,0):C.UVGC_434_282,(0,1,2):C.UVGC_434_283,(0,1,1):C.UVGC_434_284})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_356_100,(0,0,2):C.UVGC_356_101,(0,0,1):C.UVGC_356_102,(0,1,0):C.UVGC_354_94,(0,1,2):C.UVGC_354_95,(0,1,1):C.UVGC_354_96})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_357_103,(0,0,2):C.UVGC_357_104,(0,0,0):C.UVGC_357_105,(0,1,1):C.UVGC_355_97,(0,1,2):C.UVGC_355_98,(0,1,0):C.UVGC_355_99})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_377_147,(0,0,2):C.UVGC_377_148,(0,0,1):C.UVGC_377_149,(0,1,0):C.UVGC_376_144,(0,1,2):C.UVGC_376_145,(0,1,1):C.UVGC_376_146})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_335_51,(0,0,1):C.UVGC_335_52,(0,1,0):C.UVGC_334_49,(0,1,1):C.UVGC_334_50})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_332_45,(0,0,1):C.UVGC_332_46,(0,1,0):C.UVGC_331_43,(0,1,1):C.UVGC_331_44})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_379_153,(0,0,2):C.UVGC_379_154,(0,0,1):C.UVGC_379_155,(0,1,0):C.UVGC_378_150,(0,1,2):C.UVGC_378_151,(0,1,1):C.UVGC_378_152})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_403_205,(0,0,2):C.UVGC_403_206,(0,0,1):C.UVGC_403_207,(0,1,0):C.UVGC_400_196,(0,1,2):C.UVGC_400_197,(0,1,1):C.UVGC_400_198})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_404_208,(0,0,2):C.UVGC_404_209,(0,0,1):C.UVGC_404_210,(0,1,0):C.UVGC_401_199,(0,1,2):C.UVGC_401_200,(0,1,1):C.UVGC_401_201})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_405_211,(0,0,2):C.UVGC_405_212,(0,0,1):C.UVGC_405_213,(0,1,0):C.UVGC_402_202,(0,1,2):C.UVGC_402_203,(0,1,1):C.UVGC_402_204})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_439_297,(0,0,2):C.UVGC_439_298,(0,0,1):C.UVGC_439_299,(0,1,0):C.UVGC_436_288,(0,1,2):C.UVGC_436_289,(0,1,1):C.UVGC_436_290})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_440_300,(0,0,2):C.UVGC_440_301,(0,0,1):C.UVGC_440_302,(0,1,0):C.UVGC_437_291,(0,1,2):C.UVGC_437_292,(0,1,1):C.UVGC_437_293})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_441_303,(0,0,2):C.UVGC_441_304,(0,0,1):C.UVGC_441_305,(0,1,0):C.UVGC_438_294,(0,1,2):C.UVGC_438_295,(0,1,1):C.UVGC_438_296})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_480_430,(0,0,2):C.UVGC_480_431,(0,0,1):C.UVGC_480_432,(0,1,0):C.UVGC_477_421,(0,1,2):C.UVGC_477_422,(0,1,1):C.UVGC_477_423})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_481_433,(0,0,2):C.UVGC_481_434,(0,0,1):C.UVGC_481_435,(0,1,0):C.UVGC_478_424,(0,1,2):C.UVGC_478_425,(0,1,1):C.UVGC_478_426})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_482_436,(0,0,2):C.UVGC_482_437,(0,0,1):C.UVGC_482_438,(0,1,0):C.UVGC_479_427,(0,1,2):C.UVGC_479_428,(0,1,1):C.UVGC_479_429})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_443_309,(0,0,2):C.UVGC_443_310,(0,0,1):C.UVGC_443_311,(0,1,0):C.UVGC_442_306,(0,1,2):C.UVGC_442_307,(0,1,1):C.UVGC_442_308})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_484_442,(0,0,2):C.UVGC_484_443,(0,0,1):C.UVGC_484_444,(0,1,0):C.UVGC_483_439,(0,1,2):C.UVGC_483_440,(0,1,1):C.UVGC_483_441})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_447_321,(0,0,2):C.UVGC_447_322,(0,0,1):C.UVGC_447_323,(0,1,0):C.UVGC_444_312,(0,1,2):C.UVGC_444_313,(0,1,1):C.UVGC_444_314})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_448_324,(0,0,2):C.UVGC_448_325,(0,0,1):C.UVGC_448_326,(0,1,0):C.UVGC_445_315,(0,1,2):C.UVGC_445_316,(0,1,1):C.UVGC_445_317})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_449_327,(0,0,2):C.UVGC_449_328,(0,0,1):C.UVGC_449_329,(0,1,0):C.UVGC_446_318,(0,1,2):C.UVGC_446_319,(0,1,1):C.UVGC_446_320})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_488_454,(0,0,2):C.UVGC_488_455,(0,0,1):C.UVGC_488_456,(0,1,0):C.UVGC_485_445,(0,1,2):C.UVGC_485_446,(0,1,1):C.UVGC_485_447})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_489_457,(0,0,2):C.UVGC_489_458,(0,0,1):C.UVGC_489_459,(0,1,0):C.UVGC_486_448,(0,1,2):C.UVGC_486_449,(0,1,1):C.UVGC_486_450})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_490_460,(0,0,2):C.UVGC_490_461,(0,0,1):C.UVGC_490_462,(0,1,0):C.UVGC_487_451,(0,1,2):C.UVGC_487_452,(0,1,1):C.UVGC_487_453})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_475_415,(0,0,2):C.UVGC_475_416,(0,0,1):C.UVGC_475_417,(0,1,0):C.UVGC_476_418,(0,1,2):C.UVGC_476_419,(0,1,1):C.UVGC_476_420})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_398_190,(0,0,2):C.UVGC_398_191,(0,0,1):C.UVGC_398_192,(0,1,0):C.UVGC_399_193,(0,1,2):C.UVGC_399_194,(0,1,1):C.UVGC_399_195})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_434_282,(0,0,2):C.UVGC_434_283,(0,0,1):C.UVGC_434_284,(0,1,0):C.UVGC_435_285,(0,1,2):C.UVGC_435_286,(0,1,1):C.UVGC_435_287})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_442_306,(0,0,2):C.UVGC_442_307,(0,0,1):C.UVGC_442_308,(0,1,0):C.UVGC_443_309,(0,1,2):C.UVGC_443_310,(0,1,1):C.UVGC_443_311})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_483_439,(0,0,2):C.UVGC_483_440,(0,0,1):C.UVGC_483_441,(0,1,0):C.UVGC_484_442,(0,1,2):C.UVGC_484_443,(0,1,1):C.UVGC_484_444})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_348_76,(0,0,2):C.UVGC_348_77,(0,0,0):C.UVGC_348_78,(0,1,1):C.UVGC_351_85,(0,1,2):C.UVGC_351_86,(0,1,0):C.UVGC_351_87})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_349_79,(0,0,2):C.UVGC_349_80,(0,0,1):C.UVGC_349_81,(0,1,0):C.UVGC_352_88,(0,1,2):C.UVGC_352_89,(0,1,1):C.UVGC_352_90})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_350_82,(0,0,2):C.UVGC_350_83,(0,0,0):C.UVGC_350_84,(0,1,1):C.UVGC_353_91,(0,1,2):C.UVGC_353_92,(0,1,0):C.UVGC_353_93})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_391_171,(0,0,2):C.UVGC_391_172,(0,0,1):C.UVGC_391_173,(0,1,0):C.UVGC_394_180,(0,1,2):C.UVGC_394_181,(0,1,1):C.UVGC_394_182})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_392_174,(0,0,2):C.UVGC_392_175,(0,0,1):C.UVGC_392_176,(0,1,0):C.UVGC_395_183,(0,1,2):C.UVGC_395_184,(0,1,1):C.UVGC_395_185})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_393_177,(0,0,1):C.UVGC_393_178,(0,0,2):C.UVGC_393_179,(0,1,0):C.UVGC_396_186,(0,1,1):C.UVGC_396_187,(0,1,2):C.UVGC_396_188})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_354_94,(0,0,2):C.UVGC_354_95,(0,0,1):C.UVGC_354_96,(0,1,0):C.UVGC_356_100,(0,1,2):C.UVGC_356_101,(0,1,1):C.UVGC_356_102})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_355_97,(0,0,2):C.UVGC_355_98,(0,0,0):C.UVGC_355_99,(0,1,1):C.UVGC_357_103,(0,1,2):C.UVGC_357_104,(0,1,0):C.UVGC_357_105})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_376_144,(0,0,2):C.UVGC_376_145,(0,0,1):C.UVGC_376_146,(0,1,0):C.UVGC_377_147,(0,1,2):C.UVGC_377_148,(0,1,1):C.UVGC_377_149})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_334_49,(0,0,1):C.UVGC_334_50,(0,1,0):C.UVGC_335_51,(0,1,1):C.UVGC_335_52})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_331_43,(0,0,1):C.UVGC_331_44,(0,1,0):C.UVGC_332_45,(0,1,1):C.UVGC_332_46})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_378_150,(0,0,2):C.UVGC_378_151,(0,0,1):C.UVGC_378_152,(0,1,0):C.UVGC_379_153,(0,1,2):C.UVGC_379_154,(0,1,1):C.UVGC_379_155})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_400_196,(0,0,2):C.UVGC_400_197,(0,0,1):C.UVGC_400_198,(0,1,0):C.UVGC_403_205,(0,1,2):C.UVGC_403_206,(0,1,1):C.UVGC_403_207})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_401_199,(0,0,2):C.UVGC_401_200,(0,0,1):C.UVGC_401_201,(0,1,0):C.UVGC_404_208,(0,1,2):C.UVGC_404_209,(0,1,1):C.UVGC_404_210})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_402_202,(0,0,2):C.UVGC_402_203,(0,0,1):C.UVGC_402_204,(0,1,0):C.UVGC_405_211,(0,1,2):C.UVGC_405_212,(0,1,1):C.UVGC_405_213})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_436_288,(0,0,2):C.UVGC_436_289,(0,0,1):C.UVGC_436_290,(0,1,0):C.UVGC_439_297,(0,1,2):C.UVGC_439_298,(0,1,1):C.UVGC_439_299})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_437_291,(0,0,2):C.UVGC_437_292,(0,0,1):C.UVGC_437_293,(0,1,0):C.UVGC_440_300,(0,1,2):C.UVGC_440_301,(0,1,1):C.UVGC_440_302})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_438_294,(0,0,2):C.UVGC_438_295,(0,0,1):C.UVGC_438_296,(0,1,0):C.UVGC_441_303,(0,1,2):C.UVGC_441_304,(0,1,1):C.UVGC_441_305})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_477_421,(0,0,2):C.UVGC_477_422,(0,0,1):C.UVGC_477_423,(0,1,0):C.UVGC_480_430,(0,1,2):C.UVGC_480_431,(0,1,1):C.UVGC_480_432})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_478_424,(0,0,2):C.UVGC_478_425,(0,0,1):C.UVGC_478_426,(0,1,0):C.UVGC_481_433,(0,1,2):C.UVGC_481_434,(0,1,1):C.UVGC_481_435})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_479_427,(0,0,2):C.UVGC_479_428,(0,0,1):C.UVGC_479_429,(0,1,0):C.UVGC_482_436,(0,1,2):C.UVGC_482_437,(0,1,1):C.UVGC_482_438})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_444_312,(0,0,2):C.UVGC_444_313,(0,0,1):C.UVGC_444_314,(0,1,0):C.UVGC_447_321,(0,1,2):C.UVGC_447_322,(0,1,1):C.UVGC_447_323})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_445_315,(0,0,2):C.UVGC_445_316,(0,0,1):C.UVGC_445_317,(0,1,0):C.UVGC_448_324,(0,1,2):C.UVGC_448_325,(0,1,1):C.UVGC_448_326})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_446_318,(0,0,2):C.UVGC_446_319,(0,0,1):C.UVGC_446_320,(0,1,0):C.UVGC_449_327,(0,1,2):C.UVGC_449_328,(0,1,1):C.UVGC_449_329})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_485_445,(0,0,2):C.UVGC_485_446,(0,0,1):C.UVGC_485_447,(0,1,0):C.UVGC_488_454,(0,1,2):C.UVGC_488_455,(0,1,1):C.UVGC_488_456})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_486_448,(0,0,2):C.UVGC_486_449,(0,0,1):C.UVGC_486_450,(0,1,0):C.UVGC_489_457,(0,1,2):C.UVGC_489_458,(0,1,1):C.UVGC_489_459})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_487_451,(0,0,2):C.UVGC_487_452,(0,0,1):C.UVGC_487_453,(0,1,0):C.UVGC_490_460,(0,1,2):C.UVGC_490_461,(0,1,1):C.UVGC_490_462})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_340_56,(0,0,2):C.UVGC_340_57,(0,0,0):C.UVGC_340_58,(0,1,1):C.UVGC_343_65,(0,1,2):C.UVGC_343_66,(0,1,0):C.UVGC_343_67})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_341_59,(0,0,2):C.UVGC_341_60,(0,0,1):C.UVGC_341_61,(0,1,0):C.UVGC_344_68,(0,1,2):C.UVGC_344_69,(0,1,1):C.UVGC_344_70})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_342_62,(0,0,2):C.UVGC_342_63,(0,0,0):C.UVGC_342_64,(0,1,1):C.UVGC_345_71,(0,1,2):C.UVGC_345_72,(0,1,0):C.UVGC_345_73})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_406_214,(0,0,2):C.UVGC_406_215,(0,0,1):C.UVGC_406_216,(0,1,0):C.UVGC_409_223,(0,1,2):C.UVGC_409_224,(0,1,1):C.UVGC_409_225})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_407_217,(0,0,2):C.UVGC_407_218,(0,0,1):C.UVGC_407_219,(0,1,0):C.UVGC_410_226,(0,1,2):C.UVGC_410_227,(0,1,1):C.UVGC_410_228})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_408_220,(0,0,1):C.UVGC_408_221,(0,0,2):C.UVGC_408_222,(0,1,0):C.UVGC_411_229,(0,1,1):C.UVGC_411_230,(0,1,2):C.UVGC_411_231})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,2):C.UVGC_293_22,(0,1,3):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,4):C.UVGC_389_169})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.bp, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,3):C.UVGC_293_22,(0,1,4):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,2):C.UVGC_339_55})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.x] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,2):C.UVGC_293_22,(0,1,3):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,4):C.UVGC_431_279})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.y] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,2):C.UVGC_293_22,(0,1,3):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,4):C.UVGC_472_412})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_413_233,(0,0,2):C.UVGC_413_234,(0,0,1):C.UVGC_413_235,(0,1,0):C.UVGC_419_251,(0,1,2):C.UVGC_419_252,(0,1,1):C.UVGC_419_253})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_414_236,(0,0,2):C.UVGC_414_237,(0,0,1):C.UVGC_414_238,(0,1,0):C.UVGC_420_254,(0,1,2):C.UVGC_420_255,(0,1,1):C.UVGC_420_256})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_415_239,(0,0,2):C.UVGC_415_240,(0,0,1):C.UVGC_415_241,(0,1,0):C.UVGC_421_257,(0,1,2):C.UVGC_421_258,(0,1,1):C.UVGC_421_259})

V_292 = CTVertex(name = 'V_292',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_453_337,(0,0,2):C.UVGC_453_338,(0,0,1):C.UVGC_453_339,(0,1,0):C.UVGC_456_346,(0,1,2):C.UVGC_456_347,(0,1,1):C.UVGC_456_348})

V_293 = CTVertex(name = 'V_293',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_454_340,(0,0,2):C.UVGC_454_341,(0,0,1):C.UVGC_454_342,(0,1,0):C.UVGC_457_349,(0,1,2):C.UVGC_457_350,(0,1,1):C.UVGC_457_351})

V_294 = CTVertex(name = 'V_294',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_455_343,(0,0,2):C.UVGC_455_344,(0,0,1):C.UVGC_455_345,(0,1,0):C.UVGC_458_352,(0,1,2):C.UVGC_458_353,(0,1,1):C.UVGC_458_354})

V_295 = CTVertex(name = 'V_295',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_359_107,(0,0,2):C.UVGC_359_108,(0,0,1):C.UVGC_359_109,(0,1,0):C.UVGC_364_122,(0,1,2):C.UVGC_364_123,(0,1,1):C.UVGC_364_124})

V_296 = CTVertex(name = 'V_296',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_360_110,(0,0,2):C.UVGC_360_111,(0,0,0):C.UVGC_360_112,(0,1,1):C.UVGC_365_125,(0,1,2):C.UVGC_365_126,(0,1,0):C.UVGC_365_127})

V_297 = CTVertex(name = 'V_297',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_382_158,(0,0,2):C.UVGC_382_159,(0,0,1):C.UVGC_382_160,(0,1,0):C.UVGC_383_161,(0,1,2):C.UVGC_383_162,(0,1,1):C.UVGC_383_163})

V_298 = CTVertex(name = 'V_298',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_494_470,(0,0,2):C.UVGC_494_471,(0,0,1):C.UVGC_494_472,(0,1,0):C.UVGC_497_479,(0,1,2):C.UVGC_497_480,(0,1,1):C.UVGC_497_481})

V_299 = CTVertex(name = 'V_299',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_495_473,(0,0,2):C.UVGC_495_474,(0,0,1):C.UVGC_495_475,(0,1,0):C.UVGC_498_482,(0,1,2):C.UVGC_498_483,(0,1,1):C.UVGC_498_484})

V_300 = CTVertex(name = 'V_300',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_496_476,(0,0,2):C.UVGC_496_477,(0,0,1):C.UVGC_496_478,(0,1,0):C.UVGC_499_485,(0,1,2):C.UVGC_499_486,(0,1,1):C.UVGC_499_487})

V_301 = CTVertex(name = 'V_301',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_361_113,(0,0,2):C.UVGC_361_114,(0,0,0):C.UVGC_361_115,(0,1,1):C.UVGC_366_128,(0,1,2):C.UVGC_366_129,(0,1,0):C.UVGC_366_130})

V_302 = CTVertex(name = 'V_302',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_362_116,(0,0,2):C.UVGC_362_117,(0,0,1):C.UVGC_362_118,(0,1,0):C.UVGC_367_131,(0,1,2):C.UVGC_367_132,(0,1,1):C.UVGC_367_133})

V_303 = CTVertex(name = 'V_303',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_363_119,(0,0,2):C.UVGC_363_120,(0,0,0):C.UVGC_363_121,(0,1,1):C.UVGC_368_134,(0,1,2):C.UVGC_368_135,(0,1,0):C.UVGC_368_136})

V_304 = CTVertex(name = 'V_304',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_416_242,(0,0,2):C.UVGC_416_243,(0,0,1):C.UVGC_416_244,(0,1,0):C.UVGC_422_260,(0,1,2):C.UVGC_422_261,(0,1,1):C.UVGC_422_262})

V_305 = CTVertex(name = 'V_305',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_417_245,(0,0,2):C.UVGC_417_246,(0,0,1):C.UVGC_417_247,(0,1,0):C.UVGC_423_263,(0,1,2):C.UVGC_423_264,(0,1,1):C.UVGC_423_265})

V_306 = CTVertex(name = 'V_306',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_418_248,(0,0,1):C.UVGC_418_249,(0,0,2):C.UVGC_418_250,(0,1,0):C.UVGC_424_266,(0,1,1):C.UVGC_424_267,(0,1,2):C.UVGC_424_268})

V_307 = CTVertex(name = 'V_307',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_492_464,(0,0,2):C.UVGC_492_465,(0,0,1):C.UVGC_492_466,(0,1,0):C.UVGC_493_467,(0,1,2):C.UVGC_493_468,(0,1,1):C.UVGC_493_469})

V_308 = CTVertex(name = 'V_308',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_425_269,(0,0,2):C.UVGC_425_270,(0,0,1):C.UVGC_425_271,(0,1,0):C.UVGC_426_272,(0,1,2):C.UVGC_426_273,(0,1,1):C.UVGC_426_274})

V_309 = CTVertex(name = 'V_309',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_451_331,(0,0,2):C.UVGC_451_332,(0,0,1):C.UVGC_451_333,(0,1,0):C.UVGC_452_334,(0,1,2):C.UVGC_452_335,(0,1,1):C.UVGC_452_336})

V_310 = CTVertex(name = 'V_310',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_492_464,(0,0,2):C.UVGC_492_465,(0,0,1):C.UVGC_492_466,(0,1,0):C.UVGC_493_467,(0,1,2):C.UVGC_493_468,(0,1,1):C.UVGC_493_469})

V_311 = CTVertex(name = 'V_311',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_425_269,(0,0,2):C.UVGC_425_270,(0,0,1):C.UVGC_425_271,(0,1,0):C.UVGC_426_272,(0,1,2):C.UVGC_426_273,(0,1,1):C.UVGC_426_274})

V_312 = CTVertex(name = 'V_312',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_451_331,(0,0,2):C.UVGC_451_332,(0,0,1):C.UVGC_451_333,(0,1,0):C.UVGC_452_334,(0,1,2):C.UVGC_452_335,(0,1,1):C.UVGC_452_336})

V_313 = CTVertex(name = 'V_313',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_413_233,(0,0,2):C.UVGC_413_234,(0,0,1):C.UVGC_413_235,(0,1,0):C.UVGC_419_251,(0,1,2):C.UVGC_419_252,(0,1,1):C.UVGC_419_253})

V_314 = CTVertex(name = 'V_314',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_414_236,(0,0,2):C.UVGC_414_237,(0,0,1):C.UVGC_414_238,(0,1,0):C.UVGC_420_254,(0,1,2):C.UVGC_420_255,(0,1,1):C.UVGC_420_256})

V_315 = CTVertex(name = 'V_315',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_415_239,(0,0,2):C.UVGC_415_240,(0,0,1):C.UVGC_415_241,(0,1,0):C.UVGC_421_257,(0,1,2):C.UVGC_421_258,(0,1,1):C.UVGC_421_259})

V_316 = CTVertex(name = 'V_316',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_453_337,(0,0,2):C.UVGC_453_338,(0,0,1):C.UVGC_453_339,(0,1,0):C.UVGC_456_346,(0,1,2):C.UVGC_456_347,(0,1,1):C.UVGC_456_348})

V_317 = CTVertex(name = 'V_317',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_454_340,(0,0,2):C.UVGC_454_341,(0,0,1):C.UVGC_454_342,(0,1,0):C.UVGC_457_349,(0,1,2):C.UVGC_457_350,(0,1,1):C.UVGC_457_351})

V_318 = CTVertex(name = 'V_318',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_455_343,(0,0,2):C.UVGC_455_344,(0,0,1):C.UVGC_455_345,(0,1,0):C.UVGC_458_352,(0,1,2):C.UVGC_458_353,(0,1,1):C.UVGC_458_354})

V_319 = CTVertex(name = 'V_319',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_359_107,(0,0,2):C.UVGC_359_108,(0,0,1):C.UVGC_359_109,(0,1,0):C.UVGC_364_122,(0,1,2):C.UVGC_364_123,(0,1,1):C.UVGC_364_124})

V_320 = CTVertex(name = 'V_320',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_360_110,(0,0,2):C.UVGC_360_111,(0,0,0):C.UVGC_360_112,(0,1,1):C.UVGC_365_125,(0,1,2):C.UVGC_365_126,(0,1,0):C.UVGC_365_127})

V_321 = CTVertex(name = 'V_321',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_382_158,(0,0,2):C.UVGC_382_159,(0,0,1):C.UVGC_382_160,(0,1,0):C.UVGC_383_161,(0,1,2):C.UVGC_383_162,(0,1,1):C.UVGC_383_163})

V_322 = CTVertex(name = 'V_322',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_494_470,(0,0,2):C.UVGC_494_471,(0,0,1):C.UVGC_494_472,(0,1,0):C.UVGC_497_479,(0,1,2):C.UVGC_497_480,(0,1,1):C.UVGC_497_481})

V_323 = CTVertex(name = 'V_323',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_495_473,(0,0,2):C.UVGC_495_474,(0,0,1):C.UVGC_495_475,(0,1,0):C.UVGC_498_482,(0,1,2):C.UVGC_498_483,(0,1,1):C.UVGC_498_484})

V_324 = CTVertex(name = 'V_324',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_496_476,(0,0,2):C.UVGC_496_477,(0,0,1):C.UVGC_496_478,(0,1,0):C.UVGC_499_485,(0,1,2):C.UVGC_499_486,(0,1,1):C.UVGC_499_487})

V_325 = CTVertex(name = 'V_325',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_369_137,(0,1,0):C.UVGC_370_138})

V_326 = CTVertex(name = 'V_326',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_427_275,(0,1,0):C.UVGC_428_276})

V_327 = CTVertex(name = 'V_327',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_459_355,(0,1,0):C.UVGC_460_356})

V_328 = CTVertex(name = 'V_328',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_500_488,(0,1,0):C.UVGC_501_489})

V_329 = CTVertex(name = 'V_329',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_361_113,(0,0,2):C.UVGC_361_114,(0,0,0):C.UVGC_361_115,(0,1,1):C.UVGC_366_128,(0,1,2):C.UVGC_366_129,(0,1,0):C.UVGC_366_130})

V_330 = CTVertex(name = 'V_330',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_362_116,(0,0,2):C.UVGC_362_117,(0,0,1):C.UVGC_362_118,(0,1,0):C.UVGC_367_131,(0,1,2):C.UVGC_367_132,(0,1,1):C.UVGC_367_133})

V_331 = CTVertex(name = 'V_331',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_363_119,(0,0,2):C.UVGC_363_120,(0,0,0):C.UVGC_363_121,(0,1,1):C.UVGC_368_134,(0,1,2):C.UVGC_368_135,(0,1,0):C.UVGC_368_136})

V_332 = CTVertex(name = 'V_332',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_416_242,(0,0,2):C.UVGC_416_243,(0,0,1):C.UVGC_416_244,(0,1,0):C.UVGC_422_260,(0,1,2):C.UVGC_422_261,(0,1,1):C.UVGC_422_262})

V_333 = CTVertex(name = 'V_333',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_417_245,(0,0,2):C.UVGC_417_246,(0,0,1):C.UVGC_417_247,(0,1,0):C.UVGC_423_263,(0,1,2):C.UVGC_423_264,(0,1,1):C.UVGC_423_265})

V_334 = CTVertex(name = 'V_334',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_418_248,(0,0,1):C.UVGC_418_249,(0,0,2):C.UVGC_418_250,(0,1,0):C.UVGC_424_266,(0,1,1):C.UVGC_424_267,(0,1,2):C.UVGC_424_268})

V_335 = CTVertex(name = 'V_335',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_300_32,(0,1,0):C.UVGC_277_5,(0,2,0):C.UVGC_277_5})

V_336 = CTVertex(name = 'V_336',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_300_32,(0,1,0):C.UVGC_277_5,(0,2,0):C.UVGC_277_5})

V_337 = CTVertex(name = 'V_337',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_300_32,(0,1,0):C.UVGC_372_140,(0,2,0):C.UVGC_372_140})

V_338 = CTVertex(name = 'V_338',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_292_19,(0,1,0):C.UVGC_275_4,(0,2,0):C.UVGC_275_4})

V_339 = CTVertex(name = 'V_339',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_292_19,(0,1,0):C.UVGC_275_4,(0,2,0):C.UVGC_275_4})

V_340 = CTVertex(name = 'V_340',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_292_19,(0,1,0):C.UVGC_275_4,(0,2,0):C.UVGC_275_4})

V_341 = CTVertex(name = 'V_341',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,2):C.UVGC_293_22,(0,1,3):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,4):C.UVGC_293_28,(0,2,1):C.UVGC_293_20,(0,2,0):C.UVGC_293_21,(0,2,2):C.UVGC_293_22,(0,2,3):C.UVGC_293_23,(0,2,5):C.UVGC_293_24,(0,2,6):C.UVGC_293_25,(0,2,7):C.UVGC_293_26,(0,2,8):C.UVGC_293_27,(0,2,4):C.UVGC_293_28})

V_342 = CTVertex(name = 'V_342',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,3):C.UVGC_293_22,(0,1,4):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,2):C.UVGC_293_28,(0,2,1):C.UVGC_293_20,(0,2,0):C.UVGC_293_21,(0,2,3):C.UVGC_293_22,(0,2,4):C.UVGC_293_23,(0,2,5):C.UVGC_293_24,(0,2,6):C.UVGC_293_25,(0,2,7):C.UVGC_293_26,(0,2,8):C.UVGC_293_27,(0,2,2):C.UVGC_293_28})

V_343 = CTVertex(name = 'V_343',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,2):C.UVGC_293_22,(0,1,3):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,4):C.UVGC_373_141,(0,2,1):C.UVGC_293_20,(0,2,0):C.UVGC_293_21,(0,2,2):C.UVGC_293_22,(0,2,3):C.UVGC_293_23,(0,2,5):C.UVGC_293_24,(0,2,6):C.UVGC_293_25,(0,2,7):C.UVGC_293_26,(0,2,8):C.UVGC_293_27,(0,2,4):C.UVGC_373_141})

V_344 = CTVertex(name = 'V_344',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,3):C.UVGC_293_22,(0,1,4):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,2):C.UVGC_293_28,(0,2,1):C.UVGC_293_20,(0,2,0):C.UVGC_293_21,(0,2,3):C.UVGC_293_22,(0,2,4):C.UVGC_293_23,(0,2,5):C.UVGC_293_24,(0,2,6):C.UVGC_293_25,(0,2,7):C.UVGC_293_26,(0,2,8):C.UVGC_293_27,(0,2,2):C.UVGC_293_28})

V_345 = CTVertex(name = 'V_345',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,4):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,2):C.UVGC_293_22,(0,1,3):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,4):C.UVGC_293_28,(0,2,1):C.UVGC_293_20,(0,2,0):C.UVGC_293_21,(0,2,2):C.UVGC_293_22,(0,2,3):C.UVGC_293_23,(0,2,5):C.UVGC_293_24,(0,2,6):C.UVGC_293_25,(0,2,7):C.UVGC_293_26,(0,2,8):C.UVGC_293_27,(0,2,4):C.UVGC_293_28})

V_346 = CTVertex(name = 'V_346',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_294_29,(0,1,1):C.UVGC_293_20,(0,1,0):C.UVGC_293_21,(0,1,3):C.UVGC_293_22,(0,1,4):C.UVGC_293_23,(0,1,5):C.UVGC_293_24,(0,1,6):C.UVGC_293_25,(0,1,7):C.UVGC_293_26,(0,1,8):C.UVGC_293_27,(0,1,2):C.UVGC_293_28,(0,2,1):C.UVGC_293_20,(0,2,0):C.UVGC_293_21,(0,2,3):C.UVGC_293_22,(0,2,4):C.UVGC_293_23,(0,2,5):C.UVGC_293_24,(0,2,6):C.UVGC_293_25,(0,2,7):C.UVGC_293_26,(0,2,8):C.UVGC_293_27,(0,2,2):C.UVGC_293_28})

V_347 = CTVertex(name = 'V_347',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_333_47,(0,0,1):C.UVGC_333_48})

V_348 = CTVertex(name = 'V_348',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_333_47,(0,0,1):C.UVGC_333_48})

V_349 = CTVertex(name = 'V_349',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_333_47,(0,0,2):C.UVGC_381_157,(0,0,1):C.UVGC_333_48})

V_350 = CTVertex(name = 'V_350',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_333_47,(0,0,1):C.UVGC_333_48})

V_351 = CTVertex(name = 'V_351',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_333_47,(0,0,1):C.UVGC_333_48})

V_352 = CTVertex(name = 'V_352',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_333_47,(0,0,2):C.UVGC_381_157,(0,0,1):C.UVGC_333_48})

V_353 = CTVertex(name = 'V_353',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_384_164,(0,1,0):C.UVGC_385_165})

V_354 = CTVertex(name = 'V_354',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_291_18,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_355 = CTVertex(name = 'V_355',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_291_18,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_356 = CTVertex(name = 'V_356',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_380_156,(0,2,0):C.UVGC_380_156,(0,1,0):C.UVGC_371_139,(0,3,0):C.UVGC_371_139})

V_357 = CTVertex(name = 'V_357',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_291_18,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_358 = CTVertex(name = 'V_358',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_291_18,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_359 = CTVertex(name = 'V_359',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_291_18,(0,1,0):C.UVGC_274_3,(0,2,0):C.UVGC_274_3})

V_360 = CTVertex(name = 'V_360',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_450_330,(0,2,0):C.UVGC_450_330,(0,1,0):C.UVGC_429_277,(0,3,0):C.UVGC_429_277})

V_361 = CTVertex(name = 'V_361',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_412_232,(0,2,0):C.UVGC_412_232,(0,1,0):C.UVGC_387_167,(0,3,0):C.UVGC_387_167})

V_362 = CTVertex(name = 'V_362',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_358_106,(0,2,0):C.UVGC_358_106,(0,1,0):C.UVGC_337_53,(0,3,0):C.UVGC_337_53})

V_363 = CTVertex(name = 'V_363',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_491_463,(0,2,0):C.UVGC_491_463,(0,1,0):C.UVGC_470_410,(0,3,0):C.UVGC_470_410})

V_364 = CTVertex(name = 'V_364',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.bp] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_462_362,(0,0,1):C.UVGC_462_363,(0,0,2):C.UVGC_462_364,(0,0,3):C.UVGC_462_365,(0,0,4):C.UVGC_462_366,(0,0,5):C.UVGC_462_367,(0,0,6):C.UVGC_462_368,(0,1,0):C.UVGC_461_357,(0,1,3):C.UVGC_461_358,(0,1,4):C.UVGC_461_359,(0,1,5):C.UVGC_461_360,(0,1,6):C.UVGC_461_361})

