from matplotlib import pyplot as plt
import pandas as pd


datafile = 'xs-rep-14TeV-fermions.csv'
pdfname = 'M8_at14TeV.pdf'
FONT = 13
lw = 1.8

data = pd.read_csv(datafile, index_col=0)
mrange = data.index

# M8
B6 = data['3']
B50 = data['15'] + data['10']
B64 = data['15'] + data['6'] + data['3'] + data['8']
B300 = data['42'] + data['24'] + data['15'] + data['6'] + data['3'] + data['27'] + data['10'] + data['8'] + data['15']

# M3
B384 = data['35'] + data['27'] + data['10'] + data['24'] + data['42'] + data["15'"] + data['24'] + data['15']
B960 = data['90'] + data['60'] + data['42'] + data['24'] + data['15'] + data['6'] + data['3'] + data['64'] + data['35'] + data['27'] + data['10'] + data['8'] + data['42'] + data["15'"] + data['15'] + data['24']


fig, ax = plt.subplots()
ax.plot(mrange, B6, label=r'$\mathcal{B}_6$', linewidth=lw, linestyle='-', color='C0')
ax.plot(mrange, B50, label=r'$\mathcal{B}_{50}$', linewidth=lw, linestyle='--', color='C1', zorder=3)
ax.plot(mrange, B64, label=r'$\mathcal{B}_{64}$', linewidth=lw, linestyle='-', color='C2')
ax.plot(mrange, B300, label=r'$\mathcal{B}_{300}$', linewidth=lw, linestyle='-', color='C3')
# ax.plot(mrange, B384, label=r'$\mathcal{B}_{384}$', linewidth=lw, linestyle='-', color='C4')
# ax.plot(mrange, B960, label=r'$\mathcal{B}_{960}$', linewidth=lw, linestyle=':', color='C5')

ax.legend(title='multiplets', fontsize=FONT-1, title_fontsize=FONT)
# ax.set_title('M8', fontsize=FONT+1)
ax.grid(color='grey', axis='both')

ax.set_xbound(mrange[0], 3.5)
ax.set_xlabel(r'$M$ [TeV]', fontsize=16)
plt.xticks(fontsize=FONT)

ax.set_yscale('log')
ax.set_ybound(lower=10**(-5), upper=10**1)
ax.set_ylabel(r'$\sigma$ [pb]', fontsize=FONT)
plt.yticks(fontsize=FONT)

fig.savefig(pdfname, dpi=300, pad_inches=0)
