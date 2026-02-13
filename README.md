🌱 URJA NIDHI
AI-Powered Biogas & Smart Agriculture Monitoring System
🚀 Overview

URJA NIDHI is a full-stack IoT + AI system designed for real-time biogas monitoring and smart agricultural intelligence.

The system integrates:

🔌 ESP32-based sensor network

☁ Firebase Realtime Database

🧠 Machine Learning prediction pipeline

🐳 Dockerized Flask backend

🌐 Interactive frontend dashboard

It provides real-time sensor monitoring, biogas yield estimation, nutrient analysis, and intelligent agricultural insights.

🏗 System Architecture
ESP32 Sensors
     ↓
Firebase Realtime Database
     ↓
Flask Backend API (Dockerized)
     ↓
ML Prediction Engine
     ↓
Frontend Dashboard

🔌 Hardware Components

ESP32

DS18B20 (Temperature Sensor)

MQ-5 (Methane Gas Sensor)

ADS1115 ADC

pH Sensor

Pressure Sensor

📊 Features
🔥 Real-Time Monitoring

Methane concentration (PPM)

Temperature (°C)

Pressure (Voltage)

pH level

Raw + processed values

🌾 Agriculture Intelligence

NPK estimation

Crop recommendations

Weather-based insights

Fertilizer recommendation

🧠 Machine Learning

Biogas yield prediction

Energy value estimation

Smart nutrient balancing

Data-driven insights

🐳 Backend & DevOps

Flask API

Firebase Admin SDK integration

Secure service account authentication

Docker containerization

Backend-driven polling architecture

🔐 Security Design

Instead of exposing Firebase directly to the frontend:

Frontend communicates only with backend API

Backend securely connects to Firebase using Admin SDK

No Firebase credentials exposed in browser

Improved security & reliability

📁 Project Structure
Urja_Nidhi/
│
├── backend/
│   ├── app.py
│   ├── serviceAccountKey.json (not pushed to GitHub)
│
├── docker-compose.yml
├── Dockerfile
├── ML_model.pkl
├── dataset.csv
├── README.md

🐳 Running with Docker
docker-compose up --build


Application will run at:

http://localhost:5000

📡 ESP32 → Firebase Data Format
sensorData: {
  temperature: 28.5,
  methane_ppm: 1023.45,
  pressure_voltage: 1.23,
  ph_value: 6.85
}

🎯 Why This Project Matters

This project demonstrates:

IoT hardware integration

Cloud database architecture

Secure backend API design

Real-time data streaming

Machine Learning deployment

Docker-based containerization

Full-stack system integration

It is a production-ready architecture model for:

Smart agriculture systems

Biogas plants

Renewable energy monitoring

Industrial IoT platforms

🧠 Future Improvements

Historical trend graphs

Alert notification system

ML-based anomaly detection

Cloud deployment (AWS / GCP / Render)

Mobile app integration
