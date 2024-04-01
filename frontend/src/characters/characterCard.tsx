import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";

import CardContent from "@mui/material/CardContent";
import { Button, CardActions } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import React from "react";

interface CharacterCardProps {
  character: any;
  selected?: boolean;
  onSelect?: (character: any) => void;
  onView?: (character: any) => void;
  onEdit?: (character: any) => void;
  onDelete?: (id: number) => void;
}

const CharacterCard = ({
  character,
  selected,
  onSelect,
  onView,
  onEdit,
  onDelete,
}: CharacterCardProps) => {
  return (
    <Card
      onClick={() => onSelect?.(character)}
      sx={{
        border: selected ? "1px solid black" : "",
      }}
    >
      <CardHeader title={`${character.firstName} ${character.lastName}`} />
      <CardContent>{character.isPlayer ? "Player" : "NPC"}</CardContent>
      <CardActions sx={{ justifyContent: "flex-end" }}>
        {onView && (
          <Button
            size="small"
            onClick={(e) => {
              e.preventDefault();
              onView?.(character);
            }}
          >
            View
          </Button>
        )}
        {onEdit && (
          <Button
            size="small"
            startIcon={<EditIcon />}
            onClick={(e) => {
              e.preventDefault();
              onEdit?.(character);
            }}
          >
            Edit
          </Button>
        )}
        {onDelete && (
          <Button
            color={"error"}
            size="small"
            startIcon={<DeleteForeverIcon />}
            onClick={(e) => {
              e.preventDefault();
              onDelete?.(character.id);
            }}
          >
            Delete
          </Button>
        )}
      </CardActions>
    </Card>
  );
};

export default CharacterCard;
