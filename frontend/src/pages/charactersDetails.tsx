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

const CharactersDetailPage = () => {
  const { characterId } = useParams();
  const characterIdInt = parseInt(characterId as string);
  const character = useCharacter(characterIdInt) as ICharacter;
  const characterResources = useCharactersResources(character);
  const editCharacter = useUpdateCharacters();

  const handleUnlink = (id: number) => {
    editCharacter({
      ...character,
      resources: (character?.resources ?? []).filter((r) => r !== id),
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
      <Bucket xs={6}>
        <Character
          character={character as ICharacter}
          onSubmit={(values) => editCharacter(values)}
        />
      </Bucket>
      <Bucket item xs={6}>
        <Resources
          resources={characterResources}
          error={null}
          onUnlink={handleUnlink}
          onNewResource={handleNewResource}
        />
      </Bucket>
    </BucketContainer>
  );
};

export default CharactersDetailPage;
