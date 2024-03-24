import { useEffect, useState } from "react";
import Grid from "@mui/material/Grid";
import NarratorAPI from "../api/NarratorAPI";
import {
  Alert,
  Button,
  Card,
  CardContent,
  CardHeader,
  Typography,
} from "@mui/material";
import { useNavigate } from "react-router-dom";

const api = new NarratorAPI();
const Characters = () => {
  const [characters, setCharacters] = useState<any[]>([]);
  const [selectedCharacters, setSelectedCharacters] = useState<any[]>([]);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    api.getCharacters().then((response: any) => {
      setCharacters(response);
    });
  }, []);

  const selectCharacter = (character: any) => {
    setSelectedCharacters([character, ...selectedCharacters].slice(0, 2));
  };

  const handleGoToChat = () => {
    const player = selectedCharacters.find((c) => c.is_player);
    const npc = selectedCharacters.find((c) => !c.is_player);
    if (!player || !npc) {
      setError("You must select one Player and one NPC");
      return;
    }

    navigate(`/chat/${player.id}/${npc.id}`);
  };

  return (
    <>
      <Grid container spacing={2} justifyContent={"center"}>
        <Grid item xs>
          {error && <Alert severity={"error"}>{error}</Alert>}
        </Grid>
      </Grid>

      <Grid container spacing={2} justifyContent={"center"}>
        <Grid item xs={12} textAlign={"center"} sx={{ p: 2 }}>
          <Typography variant={"h4"}>Players</Typography>
        </Grid>
        {characters
          .filter((c) => c.is_player)
          .map((character: any) => (
            <Grid item key={character.id}>
              <Card
                onClick={() => selectCharacter(character)}
                sx={{
                  border: selectedCharacters.includes(character)
                    ? "1px solid black"
                    : "",
                }}
              >
                <CardHeader
                  title={`${character.first_name} ${character.last_name}`}
                />
                <CardContent>
                  {character.is_player ? "Player" : "NPC"}
                </CardContent>
              </Card>
            </Grid>
          ))}
      </Grid>
      <Grid container spacing={2} justifyContent={"center"} sx={{ p: 2 }}>
        <Grid item xs={12} textAlign={"center"}>
          <Typography variant={"h4"}>Characters</Typography>
        </Grid>
        {characters
          .filter((c) => !c.is_player)
          .map((character: any) => (
            <Grid item key={character.id}>
              <Card
                onClick={() => selectCharacter(character)}
                sx={{
                  border: selectedCharacters.includes(character)
                    ? "1px solid black"
                    : "",
                }}
              >
                <CardHeader
                  title={`${character.first_name} ${character.last_name}`}
                />
                <CardContent>
                  {character.is_player ? "Player" : "NPC"}
                </CardContent>
              </Card>
            </Grid>
          ))}
      </Grid>
      <Grid container justifyContent={"center"} sx={{ p: 4 }}>
        <Grid item>
          <Button onClick={handleGoToChat}>Chat</Button>
          <Button onClick={() => setSelectedCharacters([])}>Clear</Button>
        </Grid>
      </Grid>
    </>
  );
};

export default Characters;
