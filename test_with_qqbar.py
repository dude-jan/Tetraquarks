"""Leading-order QCD pair production of a Dirac fermion in an SU(3) irrep.

The returned hadronic cross sections are in pb. All masses and energies are
in GeV. The calculation includes gg and same-flavour q qbar initial states.
"""

import lhapdf
import numpy as np
from scipy.integrate import quad


PB_PER_GEV2 = 3.89379e8
DYNKIN = {
    "3": 1 / 2, "6": 5 / 2, "8": 3,
    "10": 15 / 2, "15": 10, "15'": 35 / 2,
    "21": 35, "24": 25, "27": 27, "42": 119 / 2,
}
DIM = {
    "3": 3, "6": 6, "8": 8,
    "10": 10, "15": 15, "15'": 15,
    "21": 21, "24": 24, "27": 27, "42": 42,
}


def representation_invariants(rep: str | tuple[int, int]) -> tuple[float, float]:
    """Return (dimension, Dynkin index) for an SU(3) representation.

    A (p, q) tuple of nonnegative Dynkin labels permits any SU(3) irrep.
    String names retain compatibility with the original representation table.
    """
    if isinstance(rep, str):
        if rep not in DYNKIN or rep not in DIM:
            raise ValueError(f"unknown SU(3) representation: {rep}")
        return DIM[rep], DYNKIN[rep]
    if (not isinstance(rep, tuple) or len(rep) != 2
            or any(type(label) is not int or label < 0 for label in rep)):
        raise ValueError("rep must be a known name or nonnegative SU(3) Dynkin labels (p, q)")
    p, q = rep
    dimension = (p + 1) * (q + 1) * (p + q + 2) // 2
    casimir = (p*p + q*q + p*q + 3*p + 3*q) / 3.0
    return dimension, dimension * casimir / 8.0


def beta(shat: float, mass: float) -> float:
    return np.sqrt(max(0.0, 1.0 - 4.0 * mass**2 / shat))


def sigma_hat_gg(shat: float, mass: float, rep: str | tuple[int, int], alpha_s: float) -> float:
    """Original gg result, with a threshold guard; returns pb."""
    if shat <= 4.0 * mass**2:
        return 0.0
    b = beta(shat, mass)
    d, tr = representation_invariants(rep)
    return -PB_PER_GEV2 * np.pi * alpha_s**2 * tr / (2.0 * d * shat**3) * (
        b * shat * (d * (5.0 * mass**2 + shat) + 8.0 * tr * (4.0 * mass**2 + shat))
        - 8.0 * np.arctanh(b) * (
            3.0 * d * mass**4
            + 2.0 * tr * (-8.0 * mass**4 + 4.0 * mass**2 * shat + shat**2)
        )
    )


def sigma_hat_qqbar(shat: float, mass: float, rep: str | tuple[int, int], alpha_s: float) -> float:
    """q qbar -> X_R Xbar_R via one gluon; spin/color averaged, in pb.

    T(R) is defined by Tr(T_R^a T_R^b) = T(R) delta^{ab}. For R=3,
    this reduces to the standard heavy-quark Born cross section.
    """
    if shat <= 4.0 * mass**2:
        return 0.0
    b = beta(shat, mass)
    _, tr = representation_invariants(rep)
    return (PB_PER_GEV2 * 16.0 * np.pi * alpha_s**2 * tr
            / (27.0 * shat) * b * (1.0 + 2.0 * mass**2 / shat))


def sigma_pp_components(
    mass: float,
    rep: str | tuple[int, int],
    pdf: lhapdf.PDF,
    sqrt_s: float = 100_000.0,
    flavours=(1, 2, 3, 4, 5),
) -> dict[str, float]:
    """Return separate gg and q qbar contributions to pp -> X_R Xbar_R.

    The coordinates t=log(tau), y=log(x1/x2)/2 satisfy
    x1*x2=tau and dx1*dx2=x1*x2*dt*dy. Since LHAPDF's xfxQ
    returns x*f(x,Q), the Jacobian cancels the two factors of x.
    """
    if mass <= 0 or sqrt_s <= 0:
        raise ValueError("mass and sqrt_s must be positive")
    representation_invariants(rep)
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
            q_scale = np.sqrt(shat)  # same mu_F and mu_R choice as the original script
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


def sigma_pp(
    mass: float,
    rep: str | tuple[int, int],
    pdf: lhapdf.PDF,
    sqrt_s: float = 100_000.0,
) -> float:
    """Total LO QCD pp pair-production cross section, in pb."""
    return sum(sigma_pp_components(mass, rep, pdf, sqrt_s).values())


if __name__ == "__main__":
    pdf = lhapdf.mkPDF("NNPDF40_lo_as_01180", 0)
    for rep in ("3", "6", "8"):
        parts = sigma_pp_components(5_000.0, rep, pdf)
        print(rep, parts, "total", sum(parts.values()), "pb")
