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
import CharacterCard from "./characterCard";

interface CharactersProps {
  title?: string;
  characters: Character[];
  selectedCharacters?: Character[];
  onSelect?: (character: Character) => void;
  onView?: (character: Character) => void;
  onEdit?: (character: Character) => void;
  onDelete?: (id: number) => void;
}

const Characters = ({
  title,
  characters,
  selectedCharacters,
  onSelect,
  onView,
  onEdit,
  onDelete,
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
            <CharacterCard
              character={character}
              selected={selectedCharacters?.includes(character)}
              onSelect={() => onSelect?.(character)}
              onView={onView ? () => onView(character) : undefined}
              onEdit={onEdit ? () => onEdit(character) : undefined}
              onDelete={onDelete ? () => onDelete(character.id) : undefined}
            />
          </Grid>
        ))}
      </Grid>
    </>
  );
};

export default Characters;
