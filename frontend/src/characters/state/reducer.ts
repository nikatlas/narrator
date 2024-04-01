import { createSlice } from "@reduxjs/toolkit";
import {
  CharactersCreateFetcher,
  CharactersDeleteFetcher,
  CharactersFetcher,
  CharactersUpdateFetcher,
} from "@/characters/state/thunk";
import { fetcherInitialState } from "@/redux/fetcher";

// Define the initial state using that type
const initialState = fetcherInitialState;

export const charactersSlice = createSlice({
  name: "characters",
  // `createSlice` will infer the state type from the `initialState` argument
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    CharactersFetcher.reducers(builder);
    CharactersCreateFetcher.reducers(builder);
    CharactersDeleteFetcher.reducers(builder);
    CharactersUpdateFetcher.reducers(builder);
  },
});

export default charactersSlice.reducer;
