# This file was automatically created by FeynRules 2.4.16
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Fri 21 Aug 2015 09:21:20


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
                      mass = Param.ZERO,
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
                       mass = Param.ZERO,
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
             mass = Param.ZERO,
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
             mass = Param.ZERO,
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
             mass = Param.ZERO,
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
             mass = Param.ZERO,
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
             mass = Param.ZERO,
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

go = Particle(pdg_code = 1000021,
              name = 'go',
              antiname = 'go',
              spin = 2,
              color = 8,
              mass = Param.Mgo,
              width = Param.Wgo,
              texname = 'go',
              antitexname = 'go',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

chi = Particle(pdg_code = 1000022,
               name = 'chi',
               antiname = 'chi',
               spin = 2,
               color = 1,
               mass = Param.Mchi,
               width = Param.ZERO,
               texname = 'chi',
               antitexname = 'chi',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

suL = Particle(pdg_code = 1000002,
               name = 'suL',
               antiname = 'suL~',
               spin = 1,
               color = 3,
               mass = Param.MsuL,
               width = Param.WsuL,
               texname = 'suL',
               antitexname = 'suL~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

suL__tilde__ = suL.anti()

scL = Particle(pdg_code = 1000004,
               name = 'scL',
               antiname = 'scL~',
               spin = 1,
               color = 3,
               mass = Param.MscL,
               width = Param.WscL,
               texname = 'scL',
               antitexname = 'scL~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

scL__tilde__ = scL.anti()

stL = Particle(pdg_code = 1000006,
               name = 'stL',
               antiname = 'stL~',
               spin = 1,
               color = 3,
               mass = Param.MstL,
               width = Param.WstL,
               texname = 'stL',
               antitexname = 'stL~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

stL__tilde__ = stL.anti()

suR = Particle(pdg_code = 2000002,
               name = 'suR',
               antiname = 'suR~',
               spin = 1,
               color = 3,
               mass = Param.MsuR,
               width = Param.WsuR,
               texname = 'suR',
               antitexname = 'suR~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

suR__tilde__ = suR.anti()

scR = Particle(pdg_code = 2000004,
               name = 'scR',
               antiname = 'scR~',
               spin = 1,
               color = 3,
               mass = Param.MscR,
               width = Param.WscR,
               texname = 'scR',
               antitexname = 'scR~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

scR__tilde__ = scR.anti()

stR = Particle(pdg_code = 2000006,
               name = 'stR',
               antiname = 'stR~',
               spin = 1,
               color = 3,
               mass = Param.MstR,
               width = Param.WstR,
               texname = 'stR',
               antitexname = 'stR~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

stR__tilde__ = stR.anti()

sdL = Particle(pdg_code = 1000001,
               name = 'sdL',
               antiname = 'sdL~',
               spin = 1,
               color = 3,
               mass = Param.MsdL,
               width = Param.WsdL,
               texname = 'sdL',
               antitexname = 'sdL~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sdL__tilde__ = sdL.anti()

ssL = Particle(pdg_code = 1000003,
               name = 'ssL',
               antiname = 'ssL~',
               spin = 1,
               color = 3,
               mass = Param.MssL,
               width = Param.WssL,
               texname = 'ssL',
               antitexname = 'ssL~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

ssL__tilde__ = ssL.anti()

sbL = Particle(pdg_code = 1000005,
               name = 'sbL',
               antiname = 'sbL~',
               spin = 1,
               color = 3,
               mass = Param.MsbL,
               width = Param.WsbL,
               texname = 'sbL',
               antitexname = 'sbL~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sbL__tilde__ = sbL.anti()

sdR = Particle(pdg_code = 2000001,
               name = 'sdR',
               antiname = 'sdR~',
               spin = 1,
               color = 3,
               mass = Param.MsdR,
               width = Param.WsdR,
               texname = 'sdR',
               antitexname = 'sdR~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sdR__tilde__ = sdR.anti()

ssR = Particle(pdg_code = 2000003,
               name = 'ssR',
               antiname = 'ssR~',
               spin = 1,
               color = 3,
               mass = Param.MssR,
               width = Param.WssR,
               texname = 'ssR',
               antitexname = 'ssR~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

ssR__tilde__ = ssR.anti()

sbR = Particle(pdg_code = 2000005,
               name = 'sbR',
               antiname = 'sbR~',
               spin = 1,
               color = 3,
               mass = Param.MsbR,
               width = Param.WsbR,
               texname = 'sbR',
               antitexname = 'sbR~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sbR__tilde__ = sbR.anti()

