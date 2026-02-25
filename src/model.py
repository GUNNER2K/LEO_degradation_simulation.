import numpy as np


# Technology radiation sensitivity coefficients
# Higher value = more radiation sensitive
TECH_COEFF = {
    "Si": 0.015,
    "GaAs": 0.008,
}

def altitude_factor(h_km):
    """Radiation scaling with altitude. Baseline at 400 km."""
    return max(0.0, (h_km - 400.0) / 500.0)

def inclination_factor(i_deg):
    """Inclination scaling using sin^2 dependence."""
    i_rad = np.radians(i_deg)
    return 1.0 + 0.3 * np.sin(i_rad) ** 2

def glass_shielding(g_mil, alpha=0.15):
    """Exponential shielding effect of coverglass."""
    return np.exp(-alpha * g_mil)

def annual_degradation_rate(
    altitude_km,
    inclination_deg,
    glass_thickness_mil,
    tech="GaAs",
    d_const=0.01,
):
    """Compute total annual degradation rate."""
    k_tech = TECH_COEFF[tech]

    d_rad = (
        k_tech
        * altitude_factor(altitude_km)
        * inclination_factor(inclination_deg)
        * glass_shielding(glass_thickness_mil)
    )

    return d_const + d_rad
