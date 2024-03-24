import KeyboardVoiceIcon from "@mui/icons-material/KeyboardVoice";
import { IconButton } from "@mui/material";
import SpeechToText from "./SpeechToText";

const Recognizer: SpeechToText = new SpeechToText();

interface MicrophoneProps {
  onText: (text: string) => void;
  onError: (error: any) => void;
}

const Microphone = ({ onText, onError }: MicrophoneProps) => {
  const handleRecord = () => {
    Recognizer.recognize()
      .then((text: string) => {
        onText(text);
      })
      .catch((error: any) => {
        onError(error);
      });
  };

  return (
    <IconButton color="primary" onClick={handleRecord}>
      <KeyboardVoiceIcon />
    </IconButton>
  );
};

export default Microphone;
