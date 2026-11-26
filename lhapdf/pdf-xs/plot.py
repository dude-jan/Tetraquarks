from matplotlib import pyplot as plt
import pandas as pd


datafile = 'xs-rep-14TeV-fermions.csv'
FONT = 13

style = {
    '3': {'l': '-', 'c': 'C0'},
    '6': {'l': '-', 'c': 'C1'},
    '8': {'l': '--', 'c': 'C2'},
    '10': {'l': '-', 'c': 'C3'},
    "15'": {'l': '-', 'c': 'C4'},

    '15': {'l': '--', 'c': 'C5'},
    # '21': {'l': ':', 'c': 'cornflowerblue'},
    '24': {'l': '-', 'c': 'tab:cyan'},
    '27': {'l': '--', 'c': 'C7'},
    # '35': {'l': ':', 'c': 'chocolate'},

    '42': {'l': '-', 'c': 'C8'},
    # '60': {'l': '-', 'c': 'cornflowerblue'},
    # '64': {'l': '--', 'c': 'red'},
    # '90': {'l': '-', 'c': 'k'}
}

pdfname = datafile[:-4] + '.pdf'
data = pd.read_csv(datafile, index_col=0)
mrange = data.index

fig, ax = plt.subplots()
for rep in style.keys():
    ax.plot(mrange, data[rep], label=rep, linewidth=1.8, linestyle=style[rep]['l'], color=style[rep]['c'],
            zorder=3 if rep == "35" else 2)

ax.legend(title='SU(3) irrep', ncol=3, fontsize=FONT-1, title_fontsize=FONT, fancybox=True)
ax.grid(color='lightgrey', axis='both')

ax.set_xbound(mrange[0], 3.5)
ax.set_xlabel(r'$M$ [TeV]', fontsize=FONT)
plt.xticks(fontsize=FONT)

ax.set_yscale('log')
ax.set_ybound(lower=10**(-5), upper=10**1)
ax.set_ylabel(r'$\sigma$ [pb]', fontsize=FONT)
plt.yticks(fontsize=FONT)

fig.savefig(pdfname, dpi=300, pad_inches=0)
