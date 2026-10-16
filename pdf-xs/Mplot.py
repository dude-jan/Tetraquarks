from matplotlib import pyplot as plt
import pandas as pd


datafile = 'xs-rep-100TeV_extended.csv'
pdfname = 'M8.pdf'
FONT = 13

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
ax.plot(mrange, B6, label=r'$\mathcal{B}_6$', linewidth=1.5, linestyle='-', color='darkgreen')
ax.plot(mrange, B50, label=r'$\mathcal{B}_{50}$', linewidth=1.5, linestyle='--', color='blue')
ax.plot(mrange, B64, label=r'$\mathcal{B}_{64}$', linewidth=1.5, linestyle='-', color='red')
ax.plot(mrange, B300, label=r'$\mathcal{B}_{300}$', linewidth=1.5, linestyle='--', color='k')
# ax.plot(mrange, B384, label=r'$\mathcal{B}_{384}$', linewidth=1.5, linestyle='-', color='yellow')
# ax.plot(mrange, B960, label=r'$\mathcal{B}_{960}$', linewidth=1.5, linestyle='-', color='purple')

ax.legend(title='multiplets', fontsize=FONT, title_fontsize=FONT)
# ax.set_title('M8', fontsize=FONT+1)
ax.grid(color='grey', axis='both')

ax.set_xbound(mrange[0], mrange[-1])
ax.set_xlabel(r'$M$ [TeV]', fontsize=16)
plt.xticks(fontsize = FONT)

ax.set_yscale('log')
ax.set_ybound(lower=10**(-6))
ax.set_ylabel(r'$\sigma$ [pb]', fontsize=FONT)
plt.yticks(fontsize = FONT)

fig.savefig(pdfname, dpi=300, pad_inches=0)
