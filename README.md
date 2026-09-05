# Analog Temperature Controller with Hysteresis

Built, simulated, and tested an analog temperature controller using an NTC thermistor, op-amp signal conditioning, a Schmitt trigger, an NPN transistor, and resistive heating elements.

---

## Project Overview

The goal of this project was to regulate temperature within a defined range using analog feedback and hysteresis.

### Control Chain

**Temperature → Thermistor → Voltage Divider → Voltage Buffers → Differential Amplifier → Schmitt Trigger → BJT Switch → Heater**

---

## Circuit Schematic

The complete system combines temperature sensing, signal conditioning, hysteresis, and power switching in one analog control circuit.

![Circuit Schematic](images/Circuitschematic.png)

---

## Key Features

- NTC thermistor temperature sensing
- Op-amp voltage buffering
- Differential signal conditioning
- Schmitt-trigger hysteresis
- NPN low-side heater switching
- Resistive heater load
- LTspice transient simulation
- Physical prototype validation
- Simulation-to-hardware comparison

---

## Thermistor Characterization

The thermistor was experimentally characterized by measuring its resistance at two temperatures.

| Temperature | Measured Resistance |
|---:|---:|
| 74.7°F | 569 Ω |
| 90.4°F | 435 Ω |

A linear approximation was used over the operating range:

$$
R_T = -8.53503T + 1206.56688
$$

where:

- \(R_T\) is the thermistor resistance in ohms
- \(T\) is the temperature in °F

The negative slope confirms the expected **NTC behavior**: thermistor resistance decreases as temperature increases.

![Thermistor Characterization](images/thermistor_characterization.png)

---

## Design Targets

The controller was designed around a hysteresis band of approximately:

| Control Event | Target Temperature |
|---|---:|
| Heater ON | 83°F |
| Heater OFF | 87°F |

Using the thermistor model:

| Temperature | Calculated Thermistor Resistance |
|---:|---:|
| 83°F | 498.16 Ω |
| 87°F | 464.02 Ω |

The temperature-sensitive divider uses:

$$
V_2 = 5\left(\frac{R_1}{R_1 + R_T}\right)
$$

with:

$$
R_1 = 481\ \Omega
$$

This gives:

| Temperature | Sensor Voltage \(V_2\) |
|---:|---:|
| 83°F | 2.456 V |
| 87°F | 2.544 V |

Therefore, the sensor voltage changes by only:

$$
\Delta V_2 = 2.544 - 2.456 \approx 0.088\text{ V}
$$

or approximately **88 mV** across the design temperature range.

---

## Signal Conditioning

Because the thermistor divider produces only a small voltage change, a differential amplifier is used to amplify the difference between the thermistor signal and the adjustable reference voltage.

Voltage followers are placed before the differential stage to buffer both signals and prevent loading of the sensing networks.

### Differential Amplifier Values

| Component | Value |
|---|---:|
| \(Ra\) | 100 Ω |
| \(Rb\) | 1082 Ω |
| \(Rc\) | 100 Ω |
| \(Rd\) | 1082 Ω |

The differential gain is approximately:

$$
A_v = \frac{R_b}{R_a}
$$

$$
A_v = \frac{1082}{100} \approx 10.82
$$

The amplified difference is then sent to the Schmitt trigger.

---

## Schmitt Trigger and Hysteresis

The Schmitt trigger uses **positive feedback** to create two switching thresholds rather than a single switching voltage.

Measured physical thresholds were:

| Threshold | Measured Voltage |
|---|---:|
| Upper threshold | +0.5369 V |
| Lower threshold | -0.431 V |

This hysteresis prevents rapid ON/OFF switching when the sensed temperature is near the desired operating point.

### Control Behavior

**Low temperature → Schmitt output HIGH → NPN transistor ON → Heater ON**

**High temperature → Schmitt output LOW → NPN transistor OFF → Heater OFF**

Between the two thresholds, the Schmitt trigger retains its previous state.

---

## LTspice Simulation

The complete controller was recreated in LTspice.

A transient simulation varied the modeled thermistor temperature continuously through:

$$
80^\circ F \rightarrow 90^\circ F \rightarrow 80^\circ F
$$

Unlike separate DC operating-point simulations, the transient analysis allowed the Schmitt trigger to retain its previous state and demonstrate true hysteresis.

The simulation showed:

- heater ON at low temperature
- heater switching OFF after the upper threshold was crossed
- heater remaining OFF during initial cooling
- heater switching back ON only after the lower threshold was crossed

![LTspice Transient Response](images/ltspice_transient_response.png)

### LTspice Source File

The complete LTspice schematic is available here:

[`ltspice/hysteresis_temperature_controller.asc`](ltspice/hysteresis_temperature_controller.asc)

---

## Physical Prototype

The controller was also constructed and tested on a breadboard.

![Physical Prototype](images/physical_prototype.png)

The physical system switched at approximately:

| Control Event | Measured Temperature |
|---|---:|
| Heater ON | 86.7°F |
| Heater OFF | 88.7°F |

This confirmed that the physical circuit successfully regulated temperature using hysteresis.

---

## Simulation vs. Hardware

The LTspice model and physical prototype demonstrated the same fundamental switching behavior, although the exact thresholds differed.

One significant source of this difference was **op-amp saturation voltage**.

The physical circuit measured approximately:

| Parameter | Measured Value |
|---|---:|
| Positive saturation voltage | +4.330 V |
| Negative saturation voltage | -3.480 V |

The generic LTspice op-amp model saturated much closer to the ±5 V supply rails.

Because the Schmitt-trigger thresholds depend directly on the saturation voltages, this difference shifts the simulated switching points.

Other possible sources of deviation include component tolerances, simplified linear thermistor modeling, transistor nonidealities, thermal lag, and the limited number of thermistor calibration measurements.

This comparison demonstrates an important aspect of analog engineering: **simulation accurately predicts circuit behavior, but real components introduce nonideal effects that must be considered during physical implementation.**

---

## Tools and Concepts

- LTspice
- Python / Matplotlib
- Operational Amplifiers
- NTC Thermistors
- Voltage Dividers
- Voltage Followers
- Differential Amplifiers
- Schmitt Triggers
- Positive Feedback
- Hysteresis
- BJT Switching
- Analog Feedback
- Circuit Analysis
- Breadboard Prototyping

---

## Project Takeaway

This project demonstrates the complete engineering workflow from **sensor characterization and circuit design to simulation, hardware implementation, and experimental validation**.
