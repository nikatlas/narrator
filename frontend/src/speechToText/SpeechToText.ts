import {
  AudioConfig,
  ResultReason,
  SpeechConfig,
  SpeechRecognizer,
} from "microsoft-cognitiveservices-speech-sdk";

// DOCS https://github.com/Azure-Samples/AzureSpeechReactSample

class SpeechToText {
  private recognizer: SpeechRecognizer;
  constructor() {
    const SPEECH_AZURE_KEY = "5738c9014fc04c459a6e20091a7117fc";
    const SPEECH_AZURE_REGION = "westeurope";

    const speechConfig = SpeechConfig.fromSubscription(
      SPEECH_AZURE_KEY,
      SPEECH_AZURE_REGION,
    );
    speechConfig.speechRecognitionLanguage = "en-US";
    const audioConfig = AudioConfig.fromDefaultMicrophoneInput();
    this.recognizer = new SpeechRecognizer(speechConfig, audioConfig);
  }

  recognize(): Promise<string> {
    return new Promise((resolve, reject) => {
      this.recognizer.recognizeOnceAsync((result) => {
        if (result.reason === ResultReason.RecognizedSpeech) {
          resolve(result.text as string);
        } else {
          reject(result.reason);
        }
      });
    });
  }

  start() {
    this.recognizer.startContinuousRecognitionAsync();
  }

  stop() {
    this.recognizer.stopContinuousRecognitionAsync();
  }
}

export default SpeechToText;
