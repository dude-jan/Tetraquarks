
protected_couplings = ["ymb","ymt","ymtau","aEWM1","Gf","aS"]

with open("param_card.dat", "r") as inputF, open("zero_couplings.dat", "w") as outputF:
    for line in inputF:
        words = line.split()
        not_coupling = "DECAY" in line or "Block" in line or len(words)==0 or "# M" in line or "##" in line
        if not not_coupling:
            coupling = words[-1]
            if not coupling in protected_couplings:
                outputF.write("set /Herwig/FRModel/FRModel:" + words[-1] + " 0\n")
        