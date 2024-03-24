import NarratorAPI from "../api/NarratorAPI";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Alert, Button, Grid, TextField } from "@mui/material";
import { ChatBox, ReceiverMessage, SenderMessage } from "mui-chat-box";
import Microphone from "../speechToText/microphone";
import TextToSpeech from "../textToSpeech/TextToSpeech";

const api = new NarratorAPI();
const Synthesizer = new TextToSpeech();

interface Interaction {
  id: number;
  transmitter_character: any;
  receiver_character: any;
  text: string;
  receiver: string;
  created_at: string;
}

interface MessageProps {
  interaction: Interaction;
  receiver?: boolean;
}
const Message = ({ interaction, receiver = false }: MessageProps) => {
  return receiver ? (
    <ReceiverMessage avatar={""}>{interaction.text}</ReceiverMessage>
  ) : (
    <SenderMessage avatar={""}>{interaction.text}</SenderMessage>
  );
};
const Chat = () => {
  const [interactions, setInteractions] = useState<any[]>([]);
  const [message, setMessage] = useState<string>("");
  const [error, setError] = useState<string>("");
  const { playerId, npcId } = useParams();
  const [npc, setNpc] = useState<any>({});

  useEffect(() => {
    if (!playerId || !npcId) return;
    api.getInteractions(playerId, npcId).then((response: any) => {
      setInteractions(response);
    });
  }, [playerId, npcId]);

  useEffect(() => {
    if (!playerId || !npcId) return;
    api.getCharacter(npcId).then((response: any) => {
      setNpc(response);
    });
  }, [playerId, npcId]);

  const handleSendMessage = () => {
    sendMessage(message);
  };

  const handleMicrophoneText = (text: string) => {
    setMessage(text);
    // sendMessage(text);
  };

  const handleError = (error: any) => {
    setError(error);
  };

  const handleSpeak = () => {
    speakLastInteraction(interactions);
  };

  const speakLastInteraction = (messages: Array<Interaction>) => {
    const lastInteraction = messages[messages.length - 1];
    Synthesizer.setVoice(npc?.voice);
    Synthesizer.speak(lastInteraction.text)
      .then((result) => {
        console.log(result);
      })
      .catch((error: any) => {
        setError(error);
      });
  };

  const sendMessage = (text: string) => {
    if (!playerId || !npcId || !text) return;
    api.sendMessage(playerId, npcId, text).then((response: any) => {
      setInteractions(response);
      setMessage("");
      speakLastInteraction(response);
    });
  };

  function handleClearThread() {
    if (!playerId || !npcId) return;
    api
      .clearThread(playerId, npcId)
      .then(() => api.getInteractions(playerId, npcId))
      .then((response: any) => {
        setInteractions(response);
      });
  }

  return (
    <>
      <Grid container spacing={2} justifyContent={"center"}>
        <Grid item xs>
          {error && <Alert severity={"error"}>{error}</Alert>}
        </Grid>
      </Grid>
      <Grid container justifyContent={"center"}>
        <Grid item xs={6}>
          <ChatBox>
            {interactions.map((interaction) => (
              <Message
                key={interaction.id}
                interaction={interaction}
                receiver={`${interaction.transmitter_character}` === playerId}
              />
            ))}
          </ChatBox>
        </Grid>
      </Grid>
      <Grid container justifyContent={"center"} sx={{ p: 2 }}>
        <Grid item xs={4}>
          <TextField
            fullWidth={true}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </Grid>
        <Grid item>
          <Button onClick={handleSendMessage} disabled={!message}>
            Send
          </Button>
        </Grid>
        <Grid item>
          <Microphone onText={handleMicrophoneText} onError={handleError} />
        </Grid>
        <Grid item>
          <Button onClick={handleSpeak} disabled={!interactions.length}>
            Speak
          </Button>
        </Grid>
        <Grid item>
          <Button onClick={handleClearThread} disabled={!interactions.length}>
            Clear Thread
          </Button>
        </Grid>
      </Grid>
    </>
  );
};

export default Chat;
