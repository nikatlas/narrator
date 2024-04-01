import { Place } from "@/places";
import { Place as IPlace } from "@/places/types";
import {
  useUpdatePlace,
  usePlace,
  usePlaceResources,
} from "@/places/state/hooks";
import { Navigate, useParams } from "react-router-dom";
import { Grid } from "@mui/material";
import { Resources } from "@/resources";
import EditPlaceModal from "@/places/editPlaceModal";
import BucketSection, {
  Bucket,
  BucketContainer,
} from "@/sections/bucketSection";

const PlacesDetailPage = () => {
  const { placeId } = useParams();
  const placeIdInt = parseInt(placeId as string);
  const place = usePlace(placeIdInt) as IPlace;
  const placeResources = usePlaceResources(place);
  const editPlace = useUpdatePlace();

  const handleUnlink = (id: number) => {
    editPlace({
      ...place,
      resources: (place?.resources ?? []).filter((r) => r !== id),
    });
  };

  const handleNewResource = (resource: any) => {
    editPlace({
      ...place,
      resources: [...(place?.resources ?? []), resource.id],
    });
  };

  if (!place) {
    return <Navigate to={"/places"} replace={true} />;
  }

  return (
    <BucketContainer isVertical={false}>
      <Bucket xs={6}>
        <Place place={place as IPlace} />
        <EditPlaceModal place={place} showTriggerButton />
      </Bucket>
      <Bucket item xs={6}>
        <Resources
          resources={placeResources}
          error={null}
          onUnlink={handleUnlink}
          onNewResource={handleNewResource}
        />
      </Bucket>
    </BucketContainer>
  );
};

export default PlacesDetailPage;
