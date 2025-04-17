# 🔐 AI-Enhanced Threat Detection
Real-time AI-powered threat detection for Wi-Fi networks using ML and packet sniffing.

## 🚀 Features
- 🔎 Real-Time Packet Sniffing: Monitors live network traffic using Scapy.
- 🧠 AI-Based Threat Detection: Detects anomalies and known attacks using trained ML models.
- ⚠️ User Notifications: Notifies users in real-time via a Streamlit dashboard.
- 📊 Visual Dashboard: Interactive interface built with Streamlit for live monitoring and analysis.

## 📁 Project Structure
```
AI-ENHANCED-THREAT-DETECTION/
├── backend/              # Feature extraction, real-time sniffing
├── frontend/             # Streamlit dashboard
├── models/               # Trained models, scalers, feature selectors
├── requirements.txt      # All dependencies
└── README.md             # Project documentation
```

## 🧰 Installation
### ✅ Prerequisites
- Python 3.x  
- Streamlit  
- Scikit-learn  
- Scapy  

### 🛠️ Setup
Run the following commands on the terminal:
```bash
# Clone the repository
git clone https://github.com/Shafia-01/AI-ENHANCED-THREAT-DETECTION.git
cd AI-ENHANCED-THREAT-DETECTION

# Install required packages
pip install -r requirements.txt

# Run the Streamlit dashboard
cd frontend
streamlit run main.py
```

### ⚙️ How It Works
- Packet Sniffing: Captures live traffic from your network interface.
- Feature Extraction: Converts raw packets into structured features for the ML model.
- Threat Detection: Classifies network traffic as benign or malicious using a trained model.
- Notification: Displays detected threats on the Streamlit dashboard in real time.

### 🌐 Deployment Use Cases
- 🏠 Home Wi-Fi monitoring  
- 🏫 College/university campus networks  
- ☕ Public networks like cafés or libraries  

### 📄 License
This project is licensed under the MIT License.
