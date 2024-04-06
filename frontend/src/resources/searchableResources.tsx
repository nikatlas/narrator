import { Bucket, BucketContainer } from "@/sections/bucketSection";
import { TextField } from "@mui/material";
import { Resources } from "@/resources/index";
import React from "react";
import { Resource } from "./types";

interface ResourceSet {
  title: string;
  resources: Array<Resource>;
  onLink?: (id: number) => void;
  onUnlink?: (id: number) => void;
  onNewResource?: (values: any) => void;
}

interface SearchableResourcesProps {
  resourceSets: Array<ResourceSet>;
  onLink?: (id: number) => void;
  onUnlink?: (id: number) => void;
  onNewResource?: (values: any) => void;
  onSearch: (searchTerm: string) => void;
}

const SearchableResources = ({
  resourceSets,
  onLink,
  onUnlink,
  onNewResource,
  onSearch,
}: SearchableResourcesProps) => {
  return (
    <BucketContainer isVertical>
      <Bucket mt={2}>
        <TextField
          fullWidth
          label={"Search"}
          onChange={(e) => onSearch(e.target.value)}
        />
      </Bucket>
      {resourceSets.map(
        ({
          title,
          resources,
          onLink: onResourceLink,
          onUnlink: onResourceUnlink,
          onNewResource: onResourceNewResource,
        }) => (
          <Bucket>
            <Resources
              title={title}
              resources={resources}
              error={null}
              onLink={onResourceLink ?? onLink}
              onUnlink={onResourceUnlink ?? onUnlink}
              onNewResource={onResourceNewResource ?? onNewResource}
              withCreateButton={Boolean(onResourceNewResource ?? onNewResource)}
            />
          </Bucket>
        ),
      )}
    </BucketContainer>
  );
};

export default SearchableResources;
