import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
c_model = spacy.load('en_core_web_sm')
e_model = SentenceTransformer.load('all-MiniLM-L6-v2')

def cleaning_and_embedding_data(data):
  en_doc = (c_model(item['question']) for item in data)
  en_doc = list(en_doc)
  cleaned_questions = [" ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct]) for doc in en_doc]
  faq_embeddings = e_model.encode(cleaned_questions, convert_to_tensor = True)
  return faq_embeddings, cleaned_questions

def cleaning_and_embedding_userinp(text):
  doc = c_model(text)
  cleaned_text = " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
  text_embedding = e_model.encode(cleaned_text, convert_to_tensors = True)
  return text_embedding

def Question_matcher(user_inp, data, faq_embeddings):
  input_embeddings = cleaning_and_embedding_userinp(user_inp)
  cos_sim = cosine_similarity([input_embeddings], faq_embeddings.cpu().numpy())[0]
  best_idx = cos_sim.argmax()
  best_score = cos_sim[best_idx]

  if cos_sim.argmax() >= 0.3:
    return data[best_idx]['answer'], best_score
  else:
    return "Sorry try again"

import json
with open('faqs.json','r') as f:
  data = json.load(f)
user_inp = input("Question : ")
faq_embeddings, cleaned_questions = cleaning_and_embedding_data(data)
ans, score = Question_matcher(user_inp, data, faq_embeddings)
print("Answer : ",ans)
print("Similarity : ",score)

