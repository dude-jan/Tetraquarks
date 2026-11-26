import sys
import lhapdf
import numpy as np
from scipy.integrate import quad
import csv
from pathlib import Path
import pandas as pd


# print("Python:", sys.executable)
# print("LHAPDF:", lhapdf.version())
# print(lhapdf.getPDFSet("NNPDF40_lo_as_01180").description)


DYNKIN = {
    '3': 1/2, '6': 5/2, '8': 3,
    '10': 15/2, "15'": 35/2,
    }
REPS = DYNKIN.keys()

DIM = {
    '3': 3, '6': 6, '8': 8,
    '10': 10, '15': 15, "15'": 15,
    }


def T(R: str) -> float:
    return DYNKIN[R]


def dim(R: str) -> float:
    return DIM[R]


def beta(s, m):
    return np.sqrt(1-4*m**2/s)


def sigma_hat_gg(s: float, m: float, R: str, alpha=0.06):
    """g g -> X X*; spin/color averaged, in pb
    """
    if s <= 4.0 * m**2:
        return 0.0

    return (3.89379*10**8) * np.pi*alpha**2*T(R)/(6*8*dim(R)*s) * (
        3*dim(R)*beta(s, m)*(3 - 5*beta(s, m)**2) - 12*8*T(R)*beta(s, m)*(beta(s, m)**2 - 2)
        + 2*np.arctanh(beta(s, m))*(6*8*T(R)*(beta(s, m)**4 - 1) - 3*3*dim(R)*(beta(s, m)**2-1)**2)
        )


def sigma_hat_qqbar(s: float, m: float, R: str, alpha: float = 0.06) -> float:
    """q qbar -> X X* via one gluon; spin/color averaged, in pb
    """
    if s <= 4.0 * m**2:
        return 0.0

    return (3.89379*10**8)*4*np.pi*alpha**2*T(R) / (27*s) * beta(s, m)**3


def sigma_pp_components(mass: float, rep: str, pdf: lhapdf.PDF,
                        sqrt_s: float = 100_000.0, flavours=(1, 2, 3, 4, 5)) -> dict[str, float]:
    """Return separate gg and q qbar contributions to pp -> X Xbar
    """
    if mass <= 0 or sqrt_s <= 0:
        raise ValueError("mass and sqrt_s must be positive")

    if any(flavour not in (1, 2, 3, 4, 5, 6) for flavour in flavours):
        raise ValueError("flavours must contain quark PDG IDs 1 through 6")

    tau_min = (2.0 * mass / sqrt_s)**2
    if tau_min >= 1.0:
        return {"gg": 0.0, "qqbar": 0.0}
    t_min = np.log(tau_min)

    def integrate_channel(channel: str) -> float:
        def integrate_y(t: float) -> float:
            tau = np.exp(t)
            shat = tau * sqrt_s**2
            q_scale = np.sqrt(shat)  # example factorization scale
            alpha_s = pdf.alphasQ(q_scale)
            y_max = -t / 2.0
            hat = (sigma_hat_gg if channel == "gg" else sigma_hat_qqbar)(
                shat, mass, rep, alpha_s
            )

            def integrand(y: float) -> float:
                x1 = np.exp(t / 2.0 + y)
                x2 = np.exp(t / 2.0 - y)
                if channel == "gg":
                    luminosity = pdf.xfxQ(21, x1, q_scale) * pdf.xfxQ(21, x2, q_scale)
                else:
                    luminosity = sum(
                        pdf.xfxQ(q, x1, q_scale) * pdf.xfxQ(-q, x2, q_scale)
                        + pdf.xfxQ(-q, x1, q_scale) * pdf.xfxQ(q, x2, q_scale)
                        for q in flavours
                    )
                return luminosity * hat

            return quad(integrand, -y_max, y_max, epsrel=1e-4, limit=100)[0]

        return quad(integrate_y, t_min, 0.0, epsrel=1e-4, limit=100)[0]

    return {channel: integrate_channel(channel) for channel in ("gg", "qqbar")}


def sigma_pp(m: float, R: str, pdf: lhapdf.PDF,
             sqrt_s: float = 100_000.0) -> float:
    """Total LO QCD pp pair-production cross section, in pb."""
    return sum(sigma_pp_components(m, R, pdf, sqrt_s).values())


def xsrep(output, energy: float = 100.0, mrange=np.linspace(1.0, 20.0, num=5)):
    NNPDF = "NNPDF40_lo_as_01180"
    pdf = lhapdf.mkPDF(NNPDF, 0)

    data = np.empty((len(mrange), len(REPS)))
    for r, rep in enumerate(REPS):
        for m, mass in enumerate(mrange):
            sigma = sigma_pp(1e3*mass, rep, pdf, sqrt_s=1e3*energy)
            data[m, r] = sigma

    pd.DataFrame(data, columns=REPS, index=mrange).to_csv(output)


def main():
    NNPDF = "NNPDF40_lo_as_01180"
    pdf = lhapdf.mkPDF(NNPDF, 0)

    output = Path("./s=14&m=3&dynscale.csv").resolve()
    # output = Path("./projects/lhapdf-test/s=14&m=3&dynscale.csv").resolve()
    print("Writing to:", output, flush=True)

    with open(output, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['rep', 'gg [pb]', 'qqbar [pb]', 'total [pb]'])

        for rep in REPS:
            parts = sigma_pp_components(3000.0, rep, pdf, sqrt_s=14_000)
            print(rep, parts, 'total', sum(parts.values()), 'pb')
            writer.writerow([rep, parts['gg'], parts['qqbar'], sum(parts.values())])


# NNPDF = "NNPDF40_lo_as_01180"
# pdf = lhapdf.mkPDF(NNPDF, 0)

# NNPDF = "NNPDF23_nlo_as_0119"
# pdf = lhapdf.mkPDF(NNPDF, 0)

# comp = sigma_pp_components(500, '3', pdf, 14_000, flavours=(1, 2, 3, 4))
# print(comp, sum(comp.values()))

datafile = 'comparison-scalars.csv'  # 'xs-rep-100TeV_extended.csv'
xsrep(datafile, energy=13.0, mrange=np.linspace(.2, 1.8, num=10))
