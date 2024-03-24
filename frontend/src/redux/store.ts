import { configureStore } from "@reduxjs/toolkit";
import placesReducer from "@/places/state/reducer";

import logger from "redux-logger";

export const store = configureStore({
  reducer: {
    // campaigns: campaignsReducer,
    // characters: charactersReducer,
    places: placesReducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
});
