import React from "react";
import Grid from "@mui/material/Grid";
import {
  Alert,
  Button,
  Card,
  CardContent,
  CardHeader,
  Typography,
} from "@mui/material";
import { useDeleteResource, useResources } from "@/resources/state/hooks";
import NewResourceModal from "@/resources/newResourceModal";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";

const Resources = () => {
  const { data: resources, error } = useResources();
  const deleteResource = useDeleteResource();

  const handleDelete = (id: number) => {
    deleteResource(id);
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
          <Typography variant={"h4"}>Resources</Typography>
        </Grid>
        <Grid>
          <NewResourceModal />
        </Grid>
        {resources.map((resource: any) => (
          <Grid item key={resource.id}>
            <Card sx={{}}>
              <CardHeader title={`${resource.name}`} />
              <CardContent>
                <Typography>{resource.text}</Typography>
                <Typography variant={"subtitle2"}>{resource.file}</Typography>
                <Button
                  color={"error"}
                  size="small"
                  startIcon={<DeleteForeverIcon />}
                  onClick={() => handleDelete(resource.id)}
                >
                  Delete
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
};

export default Resources;
