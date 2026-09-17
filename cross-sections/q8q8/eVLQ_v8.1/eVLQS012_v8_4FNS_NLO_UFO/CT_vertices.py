# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Wed 27 Jul 2022 15:38:55


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
               couplings = {(0,0,0):C.R2GC_352_179})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_362_186,(0,1,0):C.R2GC_363_187})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_404_223})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.tp__tilde__, P.tp, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.tp] ] ],
               couplings = {(0,0,0):C.R2GC_408_224,(0,1,0):C.R2GC_415_231})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.x__tilde__, P.x, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.x] ] ],
               couplings = {(0,0,0):C.R2GC_450_263,(0,1,0):C.R2GC_451_264})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.y__tilde__, P.y, P.s0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.y] ] ],
               couplings = {(0,0,0):C.R2GC_491_304,(0,1,0):C.R2GC_492_305})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_481_295,(0,0,1):C.R2GC_481_296})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_293_143,(2,1,1):C.R2GC_293_144,(0,1,0):C.R2GC_293_143,(0,1,1):C.R2GC_293_144,(4,1,0):C.R2GC_291_139,(4,1,1):C.R2GC_291_140,(3,1,0):C.R2GC_291_139,(3,1,1):C.R2GC_291_140,(8,1,0):C.R2GC_292_141,(8,1,1):C.R2GC_292_142,(6,1,0):C.R2GC_296_148,(6,1,1):C.R2GC_487_303,(7,1,0):C.R2GC_297_150,(7,1,1):C.R2GC_486_302,(5,1,0):C.R2GC_291_139,(5,1,1):C.R2GC_291_140,(1,1,0):C.R2GC_291_139,(1,1,1):C.R2GC_291_140,(11,0,0):C.R2GC_295_146,(11,0,1):C.R2GC_295_147,(10,0,0):C.R2GC_295_146,(10,0,1):C.R2GC_295_147,(9,0,1):C.R2GC_294_145,(0,2,0):C.R2GC_293_143,(0,2,1):C.R2GC_293_144,(2,2,0):C.R2GC_293_143,(2,2,1):C.R2GC_293_144,(5,2,0):C.R2GC_291_139,(5,2,1):C.R2GC_291_140,(1,2,0):C.R2GC_291_139,(1,2,1):C.R2GC_291_140,(7,2,0):C.R2GC_297_150,(7,2,1):C.R2GC_297_151,(4,2,0):C.R2GC_291_139,(4,2,1):C.R2GC_291_140,(3,2,0):C.R2GC_291_139,(3,2,1):C.R2GC_291_140,(8,2,0):C.R2GC_292_141,(8,2,1):C.R2GC_485_301,(6,2,0):C.R2GC_483_298,(6,2,1):C.R2GC_483_299,(0,3,0):C.R2GC_293_143,(0,3,1):C.R2GC_293_144,(2,3,0):C.R2GC_293_143,(2,3,1):C.R2GC_293_144,(5,3,0):C.R2GC_291_139,(5,3,1):C.R2GC_291_140,(1,3,0):C.R2GC_291_139,(1,3,1):C.R2GC_291_140,(7,3,0):C.R2GC_484_300,(7,3,1):C.R2GC_293_144,(4,3,0):C.R2GC_291_139,(4,3,1):C.R2GC_291_140,(3,3,0):C.R2GC_291_139,(3,3,1):C.R2GC_291_140,(8,3,0):C.R2GC_292_141,(8,3,1):C.R2GC_482_297,(6,3,0):C.R2GC_296_148,(6,3,1):C.R2GC_296_149})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.bp__tilde__, P.bp, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.bp, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_298_152})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_303_155})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_330_164})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_332_165})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_312_158,(0,1,0):C.R2GC_313_159})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_318_160,(0,1,0):C.R2GC_319_161})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_345_174,(0,1,0):C.R2GC_346_175})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_328_162,(0,1,0):C.R2GC_329_163})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_306_156,(0,1,0):C.R2GC_307_157})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_391_212,(0,1,0):C.R2GC_390_211})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_359_183,(0,1,0):C.R2GC_356_180})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_360_184,(0,1,0):C.R2GC_357_181})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_361_185,(0,1,0):C.R2GC_358_182})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_427_243,(0,1,0):C.R2GC_424_240})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_428_244,(0,1,0):C.R2GC_425_241})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_429_245,(0,1,0):C.R2GC_426_242})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.bp__tilde__, P.d, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_367_191,(0,1,0):C.R2GC_364_188})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.bp__tilde__, P.s, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_368_192,(0,1,0):C.R2GC_365_189})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.bp__tilde__, P.b, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_369_193,(0,1,0):C.R2GC_366_190})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.tp__tilde__, P.u, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_412_228,(0,1,0):C.R2GC_409_225})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.tp__tilde__, P.c, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_413_229,(0,1,0):C.R2GC_410_226})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.tp__tilde__, P.t, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_414_230,(0,1,0):C.R2GC_411_227})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_494_307,(0,1,0):C.R2GC_493_306})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_417_233,(0,1,0):C.R2GC_416_232})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_453_266,(0,1,0):C.R2GC_452_265})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_372_196,(0,1,0):C.R2GC_370_194})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_373_197,(0,1,0):C.R2GC_371_195})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_393_214,(0,1,0):C.R2GC_392_213})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_339_171,(0,1,0):C.R2GC_338_170})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_336_168,(0,1,0):C.R2GC_335_167})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_395_216,(0,1,0):C.R2GC_394_215})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_421_237,(0,1,0):C.R2GC_418_234})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_422_238,(0,1,0):C.R2GC_419_235})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_423_239,(0,1,0):C.R2GC_420_236})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_457_270,(0,1,0):C.R2GC_454_267})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_458_271,(0,1,0):C.R2GC_455_268})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_459_272,(0,1,0):C.R2GC_456_269})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_498_311,(0,1,0):C.R2GC_495_308})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_499_312,(0,1,0):C.R2GC_496_309})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_500_313,(0,1,0):C.R2GC_497_310})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_461_274,(0,1,0):C.R2GC_460_273})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_502_315,(0,1,0):C.R2GC_501_314})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_465_278,(0,1,0):C.R2GC_462_275})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_466_279,(0,1,0):C.R2GC_463_276})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_467_280,(0,1,0):C.R2GC_464_277})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_506_319,(0,1,0):C.R2GC_503_316})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_507_320,(0,1,0):C.R2GC_504_317})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_508_321,(0,1,0):C.R2GC_505_318})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_493_306,(0,1,0):C.R2GC_494_307})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_416_232,(0,1,0):C.R2GC_417_233})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_452_265,(0,1,0):C.R2GC_453_266})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_460_273,(0,1,0):C.R2GC_461_274})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_501_314,(0,1,0):C.R2GC_502_315})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_364_188,(0,1,0):C.R2GC_367_191})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_365_189,(0,1,0):C.R2GC_368_192})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_366_190,(0,1,0):C.R2GC_369_193})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_409_225,(0,1,0):C.R2GC_412_228})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_410_226,(0,1,0):C.R2GC_413_229})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.s0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_411_227,(0,1,0):C.R2GC_414_230})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_370_194,(0,1,0):C.R2GC_372_196})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_371_195,(0,1,0):C.R2GC_373_197})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_392_213,(0,1,0):C.R2GC_393_214})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_338_170,(0,1,0):C.R2GC_339_171})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_335_167,(0,1,0):C.R2GC_336_168})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_394_215,(0,1,0):C.R2GC_395_216})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_418_234,(0,1,0):C.R2GC_421_237})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_419_235,(0,1,0):C.R2GC_422_238})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_420_236,(0,1,0):C.R2GC_423_239})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_454_267,(0,1,0):C.R2GC_457_270})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_455_268,(0,1,0):C.R2GC_458_271})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_456_269,(0,1,0):C.R2GC_459_272})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_495_308,(0,1,0):C.R2GC_498_311})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_496_309,(0,1,0):C.R2GC_499_312})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_497_310,(0,1,0):C.R2GC_500_313})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_462_275,(0,1,0):C.R2GC_465_278})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_463_276,(0,1,0):C.R2GC_466_279})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_464_277,(0,1,0):C.R2GC_467_280})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_503_316,(0,1,0):C.R2GC_506_319})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_504_317,(0,1,0):C.R2GC_507_320})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_505_318,(0,1,0):C.R2GC_508_321})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.d__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_356_180,(0,1,0):C.R2GC_359_183})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.s__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_357_181,(0,1,0):C.R2GC_360_184})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_358_182,(0,1,0):C.R2GC_361_185})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.u__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_424_240,(0,1,0):C.R2GC_427_243})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.c__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_425_241,(0,1,0):C.R2GC_428_244})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_426_242,(0,1,0):C.R2GC_429_245})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.tp__tilde__, P.tp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_299_153})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.bp__tilde__, P.bp, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.bp, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_299_153})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.x__tilde__, P.x, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.x] ] ],
                couplings = {(0,0,0):C.R2GC_299_153})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.y__tilde__, P.y, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.y] ] ],
                couplings = {(0,0,0):C.R2GC_299_153})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                couplings = {(0,0,0):C.R2GC_431_247,(0,1,0):C.R2GC_437_253})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_432_248,(0,1,0):C.R2GC_438_254})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_433_249,(0,1,0):C.R2GC_439_255})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_471_284,(0,1,0):C.R2GC_474_287})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_472_285,(0,1,0):C.R2GC_475_288})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_473_286,(0,1,0):C.R2GC_476_289})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_375_199,(0,1,0):C.R2GC_380_204})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_376_200,(0,1,0):C.R2GC_381_205})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_400_221,(0,1,0):C.R2GC_401_222})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_512_325,(0,1,0):C.R2GC_515_328})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_513_326,(0,1,0):C.R2GC_516_329})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_514_327,(0,1,0):C.R2GC_517_330})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_377_201,(0,1,0):C.R2GC_382_206})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_378_202,(0,1,0):C.R2GC_383_207})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_379_203,(0,1,0):C.R2GC_384_208})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_434_250,(0,1,0):C.R2GC_440_256})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_435_251,(0,1,0):C.R2GC_441_257})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_436_252,(0,1,0):C.R2GC_442_258})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_510_323,(0,1,0):C.R2GC_511_324})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_443_259,(0,1,0):C.R2GC_444_260})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_469_282,(0,1,0):C.R2GC_470_283})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_510_323,(0,1,0):C.R2GC_511_324})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_443_259,(0,1,0):C.R2GC_444_260})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_469_282,(0,1,0):C.R2GC_470_283})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_431_247,(0,1,0):C.R2GC_437_253})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_432_248,(0,1,0):C.R2GC_438_254})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_433_249,(0,1,0):C.R2GC_439_255})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_471_284,(0,1,0):C.R2GC_474_287})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_472_285,(0,1,0):C.R2GC_475_288})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_473_286,(0,1,0):C.R2GC_476_289})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_375_199,(0,1,0):C.R2GC_380_204})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_376_200,(0,1,0):C.R2GC_381_205})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_400_221,(0,1,0):C.R2GC_401_222})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_512_325,(0,1,0):C.R2GC_515_328})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_513_326,(0,1,0):C.R2GC_516_329})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_514_327,(0,1,0):C.R2GC_517_330})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_385_209,(0,1,0):C.R2GC_386_210})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_445_261,(0,1,0):C.R2GC_446_262})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_477_290,(0,1,0):C.R2GC_478_291})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_518_331,(0,1,0):C.R2GC_519_332})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_377_201,(0,1,0):C.R2GC_382_206})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_378_202,(0,1,0):C.R2GC_383_207})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_379_203,(0,1,0):C.R2GC_384_208})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_434_250,(0,1,0):C.R2GC_440_256})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_435_251,(0,1,0):C.R2GC_441_257})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_436_252,(0,1,0):C.R2GC_442_258})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_303_155})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_303_155})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_303_155})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_298_152})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_298_152})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_298_152})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_299_153})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_299_153})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_299_153})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_299_153})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_299_153})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_299_153})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_340_172})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_341_173})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_348_177})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_334_166})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_337_169})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_349_178})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_397_218})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_398_219})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_399_220})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_340_172})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_334_166})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_397_218})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_341_173})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_337_169})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_398_219})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_348_177})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_349_178})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_399_220})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_270_43,(0,1,0):C.R2GC_258_1})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_270_43,(0,1,0):C.R2GC_258_1})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_270_43,(0,1,0):C.R2GC_258_1})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_271_44,(0,1,0):C.R2GC_259_2})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_271_44,(0,1,0):C.R2GC_259_2})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_271_44,(0,1,0):C.R2GC_259_2})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_302_154})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_302_154})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_396_217,(0,2,0):C.R2GC_396_217,(0,1,0):C.R2GC_302_154,(0,3,0):C.R2GC_302_154})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_302_154})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_302_154})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_347_176,(0,2,0):C.R2GC_347_176,(0,1,0):C.R2GC_302_154,(0,3,0):C.R2GC_302_154})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_468_281,(0,2,0):C.R2GC_468_281,(0,1,0):C.R2GC_302_154,(0,3,0):C.R2GC_302_154})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_430_246,(0,2,0):C.R2GC_430_246,(0,1,0):C.R2GC_302_154,(0,3,0):C.R2GC_302_154})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_374_198,(0,2,0):C.R2GC_374_198,(0,1,0):C.R2GC_302_154,(0,3,0):C.R2GC_302_154})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_509_322,(0,2,0):C.R2GC_509_322,(0,1,0):C.R2GC_302_154,(0,3,0):C.R2GC_302_154})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.g] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.R2GC_480_294,(0,1,0):C.R2GC_266_19,(0,1,1):C.R2GC_266_20,(0,1,4):C.R2GC_266_21,(0,1,5):C.R2GC_266_22,(0,1,6):C.R2GC_266_23,(0,1,7):C.R2GC_266_24,(0,2,2):C.R2GC_479_292,(0,2,3):C.R2GC_479_293})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_262_3,(0,0,1):C.R2GC_262_4})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_265_13,(0,0,1):C.R2GC_265_14,(0,0,2):C.R2GC_265_15,(0,0,3):C.R2GC_265_16,(0,0,4):C.R2GC_265_17,(0,0,5):C.R2GC_265_18})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.u] ], [ [P.b, P.y] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.c, P.x] ], [ [P.d, P.t] ], [ [P.d, P.tp] ], [ [P.d, P.u] ], [ [P.d, P.y] ], [ [P.s, P.t] ], [ [P.s, P.tp] ], [ [P.s, P.u] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,0):C.R2GC_280_115,(0,0,6):C.R2GC_280_116,(0,0,7):C.R2GC_280_117,(0,0,8):C.R2GC_280_118,(0,0,9):C.R2GC_280_119,(0,0,1):C.R2GC_280_120,(0,0,2):C.R2GC_280_121,(0,0,3):C.R2GC_280_122,(0,0,4):C.R2GC_280_123,(0,0,5):C.R2GC_280_124,(0,0,10):C.R2GC_280_125,(0,0,11):C.R2GC_280_126,(0,0,12):C.R2GC_280_127,(0,0,13):C.R2GC_280_128,(0,0,14):C.R2GC_280_129,(0,0,15):C.R2GC_280_130,(0,0,16):C.R2GC_280_131,(0,0,17):C.R2GC_280_132,(0,0,18):C.R2GC_280_133,(0,0,19):C.R2GC_280_134,(0,0,20):C.R2GC_280_135,(0,0,22):C.R2GC_280_136,(0,0,21):C.R2GC_280_137,(0,0,23):C.R2GC_280_138,(0,1,0):C.R2GC_280_115,(0,1,6):C.R2GC_280_116,(0,1,7):C.R2GC_280_117,(0,1,8):C.R2GC_280_118,(0,1,9):C.R2GC_280_119,(0,1,1):C.R2GC_280_120,(0,1,2):C.R2GC_280_121,(0,1,3):C.R2GC_280_122,(0,1,4):C.R2GC_280_123,(0,1,5):C.R2GC_280_124,(0,1,10):C.R2GC_280_125,(0,1,11):C.R2GC_280_126,(0,1,12):C.R2GC_280_127,(0,1,13):C.R2GC_280_128,(0,1,14):C.R2GC_280_129,(0,1,15):C.R2GC_280_130,(0,1,16):C.R2GC_280_131,(0,1,17):C.R2GC_280_132,(0,1,18):C.R2GC_280_133,(0,1,19):C.R2GC_280_134,(0,1,20):C.R2GC_280_135,(0,1,22):C.R2GC_280_136,(0,1,21):C.R2GC_280_137,(0,1,23):C.R2GC_280_138,(0,2,0):C.R2GC_280_115,(0,2,6):C.R2GC_280_116,(0,2,7):C.R2GC_280_117,(0,2,8):C.R2GC_280_118,(0,2,9):C.R2GC_280_119,(0,2,1):C.R2GC_280_120,(0,2,2):C.R2GC_280_121,(0,2,3):C.R2GC_280_122,(0,2,4):C.R2GC_280_123,(0,2,5):C.R2GC_280_124,(0,2,10):C.R2GC_280_125,(0,2,11):C.R2GC_280_126,(0,2,12):C.R2GC_280_127,(0,2,13):C.R2GC_280_128,(0,2,14):C.R2GC_280_129,(0,2,15):C.R2GC_280_130,(0,2,16):C.R2GC_280_131,(0,2,17):C.R2GC_280_132,(0,2,18):C.R2GC_280_133,(0,2,19):C.R2GC_280_134,(0,2,20):C.R2GC_280_135,(0,2,22):C.R2GC_280_136,(0,2,21):C.R2GC_280_137,(0,2,23):C.R2GC_280_138})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b, P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.R2GC_277_77,(0,0,0):C.R2GC_277_78,(0,0,6):C.R2GC_277_79,(0,0,7):C.R2GC_277_80,(0,0,10):C.R2GC_277_81,(0,0,11):C.R2GC_277_82,(0,0,1):C.R2GC_277_83,(0,0,3):C.R2GC_277_84,(0,0,4):C.R2GC_277_85,(0,0,5):C.R2GC_277_86,(0,0,9):C.R2GC_277_87,(0,0,8):C.R2GC_277_88,(0,1,2):C.R2GC_277_77,(0,1,0):C.R2GC_277_78,(0,1,6):C.R2GC_277_79,(0,1,7):C.R2GC_277_80,(0,1,10):C.R2GC_277_81,(0,1,11):C.R2GC_277_82,(0,1,1):C.R2GC_277_83,(0,1,3):C.R2GC_277_84,(0,1,4):C.R2GC_277_85,(0,1,5):C.R2GC_277_86,(0,1,9):C.R2GC_277_87,(0,1,8):C.R2GC_277_88,(0,2,2):C.R2GC_277_77,(0,2,0):C.R2GC_277_78,(0,2,6):C.R2GC_277_79,(0,2,7):C.R2GC_277_80,(0,2,10):C.R2GC_277_81,(0,2,11):C.R2GC_277_82,(0,2,1):C.R2GC_277_83,(0,2,3):C.R2GC_277_84,(0,2,4):C.R2GC_277_85,(0,2,5):C.R2GC_277_86,(0,2,9):C.R2GC_277_87,(0,2,8):C.R2GC_277_88})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_267_25,(0,0,0):C.R2GC_267_26,(0,0,2):C.R2GC_267_27,(0,0,3):C.R2GC_267_28,(0,0,4):C.R2GC_267_29,(0,0,5):C.R2GC_267_30,(0,1,1):C.R2GC_267_25,(0,1,0):C.R2GC_267_26,(0,1,2):C.R2GC_267_27,(0,1,3):C.R2GC_267_28,(0,1,4):C.R2GC_267_29,(0,1,5):C.R2GC_267_30,(0,2,1):C.R2GC_267_25,(0,2,0):C.R2GC_267_26,(0,2,2):C.R2GC_267_27,(0,2,3):C.R2GC_267_28,(0,2,4):C.R2GC_267_29,(0,2,5):C.R2GC_267_30})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_263_5,(0,0,1):C.R2GC_263_6,(0,0,2):C.R2GC_263_7,(0,0,3):C.R2GC_263_8,(0,1,0):C.R2GC_263_5,(0,1,1):C.R2GC_263_6,(0,1,2):C.R2GC_263_7,(0,1,3):C.R2GC_263_8,(0,2,0):C.R2GC_263_5,(0,2,1):C.R2GC_263_6,(0,2,2):C.R2GC_263_7,(0,2,3):C.R2GC_263_8})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.bp] ], [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(1,0,1):C.R2GC_269_37,(1,0,0):C.R2GC_269_38,(1,0,2):C.R2GC_269_39,(1,0,3):C.R2GC_269_40,(1,0,4):C.R2GC_269_41,(1,0,5):C.R2GC_269_42,(0,1,1):C.R2GC_268_31,(0,1,0):C.R2GC_268_32,(0,1,2):C.R2GC_268_33,(0,1,3):C.R2GC_268_34,(0,1,4):C.R2GC_268_35,(0,1,5):C.R2GC_268_36,(0,2,1):C.R2GC_268_31,(0,2,0):C.R2GC_268_32,(0,2,2):C.R2GC_268_33,(0,2,3):C.R2GC_268_34,(0,2,4):C.R2GC_268_35,(0,2,5):C.R2GC_268_36,(0,3,1):C.R2GC_268_31,(0,3,0):C.R2GC_268_32,(0,3,2):C.R2GC_268_33,(0,3,3):C.R2GC_268_34,(0,3,4):C.R2GC_268_35,(0,3,5):C.R2GC_268_36})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.bp], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp], [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_264_9,(0,0,1):C.R2GC_264_10,(0,0,2):C.R2GC_264_11,(0,0,3):C.R2GC_264_12,(0,1,0):C.R2GC_264_9,(0,1,1):C.R2GC_264_10,(0,1,2):C.R2GC_264_11,(0,1,3):C.R2GC_264_12,(0,2,0):C.R2GC_264_9,(0,2,1):C.R2GC_264_10,(0,2,2):C.R2GC_264_11,(0,2,3):C.R2GC_264_12})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_276_69,(0,0,5):C.R2GC_276_70,(0,0,1):C.R2GC_276_71,(0,0,2):C.R2GC_276_72,(0,0,3):C.R2GC_276_73,(0,0,4):C.R2GC_276_74,(0,0,7):C.R2GC_276_75,(0,0,6):C.R2GC_276_76})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c, P.tp] ], [ [P.t] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.R2GC_275_61,(0,0,5):C.R2GC_275_62,(0,0,1):C.R2GC_275_63,(0,0,2):C.R2GC_275_64,(0,0,3):C.R2GC_275_65,(0,0,4):C.R2GC_275_66,(0,0,7):C.R2GC_275_67,(0,0,6):C.R2GC_275_68})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s0, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.bp] ], [ [P.bp, P.d] ], [ [P.bp, P.s] ], [ [P.c] ], [ [P.c, P.tp] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.tp, P.u] ], [ [P.t, P.tp] ], [ [P.u] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.R2GC_274_45,(0,0,1):C.R2GC_274_46,(0,0,5):C.R2GC_274_47,(0,0,7):C.R2GC_274_48,(0,0,8):C.R2GC_274_49,(0,0,9):C.R2GC_274_50,(0,0,10):C.R2GC_274_51,(0,0,13):C.R2GC_274_52,(0,0,14):C.R2GC_274_53,(0,0,15):C.R2GC_274_54,(0,0,2):C.R2GC_274_55,(0,0,3):C.R2GC_274_56,(0,0,4):C.R2GC_274_57,(0,0,6):C.R2GC_274_58,(0,0,12):C.R2GC_274_59,(0,0,11):C.R2GC_274_60})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus__, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.c] ], [ [P.bp, P.t] ], [ [P.bp, P.tp] ], [ [P.bp, P.u] ], [ [P.bp, P.y] ], [ [P.b, P.t] ], [ [P.b, P.tp] ], [ [P.b, P.y] ], [ [P.c, P.s] ], [ [P.c, P.x] ], [ [P.d, P.tp] ], [ [P.d, P.u] ], [ [P.d, P.y] ], [ [P.s, P.tp] ], [ [P.s, P.y] ], [ [P.tp, P.x] ], [ [P.t, P.x] ], [ [P.u, P.x] ] ],
                 couplings = {(0,0,5):C.R2GC_279_97,(0,0,6):C.R2GC_279_98,(0,0,7):C.R2GC_279_99,(0,0,0):C.R2GC_279_100,(0,0,1):C.R2GC_279_101,(0,0,2):C.R2GC_279_102,(0,0,3):C.R2GC_279_103,(0,0,4):C.R2GC_279_104,(0,0,8):C.R2GC_279_105,(0,0,9):C.R2GC_279_106,(0,0,10):C.R2GC_279_107,(0,0,11):C.R2GC_279_108,(0,0,12):C.R2GC_279_109,(0,0,13):C.R2GC_279_110,(0,0,14):C.R2GC_279_111,(0,0,16):C.R2GC_279_112,(0,0,15):C.R2GC_279_113,(0,0,17):C.R2GC_279_114})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s__minus____minus__, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.bp, P.x] ], [ [P.b, P.x] ], [ [P.c, P.y] ], [ [P.d, P.x] ], [ [P.s, P.x] ], [ [P.tp, P.y] ], [ [P.t, P.y] ], [ [P.u, P.y] ] ],
                 couplings = {(0,0,1):C.R2GC_278_89,(0,0,0):C.R2GC_278_90,(0,0,2):C.R2GC_278_91,(0,0,3):C.R2GC_278_92,(0,0,4):C.R2GC_278_93,(0,0,6):C.R2GC_278_94,(0,0,5):C.R2GC_278_95,(0,0,7):C.R2GC_278_96})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_352_72})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_362_94,(0,1,0):C.UVGC_363_95})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_404_194})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_408_198,(0,1,0):C.UVGC_415_217})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_450_308,(0,1,0):C.UVGC_451_309})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_491_448,(0,1,0):C.UVGC_492_449})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,1,0):C.UVGC_481_399,(0,1,1):C.UVGC_481_400,(0,1,2):C.UVGC_481_401,(0,1,5):C.UVGC_481_402,(0,1,6):C.UVGC_481_403,(0,1,7):C.UVGC_481_404,(0,1,8):C.UVGC_481_405,(0,2,3):C.UVGC_281_1,(0,0,4):C.UVGC_282_2})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b], [P.bp], [P.c], [P.d], [P.s], [P.t], [P.tp], [P.u], [P.x], [P.y] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(2,1,4):C.UVGC_292_9,(2,1,5):C.UVGC_292_8,(0,1,4):C.UVGC_292_9,(0,1,5):C.UVGC_292_8,(4,1,4):C.UVGC_291_6,(4,1,5):C.UVGC_291_7,(3,1,4):C.UVGC_291_6,(3,1,5):C.UVGC_291_7,(8,1,4):C.UVGC_292_8,(8,1,5):C.UVGC_292_9,(6,1,0):C.UVGC_486_434,(6,1,1):C.UVGC_486_435,(6,1,3):C.UVGC_486_436,(6,1,4):C.UVGC_487_443,(6,1,5):C.UVGC_487_444,(6,1,6):C.UVGC_486_439,(6,1,7):C.UVGC_486_440,(6,1,8):C.UVGC_486_441,(6,1,9):C.UVGC_486_442,(7,1,0):C.UVGC_486_434,(7,1,1):C.UVGC_486_435,(7,1,3):C.UVGC_486_436,(7,1,4):C.UVGC_486_437,(7,1,5):C.UVGC_486_438,(7,1,6):C.UVGC_486_439,(7,1,7):C.UVGC_486_440,(7,1,8):C.UVGC_486_441,(7,1,9):C.UVGC_486_442,(5,1,4):C.UVGC_291_6,(5,1,5):C.UVGC_291_7,(1,1,4):C.UVGC_291_6,(1,1,5):C.UVGC_291_7,(11,0,4):C.UVGC_295_12,(11,0,5):C.UVGC_295_13,(10,0,4):C.UVGC_295_12,(10,0,5):C.UVGC_295_13,(9,0,4):C.UVGC_294_10,(9,0,5):C.UVGC_294_11,(0,2,4):C.UVGC_292_9,(0,2,5):C.UVGC_292_8,(2,2,4):C.UVGC_292_9,(2,2,5):C.UVGC_292_8,(5,2,4):C.UVGC_291_6,(5,2,5):C.UVGC_291_7,(1,2,4):C.UVGC_291_6,(1,2,5):C.UVGC_291_7,(7,2,2):C.UVGC_296_14,(7,2,4):C.UVGC_297_16,(7,2,5):C.UVGC_297_17,(4,2,4):C.UVGC_291_6,(4,2,5):C.UVGC_291_7,(3,2,4):C.UVGC_291_6,(3,2,5):C.UVGC_291_7,(8,2,0):C.UVGC_485_425,(8,2,1):C.UVGC_485_426,(8,2,3):C.UVGC_485_427,(8,2,4):C.UVGC_485_428,(8,2,5):C.UVGC_485_429,(8,2,6):C.UVGC_485_430,(8,2,7):C.UVGC_485_431,(8,2,8):C.UVGC_485_432,(8,2,9):C.UVGC_485_433,(6,2,0):C.UVGC_483_415,(6,2,1):C.UVGC_483_416,(6,2,4):C.UVGC_483_417,(6,2,5):C.UVGC_483_418,(6,2,6):C.UVGC_483_419,(6,2,7):C.UVGC_483_420,(6,2,8):C.UVGC_483_421,(6,2,9):C.UVGC_483_422,(0,3,4):C.UVGC_292_9,(0,3,5):C.UVGC_292_8,(2,3,4):C.UVGC_292_9,(2,3,5):C.UVGC_292_8,(5,3,4):C.UVGC_291_6,(5,3,5):C.UVGC_291_7,(1,3,4):C.UVGC_291_6,(1,3,5):C.UVGC_291_7,(7,3,0):C.UVGC_483_415,(7,3,1):C.UVGC_483_416,(7,3,4):C.UVGC_484_423,(7,3,5):C.UVGC_484_424,(7,3,6):C.UVGC_483_419,(7,3,7):C.UVGC_483_420,(7,3,8):C.UVGC_483_421,(7,3,9):C.UVGC_483_422,(4,3,4):C.UVGC_291_6,(4,3,5):C.UVGC_291_7,(3,3,4):C.UVGC_291_6,(3,3,5):C.UVGC_291_7,(8,3,0):C.UVGC_482_406,(8,3,1):C.UVGC_482_407,(8,3,3):C.UVGC_482_408,(8,3,4):C.UVGC_482_409,(8,3,5):C.UVGC_482_410,(8,3,6):C.UVGC_482_411,(8,3,7):C.UVGC_482_412,(8,3,8):C.UVGC_482_413,(8,3,9):C.UVGC_482_414,(6,3,2):C.UVGC_296_14,(6,3,4):C.UVGC_296_15,(6,3,5):C.UVGC_294_10})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_298_18,(0,1,0):C.UVGC_354_74})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_303_21,(0,1,0):C.UVGC_406_196})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_330_40,(0,1,0):C.UVGC_448_306})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_332_41,(0,1,0):C.UVGC_489_446})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_312_34,(0,1,0):C.UVGC_313_35})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_318_36,(0,1,0):C.UVGC_319_37})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_345_61,(0,1,0):C.UVGC_346_62})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_328_38,(0,1,0):C.UVGC_329_39})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4, L.FFS6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_306_32,(0,1,0):C.UVGC_307_33})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_391_163,(0,1,0):C.UVGC_390_162})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_359_85,(0,0,2):C.UVGC_359_86,(0,0,0):C.UVGC_359_87,(0,1,1):C.UVGC_356_76,(0,1,2):C.UVGC_356_77,(0,1,0):C.UVGC_356_78})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_360_88,(0,0,2):C.UVGC_360_89,(0,0,1):C.UVGC_360_90,(0,1,0):C.UVGC_357_79,(0,1,2):C.UVGC_357_80,(0,1,1):C.UVGC_357_81})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_361_91,(0,0,2):C.UVGC_361_92,(0,0,0):C.UVGC_361_93,(0,1,1):C.UVGC_358_82,(0,1,2):C.UVGC_358_83,(0,1,0):C.UVGC_358_84})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_427_251,(0,0,2):C.UVGC_427_252,(0,0,1):C.UVGC_427_253,(0,1,0):C.UVGC_424_242,(0,1,2):C.UVGC_424_243,(0,1,1):C.UVGC_424_244})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_428_254,(0,0,2):C.UVGC_428_255,(0,0,1):C.UVGC_428_256,(0,1,0):C.UVGC_425_245,(0,1,2):C.UVGC_425_246,(0,1,1):C.UVGC_425_247})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_429_257,(0,0,1):C.UVGC_429_258,(0,0,2):C.UVGC_429_259,(0,1,0):C.UVGC_426_248,(0,1,1):C.UVGC_426_249,(0,1,2):C.UVGC_426_250})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_367_105,(0,0,2):C.UVGC_367_106,(0,0,0):C.UVGC_367_107,(0,1,1):C.UVGC_364_96,(0,1,2):C.UVGC_364_97,(0,1,0):C.UVGC_364_98})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_368_108,(0,0,2):C.UVGC_368_109,(0,0,1):C.UVGC_368_110,(0,1,0):C.UVGC_365_99,(0,1,2):C.UVGC_365_100,(0,1,1):C.UVGC_365_101})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_369_111,(0,0,2):C.UVGC_369_112,(0,0,0):C.UVGC_369_113,(0,1,1):C.UVGC_366_102,(0,1,2):C.UVGC_366_103,(0,1,0):C.UVGC_366_104})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_412_208,(0,0,2):C.UVGC_412_209,(0,0,1):C.UVGC_412_210,(0,1,0):C.UVGC_409_199,(0,1,2):C.UVGC_409_200,(0,1,1):C.UVGC_409_201})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_413_211,(0,0,2):C.UVGC_413_212,(0,0,1):C.UVGC_413_213,(0,1,0):C.UVGC_410_202,(0,1,2):C.UVGC_410_203,(0,1,1):C.UVGC_410_204})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_414_214,(0,0,1):C.UVGC_414_215,(0,0,2):C.UVGC_414_216,(0,1,0):C.UVGC_411_205,(0,1,1):C.UVGC_411_206,(0,1,2):C.UVGC_411_207})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_494_453,(0,0,2):C.UVGC_494_454,(0,0,1):C.UVGC_494_455,(0,1,0):C.UVGC_493_450,(0,1,2):C.UVGC_493_451,(0,1,1):C.UVGC_493_452})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_417_221,(0,0,2):C.UVGC_417_222,(0,0,1):C.UVGC_417_223,(0,1,0):C.UVGC_416_218,(0,1,2):C.UVGC_416_219,(0,1,1):C.UVGC_416_220})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_453_313,(0,0,2):C.UVGC_453_314,(0,0,1):C.UVGC_453_315,(0,1,0):C.UVGC_452_310,(0,1,2):C.UVGC_452_311,(0,1,1):C.UVGC_452_312})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_372_120,(0,0,2):C.UVGC_372_121,(0,0,1):C.UVGC_372_122,(0,1,0):C.UVGC_370_114,(0,1,2):C.UVGC_370_115,(0,1,1):C.UVGC_370_116})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_373_123,(0,0,2):C.UVGC_373_124,(0,0,0):C.UVGC_373_125,(0,1,1):C.UVGC_371_117,(0,1,2):C.UVGC_371_118,(0,1,0):C.UVGC_371_119})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_393_167,(0,0,2):C.UVGC_393_168,(0,0,1):C.UVGC_393_169,(0,1,0):C.UVGC_392_164,(0,1,2):C.UVGC_392_165,(0,1,1):C.UVGC_392_166})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_339_52,(0,0,1):C.UVGC_339_53,(0,1,0):C.UVGC_338_50,(0,1,1):C.UVGC_338_51})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_336_46,(0,0,1):C.UVGC_336_47,(0,1,0):C.UVGC_335_44,(0,1,1):C.UVGC_335_45})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_395_173,(0,0,2):C.UVGC_395_174,(0,0,1):C.UVGC_395_175,(0,1,0):C.UVGC_394_170,(0,1,2):C.UVGC_394_171,(0,1,1):C.UVGC_394_172})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_421_233,(0,0,2):C.UVGC_421_234,(0,0,1):C.UVGC_421_235,(0,1,0):C.UVGC_418_224,(0,1,2):C.UVGC_418_225,(0,1,1):C.UVGC_418_226})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_422_236,(0,0,2):C.UVGC_422_237,(0,0,1):C.UVGC_422_238,(0,1,0):C.UVGC_419_227,(0,1,2):C.UVGC_419_228,(0,1,1):C.UVGC_419_229})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_423_239,(0,0,2):C.UVGC_423_240,(0,0,1):C.UVGC_423_241,(0,1,0):C.UVGC_420_230,(0,1,2):C.UVGC_420_231,(0,1,1):C.UVGC_420_232})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_457_325,(0,0,2):C.UVGC_457_326,(0,0,1):C.UVGC_457_327,(0,1,0):C.UVGC_454_316,(0,1,2):C.UVGC_454_317,(0,1,1):C.UVGC_454_318})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_458_328,(0,0,2):C.UVGC_458_329,(0,0,1):C.UVGC_458_330,(0,1,0):C.UVGC_455_319,(0,1,2):C.UVGC_455_320,(0,1,1):C.UVGC_455_321})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_459_331,(0,0,2):C.UVGC_459_332,(0,0,1):C.UVGC_459_333,(0,1,0):C.UVGC_456_322,(0,1,2):C.UVGC_456_323,(0,1,1):C.UVGC_456_324})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_498_465,(0,0,2):C.UVGC_498_466,(0,0,1):C.UVGC_498_467,(0,1,0):C.UVGC_495_456,(0,1,2):C.UVGC_495_457,(0,1,1):C.UVGC_495_458})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_499_468,(0,0,2):C.UVGC_499_469,(0,0,1):C.UVGC_499_470,(0,1,0):C.UVGC_496_459,(0,1,2):C.UVGC_496_460,(0,1,1):C.UVGC_496_461})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_500_471,(0,0,2):C.UVGC_500_472,(0,0,1):C.UVGC_500_473,(0,1,0):C.UVGC_497_462,(0,1,2):C.UVGC_497_463,(0,1,1):C.UVGC_497_464})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.bp, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_461_337,(0,0,2):C.UVGC_461_338,(0,0,1):C.UVGC_461_339,(0,1,0):C.UVGC_460_334,(0,1,2):C.UVGC_460_335,(0,1,1):C.UVGC_460_336})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.tp, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_502_477,(0,0,2):C.UVGC_502_478,(0,0,1):C.UVGC_502_479,(0,1,0):C.UVGC_501_474,(0,1,2):C.UVGC_501_475,(0,1,1):C.UVGC_501_476})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.d, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_465_349,(0,0,2):C.UVGC_465_350,(0,0,1):C.UVGC_465_351,(0,1,0):C.UVGC_462_340,(0,1,2):C.UVGC_462_341,(0,1,1):C.UVGC_462_342})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.s, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_466_352,(0,0,2):C.UVGC_466_353,(0,0,1):C.UVGC_466_354,(0,1,0):C.UVGC_463_343,(0,1,2):C.UVGC_463_344,(0,1,1):C.UVGC_463_345})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.b, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_467_355,(0,0,2):C.UVGC_467_356,(0,0,1):C.UVGC_467_357,(0,1,0):C.UVGC_464_346,(0,1,2):C.UVGC_464_347,(0,1,1):C.UVGC_464_348})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.u, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_506_489,(0,0,2):C.UVGC_506_490,(0,0,1):C.UVGC_506_491,(0,1,0):C.UVGC_503_480,(0,1,2):C.UVGC_503_481,(0,1,1):C.UVGC_503_482})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.c, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_507_492,(0,0,2):C.UVGC_507_493,(0,0,1):C.UVGC_507_494,(0,1,0):C.UVGC_504_483,(0,1,2):C.UVGC_504_484,(0,1,1):C.UVGC_504_485})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.t, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_508_495,(0,0,2):C.UVGC_508_496,(0,0,1):C.UVGC_508_497,(0,1,0):C.UVGC_505_486,(0,1,2):C.UVGC_505_487,(0,1,1):C.UVGC_505_488})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_493_450,(0,0,2):C.UVGC_493_451,(0,0,1):C.UVGC_493_452,(0,1,0):C.UVGC_494_453,(0,1,2):C.UVGC_494_454,(0,1,1):C.UVGC_494_455})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_416_218,(0,0,2):C.UVGC_416_219,(0,0,1):C.UVGC_416_220,(0,1,0):C.UVGC_417_221,(0,1,2):C.UVGC_417_222,(0,1,1):C.UVGC_417_223})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_452_310,(0,0,2):C.UVGC_452_311,(0,0,1):C.UVGC_452_312,(0,1,0):C.UVGC_453_313,(0,1,2):C.UVGC_453_314,(0,1,1):C.UVGC_453_315})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_460_334,(0,0,2):C.UVGC_460_335,(0,0,1):C.UVGC_460_336,(0,1,0):C.UVGC_461_337,(0,1,2):C.UVGC_461_338,(0,1,1):C.UVGC_461_339})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_501_474,(0,0,2):C.UVGC_501_475,(0,0,1):C.UVGC_501_476,(0,1,0):C.UVGC_502_477,(0,1,2):C.UVGC_502_478,(0,1,1):C.UVGC_502_479})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_364_96,(0,0,2):C.UVGC_364_97,(0,0,0):C.UVGC_364_98,(0,1,1):C.UVGC_367_105,(0,1,2):C.UVGC_367_106,(0,1,0):C.UVGC_367_107})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_365_99,(0,0,2):C.UVGC_365_100,(0,0,1):C.UVGC_365_101,(0,1,0):C.UVGC_368_108,(0,1,2):C.UVGC_368_109,(0,1,1):C.UVGC_368_110})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_366_102,(0,0,2):C.UVGC_366_103,(0,0,0):C.UVGC_366_104,(0,1,1):C.UVGC_369_111,(0,1,2):C.UVGC_369_112,(0,1,0):C.UVGC_369_113})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_409_199,(0,0,2):C.UVGC_409_200,(0,0,1):C.UVGC_409_201,(0,1,0):C.UVGC_412_208,(0,1,2):C.UVGC_412_209,(0,1,1):C.UVGC_412_210})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_410_202,(0,0,2):C.UVGC_410_203,(0,0,1):C.UVGC_410_204,(0,1,0):C.UVGC_413_211,(0,1,2):C.UVGC_413_212,(0,1,1):C.UVGC_413_213})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.s0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_411_205,(0,0,1):C.UVGC_411_206,(0,0,2):C.UVGC_411_207,(0,1,0):C.UVGC_414_214,(0,1,1):C.UVGC_414_215,(0,1,2):C.UVGC_414_216})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_370_114,(0,0,2):C.UVGC_370_115,(0,0,1):C.UVGC_370_116,(0,1,0):C.UVGC_372_120,(0,1,2):C.UVGC_372_121,(0,1,1):C.UVGC_372_122})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_371_117,(0,0,2):C.UVGC_371_118,(0,0,0):C.UVGC_371_119,(0,1,1):C.UVGC_373_123,(0,1,2):C.UVGC_373_124,(0,1,0):C.UVGC_373_125})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_392_164,(0,0,2):C.UVGC_392_165,(0,0,1):C.UVGC_392_166,(0,1,0):C.UVGC_393_167,(0,1,2):C.UVGC_393_168,(0,1,1):C.UVGC_393_169})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_338_50,(0,0,1):C.UVGC_338_51,(0,1,0):C.UVGC_339_52,(0,1,1):C.UVGC_339_53})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_335_44,(0,0,1):C.UVGC_335_45,(0,1,0):C.UVGC_336_46,(0,1,1):C.UVGC_336_47})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_394_170,(0,0,2):C.UVGC_394_171,(0,0,1):C.UVGC_394_172,(0,1,0):C.UVGC_395_173,(0,1,2):C.UVGC_395_174,(0,1,1):C.UVGC_395_175})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_418_224,(0,0,2):C.UVGC_418_225,(0,0,1):C.UVGC_418_226,(0,1,0):C.UVGC_421_233,(0,1,2):C.UVGC_421_234,(0,1,1):C.UVGC_421_235})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_419_227,(0,0,2):C.UVGC_419_228,(0,0,1):C.UVGC_419_229,(0,1,0):C.UVGC_422_236,(0,1,2):C.UVGC_422_237,(0,1,1):C.UVGC_422_238})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_420_230,(0,0,2):C.UVGC_420_231,(0,0,1):C.UVGC_420_232,(0,1,0):C.UVGC_423_239,(0,1,2):C.UVGC_423_240,(0,1,1):C.UVGC_423_241})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_454_316,(0,0,2):C.UVGC_454_317,(0,0,1):C.UVGC_454_318,(0,1,0):C.UVGC_457_325,(0,1,2):C.UVGC_457_326,(0,1,1):C.UVGC_457_327})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_455_319,(0,0,2):C.UVGC_455_320,(0,0,1):C.UVGC_455_321,(0,1,0):C.UVGC_458_328,(0,1,2):C.UVGC_458_329,(0,1,1):C.UVGC_458_330})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.s__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_456_322,(0,0,2):C.UVGC_456_323,(0,0,1):C.UVGC_456_324,(0,1,0):C.UVGC_459_331,(0,1,2):C.UVGC_459_332,(0,1,1):C.UVGC_459_333})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_495_456,(0,0,2):C.UVGC_495_457,(0,0,1):C.UVGC_495_458,(0,1,0):C.UVGC_498_465,(0,1,2):C.UVGC_498_466,(0,1,1):C.UVGC_498_467})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_496_459,(0,0,2):C.UVGC_496_460,(0,0,1):C.UVGC_496_461,(0,1,0):C.UVGC_499_468,(0,1,2):C.UVGC_499_469,(0,1,1):C.UVGC_499_470})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.s__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_497_462,(0,0,2):C.UVGC_497_463,(0,0,1):C.UVGC_497_464,(0,1,0):C.UVGC_500_471,(0,1,2):C.UVGC_500_472,(0,1,1):C.UVGC_500_473})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_462_340,(0,0,2):C.UVGC_462_341,(0,0,1):C.UVGC_462_342,(0,1,0):C.UVGC_465_349,(0,1,2):C.UVGC_465_350,(0,1,1):C.UVGC_465_351})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_463_343,(0,0,2):C.UVGC_463_344,(0,0,1):C.UVGC_463_345,(0,1,0):C.UVGC_466_352,(0,1,2):C.UVGC_466_353,(0,1,1):C.UVGC_466_354})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.x, P.s__minus____minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_464_346,(0,0,2):C.UVGC_464_347,(0,0,1):C.UVGC_464_348,(0,1,0):C.UVGC_467_355,(0,1,2):C.UVGC_467_356,(0,1,1):C.UVGC_467_357})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_503_480,(0,0,2):C.UVGC_503_481,(0,0,1):C.UVGC_503_482,(0,1,0):C.UVGC_506_489,(0,1,2):C.UVGC_506_490,(0,1,1):C.UVGC_506_491})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_504_483,(0,0,2):C.UVGC_504_484,(0,0,1):C.UVGC_504_485,(0,1,0):C.UVGC_507_492,(0,1,2):C.UVGC_507_493,(0,1,1):C.UVGC_507_494})

V_292 = CTVertex(name = 'V_292',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.y, P.s__plus____plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_505_486,(0,0,2):C.UVGC_505_487,(0,0,1):C.UVGC_505_488,(0,1,0):C.UVGC_508_495,(0,1,2):C.UVGC_508_496,(0,1,1):C.UVGC_508_497})

V_293 = CTVertex(name = 'V_293',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_356_76,(0,0,2):C.UVGC_356_77,(0,0,0):C.UVGC_356_78,(0,1,1):C.UVGC_359_85,(0,1,2):C.UVGC_359_86,(0,1,0):C.UVGC_359_87})

V_294 = CTVertex(name = 'V_294',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_357_79,(0,0,2):C.UVGC_357_80,(0,0,1):C.UVGC_357_81,(0,1,0):C.UVGC_360_88,(0,1,2):C.UVGC_360_89,(0,1,1):C.UVGC_360_90})

V_295 = CTVertex(name = 'V_295',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_358_82,(0,0,2):C.UVGC_358_83,(0,0,0):C.UVGC_358_84,(0,1,1):C.UVGC_361_91,(0,1,2):C.UVGC_361_92,(0,1,0):C.UVGC_361_93})

V_296 = CTVertex(name = 'V_296',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_424_242,(0,0,2):C.UVGC_424_243,(0,0,1):C.UVGC_424_244,(0,1,0):C.UVGC_427_251,(0,1,2):C.UVGC_427_252,(0,1,1):C.UVGC_427_253})

V_297 = CTVertex(name = 'V_297',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_425_245,(0,0,2):C.UVGC_425_246,(0,0,1):C.UVGC_425_247,(0,1,0):C.UVGC_428_254,(0,1,2):C.UVGC_428_255,(0,1,1):C.UVGC_428_256})

V_298 = CTVertex(name = 'V_298',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_426_248,(0,0,1):C.UVGC_426_249,(0,0,2):C.UVGC_426_250,(0,1,0):C.UVGC_429_257,(0,1,1):C.UVGC_429_258,(0,1,2):C.UVGC_429_259})

V_299 = CTVertex(name = 'V_299',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,3):C.UVGC_304_25,(0,1,4):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,5):C.UVGC_407_197})

V_300 = CTVertex(name = 'V_300',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.bp, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,3):C.UVGC_304_24,(0,1,4):C.UVGC_304_25,(0,1,5):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,2):C.UVGC_355_75})

V_301 = CTVertex(name = 'V_301',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.x] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,3):C.UVGC_304_25,(0,1,4):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,5):C.UVGC_449_307})

V_302 = CTVertex(name = 'V_302',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.y] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,3):C.UVGC_304_25,(0,1,4):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,5):C.UVGC_490_447})

V_303 = CTVertex(name = 'V_303',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_431_261,(0,0,2):C.UVGC_431_262,(0,0,1):C.UVGC_431_263,(0,1,0):C.UVGC_437_279,(0,1,2):C.UVGC_437_280,(0,1,1):C.UVGC_437_281})

V_304 = CTVertex(name = 'V_304',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_432_264,(0,0,2):C.UVGC_432_265,(0,0,1):C.UVGC_432_266,(0,1,0):C.UVGC_438_282,(0,1,2):C.UVGC_438_283,(0,1,1):C.UVGC_438_284})

V_305 = CTVertex(name = 'V_305',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_433_267,(0,0,2):C.UVGC_433_268,(0,0,1):C.UVGC_433_269,(0,1,0):C.UVGC_439_285,(0,1,2):C.UVGC_439_286,(0,1,1):C.UVGC_439_287})

V_306 = CTVertex(name = 'V_306',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.u, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_471_365,(0,0,2):C.UVGC_471_366,(0,0,1):C.UVGC_471_367,(0,1,0):C.UVGC_474_374,(0,1,2):C.UVGC_474_375,(0,1,1):C.UVGC_474_376})

V_307 = CTVertex(name = 'V_307',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.c, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_472_368,(0,0,2):C.UVGC_472_369,(0,0,1):C.UVGC_472_370,(0,1,0):C.UVGC_475_377,(0,1,2):C.UVGC_475_378,(0,1,1):C.UVGC_475_379})

V_308 = CTVertex(name = 'V_308',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.t, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_473_371,(0,0,2):C.UVGC_473_372,(0,0,1):C.UVGC_473_373,(0,1,0):C.UVGC_476_380,(0,1,2):C.UVGC_476_381,(0,1,1):C.UVGC_476_382})

V_309 = CTVertex(name = 'V_309',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_375_127,(0,0,2):C.UVGC_375_128,(0,0,1):C.UVGC_375_129,(0,1,0):C.UVGC_380_142,(0,1,2):C.UVGC_380_143,(0,1,1):C.UVGC_380_144})

V_310 = CTVertex(name = 'V_310',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_376_130,(0,0,2):C.UVGC_376_131,(0,0,0):C.UVGC_376_132,(0,1,1):C.UVGC_381_145,(0,1,2):C.UVGC_381_146,(0,1,0):C.UVGC_381_147})

V_311 = CTVertex(name = 'V_311',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_400_186,(0,0,2):C.UVGC_400_187,(0,0,1):C.UVGC_400_188,(0,1,0):C.UVGC_401_189,(0,1,2):C.UVGC_401_190,(0,1,1):C.UVGC_401_191})

V_312 = CTVertex(name = 'V_312',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.d, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_512_505,(0,0,2):C.UVGC_512_506,(0,0,1):C.UVGC_512_507,(0,1,0):C.UVGC_515_514,(0,1,2):C.UVGC_515_515,(0,1,1):C.UVGC_515_516})

V_313 = CTVertex(name = 'V_313',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.s, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_513_508,(0,0,2):C.UVGC_513_509,(0,0,1):C.UVGC_513_510,(0,1,0):C.UVGC_516_517,(0,1,2):C.UVGC_516_518,(0,1,1):C.UVGC_516_519})

V_314 = CTVertex(name = 'V_314',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.b, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_514_511,(0,0,2):C.UVGC_514_512,(0,0,1):C.UVGC_514_513,(0,1,0):C.UVGC_517_520,(0,1,2):C.UVGC_517_521,(0,1,1):C.UVGC_517_522})

V_315 = CTVertex(name = 'V_315',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_377_133,(0,0,2):C.UVGC_377_134,(0,0,0):C.UVGC_377_135,(0,1,1):C.UVGC_382_148,(0,1,2):C.UVGC_382_149,(0,1,0):C.UVGC_382_150})

V_316 = CTVertex(name = 'V_316',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_378_136,(0,0,2):C.UVGC_378_137,(0,0,1):C.UVGC_378_138,(0,1,0):C.UVGC_383_151,(0,1,2):C.UVGC_383_152,(0,1,1):C.UVGC_383_153})

V_317 = CTVertex(name = 'V_317',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_379_139,(0,0,2):C.UVGC_379_140,(0,0,0):C.UVGC_379_141,(0,1,1):C.UVGC_384_154,(0,1,2):C.UVGC_384_155,(0,1,0):C.UVGC_384_156})

V_318 = CTVertex(name = 'V_318',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_434_270,(0,0,2):C.UVGC_434_271,(0,0,1):C.UVGC_434_272,(0,1,0):C.UVGC_440_288,(0,1,2):C.UVGC_440_289,(0,1,1):C.UVGC_440_290})

V_319 = CTVertex(name = 'V_319',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_435_273,(0,0,2):C.UVGC_435_274,(0,0,1):C.UVGC_435_275,(0,1,0):C.UVGC_441_291,(0,1,2):C.UVGC_441_292,(0,1,1):C.UVGC_441_293})

V_320 = CTVertex(name = 'V_320',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_436_276,(0,0,1):C.UVGC_436_277,(0,0,2):C.UVGC_436_278,(0,1,0):C.UVGC_442_294,(0,1,1):C.UVGC_442_295,(0,1,2):C.UVGC_442_296})

V_321 = CTVertex(name = 'V_321',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_510_499,(0,0,2):C.UVGC_510_500,(0,0,1):C.UVGC_510_501,(0,1,0):C.UVGC_511_502,(0,1,2):C.UVGC_511_503,(0,1,1):C.UVGC_511_504})

V_322 = CTVertex(name = 'V_322',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_443_297,(0,0,2):C.UVGC_443_298,(0,0,1):C.UVGC_443_299,(0,1,0):C.UVGC_444_300,(0,1,2):C.UVGC_444_301,(0,1,1):C.UVGC_444_302})

V_323 = CTVertex(name = 'V_323',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.tp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_469_359,(0,0,2):C.UVGC_469_360,(0,0,1):C.UVGC_469_361,(0,1,0):C.UVGC_470_362,(0,1,2):C.UVGC_470_363,(0,1,1):C.UVGC_470_364})

V_324 = CTVertex(name = 'V_324',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.bp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_510_499,(0,0,2):C.UVGC_510_500,(0,0,1):C.UVGC_510_501,(0,1,0):C.UVGC_511_502,(0,1,2):C.UVGC_511_503,(0,1,1):C.UVGC_511_504})

V_325 = CTVertex(name = 'V_325',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_443_297,(0,0,2):C.UVGC_443_298,(0,0,1):C.UVGC_443_299,(0,1,0):C.UVGC_444_300,(0,1,2):C.UVGC_444_301,(0,1,1):C.UVGC_444_302})

V_326 = CTVertex(name = 'V_326',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_469_359,(0,0,2):C.UVGC_469_360,(0,0,1):C.UVGC_469_361,(0,1,0):C.UVGC_470_362,(0,1,2):C.UVGC_470_363,(0,1,1):C.UVGC_470_364})

V_327 = CTVertex(name = 'V_327',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_431_261,(0,0,2):C.UVGC_431_262,(0,0,1):C.UVGC_431_263,(0,1,0):C.UVGC_437_279,(0,1,2):C.UVGC_437_280,(0,1,1):C.UVGC_437_281})

V_328 = CTVertex(name = 'V_328',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_432_264,(0,0,2):C.UVGC_432_265,(0,0,1):C.UVGC_432_266,(0,1,0):C.UVGC_438_282,(0,1,2):C.UVGC_438_283,(0,1,1):C.UVGC_438_284})

V_329 = CTVertex(name = 'V_329',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_433_267,(0,0,2):C.UVGC_433_268,(0,0,1):C.UVGC_433_269,(0,1,0):C.UVGC_439_285,(0,1,2):C.UVGC_439_286,(0,1,1):C.UVGC_439_287})

V_330 = CTVertex(name = 'V_330',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_471_365,(0,0,2):C.UVGC_471_366,(0,0,1):C.UVGC_471_367,(0,1,0):C.UVGC_474_374,(0,1,2):C.UVGC_474_375,(0,1,1):C.UVGC_474_376})

V_331 = CTVertex(name = 'V_331',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_472_368,(0,0,2):C.UVGC_472_369,(0,0,1):C.UVGC_472_370,(0,1,0):C.UVGC_475_377,(0,1,2):C.UVGC_475_378,(0,1,1):C.UVGC_475_379})

V_332 = CTVertex(name = 'V_332',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.x, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.x] ], [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_473_371,(0,0,2):C.UVGC_473_372,(0,0,1):C.UVGC_473_373,(0,1,0):C.UVGC_476_380,(0,1,2):C.UVGC_476_381,(0,1,1):C.UVGC_476_382})

V_333 = CTVertex(name = 'V_333',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_375_127,(0,0,2):C.UVGC_375_128,(0,0,1):C.UVGC_375_129,(0,1,0):C.UVGC_380_142,(0,1,2):C.UVGC_380_143,(0,1,1):C.UVGC_380_144})

V_334 = CTVertex(name = 'V_334',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.c, P.g] ], [ [P.bp, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_376_130,(0,0,2):C.UVGC_376_131,(0,0,0):C.UVGC_376_132,(0,1,1):C.UVGC_381_145,(0,1,2):C.UVGC_381_146,(0,1,0):C.UVGC_381_147})

V_335 = CTVertex(name = 'V_335',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_400_186,(0,0,2):C.UVGC_400_187,(0,0,1):C.UVGC_400_188,(0,1,0):C.UVGC_401_189,(0,1,2):C.UVGC_401_190,(0,1,1):C.UVGC_401_191})

V_336 = CTVertex(name = 'V_336',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_512_505,(0,0,2):C.UVGC_512_506,(0,0,1):C.UVGC_512_507,(0,1,0):C.UVGC_515_514,(0,1,2):C.UVGC_515_515,(0,1,1):C.UVGC_515_516})

V_337 = CTVertex(name = 'V_337',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_513_508,(0,0,2):C.UVGC_513_509,(0,0,1):C.UVGC_513_510,(0,1,0):C.UVGC_516_517,(0,1,2):C.UVGC_516_518,(0,1,1):C.UVGC_516_519})

V_338 = CTVertex(name = 'V_338',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.y, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.y] ], [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_514_511,(0,0,2):C.UVGC_514_512,(0,0,1):C.UVGC_514_513,(0,1,0):C.UVGC_517_520,(0,1,2):C.UVGC_517_521,(0,1,1):C.UVGC_517_522})

V_339 = CTVertex(name = 'V_339',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_385_157,(0,1,0):C.UVGC_386_158})

V_340 = CTVertex(name = 'V_340',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_445_303,(0,1,0):C.UVGC_446_304})

V_341 = CTVertex(name = 'V_341',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_477_383,(0,1,0):C.UVGC_478_384})

V_342 = CTVertex(name = 'V_342',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_518_523,(0,1,0):C.UVGC_519_524})

V_343 = CTVertex(name = 'V_343',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.d, P.g] ], [ [P.bp, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_377_133,(0,0,2):C.UVGC_377_134,(0,0,0):C.UVGC_377_135,(0,1,1):C.UVGC_382_148,(0,1,2):C.UVGC_382_149,(0,1,0):C.UVGC_382_150})

V_344 = CTVertex(name = 'V_344',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.bp, P.g] ], [ [P.bp, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_378_136,(0,0,2):C.UVGC_378_137,(0,0,1):C.UVGC_378_138,(0,1,0):C.UVGC_383_151,(0,1,2):C.UVGC_383_152,(0,1,1):C.UVGC_383_153})

V_345 = CTVertex(name = 'V_345',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.bp, P.g] ], [ [P.b, P.g] ], [ [P.bp, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_379_139,(0,0,2):C.UVGC_379_140,(0,0,0):C.UVGC_379_141,(0,1,1):C.UVGC_384_154,(0,1,2):C.UVGC_384_155,(0,1,0):C.UVGC_384_156})

V_346 = CTVertex(name = 'V_346',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.tp] ], [ [P.g, P.tp, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_434_270,(0,0,2):C.UVGC_434_271,(0,0,1):C.UVGC_434_272,(0,1,0):C.UVGC_440_288,(0,1,2):C.UVGC_440_289,(0,1,1):C.UVGC_440_290})

V_347 = CTVertex(name = 'V_347',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.tp] ], [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_435_273,(0,0,2):C.UVGC_435_274,(0,0,1):C.UVGC_435_275,(0,1,0):C.UVGC_441_291,(0,1,2):C.UVGC_441_292,(0,1,1):C.UVGC_441_293})

V_348 = CTVertex(name = 'V_348',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp] ], [ [P.g, P.t, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_436_276,(0,0,1):C.UVGC_436_277,(0,0,2):C.UVGC_436_278,(0,1,0):C.UVGC_442_294,(0,1,1):C.UVGC_442_295,(0,1,2):C.UVGC_442_296})

V_349 = CTVertex(name = 'V_349',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_303_21,(0,1,0):C.UVGC_284_4,(0,2,0):C.UVGC_284_4})

V_350 = CTVertex(name = 'V_350',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_303_21,(0,1,0):C.UVGC_284_4,(0,2,0):C.UVGC_284_4})

V_351 = CTVertex(name = 'V_351',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_303_21,(0,1,0):C.UVGC_388_160,(0,2,0):C.UVGC_388_160})

V_352 = CTVertex(name = 'V_352',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_298_18,(0,1,0):C.UVGC_286_5,(0,2,0):C.UVGC_286_5})

V_353 = CTVertex(name = 'V_353',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_298_18,(0,1,0):C.UVGC_286_5,(0,2,0):C.UVGC_286_5})

V_354 = CTVertex(name = 'V_354',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_298_18,(0,1,0):C.UVGC_343_59,(0,2,0):C.UVGC_343_59})

V_355 = CTVertex(name = 'V_355',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,3):C.UVGC_304_25,(0,1,4):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,5):C.UVGC_304_31,(0,2,0):C.UVGC_304_22,(0,2,1):C.UVGC_304_23,(0,2,2):C.UVGC_304_24,(0,2,3):C.UVGC_304_25,(0,2,4):C.UVGC_304_26,(0,2,6):C.UVGC_304_27,(0,2,7):C.UVGC_304_28,(0,2,8):C.UVGC_304_29,(0,2,9):C.UVGC_304_30,(0,2,5):C.UVGC_304_31})

V_356 = CTVertex(name = 'V_356',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,4):C.UVGC_304_25,(0,1,5):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,3):C.UVGC_304_31,(0,2,0):C.UVGC_304_22,(0,2,1):C.UVGC_304_23,(0,2,2):C.UVGC_304_24,(0,2,4):C.UVGC_304_25,(0,2,5):C.UVGC_304_26,(0,2,6):C.UVGC_304_27,(0,2,7):C.UVGC_304_28,(0,2,8):C.UVGC_304_29,(0,2,9):C.UVGC_304_30,(0,2,3):C.UVGC_304_31})

V_357 = CTVertex(name = 'V_357',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,3):C.UVGC_304_25,(0,1,4):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,5):C.UVGC_389_161,(0,2,0):C.UVGC_304_22,(0,2,1):C.UVGC_304_23,(0,2,2):C.UVGC_304_24,(0,2,3):C.UVGC_304_25,(0,2,4):C.UVGC_304_26,(0,2,6):C.UVGC_304_27,(0,2,7):C.UVGC_304_28,(0,2,8):C.UVGC_304_29,(0,2,9):C.UVGC_304_30,(0,2,5):C.UVGC_389_161})

V_358 = CTVertex(name = 'V_358',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,3):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,4):C.UVGC_304_25,(0,1,5):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,3):C.UVGC_304_31,(0,2,0):C.UVGC_304_22,(0,2,1):C.UVGC_304_23,(0,2,2):C.UVGC_304_24,(0,2,4):C.UVGC_304_25,(0,2,5):C.UVGC_304_26,(0,2,6):C.UVGC_304_27,(0,2,7):C.UVGC_304_28,(0,2,8):C.UVGC_304_29,(0,2,9):C.UVGC_304_30,(0,2,3):C.UVGC_304_31})

V_359 = CTVertex(name = 'V_359',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,5):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,2):C.UVGC_304_24,(0,1,3):C.UVGC_304_25,(0,1,4):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,5):C.UVGC_304_31,(0,2,0):C.UVGC_304_22,(0,2,1):C.UVGC_304_23,(0,2,2):C.UVGC_304_24,(0,2,3):C.UVGC_304_25,(0,2,4):C.UVGC_304_26,(0,2,6):C.UVGC_304_27,(0,2,7):C.UVGC_304_28,(0,2,8):C.UVGC_304_29,(0,2,9):C.UVGC_304_30,(0,2,5):C.UVGC_304_31})

V_360 = CTVertex(name = 'V_360',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,2):C.UVGC_299_19,(0,1,0):C.UVGC_304_22,(0,1,1):C.UVGC_304_23,(0,1,3):C.UVGC_304_24,(0,1,4):C.UVGC_304_25,(0,1,5):C.UVGC_304_26,(0,1,6):C.UVGC_304_27,(0,1,7):C.UVGC_304_28,(0,1,8):C.UVGC_304_29,(0,1,9):C.UVGC_304_30,(0,1,2):C.UVGC_344_60,(0,2,0):C.UVGC_304_22,(0,2,1):C.UVGC_304_23,(0,2,3):C.UVGC_304_24,(0,2,4):C.UVGC_304_25,(0,2,5):C.UVGC_304_26,(0,2,6):C.UVGC_304_27,(0,2,7):C.UVGC_304_28,(0,2,8):C.UVGC_304_29,(0,2,9):C.UVGC_304_30,(0,2,2):C.UVGC_344_60})

V_361 = CTVertex(name = 'V_361',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_340_54,(0,0,1):C.UVGC_340_55})

V_362 = CTVertex(name = 'V_362',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_341_56,(0,0,1):C.UVGC_341_57})

V_363 = CTVertex(name = 'V_363',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_348_64,(0,0,2):C.UVGC_348_65,(0,0,1):C.UVGC_348_66})

V_364 = CTVertex(name = 'V_364',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_334_42,(0,0,0):C.UVGC_334_43})

V_365 = CTVertex(name = 'V_365',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_337_48,(0,0,1):C.UVGC_337_49})

V_366 = CTVertex(name = 'V_366',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_349_67,(0,0,2):C.UVGC_349_68,(0,0,0):C.UVGC_349_69})

V_367 = CTVertex(name = 'V_367',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_397_177,(0,0,2):C.UVGC_397_178,(0,0,1):C.UVGC_397_179})

V_368 = CTVertex(name = 'V_368',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_398_180,(0,0,2):C.UVGC_398_181,(0,0,1):C.UVGC_398_182})

V_369 = CTVertex(name = 'V_369',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_399_183,(0,0,2):C.UVGC_399_184,(0,0,1):C.UVGC_399_185})

V_370 = CTVertex(name = 'V_370',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_340_54,(0,0,1):C.UVGC_340_55})

V_371 = CTVertex(name = 'V_371',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_334_42,(0,0,0):C.UVGC_334_43})

V_372 = CTVertex(name = 'V_372',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_397_177,(0,0,2):C.UVGC_397_178,(0,0,1):C.UVGC_397_179})

V_373 = CTVertex(name = 'V_373',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_341_56,(0,0,1):C.UVGC_341_57})

V_374 = CTVertex(name = 'V_374',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_337_48,(0,0,1):C.UVGC_337_49})

V_375 = CTVertex(name = 'V_375',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_398_180,(0,0,2):C.UVGC_398_181,(0,0,1):C.UVGC_398_182})

V_376 = CTVertex(name = 'V_376',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_348_64,(0,0,2):C.UVGC_348_65,(0,0,1):C.UVGC_348_66})

V_377 = CTVertex(name = 'V_377',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g] ], [ [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_349_67,(0,0,2):C.UVGC_349_68,(0,0,0):C.UVGC_349_69})

V_378 = CTVertex(name = 'V_378',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_399_183,(0,0,2):C.UVGC_399_184,(0,0,1):C.UVGC_399_185})

V_379 = CTVertex(name = 'V_379',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_402_192,(0,1,0):C.UVGC_403_193})

V_380 = CTVertex(name = 'V_380',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_350_70,(0,1,0):C.UVGC_351_71})

V_381 = CTVertex(name = 'V_381',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_302_20,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_382 = CTVertex(name = 'V_382',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_302_20,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_383 = CTVertex(name = 'V_383',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_396_176,(0,2,0):C.UVGC_396_176,(0,1,0):C.UVGC_387_159,(0,3,0):C.UVGC_387_159})

V_384 = CTVertex(name = 'V_384',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_302_20,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_385 = CTVertex(name = 'V_385',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_302_20,(0,1,0):C.UVGC_283_3,(0,2,0):C.UVGC_283_3})

V_386 = CTVertex(name = 'V_386',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_347_63,(0,2,0):C.UVGC_347_63,(0,1,0):C.UVGC_342_58,(0,3,0):C.UVGC_342_58})

V_387 = CTVertex(name = 'V_387',
                 type = 'UV',
                 particles = [ P.x__tilde__, P.x ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.x] ] ],
                 couplings = {(0,0,0):C.UVGC_468_358,(0,2,0):C.UVGC_468_358,(0,1,0):C.UVGC_447_305,(0,3,0):C.UVGC_447_305})

V_388 = CTVertex(name = 'V_388',
                 type = 'UV',
                 particles = [ P.tp__tilde__, P.tp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp] ] ],
                 couplings = {(0,0,0):C.UVGC_430_260,(0,2,0):C.UVGC_430_260,(0,1,0):C.UVGC_405_195,(0,3,0):C.UVGC_405_195})

V_389 = CTVertex(name = 'V_389',
                 type = 'UV',
                 particles = [ P.bp__tilde__, P.bp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.bp, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_374_126,(0,2,0):C.UVGC_374_126,(0,1,0):C.UVGC_353_73,(0,3,0):C.UVGC_353_73})

V_390 = CTVertex(name = 'V_390',
                 type = 'UV',
                 particles = [ P.y__tilde__, P.y ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_509_498,(0,2,0):C.UVGC_509_498,(0,1,0):C.UVGC_488_445,(0,3,0):C.UVGC_488_445})

V_391 = CTVertex(name = 'V_391',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.tp] ], [ [P.x] ], [ [P.y] ] ],
                 couplings = {(0,0,0):C.UVGC_480_391,(0,0,1):C.UVGC_480_392,(0,0,2):C.UVGC_480_393,(0,0,3):C.UVGC_480_394,(0,0,4):C.UVGC_480_395,(0,0,5):C.UVGC_480_396,(0,0,6):C.UVGC_480_397,(0,0,7):C.UVGC_480_398,(0,1,0):C.UVGC_479_385,(0,1,1):C.UVGC_479_386,(0,1,4):C.UVGC_479_387,(0,1,5):C.UVGC_479_388,(0,1,6):C.UVGC_479_389,(0,1,7):C.UVGC_479_390})

