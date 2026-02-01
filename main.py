from config import API_KEY, SCAM_KEYWORDS, SCAM_REPLIES, NORMAL_REPLIES
from fastapi import FastAPI, Header, HTTPException
import random
import re

SESSIONS = {}

PHONE_REGEX = r"\b\d{10}\b"
URL_REGEX = r"https?://[^\s]+"
UPI_REGEX = r"\b[\w.\-]+@[\w]+\b"



app = FastAPI()

@app.post("/hello")
def hello(payload: dict, x_api_key = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    print(payload)


    session_id = payload.get("sessionId")
    message = payload.get("message", {})
    sender = message.get("sender")
    text = message.get("text")
    text_lower = text.lower() if text else ""

    if session_id not in SESSIONS:
        SESSIONS[session_id] = {
            "turns": 0,
            "matched_keywords": [],
            "phones": [],
            "urls": [],
            "upi_ids": []
        }
    SESSIONS[session_id]["turns"] += 1
    print("Session turns:", SESSIONS[session_id]["turns"])



    session_data = SESSIONS[session_id]

    stop_conversation = False

    if session_data["turns"] >= 3:
         stop_conversation = True

    if session_data["phones"] or session_data["upi_ids"] or session_data["urls"]:
        stop_conversation = True


    scam_count = 0
    matched_keyword = []
    for keyword in SCAM_KEYWORDS:
      if keyword in text_lower:
         scam_count += 1
         matched_keyword.append(keyword)

    is_scam = scam_count >= 2

    print("Scam keywords found:", scam_count)
    print("Is scam:", is_scam)
    print("Session ID:", session_id)
    print("Sender:", sender)
    print("Text:", text)
    print("Matched keywords:", matched_keyword)


    phone_numbers = []
    urls = []
    upi_ids = []

    if is_scam:
        phone_numbers = re.findall(PHONE_REGEX, text_lower)
        urls = re.findall(URL_REGEX, text_lower)
        upi_ids = re.findall(UPI_REGEX, text_lower)

    print("Phones:", phone_numbers)
    print("URLs:", urls)
    print("UPI IDs:", upi_ids)
  

    SESSIONS[session_id]["matched_keywords"].extend(matched_keyword)
    SESSIONS[session_id]["phones"].extend(phone_numbers)
    SESSIONS[session_id]["urls"].extend(urls)               
    SESSIONS[session_id]["upi_ids"].extend(upi_ids)  

    print("Session state:", SESSIONS[session_id])

    
    if stop_conversation:
        reply = "Thank you. I have noted the information you provided and getting back to you shortly."
    elif is_scam:
        reply = random.choice(SCAM_REPLIES)
    else:
        reply = random.choice(NORMAL_REPLIES)

    #return {"reply": reply, "matched_keywords": matched_keyword, "is_scam": is_scam,"extracted": {"phone_numbers": phone_numbers, "urls": urls, "upi_ids": upi_ids}}
    
    return {
    "sessionId": session_id,
    "is_scam": is_scam,
    "turns": SESSIONS[session_id]["turns"],
    "stop_conversation": stop_conversation,
    "matched_keywords": matched_keyword,
    "extracted": {
        "phones": phone_numbers,
        "urls": urls,
        "upi_ids": upi_ids
    },
    "reply": reply
}

    

