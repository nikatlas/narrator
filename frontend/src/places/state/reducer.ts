import { createSlice } from "@reduxjs/toolkit";
import {
  PlacesCreateFetcher,
  PlacesDeleteFetcher,
  PlacesFetcher,
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
  },
});

export default placesSlice.reducer;
