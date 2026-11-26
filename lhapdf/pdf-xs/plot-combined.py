from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D


datafile1 = 'xs-rep-14TeV-fermions.csv'
datafile2 = 'xs-rep-14TeV-scalars.csv'

pdfname = 'xs-rep-14TeV-combined_final.pdf'
FONT = 13

style = {
    '3': {'c': 'C0'},
    '6': {'c': 'C1'},
    '8': {'c': 'C2'},
    '10': {'c': 'C3'},
    "15'": {'c': 'C4'},
}

fig, ax = plt.subplots()

data = pd.read_csv(datafile1, index_col=0)
mrange = data.index
data_scalar = pd.read_csv(datafile2, index_col=0)
mrange_scalar = data_scalar.index

for rep in data_scalar.columns:
    ax.plot(mrange, data[rep], label=rep+'f',
            linewidth=1.8, linestyle='-', color=style[rep]['c'], zorder=3)

for rep in data_scalar.columns:
    ax.plot(mrange_scalar, data_scalar[rep], label=rep+'s',
            linewidth=1.8, linestyle='--', color=style[rep]['c'], zorder=3)

# Custom legend entries: color and linestyle are set independently
chandles = []
for rep in style.keys():
    chandles.append(Line2D([0], [0], color=style[rep]['c'], linestyle="-",  label=rep))
clegend = ax.legend(handles=chandles, title='SU(3) irrep', ncol=3, fontsize=FONT-1, title_fontsize=FONT, fancybox=True, loc='upper right')
plt.gca().add_artist(clegend)

lhandles = [
    Line2D([0], [0], color="black", linestyle="-", linewidth=1.8, label="fermionic"),
    Line2D([0], [0], color="black", linestyle="--", linewidth=1.8, label="scalar"),
]
ax.legend(handles=lhandles, fontsize=FONT-1, fancybox=True, loc='right')
ax.grid(axis='both', linewidth=0.5, linestyle=':')
ax.tick_params(which='both', direction="in", right=True, top=True)

ax.set_xbound(mrange[0], 3.5)
ax.set_xlabel(r'$M$ [TeV]', fontsize=FONT)
plt.xticks(fontsize=FONT)

ax.set_yscale('log')
ax.set_ybound(lower=10**(-5), upper=1)
ax.set_ylabel(r'$\sigma$ [pb]', fontsize=FONT)
plt.yticks(fontsize=FONT)

fig.savefig(pdfname, dpi=300, bbox_inches='tight', transparent=True, pad_inches=0.02)
