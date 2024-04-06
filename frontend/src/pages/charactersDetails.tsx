import { Character as ICharacter } from "@/characters/types";
import {
  useUpdateCharacters,
  useCharactersResources,
  useCharacter,
} from "@/characters/state/hooks";
import { Navigate, useParams } from "react-router-dom";
import { Resources } from "@/resources";
import { Bucket, BucketContainer } from "@/sections/bucketSection";
import Character from "@/characters/character";
import Grid from "@mui/material/Grid";
import { TextField } from "@mui/material";
import React from "react";
import { useFilteredResources } from "@/resources/state/hooks";
import SearchableResources from "@/resources/searchableResources";

const CharactersDetailPage = () => {
  const { characterId } = useParams();
  const characterIdInt = parseInt(characterId as string);
  const character = useCharacter(characterIdInt) as ICharacter;
  const [search, setSearch] = React.useState("");
  const characterResources = useCharactersResources(character, search);
  const resources = useFilteredResources(
    undefined,
    search,
    characterResources.map((r) => r.id),
  );
  const editCharacter = useUpdateCharacters();

  const handleUnlink = (id: number) => {
    editCharacter({
      ...character,
      resources: (character?.resources ?? []).filter((r) => r !== id),
    });
  };

  const handleLink = (id: number) => {
    editCharacter({
      ...character,
      resources: Array.from(
        new Set([...(character?.resources ?? []), id]).values(),
      ),
    });
  };

  const handleNewResource = (resource: any) => {
    editCharacter({
      ...character,
      resources: [...(character?.resources ?? []), resource.id],
    });
  };

  if (!character) {
    return <Navigate to={"/characters"} replace={true} />;
  }

  return (
    <BucketContainer isVertical={false}>
      <Bucket xs={12} sm={4} md={3}>
        <Character
          character={character as ICharacter}
          onSubmit={(values) => editCharacter(values)}
        />
      </Bucket>
      <Bucket item xs={12} sm={8} md={9}>
        <SearchableResources
          resourceSets={[
            {
              title: "Character Resources",
              resources: characterResources,
              onUnlink: handleUnlink,
              onNewResource: handleNewResource,
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

export default CharactersDetailPage;
