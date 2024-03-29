import React from "react";
import Grid from "@mui/material/Grid";
import GroupIcon from "@mui/icons-material/Group";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import {
  Alert,
  Button,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  Typography,
} from "@mui/material";
import NewPlaceModal from "./newPlaceModal";
import { useDeletePlace, usePlaces } from "@/places/state/hooks";

const Places = () => {
  const { data: places, error } = usePlaces();
  const deletePlace = useDeletePlace();

  const handleDelete = (id: number) => {
    deletePlace(id);
  };

  return (
    <>
      <Grid container spacing={2} justifyContent={"center"}>
        <Grid item xs>
          {error && <Alert severity={"error"}>{error.message}</Alert>}
        </Grid>
      </Grid>

      <Grid container spacing={2} justifyContent={"center"}>
        <Grid item xs={12} textAlign={"center"} sx={{ p: 2 }}>
          <Typography variant={"h4"}>Places</Typography>
        </Grid>
        <Grid item xs={12} textAlign={"right"}>
          <NewPlaceModal />
        </Grid>
        {places.map((place: any) => (
          <Grid item key={place.id}>
            <Card sx={{}}>
              <CardHeader title={place.name} />
              <CardContent>{place.description}</CardContent>
              <CardActions sx={{ justifyContent: "flex-end" }}>
                <Button size="small" startIcon={<GroupIcon />}>
                  Edit
                </Button>
                <Button
                  color={"error"}
                  size="small"
                  startIcon={<DeleteForeverIcon />}
                  onClick={() => handleDelete(place.id)}
                >
                  Delete
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
};

export default Places;
