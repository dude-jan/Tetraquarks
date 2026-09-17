#!/bin/bash

my_date(){
	echo $(date +"%a %d/%m/%Y %T")
}

# Generate events
echo "$(my_date): Point 0000: Starting event generation" | tee -a timekeeping.log
/home/manu/tools/MG5_aMC_v3_5_13/bin/mg5_aMC mg.txt

# NLO without MadSpin
if [ -f mgevents/Events/run_01/events_PYTHIA8_0.hepmc.gz ]; then
	mv mgevents/Events/run_01/events_PYTHIA8_0.hepmc.gz mgevents/Events/run_01/tag_1_pythia8_events.hepmc.gz
# NLO with MadSpin
elif [ -f mgevents/Events/run_01_decayed_1/events_PYTHIA8_0.hepmc.gz ]; then
	mv mgevents/Events/run_01_decayed_1/events_PYTHIA8_0.hepmc.gz mgevents/Events/run_01/tag_1_pythia8_events.hepmc.gz
# LO with MadSpin
elif [ -f mgevents/Events/run_01_decayed_1/tag_1_pythia8_events.hepmc.gz ]; then
	mv mgevents/Events/run_01_decayed_1/tag_1_pythia8_events.hepmc.gz mgevents/Events/run_01/tag_1_pythia8_events.hepmc.gz
fi

# Save MadGraph cards and results
cp -r mgevents/Cards ./Cards
cp mgevents/Events/run_01/run_01_tag_1_banner.txt ./Cards/banner.txt
cp mgevents/HTML/run_01/results.html ./Cards/results.html

# Get cross section
xsline=($(grep -m 1 "<b>s= " mgevents/HTML/run_01/results.html))
xs=${xsline[1]}
kfactor=1.0
xs=$(python3 -c "print($xs*$kfactor)")
echo $xs > xs.dat

rm -r mgevents
if [ -f py.py ]; then rm py.py; fi
echo "$(my_date): Point 0000: Finished run" | tee -a timekeeping.log
