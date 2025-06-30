# CodeAlpha_ChatbotforFAQ
# 🤖 AI FAQ Chatbot with Spacy & Sentence Transformers

A simple chatbot that answers frequently asked questions about Artificial Intelligence using text embeddings and cosine similarity.

---

## 📚 About

This chatbot uses:
- spaCy for tokenization, cleaning, and lemmatization  
- Sentence Transformers for sentence embeddings  
- Cosine similarity to match user input with the closest FAQ  
- A JSON file (`faqs.json`) to store 20 common AI questions and answers  

---

## 🧠 FAQ Dataset Format

The data is saved in a file called `faqs.json` as a list of dictionaries:

Each entry looks like:
- question: the user's question
- answer: the correct AI-related answer

---

## 🔌 Installation

Make sure you have Python 3.7+ installed. Then run:

```
pip install spacy sentence-transformers scikit-learn
python -m spacy download en_core_web_sm
```

---

## 📂 Project Structure

- `faqs.json` — AI FAQs data (20 entries)  
- `chatbot_for_faq's.py` — main chatbot logic  
- `README.md` — documentation file  

---

## 🛠 How It Works

1. Loads and parses FAQs from a JSON file  
2. Uses spaCy to clean, lemmatize, and remove stop words  
3. Embeds both the cleaned questions and user input using a Sentence Transformer  
4. Compares input vs FAQ questions using cosine similarity  
5. Returns the most relevant answer if the score exceeds 0.3  

---

## 🧪 Sample Run

You type:
```
What is deep learning?
```

Bot searches the embeddings and replies:
```
"Deep Learning is a type of ML based on artificial neural networks with multiple layers, used for complex tasks like image and speech recognition."
```

Similarity Score: 0.91 ✅

---

## ⚙️ Improvement Ideas

- Add more diverse and domain-specific questions  
- Include follow-up questioning (contextual memory)  
- Build a web UI using Streamlit or Gradio  
- Store and embed answers as well for better ranking  

---

## 👩‍💻 Author

Built by Vivek — for learning, demos, and practical AI use-cases.  
If you like it, star it ⭐ or fork it!  
For any feedback, just raise an issue or ping me.
