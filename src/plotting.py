import os
import numpy as np
import matplotlib.pyplot as plt

P0 = 1000
years = 10
inclination = 60
default_altitude = 700
default_glass = 3
default_tech = "GaAs"

RESULT_DIR = "results"
os.makedirs(RESULT_DIR, exist_ok=True)

# 1) Altitude Comparison (rest constant)

altitudes = [400, 700, 926]

plt.figure()
for h in altitudes:
    t, P_rel = simulate_power(
        P0,
        years,
        altitude_km=h,
        inclination_deg=inclination,
        glass_thickness_mil=default_glass,
        tech=default_tech,
    )
    plt.plot(t, P_rel, label=f"{h} km")

plt.xlabel("Time (years)")
plt.ylabel("Relative Power (P / P0)")
plt.title("Degradation Comparison: Different Altitudes")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(RESULT_DIR, "comparison_altitudes.png"))
plt.close()


# 2) Technology Comparison (rest constant)

technologies = ["Si", "GaAs"]

plt.figure()
for tech in technologies:
    t, P_rel = simulate_power(
        P0,
        years,
        altitude_km=default_altitude,
        inclination_deg=inclination,
        glass_thickness_mil=default_glass,
        tech=tech,
    )
    plt.plot(t, P_rel, label=tech)

plt.xlabel("Time (years)")
plt.ylabel("Relative Power (P / P0)")
plt.title("Degradation Comparison: Different Cell Technologies")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(RESULT_DIR, "comparison_technologies.png"))
plt.close()


# 3) Glass Thickness Comparison (rest constant)

glass_thicknesses = [3, 6, 9]

plt.figure()
for g in glass_thicknesses:
    t, P_rel = simulate_power(
        P0,
        years,
        altitude_km=default_altitude,
        inclination_deg=inclination,
        glass_thickness_mil=g,
        tech=default_tech,
    )
    plt.plot(t, P_rel, label=f"{g} mil")

plt.xlabel("Time (years)")
plt.ylabel("Relative Power (P / P0)")
plt.title("Degradation Comparison: Different Coverglass Thickness")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(RESULT_DIR, "comparison_glass_thickness.png"))
plt.close()

print("Plots successfully generated in 'results/' folder.")