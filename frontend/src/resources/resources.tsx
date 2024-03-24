import { useEffect, useState } from "react";
import Grid from "@mui/material/Grid";
import AddIcon from "@mui/icons-material/Add";
import NarratorAPI from "../api/NarratorAPI";
import {
  Alert,
  Button,
  Card,
  CardContent,
  CardHeader,
  Typography,
} from "@mui/material";

const api = new NarratorAPI();
const Resources = () => {
  const [campaigns, setCampaigns] = useState<any[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    api
      .getCampaigns()
      .then((response: any) => {
        setCampaigns(response);
      })
      .catch((error) => {
        setError(error.message);
      });
  }, []);

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
          <Button variant="outlined" startIcon={<AddIcon />}>
            New resource
          </Button>
        </Grid>
        {campaigns.map((campaign: any) => (
          <Grid item key={campaign.id}>
            <Card sx={{}}>
              <CardHeader
                title={`${campaign.first_name} ${campaign.last_name}`}
              />
              <CardContent>{campaign.is_player ? "Player" : "NPC"}</CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
};

export default Resources;
