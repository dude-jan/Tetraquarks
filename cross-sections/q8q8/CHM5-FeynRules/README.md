# CHM5-FeynRules

Convention for the particle names:
- Q80M = gluino
- Q10M = bino
- S323 = pi_3/stop
- S80 = pi_8
- S11 = eta_3^+ 
- S112 = eta_5^+ 
- S10 = eta
- S102 = eta_1^0
- S103 = eta_3^0
- S104 = eta_5^0
- S105 = a

ScriptForHerwig:\
ScriptForHerwig sets couplings per default to 0. Parameters may be specified to certain values or protected to be overwritten.\
Compile: >g++ ScriptForHerwig.cc -o ScriptForHerwig.o\
Usage:	 >./ScriptForHerwig.cc configurationfile\
If no configuration file is specified, all couplings will be set to 0.\
The configuration file, for example sfhconf.dat, is used to protect parameters from setting to 0 or to set specific parameters to predefined values. The configuration file MUST NOT be names "params.dat" because this may result in problems with contur.
- Set a parameter P to Value V:

>	P V

- Protect parameter P:

>	\P

- Set incoming particle:

>	\< /Herwig/Particles/Particlename

- Set outgoing particle:

>	\> /Herwig/FRModel/Particles/Particlename

- Processes

>	:Processes Process-Type

>	:RivetAnalysis 1

- Activate Rivet

>	:RivetAnalysis 1

- Example:

>	\#Protected parameters\
>	\P1\
>	\P23\
>	\#Masses\
>	M1 1000\
>	M2 1400\
>	\#Couplings\
>	G1 0.1\
>	G53 0.4
