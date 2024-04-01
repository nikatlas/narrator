import { configureStore } from "@reduxjs/toolkit";
import placesReducer from "@/places/state/reducer";
import resourcesReducer from "@/resources/state/reducer";
import charactersReducer from "@/characters/state/reducer";

import logger from "redux-logger";

export const store = configureStore({
  reducer: {
    // campaigns: campaignsReducer,
    characters: charactersReducer,
    places: placesReducer,
    resources: resourcesReducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
});
