# Solar Array Degradation Simulation in LEO

## Overview

This project implements a **Level 2 solar array degradation model** for small satellites in **Low Earth Orbit (LEO)**. The simulation estimates **relative end-of-life (EOL) power** over a mission duration of 10 years for different conditions:

- **Altitude**: 400 km, 700 km 
- **Solar cell technology**: Silicon (Si BSF/R) and Gallium Arsenide (GaAs/Ge) (Taken from the shared papers)
- **Coverglass thickness**: 3 mil, 6 mil  (Taken from the shared papers)
- **Inclination** : 60 degrees, kept constant. (Taken from the shared papers)

The code generates comparison plots for each factor, keeping other parameters constant, and saves them into a `results/` folder.

## Before running

### Create a virtual environment
python 3.11 was used in this simulation.
```bash
conda create -p myenv python=3.11
```

### install necessary libraries
can be found in the ```requirements.txt ``` file.

```bash
pip install -r requirements.txt
```
---
## How to Run

```bash
python main.py
```
## Assumptions

1. **Degradation Components**:  
   The total annual degradation rate is:

   d_total = d_const + d_rad

   - d_const (1%/year) accounts for **UV exposure and atomic oxygen** damage.  
   - d_rad accounts for **radiation-induced degradation**, modeled as a function of altitude, inclination, coverglass thickness, and cell technology.

2. **Altitude Factor**:  
   Radiation damage increases linearly above 400 km:

   F_alt(h) = max(0, (h - 400)/500)

3. **Inclination Factor**:  

   F_inc(i) = 1 + 0.3 × sin²(i)

4. **Coverglass Shielding**:  

   S_glass(g) = exp(-α × g), α = 0.15

5. **Technology Sensitivity**:  
   - GaAs/Ge: k_tech = 0.008  
   - Si BSF/R: k_tech = 0.015

6. **Multiplicative Degradation**:

   P(t) = P₀ × (1 - d_total)^t
   
8. **Other Simplifications**:  
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
