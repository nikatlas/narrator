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
import { useDeletePlace } from "@/places/state/hooks";
import { Place } from "@/places/types";
import { Link } from "react-router-dom";
import EditPlaceModal from "./editPlaceModal";
import EditIcon from "@mui/icons-material/Edit";

interface PlacesProps {
  places: Place[];
  error: any;
}

const Places = ({ places, error }: PlacesProps) => {
  const [editPlace, setEditPlace] = React.useState<Place | null>(null);
  const deletePlace = useDeletePlace();

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
          {editPlace && (
            <EditPlaceModal
              place={editPlace}
              onClose={() => setEditPlace(null)}
            />
          )}
        </Grid>
        {places.map((place: any) => (
          <Grid item key={place.id}>
            <Link to={`${place.id}`} style={{ textDecoration: "none" }}>
              <Card sx={{}}>
                <CardHeader title={place.name} />
                <CardContent>{place.description}</CardContent>
                <CardActions sx={{ justifyContent: "flex-end" }}>
                  <Button
                    size="small"
                    startIcon={<EditIcon />}
                    onClick={(e) => {
                      e.preventDefault();
                      setEditPlace(place);
                    }}
                  >
                    Edit
                  </Button>
                  <Button
                    color={"error"}
                    size="small"
                    startIcon={<DeleteForeverIcon />}
                    onClick={(e) => {
                      e.preventDefault();
                      deletePlace(place.id);
                    }}
                  >
                    Delete
                  </Button>
                </CardActions>
              </Card>
            </Link>
          </Grid>
        ))}
      </Grid>
    </>
  );
};

export default Places;
