# 🛡️ Scam Honeypot API (Agentic AI System)

A secure, session-aware honeypot API designed to detect scam messages, safely engage with potential attackers, and extract actionable fraud intelligence.

---

## 🚀 Overview

This project implements an **agentic honeypot system** for scam detection.

Unlike traditional filters that block messages, this system:
- Detects scam intent
- Engages safely with the sender
- Extracts intelligence (phone, URL, UPI)
- Maintains multi-turn conversation context

---

## ⚙️ Features

- 🔐 **API Key Authentication** (secure access)
- 🧠 **Rule-based Scam Detection** (keyword + pattern logic)
- 🔍 **Fraud Indicator Extraction**
  - Phone numbers
  - URLs
  - UPI IDs
- 🔁 **Session-based Memory**
  - Tracks multi-turn interactions
- 🎭 **Honeypot Response Engine**
  - Generates safe, non-sensitive replies
- ⛔ **Stop Condition Logic**
  - Prevents infinite engagement
- 🌐 **Deployed Public API**

---

## 🧩 System Architecture

![Architecture Diagram]
(./images/Architecture_Diagram.png)

### Flow Explanation

1. **Message Input** – User/scammer sends message  
2. **FastAPI Endpoint** – Request received (`/hello`)  
3. **Authentication Layer** – API key validation  
4. **Scam Detection Engine** – Keyword + pattern analysis  
5. **Intelligence Extraction** – Extract phone, URL, UPI  
6. **Session Memory Manager** – Store conversation state  
7. **Honeypot Response Generator** – Create safe response  
8. **Structured JSON Output** – Return response  

---

## 📡 API Usage

### Endpoint
POST /hello


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
---
📤 Sample Response
```json
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
---

🌐 Live API
https://scam-honeypot-api-9axe.onrender.com/hello
---

📸 Screenshots
### Swagger UI (API Testing)
![Swagger UI](./images/swagger-ui.png)

### Sample API Response
![API Response](./images/api-response.png)


---

🧠 Key Concepts
Honeypot Design – Engage attackers instead of blocking
Explainable Detection – Transparent rule-based logic
Session Awareness – Multi-turn conversation tracking
Safe Interaction – No sensitive data exposure
---


⚠️ Learnings
API reliability is as important as logic
Deployment behavior affects evaluation outcomes
Strict response formats matter in automation
Simplicity and clarity outperform over-engineering
---


🔮 Future Improvements
AI-based response generation (LLMs)
Advanced ML-based scam classification
Persistent database for session storage
Real-time fraud analytics dashboard
---

🛠️ Tech Stack
Python
FastAPI
Regex (pattern extraction)
Render (deployment)
---


👤 Author

Adarsh Raj
