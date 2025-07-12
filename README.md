
# HARVIS – Personal AI Assistant

**HARVIS** (Helpful, Adaptive, Reliable Virtual Intelligent Supporter) is a lightweight, modular AI assistant designed to support your daily productivity and motivation. HARVIS runs **locally** on your machine and interacts with you through **natural voice commands** — like a helpful friend or life coach.

---

## 🧠 Features

* 🎤 **Voice-Activated** — responds to a custom wake word (“Hey HARVIS”)
* 🗣️ **Offline Speech-to-Text** using Vosk
* 💬 **Positive, Motivating Conversations**
* ⏰ **Reminders & Schedules** to help you stay on track
* 📝 **Text & Video Summarization** using lightweight LLMs
* 🚀 **App Launcher** (e.g., Notepad, YouTube)
* 🔒 **Local-First and Privacy-Friendly**

---

## 🛠️ Tech Stack

| Component     | Tool/Library                                                         |
| ------------- | -------------------------------------------------------------------- |
| Language      | Python 3.9+                                                          |
| Wake Word     | [Porcupine](https://picovoice.ai)                                    |
| STT           | [Vosk](https://alphacephei.com/vosk/)                                |
| TTS           | [Coqui TTS](https://github.com/coqui-ai/TTS)                         |
| NLP/LLM       | [Transformers](https://huggingface.co/transformers/), `spaCy`, Regex |
| Scheduling    | `schedule`, `apscheduler`                                            |
| Notifications | `plyer`                                                              |
| Audio I/O     | `PyAudio`, `sounddevice`                                             |
| Database      | `SQLite3`                                                            |
| Misc.         | `subprocess`, `threading`, `psutil`                                  |

---

## 📁 Folder Structure 

```
HARVIS/
├── harvis/
│   ├── input/              # Wake word + STT handling
│   ├── nlu/                # Intent and entity recognition
│   ├── tasks/              # Reminders, scheduling, app launcher
│   ├── llm_interface/      # Text generation and summarization
│   ├── output/             # TTS and text responses
│   ├── database/           # SQLite schemas and query logic
│   └── main.py             # Core controller
├── models/                 # Vosk & summarization models
├── config/                 # User preferences and settings
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the Repo**

   ```bash
   git clone https://github.com/yourusername/HARVIS.git
   cd HARVIS
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   .\venv\Scripts\activate       # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download Models**

   * [Vosk model (small)](https://alphacephei.com/vosk/models)
   * Lightweight LLMs from Hugging Face (e.g., `distilbart-cnn-12-6`)

5. **Run HARVIS**

   ```bash
   python harvis/main.py
   ```

---

## 🧪 Current Development Progress

| Module               | Status                   |
| -------------------- | ------------------------ |
| Wake Word Input      | 🔄 In Progress           |
| Speech-to-Text       | ✅ Working (Vosk)         |
| NLU (Intent Parsing) | 🔄 In Progress           |
| Reminders            | ⏳ Planned                |
| Summarization        | ⏳ Planned                |
| App Launcher         | ⏳ Planned                |
| TTS Output           | ✅ Working (initial test) |

---

## 🎥 Demo (Coming Soon)

HARVIS will be demonstrated in a short video showing:

* Wake word activation
* Voice commands for tasks
* Motivational dialogue
* Desktop notifications

---
