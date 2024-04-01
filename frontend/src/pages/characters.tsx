import { useCharacters } from "@/characters/state/hooks";
import { Bucket, BucketContainer } from "@/sections/bucketSection";
import { Alert, Button } from "@mui/material";
import { Characters } from "@/characters";
import Grid from "@mui/material/Grid";
import { Character } from "@/characters/types";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const CharactersPage = () => {
  const { data: characters, error: charactersError } = useCharacters();
  const [error, setError] = useState<string | null>(null);
  const [selectedPlayer, setSelectedPlayer] = useState<Character | null>(null);
  const [selectedNpc, setSelectedNpc] = useState<Character | null>(null);
  //
  const navigate = useNavigate();
  const handleGoToChat = () => {
    if (!selectedPlayer || !selectedNpc) {
      setError("You must select one Player and one NPC");
      return;
    }

    navigate(`/chat/${selectedPlayer.id}/${selectedNpc.id}`);
  };

  return (
    <BucketContainer isVertical={true}>
      {charactersError && (
        <Bucket>
          <Alert severity={"error"}>{charactersError}</Alert>
        </Bucket>
      )}
      {error && (
        <Bucket>
          <Alert severity={"warning"}>{error}</Alert>
        </Bucket>
      )}
      <Bucket>
        <Grid container justifyContent={"center"} sx={{ p: 4 }}>
          <Grid item>
            <Button onClick={handleGoToChat}>Chat</Button>
            <Button
              onClick={() => {
                setSelectedNpc(null);
                setSelectedPlayer(null);
              }}
            >
              Clear
            </Button>
          </Grid>
        </Grid>
      </Bucket>
      <Bucket>
        <BucketContainer isVertical={false}>
          <Bucket xs={6}>
            <Characters
              title={"Players"}
              characters={characters.filter((c: Character) => c.isPlayer)}
              onSelect={(character: Character) => setSelectedPlayer(character)}
              selectedCharacters={selectedPlayer ? [selectedPlayer] : []}
            />
          </Bucket>
          <Bucket xs={6}>
            <Characters
              title={"NPCs"}
              characters={characters.filter((c: Character) => !c.isPlayer)}
              onSelect={(character: Character) => setSelectedNpc(character)}
              selectedCharacters={selectedNpc ? [selectedNpc] : []}
            />
          </Bucket>
        </BucketContainer>
      </Bucket>
    </BucketContainer>
  );
};

export default CharactersPage;
