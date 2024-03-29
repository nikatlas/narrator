import { createSlice } from "@reduxjs/toolkit";
import {
  ResourcesCreateFetcher,
  ResourcesDeleteFetcher,
  ResourcesFetcher,
} from "@/resources/state/thunk";
import { fetcherInitialState } from "@/redux/fetcher";

// Define the initial state using that type
const initialState = fetcherInitialState;

export const resourcesSlice = createSlice({
  name: "resources",
  // `createSlice` will infer the state type from the `initialState` argument
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    ResourcesFetcher.reducers(builder);
    ResourcesCreateFetcher.reducers(builder);
    ResourcesDeleteFetcher.reducers(builder);
  },
});

export default resourcesSlice.reducer;
