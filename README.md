# Industrial Fault Monitoring System

An Arduino UNO-based Industrial Fault Monitoring System designed to continuously monitor industrial equipment by detecting abnormal operating conditions such as overcurrent, excessive vibration, overheating, and gas leakage. The system provides real-time fault indication through an LCD display, buzzer, relay-controlled motor shutdown, and a Streamlit-based monitoring dashboard.

---

## Project Overview

Industrial machines are susceptible to faults that can lead to equipment damage, production downtime, and safety hazards. This project demonstrates a low-cost monitoring system capable of identifying multiple fault conditions using different sensors and alerting the operator before severe damage occurs.

---

## Key Features

- Real-time industrial fault monitoring
- Overcurrent detection using ACS712
- Vibration monitoring using SW-420
- Temperature monitoring using LM35
- Gas leakage detection using MQ-2
- LCD display for live system status
- Relay-based motor protection
- Audible fault indication using buzzer
- Streamlit dashboard for sensor monitoring

---

## Hardware Components

| Component | Purpose |
|-----------|---------|
| Arduino UNO | Main Controller |
| LM35 | Temperature Measurement |
| ACS712 5A | Current Measurement |
| SW-420 | Vibration Detection |
| MQ-2 | Gas Leakage Detection |
| 16×2 LCD (I2C) | Status Display |
| 5V Relay Module | Motor Protection |
| Buzzer | Fault Alarm |
| DC Motor | Industrial Machine Prototype |
| 9V Battery | Motor Supply |

---

## Software Used

- Arduino IDE
- Python
- Streamlit
- Serial Communication

---

## System Working

1. Arduino continuously reads all sensor values.
2. Sensor readings are compared with predefined threshold values.
3. If a fault is detected:
   - LCD displays the fault message.
   - Buzzer generates an alert.
   - Relay disconnects the motor to prevent damage.
4. Sensor data can also be monitored through the Streamlit dashboard.

---

## Block Diagram & circuit diagram

<img width="1536" height="1024" alt="prjct imge" src="https://github.com/user-attachments/assets/9dff486e-80c6-45bc-b9b2-83f37bd7bedf" />

## Hardware Prototype

<img width="706" height="1045" alt="hardware setup" src="https://github.com/user-attachments/assets/ed772bde-b040-4eca-8fbf-34acb9158559" />

## Streamlit Dashboard

<img width="1898" height="903" alt="Screenshot_8-7-2026_181850_localhost" src="https://github.com/user-attachments/assets/0e19aeb9-c972-49aa-a1a1-9b62958efec3" />
<img width="1895" height="910" alt="Screenshot_8-7-2026_171938_localhost" src="https://github.com/user-attachments/assets/9268f33b-5842-4e2a-a857-37b44a317d34" />

## Project Structure

```
Industrial-Fault-Monitoring-System
│
├── Arduino_Code
├── Dashboard
├── Images
├── Documentation
└── README.md
```

---

## Future Improvements

- IoT-based remote monitoring
- Cloud data storage
- Email/SMS fault notifications
- Predictive maintenance using Machine Learning
- Mobile application integration

---

## Team Members

- Khushal Parmar
- Raxit Rangani
- Patel Nikhil
- Akhunki Abdullah

## License

This project is developed for educational and academic purposes.
