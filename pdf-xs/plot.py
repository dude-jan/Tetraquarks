from matplotlib import pyplot as plt
import pandas as pd


datafile = 'xs-rep-14TeV_extended.csv'
FONT = 13

style = {
    '3': {'l': '-', 'c': 'darkgreen'},
    '6': {'l': '-', 'c': 'blue'},
    '8': {'l': '--', 'c': 'red'},
    '10': {'l': '-', 'c': 'k'},
    '15': {'l': '-', 'c': 'yellow'},

    "15'": {'l': ':', 'c': 'darkgreen'},
    '21': {'l': ':', 'c': 'blue'},
    '24': {'l': '-', 'c': 'red'},
    '27': {'l': ':', 'c': 'k'},
    '35': {'l': '--', 'c': 'yellow'},

    '42': {'l': '--', 'c': 'darkgreen'},
    '60': {'l': '--', 'c': 'blue'},
    '64': {'l': ':', 'c': 'red'},
    '90': {'l': '--', 'c': 'k'}
}

pdfname = datafile[:-4] + '.pdf'
data = pd.read_csv(datafile, index_col=0)
mrange = data.index

fig, ax = plt.subplots()
for rep in data.columns:
    ax.plot(mrange, data[rep], label=rep, linewidth=1.5, linestyle=style[rep]['l'], color=style[rep]['c'])
    # ax.scatter(mrange, data[rep], s=12, c=style[rep]['c'], marker=style[rep]['m'])

ax.legend(title='SU(3) irrep', ncol=3, fontsize=FONT, title_fontsize=FONT, fancybox=True)
# ax.set_title('14 TeV')
ax.grid(color='lightgrey', axis='both')

ax.set_xbound(mrange[0], mrange[-1])
ax.set_xlabel(r'$M$ [TeV]', fontsize=FONT)
plt.xticks(fontsize = FONT)

ax.set_yscale('log')
ax.set_ybound(lower=10**(-6))
ax.set_ylabel(r'$\sigma$ [pb]', fontsize=FONT)
plt.yticks(fontsize = FONT)

fig.savefig(pdfname, dpi=300, pad_inches=0)
