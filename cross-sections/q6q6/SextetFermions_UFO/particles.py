# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 12.3.0 for Microsoft Windows (64-bit) (May 10, 2021)
# Date: Thu 11 Dec 2025 10:52:06


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Q11 = Particle(pdg_code = 6000011,
               name = 'Q11',
               antiname = 'Q11~',
               spin = 2,
               color = 1,
               mass = Param.MQ11,
               width = Param.WQ11,
               texname = 'Q11',
               antitexname = 'Q11~',
               charge = 1,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

Q11__tilde__ = Q11.anti()

Q10 = Particle(pdg_code = 6000010,
               name = 'Q10',
               antiname = 'Q10~',
               spin = 2,
               color = 1,
               mass = Param.MQ10,
               width = Param.WQ10,
               texname = 'Q10',
               antitexname = 'Q10~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

Q10__tilde__ = Q10.anti()

Q10M = Particle(pdg_code = 6001010,
                name = 'Q10M',
                antiname = 'Q10M',
                spin = 2,
                color = 1,
                mass = Param.MQ10M,
                width = Param.WQ10M,
                texname = 'Q10M',
                antitexname = 'Q10M',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

Q653 = Particle(pdg_code = 6000653,
                name = 'Q653',
                antiname = 'Q653~',
                spin = 2,
                color = 6,
                mass = Param.MQ653,
                width = Param.WQ653,
                texname = 'Q653',
                antitexname = 'Q653~',
                charge = -5/3,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

Q653__tilde__ = Q653.anti()

Q623 = Particle(pdg_code = 6000623,
                name = 'Q623',
                antiname = 'Q623~',
                spin = 2,
                color = 6,
                mass = Param.MQ623,
                width = Param.WQ623,
                texname = 'Q623',
                antitexname = 'Q623~',
                charge = -2/3,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

Q623__tilde__ = Q623.anti()

Q613 = Particle(pdg_code = 6000613,
                name = 'Q613',
                antiname = 'Q613~',
                spin = 2,
                color = 6,
                mass = Param.MQ613,
                width = Param.WQ613,
                texname = 'Q613',
                antitexname = 'Q613~',
                charge = 1/3,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

Q613__tilde__ = Q613.anti()

Q81 = Particle(pdg_code = 6000081,
               name = 'Q81',
               antiname = 'Q81~',
               spin = 2,
               color = 8,
               mass = Param.MQ81,
               width = Param.WQ81,
               texname = 'Q81',
               antitexname = 'Q81~',
               charge = 1,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

Q81__tilde__ = Q81.anti()

Q80 = Particle(pdg_code = 6000080,
               name = 'Q80',
               antiname = 'Q80~',
               spin = 2,
               color = 8,
               mass = Param.MQ80,
               width = Param.WQ80,
               texname = 'Q80',
               antitexname = 'Q80~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

Q80__tilde__ = Q80.anti()

Q80M = Particle(pdg_code = 6001080,
                name = 'Q80M',
                antiname = 'Q80M',
                spin = 2,
                color = 8,
                mass = Param.MQ80M,
                width = Param.WQ80M,
                texname = 'Q80M',
                antitexname = 'Q80M',
                charge = 0,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

S10 = Particle(pdg_code = 6100001,
               name = 'S10',
               antiname = 'S10',
               spin = 1,
               color = 1,
               mass = Param.MS10,
               width = Param.WS10,
               texname = 'S10',
               antitexname = 'S10',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S80 = Particle(pdg_code = 6108000,
               name = 'S80',
               antiname = 'S80',
               spin = 1,
               color = 8,
               mass = Param.MS80,
               width = Param.WS80,
               texname = 'S80',
               antitexname = 'S80',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S11 = Particle(pdg_code = 6100002,
               name = 'S11',
               antiname = 'S11~',
               spin = 1,
               color = 1,
               mass = Param.MS11,
               width = Param.WS11,
               texname = 'S11',
               antitexname = 'S11~',
               charge = 1,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S11__tilde__ = S11.anti()

S12 = Particle(pdg_code = 6100003,
               name = 'S12',
               antiname = 'S12~',
               spin = 1,
               color = 1,
               mass = Param.MS12,
               width = Param.WS12,
               texname = 'S12',
               antitexname = 'S12~',
               charge = 2,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

S12__tilde__ = S12.anti()

S323 = Particle(pdg_code = 6100300,
                name = 'S323',
                antiname = 'S323~',
                spin = 1,
                color = 3,
                mass = Param.MS323,
                width = Param.WS323,
                texname = 'S323',
                antitexname = 'S323~',
                charge = 2/3,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

S323__tilde__ = S323.anti()

six1 = Particle(pdg_code = 9000005,
                name = 'six1',
                antiname = 'six1~',
                spin = 1,
                color = 6,
                mass = Param.MSIX1,
                width = Param.WSIX1,
                texname = 'six1',
                antitexname = 'six1~',
                charge = 1/3,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

six1__tilde__ = six1.anti()

S623 = Particle(pdg_code = 9000006,
                name = 'S623',
                antiname = 'S623~',
                spin = 1,
                color = 6,
                mass = Param.MS623,
                width = Param.WS623,
                texname = 'S623',
                antitexname = 'S623~',
                charge = -2/3,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

S623__tilde__ = S623.anti()

six3 = Particle(pdg_code = 9000007,
                name = 'six3',
                antiname = 'six3~',
                spin = 1,
                color = 6,
                mass = Param.MSIX3,
                width = Param.WSIX3,
                texname = 'six3',
                antitexname = 'six3~',
                charge = 4/3,
                GhostNumber = 0,
                LeptonNumber = 0,
                Y = 0)

six3__tilde__ = six3.anti()

x = Particle(pdg_code = 6000005,
             name = 'x',
             antiname = 'x~',
             spin = 2,
             color = 3,
             mass = Param.MX,
             width = Param.WX,
             texname = 'x',
             antitexname = 'x~',
             charge = 5/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

x__tilde__ = x.anti()

tp = Particle(pdg_code = 6000006,
              name = 'tp',
              antiname = 'tp~',
              spin = 2,
              color = 3,
              mass = Param.MTP,
              width = Param.WTP,
              texname = 'tp',
              antitexname = 'tp~',
              charge = 2/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

tp__tilde__ = tp.anti()

bp = Particle(pdg_code = 6000007,
              name = 'bp',
              antiname = 'bp~',
              spin = 2,
              color = 3,
              mass = Param.MBP,
              width = Param.WBP,
              texname = 'bp',
              antitexname = 'bp~',
              charge = -1/3,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

bp__tilde__ = bp.anti()

y = Particle(pdg_code = 6000008,
             name = 'y',
             antiname = 'y~',
             spin = 2,
             color = 3,
             mass = Param.MY,
             width = Param.WY,
             texname = 'y',
             antitexname = 'y~',
             charge = -4/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

y__tilde__ = y.anti()

