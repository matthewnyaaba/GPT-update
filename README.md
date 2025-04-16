Link: https://gpt-update.onrender.com/
# 🌍 GenAI-ERA Multimodal Assistant

A ChatGPT-inspired web assistant powered by GPT-4o that supports:
- ✅ Text chat with GPT-4o
- 🎙️ Speech-to-text and 🗣️ Text-to-speech
- 📂 File upload (text, PDF, CSV) for content analysis
- 🖼️ Image generation from text prompts
- 🌐 Language translation
- 💡 Reasoning tasks and intelligent summaries

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/GPT-40_MyGPT.git
   cd GPT-40_MyGPT
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key** in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key
   ```

4. **Run the Flask app**:
   ```bash
   python app.py
   ```

## 🧠 How It Uses GPT-4o

- `gpt-4o` is used via the OpenAI API for:
  - Text input/output
  - Multimodal reasoning
  - Language translation
  - Image generation (via DALL·E endpoint)
  - Audio transcription (Whisper)

## 📸 Screenshot

![screenshot](screenshot.png)
