import { useState } from "react";
import Grid from "@mui/material/Grid";
import {
  Button,
  Card,
  CardContent,
  CardHeader,
  Typography,
} from "@mui/material";
import { Character } from "@/characters/types";

interface CharactersProps {
  title?: string;
  characters: Character[];
  onSelect?: (character: Character) => void;
  selectedCharacters?: Character[];
}

const Characters = ({
  title,
  characters,
  onSelect,
  selectedCharacters,
}: CharactersProps) => {
  return (
    <>
      <Grid container spacing={2} justifyContent={"center"}>
        {title && (
          <Grid item xs={12} textAlign={"center"} sx={{ p: 2 }}>
            <Typography variant={"h4"}>{title}</Typography>
          </Grid>
        )}
        {characters.map((character: any) => (
          <Grid item key={character.id}>
            <Card
              onClick={() => onSelect?.(character)}
              sx={{
                border: selectedCharacters?.includes(character)
                  ? "1px solid black"
                  : "",
              }}
            >
              <CardHeader
                title={`${character.firstName} ${character.lastName}`}
              />
              <CardContent>{character.isPlayer ? "Player" : "NPC"}</CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
};

export default Characters;
