# ArabicVoiceSimilarity

**ArabicVoiceSimilarity** is a Python-based project that combines speech recognition and natural language processing to transcribe Arabic audio input and evaluate the similarity between the transcribed text and a predefined correct answer. This project leverages the power of the SpeechRecognition library for audio transcription and the SentenceTransformer library for computing semantic similarity.

## Features

- **Real-time Speech Recognition**: Capture and transcribe Arabic speech using a microphone.
- **Semantic Similarity Evaluation**: Compare the transcribed text with a predefined correct answer to determine similarity.
- **Multilingual Model Support**: Utilizes a pre-trained multilingual model to handle diverse linguistic nuances.
- **Threshold-based Validation**: Determine the correctness of the transcribed answer based on a configurable similarity threshold.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ArabicVoiceSimilarity.git
   cd ArabicVoiceSimilarity
   ```

2. Install the required packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your microphone is set up and working.
2. Run the script to start transcribing audio input.
3. Speak into the microphone when prompted.
4. The script will transcribe your speech and compute the similarity score with the correct answer.
5. Based on the similarity score, the script will indicate whether the answer is correct.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or features.

## License

This project is licensed under the GPL-3.0 license.
