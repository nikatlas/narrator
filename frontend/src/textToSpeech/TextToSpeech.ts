import {
  ResultReason,
  SpeechConfig,
  SpeechSynthesizer,
} from "microsoft-cognitiveservices-speech-sdk";

class TextToSpeech {
  private speechConfig: SpeechConfig;

  constructor() {
    const SPEECH_AZURE_KEY = "5738c9014fc04c459a6e20091a7117fc";
    const SPEECH_AZURE_REGION = "westeurope";
    this.speechConfig = SpeechConfig.fromSubscription(
      SPEECH_AZURE_KEY,
      SPEECH_AZURE_REGION,
    );
  }

  speak(text: string) {
    return new Promise((resolve, reject) => {
      const synthesizer = new SpeechSynthesizer(this.speechConfig);
      synthesizer.speakTextAsync(
        text,
        (result) => {
          if (result.reason === ResultReason.SynthesizingAudioCompleted) {
            resolve(result);
          } else if (result.reason === ResultReason.Canceled) {
            reject(result.errorDetails);
          }
          synthesizer.close();
        },
        (err) => {
          reject(err);
          synthesizer.close();
        },
      );
    });
  }

  setVoice(voice?: string) {
    if (voice) {
      this.speechConfig.speechSynthesisVoiceName = voice;
    } else {
      this.speechConfig.speechSynthesisVoiceName = "en-US-AriaNeural";
    }
  }
}

export default TextToSpeech;
