import { useAppDispatch, useAppSelector } from "@/redux/hooks";
import { useCallback } from "react";
import {
  CharactersCreateFetcher,
  CharactersDeleteFetcher,
  CharactersFetcher,
  CharactersUpdateFetcher,
} from "@/characters/state/thunk";
import { NewCharacter, Character } from "@/characters/types";
import { createSelector } from "@reduxjs/toolkit";
import { selectResources, selectResourcesByIds } from "@/resources/state/hooks";
import { Resource } from "@/resources/types";
import toast from "react-hot-toast";

export const selectCharacters = (state: any) => state.characters;

export const selectCharacter = createSelector(
  (state: any) => selectCharacters(state).data,
  (_: any, characterId: number) => characterId,
  (characters: Array<Character>, characterId: number) =>
    characters?.find((character: Character) => character.id === characterId),
);

export const useCharacters = () => {
  return useAppSelector(selectCharacters);
};

export const useCharacter = (characterId: number) => {
  return useAppSelector((state) => selectCharacter(state, characterId));
};

export const useCharactersResources = (character: Character) => {
  return useAppSelector((state) =>
    selectResourcesByIds(state, character.resources ?? []),
  );
};

export const useCreateCharacters = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    async (payload: NewCharacter) =>
      toast.promise(dispatch(CharactersCreateFetcher.action(payload)), {
        loading: "Saving...",
        success: <b>Character saved!</b>,
        error: <b>{"Could not save character :("}</b>,
      }),
    [dispatch],
  );
};

export const useDeleteCharacters = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    async (id: number) => {
      return toast.promise(dispatch(CharactersDeleteFetcher.action(id)), {
        loading: "Deleting character...",
        success: <b>Character deleted!</b>,
        error: <b>{"Could not delete character :("}</b>,
      });
    },
    [dispatch],
  );
};

export const useFetchCharacters = () => {
  const dispatch = useAppDispatch();
  const { loading } = useCharacters();
  return useCallback(() => {
    if (!loading) {
      dispatch(CharactersFetcher.action());
    }
  }, [dispatch, loading]);
};

export const useUpdateCharacters = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    async (payload: Character) => {
      return toast.promise(dispatch(CharactersUpdateFetcher.action(payload)), {
        loading: "Saving...",
        success: <b>Character saved!</b>,
        error: <b>{"Could not save character :("}</b>,
      });
    },
    [dispatch],
  );
};
