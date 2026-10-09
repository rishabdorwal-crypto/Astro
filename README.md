# Astro 🌬️

### Low-Cost Aerodynamic Testing & Analysis Platform

**AeroLab** is a student engineering project exploring an affordable wind-tunnel concept combined with software for aerodynamic data analysis, design comparison, and scale-up assessment.

> **Current status:** Concept and prototype development. Software capabilities and physical testing status will be updated as they are implemented and verified.

## 🎯 Problem Statement

Access to aerodynamic testing facilities can be limited by equipment cost and availability, particularly for student engineering teams and early-stage aerospace projects.

AeroLab explores a more accessible workflow for collecting, analyzing, and interpreting aerodynamic test data.

## 💡 Proposed Solution

* A compact wind-tunnel concept for scaled-model testing.
* A software dashboard for test inputs and measurements.
* Drag coefficient and Reynolds number calculations.
* Comparison of model configurations.
* Data-quality warnings and limitations for scale-up estimates.
* Exportable test reports.

## 🛠️ Technology Stack

* Python
* Streamlit
* NumPy
* Pandas
* Plotly
* Arduino/ESP32 (planned for hardware integration)

## 🏗️ System Architecture

1. **Physical test layer:** Proposed wind tunnel and model mounting arrangement.
2. **Data acquisition:** Manual entry initially; calibrated sensor integration planned.
3. **Analysis engine:** Engineering calculations, unit validation, and test-quality checks.
4. **Visualization:** Interactive comparisons and reports.

## 📊 Engineering Principles

Drag coefficient:

$$
C_D = \frac{F_D}{\frac{1}{2}\rho V^2 A}
$$

Reynolds number:

$$
Re = \frac{\rho V L}{\mu}
$$

Full-scale extrapolation requires careful consideration of Reynolds number, geometry, turbulence, blockage, and measurement uncertainty.

## 🚧 Development Roadmap

* [ ] Implement and test engineering calculations
* [ ] Build the interactive dashboard
* [ ] Add clearly labelled demonstration data
* [ ] Document the physical prototype
* [ ] Integrate suitable sensors
* [ ] Calibrate and validate measurements
* [ ] Evaluate scale-up methods against trusted reference data

## 🧪 Validation and Data Integrity

Synthetic or illustrative data will be explicitly labelled. Physical measurements will be identified separately and documented with their test conditions and calibration status.

AeroLab is an educational prototype and is not currently claimed to replace professional aerodynamic testing facilities.

## 🚀 Running the Application

Setup instructions will be added after the first working version is implemented.

## 🤝 Contributions

Suggestions, engineering feedback, and collaboration are welcome.

## 📜 License

License to be selected before public reuse and distribution.
