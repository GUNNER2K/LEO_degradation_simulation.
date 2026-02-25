import numpy as np
from src.model import annual_degradation_rate


def simulate_power(P0, years, altitude_km, inclination_deg, glass_thickness_mil, tech):
    """Simulate power over time, returns relative power."""
    d = annual_degradation_rate(
        altitude_km=altitude_km,
        inclination_deg=inclination_deg,
        glass_thickness_mil=glass_thickness_mil,
        tech=tech,
    )
    t = np.arange(0, years + 1)
    P_rel = P0 * (1 - d) ** t / P0  # relative power
    return t, P_rel