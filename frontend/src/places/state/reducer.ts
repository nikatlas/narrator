import { createSlice } from "@reduxjs/toolkit";
import {
  PlacesCreateFetcher,
  PlacesDeleteFetcher,
  PlacesFetcher,
  PlacesUpdateFetcher,
} from "@/places/state/thunk";
import { fetcherInitialState } from "@/redux/fetcher";

// Define the initial state using that type
const initialState = fetcherInitialState;

export const placesSlice = createSlice({
  name: "places",
  // `createSlice` will infer the state type from the `initialState` argument
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    PlacesFetcher.reducers(builder);
    PlacesCreateFetcher.reducers(builder);
    PlacesDeleteFetcher.reducers(builder);
    PlacesUpdateFetcher.reducers(builder);
  },
});

export default placesSlice.reducer;
