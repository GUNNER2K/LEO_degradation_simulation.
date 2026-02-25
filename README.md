# Solar Array Degradation Simulation in LEO

## Overview

This project implements a **Level 2 solar array degradation model** for small satellites in **Low Earth Orbit (LEO)**. The simulation estimates **relative end-of-life (EOL) power** over a mission duration of 10 years for different conditions:

- **Altitude**: 400 km, 700 km, 926 km  
- **Solar cell technology**: Silicon (Si BSF/R) and Gallium Arsenide (GaAs/Ge)  
- **Coverglass thickness**: 3 mil, 6 mil, 9 mil  

The code generates comparison plots for each factor, keeping other parameters constant, and saves them into a `results/` folder.

---

## Assumptions

1. **Degradation Components**:  
   The total annual degradation rate is composed of:  

   \[
   d_{total} = d_{const} + d_{rad}
   \]

   - `d_const` (1%/year) accounts for **UV exposure and atomic oxygen** damage.  
   - `d_rad` accounts for **radiation-induced degradation**, modeled as a function of altitude, inclination, coverglass thickness, and cell technology.

2. **Altitude Factor**:  
   Radiation damage increases linearly above a baseline altitude of 400 km:
   
   $$
   F_{alt}(h) = \max(0, (h - 400)/500)
   $$

3. **Inclination Factor (Taken from the shared paper)**:  
   Exposure depends on orbit inclination (sin² dependence to model polar/SAA exposure):
   
   \[
   F_{inc}(i) = 1 + 0.3 \cdot \sin^2(i)
   \]

4. **Coverglass Shielding (Taken from the shared paper)**:  
   Radiation attenuation through glass follows an **exponential decay**:

   \[
   S_{glass}(g) = \exp(-\alpha g), \quad \alpha = 0.15
   \]

5. **Technology Sensitivity (Taken from the shared paper)**:  
   - GaAs/Ge: `k_tech = 0.008` (radiation hard)  
   - Si BSF/R: `k_tech = 0.015` (more radiation sensitive)

6. **Multiplicative Degradation**:  
   Annual degradation is multiplicative over the mission duration:

   \[
   P(t) = P_0 \cdot (1 - d_{total})^t
   \]

7. **Other Simplifications**:  
   - Thermal cycling, eclipse effects, and micrometeoroid impacts are **not included**.  
   - The model is **parameterized** for easy extension to more complex physics-based degradation.

---

## Simulation Structure

- **`main.py`** – main script performing the simulations and generating plots  
- **`results/`** – folder where all plots are automatically saved  
  - `comparison_altitudes.png`  
  - `comparison_technologies.png`  
  - `comparison_glass_thickness.png`

---

## Libraries Used

1. **NumPy**  
   - Efficient vectorized computations for power evolution over time.  
   - Handles trigonometric calculations for inclination scaling.

2. **Matplotlib**  
   - Standard library for high-quality scientific plotting.  
   - Allows flexible customization and saving of plots in PNG format.

**Rationale**:  
- Chosen for **simplicity, lightweight design, and reproducibility**.  
- No heavy frameworks are required, keeping the mini-demo clean and computationally trivial.

---

## How to Run

```bash
python main.py
