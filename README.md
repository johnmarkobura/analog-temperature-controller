# Analog Temperature Controller with Hysteresis

Built and simulated an analog closed-loop temperature controller using a thermistor, op-amp signal conditioning, a Schmitt trigger, an NPN transistor, and resistive heating elements.

## Project Overview

The goal of this project was to maintain temperature within a defined range using analog feedback.

The control chain is:

Temperature → Thermistor → Voltage Divider → Buffers → Differential Amplifier → Schmitt Trigger → BJT Switch → Heater

## Key Features

- NTC thermistor temperature sensing
- Differential signal conditioning
- Schmitt-trigger hysteresis
- NPN low-side switching
- Resistive heater load
- LTspice transient simulation
- Simulation-to-hardware comparison

## Thermistor Characterization

Measured data:

- 74.7°F → 569 Ω
- 90.4°F → 435 Ω

Linear approximation:

R_T = -8.53503T + 1206.56688

## Design Targets

Target switching temperatures:

- Heater ON: ~83°F
- Heater OFF: ~87°F

Thermistor resistances:

- R_T(83°F) ≈ 498.16 Ω
- R_T(87°F) ≈ 464.02 Ω

## Signal Conditioning

The thermistor voltage divider produces approximately:

- V2(83°F) ≈ 2.456 V
- V2(87°F) ≈ 2.544 V

The differential amplifier uses approximately:

- Ra = 100 Ω
- Rb = 1082 Ω

Giving a gain of:

Av = Rb / Ra ≈ 10.82

## Schmitt Trigger

The Schmitt trigger introduces hysteresis so the heater does not rapidly switch ON and OFF around a single threshold.

Measured physical thresholds:

- Vut ≈ +0.5369 V
- Vlt ≈ -0.431 V

## LTspice Simulation

A continuous transient simulation was used to vary temperature from 80°F to 90°F and back to 80°F.

The simulation demonstrated:

- heater ON at low temperature
- heater OFF after crossing the upper threshold
- delayed turn-on during cooling
- hysteresis behavior in the control loop

## Hardware Results

The physical system switched:

- OFF at approximately 88.7°F
- ON at approximately 86.7°F

## Simulation vs Hardware

The LTspice simulation uses an idealized op-amp model that saturates closer to the supply rails than the physical device.

This shifts the Schmitt-trigger thresholds and illustrates the importance of nonideal device behavior in analog design.

## Tools

- LTspice
- Op-Amps
- NTC Thermistor
- Schmitt Trigger
- BJT Switching
- Analog Feedback
- Circuit Analysis
- Breadboard Prototyping

## Files

- LTspice schematic
- Project report
- Design calculations
- Simulation plots
- Physical prototype images
