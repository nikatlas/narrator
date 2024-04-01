import Fetcher, { FetcherState } from "@/redux/fetcher";
import NarratorAPI from "@/api/NarratorAPI";
import { Character } from "@/characters/types";
import { Resource } from "@/resources/types";

const api = new NarratorAPI();

export const CharactersFetcher = new Fetcher("characters/list", async () => {
  return api.getCharacters();
});

export const CharactersCreateFetcher = new Fetcher(
  "characters/create",
  async (values: any) => {
    return api.createCharacter(values);
  },
  (data: any, state: FetcherState<Array<Character>>, action) => {
    return [...(state?.data ?? []), data];
  },
);

export const CharactersDeleteFetcher = new Fetcher(
  "characters/delete",
  async (id: number) => {
    return api.deleteCharacter(id);
  },
  (data: any, state: FetcherState<Array<Character>>, action) => {
    return state.data?.filter((character) => {
      return character.id !== action.payload;
    });
  },
);

export const CharactersUpdateFetcher = new Fetcher(
  "characters/update",
  async (character: Character) => {
    return api.updateCharacter(character);
  },
  (data: any, state: FetcherState<Array<Character>>, action) => {
    return [
      ...(state.data?.filter((character) => {
        return character.id !== action.payload.id;
      }) ?? []),
      data,
    ];
  },
);
