import { Place } from "@/places";
import { Place as IPlace } from "@/places/types";
import {
  useUpdatePlace,
  usePlace,
  usePlaceResources,
} from "@/places/state/hooks";
import { Navigate, useParams } from "react-router-dom";
import { Box, Grid } from "@mui/material";
import { Resources } from "@/resources";
import EditPlaceModal from "@/places/editPlaceModal";
import BucketSection, {
  Bucket,
  BucketContainer,
} from "@/sections/bucketSection";
import SearchableResources from "@/resources/searchableResources";
import React from "react";
import { useCharactersResources } from "@/characters/state/hooks";
import { useFilteredResources } from "@/resources/state/hooks";

const PlacesDetailPage = () => {
  const { placeId } = useParams();
  const placeIdInt = parseInt(placeId as string);
  const place = usePlace(placeIdInt) as IPlace;
  const [search, setSearch] = React.useState("");
  const placeResources = usePlaceResources(place, search);
  const resources = useFilteredResources(
    undefined,
    search,
    placeResources.map((r) => r.id),
  );
  const editPlace = useUpdatePlace();

  const handleUnlink = (id: number) => {
    editPlace({
      ...place,
      resources: (place?.resources ?? []).filter((r) => r !== id),
    });
  };

  const handleLink = (id: number) => {
    editPlace({
      ...place,
      resources: Array.from(
        new Set([...(place?.resources ?? []), id]).values(),
      ),
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
      <Bucket xs={5}>
        <Place place={place as IPlace} onSubmit={editPlace} />
      </Bucket>
      <Bucket xs={7}>
        <SearchableResources
          resourceSets={[
            {
              title: "Place resources",
              resources: placeResources,
              onNewResource: handleNewResource,
              onUnlink: handleUnlink,
            },
            {
              title: "All resources",
              resources: resources,
              onLink: handleLink,
            },
          ]}
          onSearch={setSearch}
        />
      </Bucket>
    </BucketContainer>
  );
};

export default PlacesDetailPage;
