# 🎮 Discord Rich Presence – Custom Status

This project lets you display a **custom Discord Rich Presence** from Python.  
It shows a game-like status such as **Playing CS2 – Competitive Mirage** with an elapsed timer and custom icon.

---

## 📦 Requirements
- **Python 3.8+**
- [Discord Desktop App](https://discord.com/download) running on your PC
- A Discord **Application ID** (from [Discord Developer Portal](https://discord.com/developers/applications))

---

## ⚙️ Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a **New Application**.
3. Copy your **Application (Client) ID** and replace it inside `p.py`:
   ```python
   client_id = "YOUR_APP_ID"
   ```
4. (Optional) Upload an image in **Rich Presence → Art Assets** with the key `cs2`.

---

## 📥 Installation

Clone or download this repository, then install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running

Run the script:

```bash
python p.py
```

It will set your Discord presence to:

- **Details:** Playing CS2  
- **State:** Competitive – Mirage  
- **Large Image:** `cs2`  
- **Large Text:** Counter-Strike 2  
- **Elapsed Time:** Shows how long you’ve been “playing”  

---
For Discord Rich Presence you upload the image to your Discord Application in the Developer Portal.
- Go to your app in the Developer Portal.
- In the left sidebar, open Rich Presence → Art Assets.
- Upload your image there (e.g., a CS2 logo).
- Give it a key name (for example: cs2).

In the script, we reference it like this:
```
"large_image": "cs2",
"large_text": "Counter-Strike 2",
```
---

## 🖼️ Example

```
Playing CS2
Competitive – Mirage
⏱️ 00:35 elapsed
```

---

## 🔧 Notes
- The bold app name (e.g., `botop`) comes from the **application name** in the Developer Portal. Change it there to rename it.  
- Images must be uploaded in the **Art Assets** section of your application.

---
