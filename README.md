# 🛡️ Scam Honeypot API (Agentic AI System)

A secure, session-aware honeypot API designed to detect scam messages, safely interact with potential attackers, and extract actionable fraud intelligence.

---

## 🚀 Project Overview

This project simulates a **honeypot system** for scam detection.

Instead of simply blocking suspicious messages, the system:
- Detects scam intent
- Engages safely
- Extracts intelligence
- Maintains conversation context

---

## ⚙️ Features

- 🔐 API Key Authentication (secure access)
- 🧠 Scam Detection using rule-based logic
- 🔍 Fraud Indicator Extraction:
  - Phone numbers
  - URLs
  - UPI IDs
- 🔁 Session-based multi-turn conversation tracking
- 🎭 Honeypot-style safe responses (no sensitive data exposure)
- ⛔ Stop-condition logic to prevent infinite interaction
- 🌐 Deployed API for real-world testing

---

## 🧩 System Architecture
User Message → API Endpoint → Authentication
→ Scam Detection → Data Extraction → Session Memory
→ Honeypot Response → JSON Output


---

## 📡 API Endpoint

**POST** `/hello`

### Headers

x-api-key: YOUR_API_KEY


### Request Body
```json
{
  "sessionId": "test123",
  "message": {
    "sender": "scammer",
    "text": "Your account is blocked. Verify UPI immediately.",
    "timestamp": "now"
  }
}

```

### Sample Responce 
``` json
{
  "is_scam": true,
  "reply": "I’m not sure, can you explain more?",
  "matched_keywords": ["verify", "upi"],
  "extracted": {
    "phones": [],
    "urls": [],
    "upi_ids": []
  }
}

```

{
  "sessionId": "test123",
  "message": {
    "sender": "scammer",
    "text": "Your account is blocked. Verify UPI immediately.",
    "timestamp": "now"
  }
}

🧠 Key Concepts
Honeypot Design: Engages attackers instead of blocking immediately
Rule-based Detection: Simple, explainable logic
Session Memory: Tracks multi-turn conversations
Safe Interaction: No sensitive data is ever shared

---

⚠️ Learnings
API reliability is as important as logic
Deployment behavior affects evaluation outcomes
Strict response formats matter in automated systems
Simplicity + clarity > over-engineering

---

🔮 Future Improvements
- AI-based response generation (LLM integration)
- Advanced ML-based scam classification
- Persistent database for sessions
- Real-time dashboard for fraud analytics

---

🛠️ Tech Stack
- Python
- FastAPI
- Regex (pattern extraction)
- Render (deployment)

---


👤 Author

Adarsh Raj
