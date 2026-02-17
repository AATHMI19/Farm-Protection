# 🌾 Farm Guard – Smart Crop Protection System
**Farm Guard** is an IoT-based bird and animal deterrent system designed to protect crops from damage using intelligent detection and automatic repelling mechanisms.
This project combines sensor technology, microcontrollers, and automation to provide a smart and sustainable solution for farmers.
## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack & Tools](#tech-stack--tools)
- [Hardware Components](#hardware-components)
- [Installation & Setup](#installation--setup)

## 📖 About the Project
Traditional crop protection methods are either manual or ineffective against persistent threats like birds and small animals. 
**Farm Guard** aims to automate the protection mechanism using sensors and deterrent devices (buzzers, ultrasonic sensors, laser beams, etc.) for real-time detection and response.

## ✅ Features
- 🛡️ Real-time detection of intruding birds or animals
- 🔊 Sound alarms and deterrents triggered automatically
- 🌙 Day and night functionality using LDR and motion sensors
- 📡 Optional wireless alert to mobile (via IoT/MQTT)
- 🔋 Low power consumption and solar-compatible design
- 🧠 Smart control via microcontroller logic
  
## ⚙️ How It Works
1. **Detection**  
   Motion sensors (PIR/Ultrasonic) and LDR monitor the field area.
2. **Trigger Mechanism**  
   When motion is detected, and the light level is suitable, the system activates:
   - Buzzers to scare birds
   - Laser or light blinkers for deterrence
   - Spray water on crops
   - Optional mobile notification for future development(if IoT module added)
3. **Reset**  
   After a predefined delay (e.g., 5–10 seconds), the system resets and monitors again.
> The logic is coded into an Arduino/ESP8266 and connected to the circuit board.

## 🛠️ Tech Stack & Tools
- **Microcontroller:** Arduino Uno / ESP8266 NodeMCU
- **Languages:** C/C++ for Arduino, optional Python for IoT integration
- **Tools:** Arduino IDE, Fritzing (for circuit design), ThinkSpeak / Blynk (optional)

## 🧾 Hardware Components
_____________________________________________________________________
| Component           | Quantity | Purpose                          |
|---------------------|----------|----------------------------------|
| Arduino Uno / ESP   | 1        | Control unit                     |
| PIR Motion Sensor   | 1–2      | Detect animals/birds             |
| LDR Sensor          | 1        | Detect light (day/night)         |
| Buzzer              | 1        | Alert & Scare mechanism          |
| Laser Module / LED  | 1        | Visual deterrent                 |
| Jumper Wires        | As req.  | Circuit connections              |
| Breadboard / PCB    | 1        | Prototyping                      |
| Power Supply        | 1        | Battery/Solar                    |
---------------------------------------------------------------------

## 🧪 Installation & Setup
> If you're replicating the project, follow these steps:
1. **Clone this repository**  
   ```bash
   git clone https://github.com/AATHMI19/farm-guard
   cd farm-guard
2.Upload Code to Arduino
3.Open farm_guard.ino in Arduino IDE
4.Select the correct board and COM port
5.Upload the code
6.Connect the hardware as per the circuit diagram (see /circuit/ folder)
7.Test the system by simulating motion in front of sensors
(Optional IoT): Use Blynk or ThinkSpeak to monitor status or trigger alerts
