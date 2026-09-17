# This file was automatically created by FeynRules 2.3.41
# Mathematica version: 11.0.1 for Microsoft Windows (64-bit) (September 20, 2016)
# Date: Thu 31 Mar 2022 19:27:36


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G0, P.G0, P.G0, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_420})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_418})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_419})

V_4 = Vertex(name = 'V_4',
             particles = [ P.G0, P.G0, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_418})

V_5 = Vertex(name = 'V_5',
             particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_418})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_420})

V_7 = Vertex(name = 'V_7',
             particles = [ P.G0, P.G0, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_590})

V_8 = Vertex(name = 'V_8',
             particles = [ P.G__minus__, P.G__plus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_590})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_591})

V_10 = Vertex(name = 'V_10',
              particles = [ P.H, P.H, P.S10 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_584})

V_11 = Vertex(name = 'V_11',
              particles = [ P.H, P.S10, P.S10 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_583})

V_12 = Vertex(name = 'V_12',
              particles = [ P.H, P.H, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_576})

V_13 = Vertex(name = 'V_13',
              particles = [ P.H, P.S102, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_575})

V_14 = Vertex(name = 'V_14',
              particles = [ P.H, P.H, P.S103 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_578})

V_15 = Vertex(name = 'V_15',
              particles = [ P.H, P.S103, P.S103 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_577})

V_16 = Vertex(name = 'V_16',
              particles = [ P.H, P.H, P.S104 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_580})

V_17 = Vertex(name = 'V_17',
              particles = [ P.H, P.S104, P.S104 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_579})

V_18 = Vertex(name = 'V_18',
              particles = [ P.H, P.H, P.S105 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_582})

V_19 = Vertex(name = 'V_19',
              particles = [ P.H, P.S105, P.S105 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_581})

V_20 = Vertex(name = 'V_20',
              particles = [ P.H, P.S112__tilde__, P.S112 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_585})

V_21 = Vertex(name = 'V_21',
              particles = [ P.H, P.S11__tilde__, P.S11 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_586})

V_22 = Vertex(name = 'V_22',
              particles = [ P.H, P.S12__tilde__, P.S12 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_587})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_26})

V_24 = Vertex(name = 'V_24',
              particles = [ P.a, P.a, P.S112__tilde__, P.S112 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_26})

V_25 = Vertex(name = 'V_25',
              particles = [ P.a, P.a, P.S11__tilde__, P.S11 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_26})

V_26 = Vertex(name = 'V_26',
              particles = [ P.a, P.a, P.S12__tilde__, P.S12 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_27})

V_27 = Vertex(name = 'V_27',
              particles = [ P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1, L.VSS2 ],
              couplings = {(0,0):C.GC_17,(0,1):C.GC_18})

V_28 = Vertex(name = 'V_28',
              particles = [ P.a, P.S11__tilde__, P.S11 ],
              color = [ '1' ],
              lorentz = [ L.VSS1, L.VSS2 ],
              couplings = {(0,0):C.GC_17,(0,1):C.GC_18})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.S112__tilde__, P.S112 ],
              color = [ '1' ],
              lorentz = [ L.VSS1, L.VSS2 ],
              couplings = {(0,0):C.GC_17,(0,1):C.GC_18})

V_30 = Vertex(name = 'V_30',
              particles = [ P.a, P.S12__tilde__, P.S12 ],
              color = [ '1' ],
              lorentz = [ L.VSS1, L.VSS2 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_22})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.W__minus__, P.S112 ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS5 ],
              couplings = {(0,1):C.GC_537,(0,0):C.GC_570,(0,2):C.GC_569})

V_32 = Vertex(name = 'V_32',
              particles = [ P.a, P.W__minus__, P.S112 ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_567})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__minus__, P.S12 ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2, L.VVS3, L.VVS5 ],
              couplings = {(0,1):C.GC_563,(0,2):C.GC_564,(0,0):C.GC_566,(0,3):C.GC_565})

V_34 = Vertex(name = 'V_34',
              particles = [ P.W__minus__, P.W__minus__, P.S12 ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_596,(0,1):C.GC_597})

V_35 = Vertex(name = 'V_35',
              particles = [ P.W__plus__, P.W__plus__, P.S12__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2, L.VVS3, L.VVS5 ],
              couplings = {(0,1):C.GC_563,(0,2):C.GC_564,(0,0):C.GC_566,(0,3):C.GC_565})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__plus__, P.W__plus__, P.S12__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_596,(0,1):C.GC_597})

V_37 = Vertex(name = 'V_37',
              particles = [ P.W__minus__, P.Z, P.S112 ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2, L.VVS5 ],
              couplings = {(0,1):C.GC_428,(0,0):C.GC_572,(0,2):C.GC_571})

V_38 = Vertex(name = 'V_38',
              particles = [ P.W__minus__, P.Z, P.S112 ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_568})

V_39 = Vertex(name = 'V_39',
              particles = [ P.bp__tilde__, P.bp, P.S10 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_102,(0,1):C.GC_252})

V_40 = Vertex(name = 'V_40',
              particles = [ P.bp__tilde__, P.bp, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_38,(0,1):C.GC_140})

V_41 = Vertex(name = 'V_41',
              particles = [ P.bp__tilde__, P.bp, P.S103 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_54,(0,1):C.GC_168})

V_42 = Vertex(name = 'V_42',
              particles = [ P.bp__tilde__, P.bp, P.S104 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_70,(0,1):C.GC_196})

V_43 = Vertex(name = 'V_43',
              particles = [ P.bp__tilde__, P.bp, P.S105 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_86,(0,1):C.GC_224})

V_44 = Vertex(name = 'V_44',
              particles = [ P.tp__tilde__, P.tp, P.S10 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_112,(0,1):C.GC_274})

V_45 = Vertex(name = 'V_45',
              particles = [ P.tp__tilde__, P.tp, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_48,(0,1):C.GC_162})

V_46 = Vertex(name = 'V_46',
              particles = [ P.tp__tilde__, P.tp, P.S103 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_64,(0,1):C.GC_190})

V_47 = Vertex(name = 'V_47',
              particles = [ P.tp__tilde__, P.tp, P.S104 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_80,(0,1):C.GC_218})

V_48 = Vertex(name = 'V_48',
              particles = [ P.tp__tilde__, P.tp, P.S105 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_96,(0,1):C.GC_246})

V_49 = Vertex(name = 'V_49',
              particles = [ P.x__tilde__, P.x, P.S10 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_116,(0,1):C.GC_278})

V_50 = Vertex(name = 'V_50',
              particles = [ P.x__tilde__, P.x, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_52,(0,1):C.GC_166})

V_51 = Vertex(name = 'V_51',
              particles = [ P.x__tilde__, P.x, P.S103 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_68,(0,1):C.GC_194})

V_52 = Vertex(name = 'V_52',
              particles = [ P.x__tilde__, P.x, P.S104 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_84,(0,1):C.GC_222})

V_53 = Vertex(name = 'V_53',
              particles = [ P.x__tilde__, P.x, P.S105 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_100,(0,1):C.GC_250})

V_54 = Vertex(name = 'V_54',
              particles = [ P.y__tilde__, P.y, P.S10 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_117,(0,1):C.GC_279})

V_55 = Vertex(name = 'V_55',
              particles = [ P.y__tilde__, P.y, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_53,(0,1):C.GC_167})

V_56 = Vertex(name = 'V_56',
              particles = [ P.y__tilde__, P.y, P.S103 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_69,(0,1):C.GC_195})

V_57 = Vertex(name = 'V_57',
              particles = [ P.y__tilde__, P.y, P.S104 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_85,(0,1):C.GC_223})

V_58 = Vertex(name = 'V_58',
              particles = [ P.y__tilde__, P.y, P.S105 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_101,(0,1):C.GC_251})

V_59 = Vertex(name = 'V_59',
              particles = [ P.a, P.a, P.S10 ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_421,(0,1):C.GC_422})

V_60 = Vertex(name = 'V_60',
              particles = [ P.a, P.Z, P.S10 ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_555})

V_61 = Vertex(name = 'V_61',
              particles = [ P.Z, P.Z, P.S10 ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_561,(0,1):C.GC_562})

V_62 = Vertex(name = 'V_62',
              particles = [ P.W__minus__, P.W__plus__, P.S10 ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_436})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.a, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_425,(0,1):C.GC_426})

V_64 = Vertex(name = 'V_64',
              particles = [ P.Z, P.Z, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_426,(0,1):C.GC_425})

V_65 = Vertex(name = 'V_65',
              particles = [ P.a, P.Z, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_557})

V_66 = Vertex(name = 'V_66',
              particles = [ P.a, P.W__plus__, P.S11__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_538})

V_67 = Vertex(name = 'V_67',
              particles = [ P.W__plus__, P.Z, P.S11__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_429})

V_68 = Vertex(name = 'V_68',
              particles = [ P.a, P.a, P.S104 ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_424,(0,1):C.GC_423})

V_69 = Vertex(name = 'V_69',
              particles = [ P.Z, P.Z, P.S104 ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3 ],
              couplings = {(0,0):C.GC_423,(0,1):C.GC_424})

V_70 = Vertex(name = 'V_70',
              particles = [ P.a, P.Z, P.S104 ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_556})

V_71 = Vertex(name = 'V_71',
              particles = [ P.a, P.W__plus__, P.S112__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_537})

V_72 = Vertex(name = 'V_72',
              particles = [ P.W__plus__, P.Z, P.S112__tilde__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_428})

V_73 = Vertex(name = 'V_73',
              particles = [ P.a, P.W__minus__, P.S11 ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_536})

V_74 = Vertex(name = 'V_74',
              particles = [ P.W__minus__, P.Z, P.S11 ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_427})

V_75 = Vertex(name = 'V_75',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_31,(0,1):C.GC_31})

V_76 = Vertex(name = 'V_76',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6 ],
              couplings = {(0,0):C.GC_31,(0,1):C.GC_34,(0,2):C.GC_34,(0,3):C.GC_31,(0,4):C.GC_31,(0,5):C.GC_34})

V_77 = Vertex(name = 'V_77',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
              couplings = {(1,0):C.GC_37,(0,0):C.GC_37,(2,1):C.GC_37,(0,1):C.GC_36,(2,2):C.GC_36,(1,2):C.GC_36})

V_78 = Vertex(name = 'V_78',
              particles = [ P.bp__tilde__, P.bp, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_14})

V_79 = Vertex(name = 'V_79',
              particles = [ P.Q11__tilde__, P.Q11, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_80 = Vertex(name = 'V_80',
              particles = [ P.Q81__tilde__, P.Q81, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_81 = Vertex(name = 'V_81',
              particles = [ P.tp2__tilde__, P.tp2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_16})

V_82 = Vertex(name = 'V_82',
              particles = [ P.tp3__tilde__, P.tp3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_16})

V_83 = Vertex(name = 'V_83',
              particles = [ P.tp__tilde__, P.tp, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_16})

V_84 = Vertex(name = 'V_84',
              particles = [ P.x__tilde__, P.x, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_20})

V_85 = Vertex(name = 'V_85',
              particles = [ P.y__tilde__, P.y, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_19})

V_86 = Vertex(name = 'V_86',
              particles = [ P.Q81__tilde__, P.Q81, P.g ],
              color = [ 'f(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_34})

V_87 = Vertex(name = 'V_87',
              particles = [ P.Q80__tilde__, P.Q80, P.g ],
              color = [ 'f(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_34})

V_88 = Vertex(name = 'V_88',
              particles = [ P.Q80M, P.Q80M, P.g ],
              color = [ 'f(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_34})

V_89 = Vertex(name = 'V_89',
              particles = [ P.d__tilde__, P.d, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_39,(0,1):C.GC_147})

V_90 = Vertex(name = 'V_90',
              particles = [ P.s__tilde__, P.s, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_40,(0,1):C.GC_148})

V_91 = Vertex(name = 'V_91',
              particles = [ P.b__tilde__, P.b, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_41,(0,1):C.GC_149})

V_92 = Vertex(name = 'V_92',
              particles = [ P.e__plus__, P.e__minus__, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_42,(0,1):C.GC_150})

V_93 = Vertex(name = 'V_93',
              particles = [ P.mu__plus__, P.mu__minus__, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_43,(0,1):C.GC_151})

V_94 = Vertex(name = 'V_94',
              particles = [ P.ta__plus__, P.ta__minus__, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_152})

V_95 = Vertex(name = 'V_95',
              particles = [ P.ve__tilde__, P.ve, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_45,(0,1):C.GC_153})

V_96 = Vertex(name = 'V_96',
              particles = [ P.vm__tilde__, P.vm, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_46,(0,1):C.GC_154})

V_97 = Vertex(name = 'V_97',
              particles = [ P.vt__tilde__, P.vt, P.S102 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_155})

V_98 = Vertex(name = 'V_98',
              particles = [ P.u__tilde__, P.u, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_49,(0,1):C.GC_163})

V_99 = Vertex(name = 'V_99',
              particles = [ P.c__tilde__, P.c, P.S102 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_50,(0,1):C.GC_164})

V_100 = Vertex(name = 'V_100',
               particles = [ P.t__tilde__, P.t, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_51,(0,1):C.GC_165})

V_101 = Vertex(name = 'V_101',
               particles = [ P.d__tilde__, P.d, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_55,(0,1):C.GC_175})

V_102 = Vertex(name = 'V_102',
               particles = [ P.s__tilde__, P.s, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_56,(0,1):C.GC_176})

V_103 = Vertex(name = 'V_103',
               particles = [ P.b__tilde__, P.b, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_177})

V_104 = Vertex(name = 'V_104',
               particles = [ P.e__plus__, P.e__minus__, P.S103 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_58,(0,1):C.GC_178})

V_105 = Vertex(name = 'V_105',
               particles = [ P.mu__plus__, P.mu__minus__, P.S103 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_59,(0,1):C.GC_179})

V_106 = Vertex(name = 'V_106',
               particles = [ P.ta__plus__, P.ta__minus__, P.S103 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_60,(0,1):C.GC_180})

V_107 = Vertex(name = 'V_107',
               particles = [ P.ve__tilde__, P.ve, P.S103 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_61,(0,1):C.GC_181})

V_108 = Vertex(name = 'V_108',
               particles = [ P.vm__tilde__, P.vm, P.S103 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_62,(0,1):C.GC_182})

V_109 = Vertex(name = 'V_109',
               particles = [ P.vt__tilde__, P.vt, P.S103 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_63,(0,1):C.GC_183})

V_110 = Vertex(name = 'V_110',
               particles = [ P.u__tilde__, P.u, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_65,(0,1):C.GC_191})

V_111 = Vertex(name = 'V_111',
               particles = [ P.c__tilde__, P.c, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_66,(0,1):C.GC_192})

V_112 = Vertex(name = 'V_112',
               particles = [ P.t__tilde__, P.t, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_67,(0,1):C.GC_193})

V_113 = Vertex(name = 'V_113',
               particles = [ P.d__tilde__, P.d, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_71,(0,1):C.GC_203})

V_114 = Vertex(name = 'V_114',
               particles = [ P.s__tilde__, P.s, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_72,(0,1):C.GC_204})

V_115 = Vertex(name = 'V_115',
               particles = [ P.b__tilde__, P.b, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_73,(0,1):C.GC_205})

V_116 = Vertex(name = 'V_116',
               particles = [ P.e__plus__, P.e__minus__, P.S104 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_74,(0,1):C.GC_206})

V_117 = Vertex(name = 'V_117',
               particles = [ P.mu__plus__, P.mu__minus__, P.S104 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_75,(0,1):C.GC_207})

V_118 = Vertex(name = 'V_118',
               particles = [ P.ta__plus__, P.ta__minus__, P.S104 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_76,(0,1):C.GC_208})

V_119 = Vertex(name = 'V_119',
               particles = [ P.ve__tilde__, P.ve, P.S104 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_77,(0,1):C.GC_209})

V_120 = Vertex(name = 'V_120',
               particles = [ P.vm__tilde__, P.vm, P.S104 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_78,(0,1):C.GC_210})

V_121 = Vertex(name = 'V_121',
               particles = [ P.vt__tilde__, P.vt, P.S104 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_79,(0,1):C.GC_211})

V_122 = Vertex(name = 'V_122',
               particles = [ P.u__tilde__, P.u, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_81,(0,1):C.GC_219})

V_123 = Vertex(name = 'V_123',
               particles = [ P.c__tilde__, P.c, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_82,(0,1):C.GC_220})

V_124 = Vertex(name = 'V_124',
               particles = [ P.t__tilde__, P.t, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_83,(0,1):C.GC_221})

V_125 = Vertex(name = 'V_125',
               particles = [ P.d__tilde__, P.d, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_87,(0,1):C.GC_231})

V_126 = Vertex(name = 'V_126',
               particles = [ P.s__tilde__, P.s, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_88,(0,1):C.GC_232})

V_127 = Vertex(name = 'V_127',
               particles = [ P.b__tilde__, P.b, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_89,(0,1):C.GC_233})

V_128 = Vertex(name = 'V_128',
               particles = [ P.e__plus__, P.e__minus__, P.S105 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_90,(0,1):C.GC_234})

V_129 = Vertex(name = 'V_129',
               particles = [ P.mu__plus__, P.mu__minus__, P.S105 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_91,(0,1):C.GC_235})

V_130 = Vertex(name = 'V_130',
               particles = [ P.ta__plus__, P.ta__minus__, P.S105 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_92,(0,1):C.GC_236})

V_131 = Vertex(name = 'V_131',
               particles = [ P.ve__tilde__, P.ve, P.S105 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_93,(0,1):C.GC_237})

V_132 = Vertex(name = 'V_132',
               particles = [ P.vm__tilde__, P.vm, P.S105 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_94,(0,1):C.GC_238})

V_133 = Vertex(name = 'V_133',
               particles = [ P.vt__tilde__, P.vt, P.S105 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_95,(0,1):C.GC_239})

V_134 = Vertex(name = 'V_134',
               particles = [ P.u__tilde__, P.u, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_97,(0,1):C.GC_247})

V_135 = Vertex(name = 'V_135',
               particles = [ P.c__tilde__, P.c, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_98,(0,1):C.GC_248})

V_136 = Vertex(name = 'V_136',
               particles = [ P.t__tilde__, P.t, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_99,(0,1):C.GC_249})

V_137 = Vertex(name = 'V_137',
               particles = [ P.d__tilde__, P.d, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_103,(0,1):C.GC_259})

V_138 = Vertex(name = 'V_138',
               particles = [ P.s__tilde__, P.s, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_260})

V_139 = Vertex(name = 'V_139',
               particles = [ P.b__tilde__, P.b, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_261})

V_140 = Vertex(name = 'V_140',
               particles = [ P.e__plus__, P.e__minus__, P.S10 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_106,(0,1):C.GC_262})

V_141 = Vertex(name = 'V_141',
               particles = [ P.mu__plus__, P.mu__minus__, P.S10 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_107,(0,1):C.GC_263})

V_142 = Vertex(name = 'V_142',
               particles = [ P.ta__plus__, P.ta__minus__, P.S10 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_108,(0,1):C.GC_264})

V_143 = Vertex(name = 'V_143',
               particles = [ P.ve__tilde__, P.ve, P.S10 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_109,(0,1):C.GC_265})

V_144 = Vertex(name = 'V_144',
               particles = [ P.vm__tilde__, P.vm, P.S10 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_110,(0,1):C.GC_266})

V_145 = Vertex(name = 'V_145',
               particles = [ P.vt__tilde__, P.vt, P.S10 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_111,(0,1):C.GC_267})

V_146 = Vertex(name = 'V_146',
               particles = [ P.u__tilde__, P.u, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_113,(0,1):C.GC_275})

V_147 = Vertex(name = 'V_147',
               particles = [ P.c__tilde__, P.c, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_114,(0,1):C.GC_276})

V_148 = Vertex(name = 'V_148',
               particles = [ P.t__tilde__, P.t, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_115,(0,1):C.GC_277})

V_149 = Vertex(name = 'V_149',
               particles = [ P.e__plus__, P.ve, P.S112__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_118,(0,1):C.GC_288})

V_150 = Vertex(name = 'V_150',
               particles = [ P.ve__tilde__, P.e__minus__, P.S112 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_118,(0,1):C.GC_288})

V_151 = Vertex(name = 'V_151',
               particles = [ P.mu__plus__, P.vm, P.S112__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_119,(0,1):C.GC_289})

V_152 = Vertex(name = 'V_152',
               particles = [ P.vm__tilde__, P.mu__minus__, P.S112 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_119,(0,1):C.GC_289})

V_153 = Vertex(name = 'V_153',
               particles = [ P.ta__plus__, P.vt, P.S112__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_120,(0,1):C.GC_290})

V_154 = Vertex(name = 'V_154',
               particles = [ P.vt__tilde__, P.ta__minus__, P.S112 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_120,(0,1):C.GC_290})

V_155 = Vertex(name = 'V_155',
               particles = [ P.u__tilde__, P.d, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_121,(0,1):C.GC_291})

V_156 = Vertex(name = 'V_156',
               particles = [ P.d__tilde__, P.u, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_121,(0,1):C.GC_291})

V_157 = Vertex(name = 'V_157',
               particles = [ P.c__tilde__, P.s, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_122,(0,1):C.GC_292})

V_158 = Vertex(name = 'V_158',
               particles = [ P.s__tilde__, P.c, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_122,(0,1):C.GC_292})

V_159 = Vertex(name = 'V_159',
               particles = [ P.t__tilde__, P.b, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_123,(0,1):C.GC_293,(0,2):C.GC_303,(0,3):C.GC_302})

V_160 = Vertex(name = 'V_160',
               particles = [ P.b__tilde__, P.t, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_123,(0,1):C.GC_293,(0,2):C.GC_302,(0,3):C.GC_303})

V_161 = Vertex(name = 'V_161',
               particles = [ P.e__plus__, P.ve, P.S11__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_124,(0,1):C.GC_326})

V_162 = Vertex(name = 'V_162',
               particles = [ P.ve__tilde__, P.e__minus__, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_124,(0,1):C.GC_326})

V_163 = Vertex(name = 'V_163',
               particles = [ P.mu__plus__, P.vm, P.S11__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_125,(0,1):C.GC_327})

V_164 = Vertex(name = 'V_164',
               particles = [ P.vm__tilde__, P.mu__minus__, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_125,(0,1):C.GC_327})

V_165 = Vertex(name = 'V_165',
               particles = [ P.ta__plus__, P.vt, P.S11__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_126,(0,1):C.GC_328})

V_166 = Vertex(name = 'V_166',
               particles = [ P.vt__tilde__, P.ta__minus__, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_126,(0,1):C.GC_328})

V_167 = Vertex(name = 'V_167',
               particles = [ P.u__tilde__, P.d, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_127,(0,1):C.GC_329})

V_168 = Vertex(name = 'V_168',
               particles = [ P.d__tilde__, P.u, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_127,(0,1):C.GC_329})

V_169 = Vertex(name = 'V_169',
               particles = [ P.c__tilde__, P.s, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_128,(0,1):C.GC_330})

V_170 = Vertex(name = 'V_170',
               particles = [ P.s__tilde__, P.c, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_128,(0,1):C.GC_330})

V_171 = Vertex(name = 'V_171',
               particles = [ P.t__tilde__, P.b, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_129,(0,1):C.GC_331,(0,2):C.GC_341,(0,3):C.GC_340})

V_172 = Vertex(name = 'V_172',
               particles = [ P.b__tilde__, P.t, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_129,(0,1):C.GC_331,(0,2):C.GC_340,(0,3):C.GC_341})

V_173 = Vertex(name = 'V_173',
               particles = [ P.bp__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_397,(0,1):C.GC_394})

V_174 = Vertex(name = 'V_174',
               particles = [ P.bp__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_398,(0,1):C.GC_395})

V_175 = Vertex(name = 'V_175',
               particles = [ P.bp__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_399,(0,1):C.GC_396})

V_176 = Vertex(name = 'V_176',
               particles = [ P.tp__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_415,(0,1):C.GC_412})

V_177 = Vertex(name = 'V_177',
               particles = [ P.tp__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_416,(0,1):C.GC_413})

V_178 = Vertex(name = 'V_178',
               particles = [ P.tp__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_417,(0,1):C.GC_414})

V_179 = Vertex(name = 'V_179',
               particles = [ P.tp2__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_403,(0,1):C.GC_400})

V_180 = Vertex(name = 'V_180',
               particles = [ P.tp2__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_404,(0,1):C.GC_401})

V_181 = Vertex(name = 'V_181',
               particles = [ P.tp2__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_405,(0,1):C.GC_402})

V_182 = Vertex(name = 'V_182',
               particles = [ P.tp3__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_409,(0,1):C.GC_406})

V_183 = Vertex(name = 'V_183',
               particles = [ P.tp3__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_410,(0,1):C.GC_407})

V_184 = Vertex(name = 'V_184',
               particles = [ P.tp3__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_411,(0,1):C.GC_408})

V_185 = Vertex(name = 'V_185',
               particles = [ P.bp__tilde__, P.d, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_256,(0,1):C.GC_253})

V_186 = Vertex(name = 'V_186',
               particles = [ P.bp__tilde__, P.s, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_257,(0,1):C.GC_254})

V_187 = Vertex(name = 'V_187',
               particles = [ P.bp__tilde__, P.b, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_258,(0,1):C.GC_255})

V_188 = Vertex(name = 'V_188',
               particles = [ P.tp__tilde__, P.u, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_271,(0,1):C.GC_268})

V_189 = Vertex(name = 'V_189',
               particles = [ P.tp__tilde__, P.c, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_272,(0,1):C.GC_269})

V_190 = Vertex(name = 'V_190',
               particles = [ P.tp__tilde__, P.t, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_273,(0,1):C.GC_270})

V_191 = Vertex(name = 'V_191',
               particles = [ P.bp__tilde__, P.d, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_144,(0,1):C.GC_141})

V_192 = Vertex(name = 'V_192',
               particles = [ P.bp__tilde__, P.s, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_145,(0,1):C.GC_142})

V_193 = Vertex(name = 'V_193',
               particles = [ P.bp__tilde__, P.b, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_146,(0,1):C.GC_143})

V_194 = Vertex(name = 'V_194',
               particles = [ P.tp__tilde__, P.u, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_159,(0,1):C.GC_156})

V_195 = Vertex(name = 'V_195',
               particles = [ P.tp__tilde__, P.c, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_157})

V_196 = Vertex(name = 'V_196',
               particles = [ P.tp__tilde__, P.t, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_158})

V_197 = Vertex(name = 'V_197',
               particles = [ P.bp__tilde__, P.d, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_172,(0,1):C.GC_169})

V_198 = Vertex(name = 'V_198',
               particles = [ P.bp__tilde__, P.s, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_173,(0,1):C.GC_170})

V_199 = Vertex(name = 'V_199',
               particles = [ P.bp__tilde__, P.b, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_171})

V_200 = Vertex(name = 'V_200',
               particles = [ P.tp__tilde__, P.u, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_187,(0,1):C.GC_184})

V_201 = Vertex(name = 'V_201',
               particles = [ P.tp__tilde__, P.c, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_188,(0,1):C.GC_185})

V_202 = Vertex(name = 'V_202',
               particles = [ P.tp__tilde__, P.t, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_189,(0,1):C.GC_186})

V_203 = Vertex(name = 'V_203',
               particles = [ P.bp__tilde__, P.d, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_200,(0,1):C.GC_197})

V_204 = Vertex(name = 'V_204',
               particles = [ P.bp__tilde__, P.s, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_201,(0,1):C.GC_198})

V_205 = Vertex(name = 'V_205',
               particles = [ P.bp__tilde__, P.b, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_202,(0,1):C.GC_199})

V_206 = Vertex(name = 'V_206',
               particles = [ P.tp__tilde__, P.u, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_215,(0,1):C.GC_212})

V_207 = Vertex(name = 'V_207',
               particles = [ P.tp__tilde__, P.c, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_213})

V_208 = Vertex(name = 'V_208',
               particles = [ P.tp__tilde__, P.t, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_214})

V_209 = Vertex(name = 'V_209',
               particles = [ P.bp__tilde__, P.d, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_228,(0,1):C.GC_225})

V_210 = Vertex(name = 'V_210',
               particles = [ P.bp__tilde__, P.s, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_229,(0,1):C.GC_226})

V_211 = Vertex(name = 'V_211',
               particles = [ P.bp__tilde__, P.b, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_230,(0,1):C.GC_227})

V_212 = Vertex(name = 'V_212',
               particles = [ P.tp__tilde__, P.u, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_243,(0,1):C.GC_240})

V_213 = Vertex(name = 'V_213',
               particles = [ P.tp__tilde__, P.c, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_244,(0,1):C.GC_241})

V_214 = Vertex(name = 'V_214',
               particles = [ P.tp__tilde__, P.t, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_245,(0,1):C.GC_242})

V_215 = Vertex(name = 'V_215',
               particles = [ P.bp__tilde__, P.y, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_325,(0,1):C.GC_324})

V_216 = Vertex(name = 'V_216',
               particles = [ P.tp__tilde__, P.bp, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_333,(0,1):C.GC_332})

V_217 = Vertex(name = 'V_217',
               particles = [ P.x__tilde__, P.tp, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_343,(0,1):C.GC_342})

V_218 = Vertex(name = 'V_218',
               particles = [ P.bp__tilde__, P.u, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_321,(0,1):C.GC_318})

V_219 = Vertex(name = 'V_219',
               particles = [ P.bp__tilde__, P.c, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_322,(0,1):C.GC_319})

V_220 = Vertex(name = 'V_220',
               particles = [ P.bp__tilde__, P.t, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_320})

V_221 = Vertex(name = 'V_221',
               particles = [ P.tp__tilde__, P.d, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_337,(0,1):C.GC_334})

V_222 = Vertex(name = 'V_222',
               particles = [ P.tp__tilde__, P.s, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_338,(0,1):C.GC_335})

V_223 = Vertex(name = 'V_223',
               particles = [ P.tp__tilde__, P.b, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_339,(0,1):C.GC_336})

V_224 = Vertex(name = 'V_224',
               particles = [ P.x__tilde__, P.u, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_347,(0,1):C.GC_344})

V_225 = Vertex(name = 'V_225',
               particles = [ P.x__tilde__, P.c, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_348,(0,1):C.GC_345})

V_226 = Vertex(name = 'V_226',
               particles = [ P.x__tilde__, P.t, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_349,(0,1):C.GC_13})

V_227 = Vertex(name = 'V_227',
               particles = [ P.x__tilde__, P.t, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_346})

V_228 = Vertex(name = 'V_228',
               particles = [ P.y__tilde__, P.d, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_353,(0,1):C.GC_350})

V_229 = Vertex(name = 'V_229',
               particles = [ P.y__tilde__, P.s, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_354,(0,1):C.GC_351})

V_230 = Vertex(name = 'V_230',
               particles = [ P.y__tilde__, P.b, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_355,(0,1):C.GC_352})

V_231 = Vertex(name = 'V_231',
               particles = [ P.bp__tilde__, P.y, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_286})

V_232 = Vertex(name = 'V_232',
               particles = [ P.tp__tilde__, P.bp, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_295,(0,1):C.GC_294})

V_233 = Vertex(name = 'V_233',
               particles = [ P.x__tilde__, P.tp, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_305,(0,1):C.GC_304})

V_234 = Vertex(name = 'V_234',
               particles = [ P.bp__tilde__, P.u, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_283,(0,1):C.GC_280})

V_235 = Vertex(name = 'V_235',
               particles = [ P.bp__tilde__, P.c, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_284,(0,1):C.GC_281})

V_236 = Vertex(name = 'V_236',
               particles = [ P.bp__tilde__, P.t, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_285,(0,1):C.GC_282})

V_237 = Vertex(name = 'V_237',
               particles = [ P.tp__tilde__, P.d, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_299,(0,1):C.GC_296})

V_238 = Vertex(name = 'V_238',
               particles = [ P.tp__tilde__, P.s, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_300,(0,1):C.GC_297})

V_239 = Vertex(name = 'V_239',
               particles = [ P.tp__tilde__, P.b, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_301,(0,1):C.GC_298})

V_240 = Vertex(name = 'V_240',
               particles = [ P.x__tilde__, P.u, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_309,(0,1):C.GC_306})

V_241 = Vertex(name = 'V_241',
               particles = [ P.x__tilde__, P.c, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_310,(0,1):C.GC_307})

V_242 = Vertex(name = 'V_242',
               particles = [ P.x__tilde__, P.t, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_311,(0,1):C.GC_12})

V_243 = Vertex(name = 'V_243',
               particles = [ P.x__tilde__, P.t, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_308})

V_244 = Vertex(name = 'V_244',
               particles = [ P.y__tilde__, P.d, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_315,(0,1):C.GC_312})

V_245 = Vertex(name = 'V_245',
               particles = [ P.y__tilde__, P.s, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_316,(0,1):C.GC_313})

V_246 = Vertex(name = 'V_246',
               particles = [ P.y__tilde__, P.b, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_317,(0,1):C.GC_314})

V_247 = Vertex(name = 'V_247',
               particles = [ P.x__tilde__, P.bp, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_357,(0,1):C.GC_356})

V_248 = Vertex(name = 'V_248',
               particles = [ P.y__tilde__, P.tp, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_365,(0,1):C.GC_364})

V_249 = Vertex(name = 'V_249',
               particles = [ P.x__tilde__, P.d, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_361,(0,1):C.GC_358})

V_250 = Vertex(name = 'V_250',
               particles = [ P.x__tilde__, P.s, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_362,(0,1):C.GC_359})

V_251 = Vertex(name = 'V_251',
               particles = [ P.x__tilde__, P.b, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_363,(0,1):C.GC_10})

V_252 = Vertex(name = 'V_252',
               particles = [ P.x__tilde__, P.b, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_360})

V_253 = Vertex(name = 'V_253',
               particles = [ P.y__tilde__, P.u, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_369,(0,1):C.GC_366})

V_254 = Vertex(name = 'V_254',
               particles = [ P.y__tilde__, P.c, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_370,(0,1):C.GC_367})

V_255 = Vertex(name = 'V_255',
               particles = [ P.y__tilde__, P.t, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_371,(0,1):C.GC_368})

V_256 = Vertex(name = 'V_256',
               particles = [ P.y__tilde__, P.bp, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_324,(0,1):C.GC_325})

V_257 = Vertex(name = 'V_257',
               particles = [ P.y__tilde__, P.bp, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_287})

V_258 = Vertex(name = 'V_258',
               particles = [ P.bp__tilde__, P.tp, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_332,(0,1):C.GC_333})

V_259 = Vertex(name = 'V_259',
               particles = [ P.bp__tilde__, P.tp, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_294,(0,1):C.GC_295})

V_260 = Vertex(name = 'V_260',
               particles = [ P.b__tilde__, P.x, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_10,(0,1):C.GC_363})

V_261 = Vertex(name = 'V_261',
               particles = [ P.b__tilde__, P.x, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_360})

V_262 = Vertex(name = 'V_262',
               particles = [ P.t__tilde__, P.x, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_11,(0,1):C.GC_349})

V_263 = Vertex(name = 'V_263',
               particles = [ P.t__tilde__, P.x, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_346})

V_264 = Vertex(name = 'V_264',
               particles = [ P.t__tilde__, P.x, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_12,(0,1):C.GC_311})

V_265 = Vertex(name = 'V_265',
               particles = [ P.t__tilde__, P.x, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_308})

V_266 = Vertex(name = 'V_266',
               particles = [ P.tp__tilde__, P.x, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_342,(0,1):C.GC_343})

V_267 = Vertex(name = 'V_267',
               particles = [ P.tp__tilde__, P.x, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_304,(0,1):C.GC_305})

V_268 = Vertex(name = 'V_268',
               particles = [ P.bp__tilde__, P.x, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_356,(0,1):C.GC_357})

V_269 = Vertex(name = 'V_269',
               particles = [ P.tp__tilde__, P.y, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_364,(0,1):C.GC_365})

V_270 = Vertex(name = 'V_270',
               particles = [ P.d__tilde__, P.bp, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_141,(0,1):C.GC_144})

V_271 = Vertex(name = 'V_271',
               particles = [ P.s__tilde__, P.bp, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_142,(0,1):C.GC_145})

V_272 = Vertex(name = 'V_272',
               particles = [ P.b__tilde__, P.bp, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_143,(0,1):C.GC_146})

V_273 = Vertex(name = 'V_273',
               particles = [ P.u__tilde__, P.tp, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_156,(0,1):C.GC_159})

V_274 = Vertex(name = 'V_274',
               particles = [ P.c__tilde__, P.tp, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_157,(0,1):C.GC_160})

V_275 = Vertex(name = 'V_275',
               particles = [ P.t__tilde__, P.tp, P.S102 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_158,(0,1):C.GC_161})

V_276 = Vertex(name = 'V_276',
               particles = [ P.d__tilde__, P.bp, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_169,(0,1):C.GC_172})

V_277 = Vertex(name = 'V_277',
               particles = [ P.s__tilde__, P.bp, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_170,(0,1):C.GC_173})

V_278 = Vertex(name = 'V_278',
               particles = [ P.b__tilde__, P.bp, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_174})

V_279 = Vertex(name = 'V_279',
               particles = [ P.u__tilde__, P.tp, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_184,(0,1):C.GC_187})

V_280 = Vertex(name = 'V_280',
               particles = [ P.c__tilde__, P.tp, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_185,(0,1):C.GC_188})

V_281 = Vertex(name = 'V_281',
               particles = [ P.t__tilde__, P.tp, P.S103 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_186,(0,1):C.GC_189})

V_282 = Vertex(name = 'V_282',
               particles = [ P.d__tilde__, P.bp, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_197,(0,1):C.GC_200})

V_283 = Vertex(name = 'V_283',
               particles = [ P.s__tilde__, P.bp, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_198,(0,1):C.GC_201})

V_284 = Vertex(name = 'V_284',
               particles = [ P.b__tilde__, P.bp, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_199,(0,1):C.GC_202})

V_285 = Vertex(name = 'V_285',
               particles = [ P.u__tilde__, P.tp, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_212,(0,1):C.GC_215})

V_286 = Vertex(name = 'V_286',
               particles = [ P.c__tilde__, P.tp, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_216})

V_287 = Vertex(name = 'V_287',
               particles = [ P.t__tilde__, P.tp, P.S104 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_217})

V_288 = Vertex(name = 'V_288',
               particles = [ P.d__tilde__, P.bp, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_225,(0,1):C.GC_228})

V_289 = Vertex(name = 'V_289',
               particles = [ P.s__tilde__, P.bp, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_226,(0,1):C.GC_229})

V_290 = Vertex(name = 'V_290',
               particles = [ P.b__tilde__, P.bp, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_227,(0,1):C.GC_230})

V_291 = Vertex(name = 'V_291',
               particles = [ P.u__tilde__, P.tp, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_243})

V_292 = Vertex(name = 'V_292',
               particles = [ P.c__tilde__, P.tp, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_241,(0,1):C.GC_244})

V_293 = Vertex(name = 'V_293',
               particles = [ P.t__tilde__, P.tp, P.S105 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_242,(0,1):C.GC_245})

V_294 = Vertex(name = 'V_294',
               particles = [ P.d__tilde__, P.bp, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_253,(0,1):C.GC_256})

V_295 = Vertex(name = 'V_295',
               particles = [ P.s__tilde__, P.bp, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_254,(0,1):C.GC_257})

V_296 = Vertex(name = 'V_296',
               particles = [ P.b__tilde__, P.bp, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_255,(0,1):C.GC_258})

V_297 = Vertex(name = 'V_297',
               particles = [ P.u__tilde__, P.tp, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_271})

V_298 = Vertex(name = 'V_298',
               particles = [ P.c__tilde__, P.tp, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_269,(0,1):C.GC_272})

V_299 = Vertex(name = 'V_299',
               particles = [ P.t__tilde__, P.tp, P.S10 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_270,(0,1):C.GC_273})

V_300 = Vertex(name = 'V_300',
               particles = [ P.u__tilde__, P.bp, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_280,(0,1):C.GC_283})

V_301 = Vertex(name = 'V_301',
               particles = [ P.c__tilde__, P.bp, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_281,(0,1):C.GC_284})

V_302 = Vertex(name = 'V_302',
               particles = [ P.t__tilde__, P.bp, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_282,(0,1):C.GC_285})

V_303 = Vertex(name = 'V_303',
               particles = [ P.d__tilde__, P.tp, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_296,(0,1):C.GC_299})

V_304 = Vertex(name = 'V_304',
               particles = [ P.s__tilde__, P.tp, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_297,(0,1):C.GC_300})

V_305 = Vertex(name = 'V_305',
               particles = [ P.b__tilde__, P.tp, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_298,(0,1):C.GC_301})

V_306 = Vertex(name = 'V_306',
               particles = [ P.u__tilde__, P.x, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_306,(0,1):C.GC_309})

V_307 = Vertex(name = 'V_307',
               particles = [ P.c__tilde__, P.x, P.S112__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_307,(0,1):C.GC_310})

V_308 = Vertex(name = 'V_308',
               particles = [ P.d__tilde__, P.y, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_312,(0,1):C.GC_315})

V_309 = Vertex(name = 'V_309',
               particles = [ P.s__tilde__, P.y, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_313,(0,1):C.GC_316})

V_310 = Vertex(name = 'V_310',
               particles = [ P.b__tilde__, P.y, P.S112 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_314,(0,1):C.GC_317})

V_311 = Vertex(name = 'V_311',
               particles = [ P.u__tilde__, P.bp, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_318,(0,1):C.GC_321})

V_312 = Vertex(name = 'V_312',
               particles = [ P.c__tilde__, P.bp, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_319,(0,1):C.GC_322})

V_313 = Vertex(name = 'V_313',
               particles = [ P.t__tilde__, P.bp, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_320,(0,1):C.GC_323})

V_314 = Vertex(name = 'V_314',
               particles = [ P.d__tilde__, P.tp, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_334,(0,1):C.GC_337})

V_315 = Vertex(name = 'V_315',
               particles = [ P.s__tilde__, P.tp, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_335,(0,1):C.GC_338})

V_316 = Vertex(name = 'V_316',
               particles = [ P.b__tilde__, P.tp, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_336,(0,1):C.GC_339})

V_317 = Vertex(name = 'V_317',
               particles = [ P.u__tilde__, P.x, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_344,(0,1):C.GC_347})

V_318 = Vertex(name = 'V_318',
               particles = [ P.c__tilde__, P.x, P.S11__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_345,(0,1):C.GC_348})

V_319 = Vertex(name = 'V_319',
               particles = [ P.d__tilde__, P.y, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_350,(0,1):C.GC_353})

V_320 = Vertex(name = 'V_320',
               particles = [ P.s__tilde__, P.y, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_351,(0,1):C.GC_354})

V_321 = Vertex(name = 'V_321',
               particles = [ P.b__tilde__, P.y, P.S11 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_352,(0,1):C.GC_355})

V_322 = Vertex(name = 'V_322',
               particles = [ P.d__tilde__, P.x, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_358,(0,1):C.GC_361})

V_323 = Vertex(name = 'V_323',
               particles = [ P.s__tilde__, P.x, P.S12__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_359,(0,1):C.GC_362})

V_324 = Vertex(name = 'V_324',
               particles = [ P.u__tilde__, P.y, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_366,(0,1):C.GC_369})

V_325 = Vertex(name = 'V_325',
               particles = [ P.c__tilde__, P.y, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_367,(0,1):C.GC_370})

V_326 = Vertex(name = 'V_326',
               particles = [ P.t__tilde__, P.y, P.S12 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_368,(0,1):C.GC_371})

V_327 = Vertex(name = 'V_327',
               particles = [ P.d__tilde__, P.bp, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_394,(0,1):C.GC_397})

V_328 = Vertex(name = 'V_328',
               particles = [ P.s__tilde__, P.bp, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_395,(0,1):C.GC_398})

V_329 = Vertex(name = 'V_329',
               particles = [ P.b__tilde__, P.bp, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_396,(0,1):C.GC_399})

V_330 = Vertex(name = 'V_330',
               particles = [ P.u__tilde__, P.tp2, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_400,(0,1):C.GC_403})

V_331 = Vertex(name = 'V_331',
               particles = [ P.c__tilde__, P.tp2, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_401,(0,1):C.GC_404})

V_332 = Vertex(name = 'V_332',
               particles = [ P.t__tilde__, P.tp2, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_402,(0,1):C.GC_405})

V_333 = Vertex(name = 'V_333',
               particles = [ P.u__tilde__, P.tp3, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_406,(0,1):C.GC_409})

V_334 = Vertex(name = 'V_334',
               particles = [ P.c__tilde__, P.tp3, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_407,(0,1):C.GC_410})

V_335 = Vertex(name = 'V_335',
               particles = [ P.t__tilde__, P.tp3, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_408,(0,1):C.GC_411})

V_336 = Vertex(name = 'V_336',
               particles = [ P.u__tilde__, P.tp, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_412,(0,1):C.GC_415})

V_337 = Vertex(name = 'V_337',
               particles = [ P.c__tilde__, P.tp, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_413,(0,1):C.GC_416})

V_338 = Vertex(name = 'V_338',
               particles = [ P.t__tilde__, P.tp, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_414,(0,1):C.GC_417})

V_339 = Vertex(name = 'V_339',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_605,(0,1):C.GC_599})

V_340 = Vertex(name = 'V_340',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_608,(0,1):C.GC_606})

V_341 = Vertex(name = 'V_341',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_607,(0,1):C.GC_607})

V_342 = Vertex(name = 'V_342',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_600,(0,1):C.GC_604})

V_343 = Vertex(name = 'V_343',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_601,(0,1):C.GC_603})

V_344 = Vertex(name = 'V_344',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_602,(0,1):C.GC_602})

V_345 = Vertex(name = 'V_345',
               particles = [ P.vt__tilde__, P.ta__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_610})

V_346 = Vertex(name = 'V_346',
               particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_611,(0,1):C.GC_613})

V_347 = Vertex(name = 'V_347',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_612,(0,1):C.GC_612})

V_348 = Vertex(name = 'V_348',
               particles = [ P.a, P.S323__tilde__, P.S323 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_16})

V_349 = Vertex(name = 'V_349',
               particles = [ P.Q10M, P.t, P.S323__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_7})

V_350 = Vertex(name = 'V_350',
               particles = [ P.ta__plus__, P.b, P.S323__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_8})

V_351 = Vertex(name = 'V_351',
               particles = [ P.vt__tilde__, P.t, P.S323__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_9})

V_352 = Vertex(name = 'V_352',
               particles = [ P.b__tilde__, P.ta__minus__, P.S323 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_8})

V_353 = Vertex(name = 'V_353',
               particles = [ P.t__tilde__, P.vt, P.S323 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_9})

V_354 = Vertex(name = 'V_354',
               particles = [ P.t__tilde__, P.Q10M, P.S323 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_7})

V_355 = Vertex(name = 'V_355',
               particles = [ P.H, P.S323__tilde__, P.S323 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_588})

V_356 = Vertex(name = 'V_356',
               particles = [ P.a, P.a, P.S323__tilde__, P.S323 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_23})

V_357 = Vertex(name = 'V_357',
               particles = [ P.Q80__tilde__, P.Q10, P.S80 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_4})

V_358 = Vertex(name = 'V_358',
               particles = [ P.Q80M, P.Q10M, P.S80 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2})

V_359 = Vertex(name = 'V_359',
               particles = [ P.Q81__tilde__, P.Q11, P.S80 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_6})

V_360 = Vertex(name = 'V_360',
               particles = [ P.Q10__tilde__, P.Q80, P.S80 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_4})

V_361 = Vertex(name = 'V_361',
               particles = [ P.Q11__tilde__, P.Q81, P.S80 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_6})

V_362 = Vertex(name = 'V_362',
               particles = [ P.H, P.S80, P.S80 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_589})

V_363 = Vertex(name = 'V_363',
               particles = [ P.g, P.S80, P.S80 ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_31})

V_364 = Vertex(name = 'V_364',
               particles = [ P.g, P.g, P.S80, P.S80 ],
               color = [ 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_37,(0,0):C.GC_37})

V_365 = Vertex(name = 'V_365',
               particles = [ P.t__tilde__, P.Q80__tilde__, P.S323 ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_3})

V_366 = Vertex(name = 'V_366',
               particles = [ P.Q81__tilde__, P.b__tilde__, P.S323 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5})

V_367 = Vertex(name = 'V_367',
               particles = [ P.t__tilde__, P.Q80M, P.S323 ],
               color = [ 'T(2,3,1)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1})

V_368 = Vertex(name = 'V_368',
               particles = [ P.bp__tilde__, P.bp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_130,(0,1):C.GC_372})

V_369 = Vertex(name = 'V_369',
               particles = [ P.tp__tilde__, P.tp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_134,(0,1):C.GC_382})

V_370 = Vertex(name = 'V_370',
               particles = [ P.x__tilde__, P.x, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_392})

V_371 = Vertex(name = 'V_371',
               particles = [ P.y__tilde__, P.y, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_139,(0,1):C.GC_393})

V_372 = Vertex(name = 'V_372',
               particles = [ P.d__tilde__, P.d, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_131,(0,1):C.GC_379})

V_373 = Vertex(name = 'V_373',
               particles = [ P.s__tilde__, P.s, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_132,(0,1):C.GC_380})

V_374 = Vertex(name = 'V_374',
               particles = [ P.b__tilde__, P.b, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_133,(0,1):C.GC_381})

V_375 = Vertex(name = 'V_375',
               particles = [ P.u__tilde__, P.u, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_135,(0,1):C.GC_389})

V_376 = Vertex(name = 'V_376',
               particles = [ P.c__tilde__, P.c, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_390})

V_377 = Vertex(name = 'V_377',
               particles = [ P.t__tilde__, P.t, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_391})

V_378 = Vertex(name = 'V_378',
               particles = [ P.d__tilde__, P.bp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_373,(0,1):C.GC_376})

V_379 = Vertex(name = 'V_379',
               particles = [ P.s__tilde__, P.bp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_374,(0,1):C.GC_377})

V_380 = Vertex(name = 'V_380',
               particles = [ P.b__tilde__, P.bp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_375,(0,1):C.GC_378})

V_381 = Vertex(name = 'V_381',
               particles = [ P.u__tilde__, P.tp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_383,(0,1):C.GC_386})

V_382 = Vertex(name = 'V_382',
               particles = [ P.c__tilde__, P.tp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_384,(0,1):C.GC_387})

V_383 = Vertex(name = 'V_383',
               particles = [ P.t__tilde__, P.tp, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_385,(0,1):C.GC_388})

V_384 = Vertex(name = 'V_384',
               particles = [ P.Q80M, P.t, P.S323__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_1})

V_385 = Vertex(name = 'V_385',
               particles = [ P.t, P.Q80, P.S323__tilde__ ],
               color = [ 'T(2,1,3)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_3})

V_386 = Vertex(name = 'V_386',
               particles = [ P.Q81, P.b, P.S323__tilde__ ],
               color = [ 'T(1,2,3)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_5})

V_387 = Vertex(name = 'V_387',
               particles = [ P.bp__tilde__, P.d, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_376,(0,1):C.GC_373})

V_388 = Vertex(name = 'V_388',
               particles = [ P.bp__tilde__, P.s, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_377,(0,1):C.GC_374})

V_389 = Vertex(name = 'V_389',
               particles = [ P.bp__tilde__, P.b, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_378,(0,1):C.GC_375})

V_390 = Vertex(name = 'V_390',
               particles = [ P.tp__tilde__, P.u, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_386,(0,1):C.GC_383})

V_391 = Vertex(name = 'V_391',
               particles = [ P.tp__tilde__, P.c, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_387,(0,1):C.GC_384})

V_392 = Vertex(name = 'V_392',
               particles = [ P.tp__tilde__, P.t, P.S80 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_388,(0,1):C.GC_385})

V_393 = Vertex(name = 'V_393',
               particles = [ P.tp__tilde__, P.tp, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_394 = Vertex(name = 'V_394',
               particles = [ P.bp__tilde__, P.bp, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_395 = Vertex(name = 'V_395',
               particles = [ P.x__tilde__, P.x, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_396 = Vertex(name = 'V_396',
               particles = [ P.y__tilde__, P.y, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_397 = Vertex(name = 'V_397',
               particles = [ P.tp2__tilde__, P.tp2, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_398 = Vertex(name = 'V_398',
               particles = [ P.tp3__tilde__, P.tp3, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_399 = Vertex(name = 'V_399',
               particles = [ P.g, P.S323__tilde__, P.S323 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_32,(0,1):C.GC_33})

V_400 = Vertex(name = 'V_400',
               particles = [ P.a, P.g, P.S323__tilde__, P.S323 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_35})

V_401 = Vertex(name = 'V_401',
               particles = [ P.g, P.g, P.S323__tilde__, P.S323 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_37,(0,0):C.GC_37})

V_402 = Vertex(name = 'V_402',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_447})

V_403 = Vertex(name = 'V_403',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_446})

V_404 = Vertex(name = 'V_404',
               particles = [ P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_593})

V_405 = Vertex(name = 'V_405',
               particles = [ P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_439,(0,1):C.GC_438})

V_406 = Vertex(name = 'V_406',
               particles = [ P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_437,(0,1):C.GC_440})

V_407 = Vertex(name = 'V_407',
               particles = [ P.W__minus__, P.S102, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_455,(0,1):C.GC_456})

V_408 = Vertex(name = 'V_408',
               particles = [ P.W__minus__, P.S103, P.S112 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_451,(0,1):C.GC_454})

V_409 = Vertex(name = 'V_409',
               particles = [ P.W__minus__, P.S103, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_452,(0,1):C.GC_453})

V_410 = Vertex(name = 'V_410',
               particles = [ P.W__minus__, P.S104, P.S112 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_464,(0,1):C.GC_463})

V_411 = Vertex(name = 'V_411',
               particles = [ P.W__minus__, P.S104, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_462,(0,1):C.GC_461})

V_412 = Vertex(name = 'V_412',
               particles = [ P.W__minus__, P.S11__tilde__, P.S12 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_457,(0,1):C.GC_460})

V_413 = Vertex(name = 'V_413',
               particles = [ P.W__minus__, P.S112__tilde__, P.S12 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_458,(0,1):C.GC_459})

V_414 = Vertex(name = 'V_414',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6 ],
               couplings = {(0,0):C.GC_18,(0,1):C.GC_17,(0,2):C.GC_17,(0,3):C.GC_18,(0,4):C.GC_18,(0,5):C.GC_17})

V_415 = Vertex(name = 'V_415',
               particles = [ P.Q10__tilde__, P.Q11, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_442})

V_416 = Vertex(name = 'V_416',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_447})

V_417 = Vertex(name = 'V_417',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_448})

V_418 = Vertex(name = 'V_418',
               particles = [ P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_594})

V_419 = Vertex(name = 'V_419',
               particles = [ P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_438,(0,1):C.GC_439})

V_420 = Vertex(name = 'V_420',
               particles = [ P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_437,(0,1):C.GC_440})

V_421 = Vertex(name = 'V_421',
               particles = [ P.W__plus__, P.S102, P.S11__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_455,(0,1):C.GC_456})

V_422 = Vertex(name = 'V_422',
               particles = [ P.W__plus__, P.S103, P.S11__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_453,(0,1):C.GC_452})

V_423 = Vertex(name = 'V_423',
               particles = [ P.W__plus__, P.S103, P.S112__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_451,(0,1):C.GC_454})

V_424 = Vertex(name = 'V_424',
               particles = [ P.W__plus__, P.S104, P.S11__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_462,(0,1):C.GC_461})

V_425 = Vertex(name = 'V_425',
               particles = [ P.W__plus__, P.S104, P.S112__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_463,(0,1):C.GC_464})

V_426 = Vertex(name = 'V_426',
               particles = [ P.W__plus__, P.S112, P.S12__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_459,(0,1):C.GC_458})

V_427 = Vertex(name = 'V_427',
               particles = [ P.W__plus__, P.S11, P.S12__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_457,(0,1):C.GC_460})

V_428 = Vertex(name = 'V_428',
               particles = [ P.Q11__tilde__, P.Q10, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_442})

V_429 = Vertex(name = 'V_429',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_430})

V_430 = Vertex(name = 'V_430',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_430})

V_431 = Vertex(name = 'V_431',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_430})

V_432 = Vertex(name = 'V_432',
               particles = [ P.W__minus__, P.W__plus__, P.S12__tilde__, P.S12 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_435})

V_433 = Vertex(name = 'V_433',
               particles = [ P.W__minus__, P.W__plus__, P.S12__tilde__, P.S12 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_595})

V_434 = Vertex(name = 'V_434',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_592})

V_435 = Vertex(name = 'V_435',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
               couplings = {(0,0):C.GC_24,(0,1):C.GC_24,(0,2):C.GC_25})

V_436 = Vertex(name = 'V_436',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6 ],
               couplings = {(0,0):C.GC_445,(0,1):C.GC_444,(0,2):C.GC_444,(0,3):C.GC_445,(0,4):C.GC_445,(0,5):C.GC_444})

V_437 = Vertex(name = 'V_437',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
               couplings = {(0,0):C.GC_431,(0,1):C.GC_431,(0,2):C.GC_432})

V_438 = Vertex(name = 'V_438',
               particles = [ P.ta__plus__, P.vt, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_609})

V_439 = Vertex(name = 'V_439',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_549})

V_440 = Vertex(name = 'V_440',
               particles = [ P.a, P.Z, P.S12__tilde__, P.S12 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_554})

V_441 = Vertex(name = 'V_441',
               particles = [ P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_542,(0,1):C.GC_548})

V_442 = Vertex(name = 'V_442',
               particles = [ P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_546,(0,1):C.GC_545})

V_443 = Vertex(name = 'V_443',
               particles = [ P.Z, P.S102, P.S103 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_468,(0,1):C.GC_467})

V_444 = Vertex(name = 'V_444',
               particles = [ P.Z, P.S103, P.S104 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_469,(0,1):C.GC_470})

V_445 = Vertex(name = 'V_445',
               particles = [ P.Z, P.S11__tilde__, P.S112 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_466,(0,1):C.GC_465})

V_446 = Vertex(name = 'V_446',
               particles = [ P.Z, P.S11__tilde__, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_551,(0,1):C.GC_550})

V_447 = Vertex(name = 'V_447',
               particles = [ P.Z, P.S112__tilde__, P.S112 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_551,(0,1):C.GC_550})

V_448 = Vertex(name = 'V_448',
               particles = [ P.Z, P.S112__tilde__, P.S11 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_465,(0,1):C.GC_466})

V_449 = Vertex(name = 'V_449',
               particles = [ P.Z, P.S12__tilde__, P.S12 ],
               color = [ '1' ],
               lorentz = [ L.VSS1, L.VSS2 ],
               couplings = {(0,0):C.GC_553,(0,1):C.GC_552})

V_450 = Vertex(name = 'V_450',
               particles = [ P.Q10__tilde__, P.Q10M, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_443})

V_451 = Vertex(name = 'V_451',
               particles = [ P.Q10__tilde__, P.Q10, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_472,(0,0):C.GC_486})

V_452 = Vertex(name = 'V_452',
               particles = [ P.Q10M, P.Q10, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_443})

V_453 = Vertex(name = 'V_453',
               particles = [ P.Q11__tilde__, P.Q11, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_473,(0,0):C.GC_487})

V_454 = Vertex(name = 'V_454',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_29})

V_455 = Vertex(name = 'V_455',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_456 = Vertex(name = 'V_456',
               particles = [ P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_574})

V_457 = Vertex(name = 'V_457',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_29})

V_458 = Vertex(name = 'V_458',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_28})

V_459 = Vertex(name = 'V_459',
               particles = [ P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_573})

V_460 = Vertex(name = 'V_460',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
               couplings = {(0,0):C.GC_450,(0,1):C.GC_449,(0,2):C.GC_449})

V_461 = Vertex(name = 'V_461',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_559})

V_462 = Vertex(name = 'V_462',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_558})

V_463 = Vertex(name = 'V_463',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_559})

V_464 = Vertex(name = 'V_464',
               particles = [ P.Z, P.Z, P.S12__tilde__, P.S12 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_560})

V_465 = Vertex(name = 'V_465',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_598})

V_466 = Vertex(name = 'V_466',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
               couplings = {(0,0):C.GC_433,(0,1):C.GC_433,(0,2):C.GC_434})

V_467 = Vertex(name = 'V_467',
               particles = [ P.tp__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_512,(0,1):C.GC_518})

V_468 = Vertex(name = 'V_468',
               particles = [ P.tp__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_513,(0,1):C.GC_519})

V_469 = Vertex(name = 'V_469',
               particles = [ P.tp__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_514,(0,1):C.GC_520})

V_470 = Vertex(name = 'V_470',
               particles = [ P.x__tilde__, P.u, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_524,(0,1):C.GC_527})

V_471 = Vertex(name = 'V_471',
               particles = [ P.x__tilde__, P.c, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_525,(0,1):C.GC_528})

V_472 = Vertex(name = 'V_472',
               particles = [ P.x__tilde__, P.t, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_526,(0,1):C.GC_529})

V_473 = Vertex(name = 'V_473',
               particles = [ P.bp__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_474,(0,1):C.GC_480})

V_474 = Vertex(name = 'V_474',
               particles = [ P.bp__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_475,(0,1):C.GC_481})

V_475 = Vertex(name = 'V_475',
               particles = [ P.bp__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_476,(0,1):C.GC_482})

V_476 = Vertex(name = 'V_476',
               particles = [ P.y__tilde__, P.d, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_530,(0,1):C.GC_533})

V_477 = Vertex(name = 'V_477',
               particles = [ P.y__tilde__, P.s, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_531,(0,1):C.GC_534})

V_478 = Vertex(name = 'V_478',
               particles = [ P.y__tilde__, P.b, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_532,(0,1):C.GC_535})

V_479 = Vertex(name = 'V_479',
               particles = [ P.bp__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_477,(0,1):C.GC_483})

V_480 = Vertex(name = 'V_480',
               particles = [ P.bp__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_478,(0,1):C.GC_484})

V_481 = Vertex(name = 'V_481',
               particles = [ P.bp__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_479,(0,1):C.GC_485})

V_482 = Vertex(name = 'V_482',
               particles = [ P.tp__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_515,(0,1):C.GC_521})

V_483 = Vertex(name = 'V_483',
               particles = [ P.tp__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_516,(0,1):C.GC_522})

V_484 = Vertex(name = 'V_484',
               particles = [ P.tp__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_517,(0,1):C.GC_523})

V_485 = Vertex(name = 'V_485',
               particles = [ P.tp2__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_488,(0,1):C.GC_494})

V_486 = Vertex(name = 'V_486',
               particles = [ P.tp2__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_489,(0,1):C.GC_495})

V_487 = Vertex(name = 'V_487',
               particles = [ P.tp2__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_490,(0,1):C.GC_496})

V_488 = Vertex(name = 'V_488',
               particles = [ P.tp2__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_491,(0,1):C.GC_497})

V_489 = Vertex(name = 'V_489',
               particles = [ P.tp2__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_492,(0,1):C.GC_498})

V_490 = Vertex(name = 'V_490',
               particles = [ P.tp2__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_493,(0,1):C.GC_499})

V_491 = Vertex(name = 'V_491',
               particles = [ P.tp3__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_500,(0,1):C.GC_506})

V_492 = Vertex(name = 'V_492',
               particles = [ P.tp3__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_501,(0,1):C.GC_507})

V_493 = Vertex(name = 'V_493',
               particles = [ P.tp3__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_502,(0,1):C.GC_508})

V_494 = Vertex(name = 'V_494',
               particles = [ P.tp3__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_503,(0,1):C.GC_509})

V_495 = Vertex(name = 'V_495',
               particles = [ P.tp3__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_504,(0,1):C.GC_510})

V_496 = Vertex(name = 'V_496',
               particles = [ P.tp3__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_505,(0,1):C.GC_511})

V_497 = Vertex(name = 'V_497',
               particles = [ P.d__tilde__, P.tp2, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_488,(0,1):C.GC_494})

V_498 = Vertex(name = 'V_498',
               particles = [ P.s__tilde__, P.tp2, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_489,(0,1):C.GC_495})

V_499 = Vertex(name = 'V_499',
               particles = [ P.b__tilde__, P.tp2, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_490,(0,1):C.GC_496})

V_500 = Vertex(name = 'V_500',
               particles = [ P.d__tilde__, P.tp3, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_500,(0,1):C.GC_506})

V_501 = Vertex(name = 'V_501',
               particles = [ P.s__tilde__, P.tp3, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_501,(0,1):C.GC_507})

V_502 = Vertex(name = 'V_502',
               particles = [ P.b__tilde__, P.tp3, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_502,(0,1):C.GC_508})

V_503 = Vertex(name = 'V_503',
               particles = [ P.d__tilde__, P.tp, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_512,(0,1):C.GC_518})

V_504 = Vertex(name = 'V_504',
               particles = [ P.s__tilde__, P.tp, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_513,(0,1):C.GC_519})

V_505 = Vertex(name = 'V_505',
               particles = [ P.b__tilde__, P.tp, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_514,(0,1):C.GC_520})

V_506 = Vertex(name = 'V_506',
               particles = [ P.u__tilde__, P.x, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_524,(0,1):C.GC_527})

V_507 = Vertex(name = 'V_507',
               particles = [ P.c__tilde__, P.x, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_525,(0,1):C.GC_528})

V_508 = Vertex(name = 'V_508',
               particles = [ P.t__tilde__, P.x, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_526,(0,1):C.GC_529})

V_509 = Vertex(name = 'V_509',
               particles = [ P.u__tilde__, P.bp, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_474,(0,1):C.GC_480})

V_510 = Vertex(name = 'V_510',
               particles = [ P.c__tilde__, P.bp, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_475,(0,1):C.GC_481})

V_511 = Vertex(name = 'V_511',
               particles = [ P.t__tilde__, P.bp, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_476,(0,1):C.GC_482})

V_512 = Vertex(name = 'V_512',
               particles = [ P.d__tilde__, P.y, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_530,(0,1):C.GC_533})

V_513 = Vertex(name = 'V_513',
               particles = [ P.s__tilde__, P.y, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_531,(0,1):C.GC_534})

V_514 = Vertex(name = 'V_514',
               particles = [ P.b__tilde__, P.y, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_532,(0,1):C.GC_535})

V_515 = Vertex(name = 'V_515',
               particles = [ P.d__tilde__, P.bp, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_477,(0,1):C.GC_483})

V_516 = Vertex(name = 'V_516',
               particles = [ P.s__tilde__, P.bp, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_478,(0,1):C.GC_484})

V_517 = Vertex(name = 'V_517',
               particles = [ P.b__tilde__, P.bp, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_479,(0,1):C.GC_485})

V_518 = Vertex(name = 'V_518',
               particles = [ P.u__tilde__, P.tp2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_491,(0,1):C.GC_497})

V_519 = Vertex(name = 'V_519',
               particles = [ P.c__tilde__, P.tp2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_492,(0,1):C.GC_498})

V_520 = Vertex(name = 'V_520',
               particles = [ P.t__tilde__, P.tp2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_493,(0,1):C.GC_499})

V_521 = Vertex(name = 'V_521',
               particles = [ P.u__tilde__, P.tp3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_503,(0,1):C.GC_509})

V_522 = Vertex(name = 'V_522',
               particles = [ P.c__tilde__, P.tp3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_504,(0,1):C.GC_510})

V_523 = Vertex(name = 'V_523',
               particles = [ P.t__tilde__, P.tp3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_505,(0,1):C.GC_511})

V_524 = Vertex(name = 'V_524',
               particles = [ P.u__tilde__, P.tp, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_515,(0,1):C.GC_521})

V_525 = Vertex(name = 'V_525',
               particles = [ P.c__tilde__, P.tp, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_516,(0,1):C.GC_522})

V_526 = Vertex(name = 'V_526',
               particles = [ P.t__tilde__, P.tp, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_517,(0,1):C.GC_523})

V_527 = Vertex(name = 'V_527',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_528 = Vertex(name = 'V_528',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_529 = Vertex(name = 'V_529',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_530 = Vertex(name = 'V_530',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_16})

V_531 = Vertex(name = 'V_531',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_16})

V_532 = Vertex(name = 'V_532',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_16})

V_533 = Vertex(name = 'V_533',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_534 = Vertex(name = 'V_534',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_535 = Vertex(name = 'V_535',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_536 = Vertex(name = 'V_536',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_537 = Vertex(name = 'V_537',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_538 = Vertex(name = 'V_538',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_539 = Vertex(name = 'V_539',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_540 = Vertex(name = 'V_540',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_541 = Vertex(name = 'V_541',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_33})

V_542 = Vertex(name = 'V_542',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_543 = Vertex(name = 'V_543',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_544 = Vertex(name = 'V_544',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_545 = Vertex(name = 'V_545',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_546 = Vertex(name = 'V_546',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_547 = Vertex(name = 'V_547',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_548 = Vertex(name = 'V_548',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_549 = Vertex(name = 'V_549',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_550 = Vertex(name = 'V_550',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_551 = Vertex(name = 'V_551',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_552 = Vertex(name = 'V_552',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_553 = Vertex(name = 'V_553',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_441})

V_554 = Vertex(name = 'V_554',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_544,(0,1):C.GC_540})

V_555 = Vertex(name = 'V_555',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_544,(0,1):C.GC_540})

V_556 = Vertex(name = 'V_556',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_544,(0,1):C.GC_540})

V_557 = Vertex(name = 'V_557',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_543,(0,1):C.GC_539})

V_558 = Vertex(name = 'V_558',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_543,(0,1):C.GC_539})

V_559 = Vertex(name = 'V_559',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_543,(0,1):C.GC_539})

V_560 = Vertex(name = 'V_560',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_547})

V_561 = Vertex(name = 'V_561',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_547})

V_562 = Vertex(name = 'V_562',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_547})

V_563 = Vertex(name = 'V_563',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_546,(0,1):C.GC_541})

V_564 = Vertex(name = 'V_564',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_546,(0,1):C.GC_541})

V_565 = Vertex(name = 'V_565',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_546,(0,1):C.GC_541})

V_566 = Vertex(name = 'V_566',
               particles = [ P.Q10M, P.Q10M, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_471})

