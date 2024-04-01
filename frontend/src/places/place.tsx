import { Alert, Grid, Typography } from "@mui/material";
import { Place as IPlace } from "@/places/types";
import React from "react";

interface PlaceProps {
  place: IPlace;
}

const Place = ({ place }: PlaceProps) => {
  return (
    <>
      <Grid container>
        <Grid item xs={12} textAlign={"center"} sx={{ p: 2 }}>
          <Typography variant={"h4"}>{place.name}</Typography>
        </Grid>
        <Grid item xs={12}>
          <p>{place?.name}</p>
          <p>{place?.description}</p>
        </Grid>
      </Grid>
    </>
  );
};

export default Place;
