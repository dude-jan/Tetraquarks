import sys
import lhapdf
import numpy as np
from scipy.integrate import quad


# print("Python:", sys.executable)
# print("LHAPDF:", lhapdf.version())
# print(lhapdf.getPDFSet("NNPDF40_lo_as_01180").description)


DYNKIN = {
    '3': 1/2, '6': 5/2, '8': 3,
    '10': 15/2, '15': 10, "15'": 35/2,
    '21': 35, '24': 25, '27': 27,
    '42': 119/2
    }

DIM = {
    '3': 3, '6': 6, '8': 8,
    '10': 10, '15': 15, "15'": 15,
    '21': 21, '24': 24, '27': 27,
    '42': 42
    }


def T(R: str) -> float:
    return DYNKIN[R]


def dim(R: str) -> float:
    return DIM[R]


def beta(s, m):
    return np.sqrt(1-4*m**2/s)


def sigma_hat_gg(s: float, m: float, R: str, alpha=0.06):
    return -(3.89379*10**8) * np.pi*alpha**2*T(R)/(2*dim(R)*s**3) * (
        beta(s, m)*s*(dim(R)*(5*m**2+s) + 8*T(R)*(4*m**2+s))
        - 8*np.arctanh(beta(s, m))*(3*dim(R)*m**4 + 2*T(R)*(-8*m**4 + 4*m**2*s + s**2)))


def sigma_pp(m: float, R: str, pdf: lhapdf.PDF,
             sqrtS: float = 100000) -> float:

    tau_min = (2 * m / sqrtS)**2
    if tau_min >= 1:
        return 0.0

    t_min = np.log(tau_min)

    def integrate_y(t):
        tau = np.exp(t)
        Q = np.sqrt(tau) * sqrtS  # example factorization scale
        alpha_s = pdf.alphasQ(Q)  # use the PDF set's alpha_s
        y_max = -t / 2

        def integrand(y):
            x1 = np.exp(t / 2 + y)
            x2 = np.exp(t / 2 - y)
            # xfxQ returns x*f(x,Q)
            xfg1 = pdf.xfxQ(21, x1, Q)
            xfg2 = pdf.xfxQ(21, x2, Q)
            shat = tau * sqrtS**2
            return xfg1 * xfg2 * sigma_hat_gg(shat, m, R, alpha_s)

        return quad(integrand, -y_max, y_max, epsrel=1e-4, limit=100)[0]

    return quad(integrate_y, t_min, 0)[0]


NNPDF = "NNPDF40_lo_as_01180"
pdf = lhapdf.mkPDF(NNPDF, 0)

print('triplet', sigma_pp(5000, '3', pdf))
print('sextet', sigma_pp(5000, '6', pdf))
print('octet', sigma_pp(5000, '8', pdf))
