import React from "react";
import { createBrowserRouter } from "react-router-dom";

import { NarratorLayout } from "@/layout";
import { Chat } from "@/chat";
import { Characters } from "@/characters";
import "./router-object-augmentation";
import { Campaigns } from "@/campaigns";
import { Places } from "@/places";
import { Resources } from "@/resources";
import { store } from "@/redux/store";
import { PlacesFetcher } from "@/places/state/thunk";
import { ResourcesFetcher } from "@/resources/state/thunk";

const dataLoader = () => {
  const promises = [
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
        element: <Characters />,
      },
      {
        name: "Places",
        path: "places",
        element: <Places />,
      },
      {
        name: "Resources",
        path: "resources",
        element: <Resources />,
      },
      {
        name: "Chat",
        path: "chat/:playerId/:npcId",
        element: <Chat />,
      },
    ],
  },
]);
