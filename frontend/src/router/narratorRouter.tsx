import React from "react";
import { createBrowserRouter } from "react-router-dom";

import { NarratorLayout } from "@/layout";
import { Chat } from "@/chat";
import { Characters } from "@/characters";
import "./router-object-augmentation";
import { Campaigns } from "@/campaigns";
import { store } from "@/redux/store";
import { CharactersFetcher } from "@/characters/state/thunk";
import { PlacesFetcher } from "@/places/state/thunk";
import { ResourcesFetcher } from "@/resources/state/thunk";
import { PlacesPage, ResourcesPage } from "@/pages";
import PlacesDetailPage from "@/pages/placesDetails";
import CharactersPage from "@/pages/characters";
import CharactersDetailPage from "@/pages/charactersDetails";

const dataLoader = () => {
  const promises = [
    store.dispatch(CharactersFetcher.action()),
    store.dispatch(PlacesFetcher.action()),
    store.dispatch(ResourcesFetcher.action()),
  ];

  return Promise.all(promises);
};

export const narratorRouter = createBrowserRouter([
  {
    path: "/",
    loader: dataLoader,
    name: "Dashboard",
    element: <NarratorLayout />,
    children: [
      {
        name: "Campaigns",
        path: "campaigns",
        element: <Campaigns />,
      },
      {
        name: "Characters",
        path: "characters",
        children: [
          {
            index: true,
            name: "Characters",
            element: <CharactersPage />,
          },
          {
            name: "Character Details",
            path: ":characterId",
            element: <CharactersDetailPage />,
          },
        ],
      },
      {
        path: "places",
        children: [
          {
            index: true,
            name: "Places",
            element: <PlacesPage />,
          },
          {
            name: "Place Details",
            path: ":placeId",
            element: <PlacesDetailPage />,
          },
        ],
      },
      {
        name: "Resources",
        path: "resources",
        element: <ResourcesPage />,
      },
      {
        name: "Chat",
        path: "chat/:playerId/:npcId",
        element: <Chat />,
      },
    ],
  },
]);
