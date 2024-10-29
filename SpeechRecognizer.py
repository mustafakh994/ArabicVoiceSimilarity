import speech_recognition as sr
from sentence_transformers import SentenceTransformer, util
import pyaudio

# Function to transcribe audio from the microphone using SpeechRecognition
def transcribe_audio_from_mic():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
      print("Please speak into the microphone...")
      recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
      audio = recognizer.listen(source)  # Listen for the first phrase and extract it into audio data
  try:
      # Recognize speech using Google Web Speech API
      return recognizer.recognize_google(audio, language='ar-SA')  # 'ar-SA' for Arabic
  except sr.UnknownValueError:
      print("Sorry, I could not understand the audio")
      return ""
  except sr.RequestError:
      print("Could not request results; check your network connection")
      return ""

# Function to compute similarity using SentenceTransformer
def compute_similarity(sentence1, sentence2, model):
  embeddings1 = model.encode(sentence1, convert_to_tensor=True)
  embeddings2 = model.encode(sentence2, convert_to_tensor=True)

  similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
  return similarity.item()

# Load a pre-trained sentence similarity model
model = SentenceTransformer('sentence-transformers/paraphrase-xlm-r-multilingual-v1')

# Example usage
transcribed_text = transcribe_audio_from_mic()
print(f"Transcribed Text: {transcribed_text}")

correct_answer = "اجابة صحيحه"  # The correct answer

# Compute similarity
similarity_score = compute_similarity(transcribed_text, correct_answer, model)
print(f"Similarity Score: {similarity_score}")

# Determine if the answer is correct based on a threshold
threshold = 0.8
if similarity_score > threshold:
  print("Correct answer!")
else:
  print("Incorrect answer. Try again.")