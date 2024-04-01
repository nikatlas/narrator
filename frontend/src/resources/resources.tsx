import React from "react";
import Grid from "@mui/material/Grid";
import {
  Alert,
  Button,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  Typography,
} from "@mui/material";
import { useDeleteResource } from "@/resources/state/hooks";
import NewResourceModal from "@/resources/newResourceModal";
import LinkOffIcon from "@mui/icons-material/LinkOff";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import GroupIcon from "@mui/icons-material/Group";
import EditResourceModal from "./editResourceModal";
import { Resource } from "@/resources/types";

interface ResourcesProps {
  resources: Resource[];
  error: any;
  onUnlink?: (id: number) => void;
  onNewResource?: (resource: Resource) => void;
}

const Resources = ({
  resources,
  error,
  onUnlink,
  onNewResource,
}: ResourcesProps) => {
  const [editResource, setEditResource] = React.useState(null);
  const deleteResource = useDeleteResource();

  const handleDelete = (id: number) => {
    deleteResource(id);
  };

  function handleEdit(resource: any) {
    setEditResource(resource);
  }

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
          <NewResourceModal onNewResource={onNewResource} />
          {editResource && (
            <EditResourceModal
              resource={editResource}
              onClose={() => setEditResource(null)}
            />
          )}
        </Grid>
      </Grid>
      <Grid container spacing={2} justifyContent={"center"}>
        {resources.map((resource: any) => (
          <Grid item key={resource.id}>
            <Card sx={{ maxWidth: 300 }}>
              <CardHeader title={`${resource.name}`} />
              <CardContent>
                <Typography>{resource.text}</Typography>
                <Typography variant={"subtitle2"}>{resource.file}</Typography>
              </CardContent>
              <CardActions sx={{ justifyContent: "flex-end" }}>
                <Button
                  size="small"
                  startIcon={<GroupIcon />}
                  onClick={() => handleEdit(resource)}
                >
                  Edit
                </Button>
                {onUnlink && (
                  <Button
                    color={"error"}
                    size="small"
                    startIcon={<LinkOffIcon />}
                    onClick={() => onUnlink(resource.id)}
                  >
                    Unlink
                  </Button>
                )}
                <Button
                  color={"error"}
                  size="small"
                  startIcon={<DeleteForeverIcon />}
                  onClick={() => handleDelete(resource.id)}
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

export default Resources;
