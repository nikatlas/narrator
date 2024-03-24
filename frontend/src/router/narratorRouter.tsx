import React, { FC, ReactNode } from "react";
import { createBrowserRouter } from "react-router-dom";

import { NarratorLayout } from "@/layout";
import { Chat } from "@/chat";
import { Characters } from "@/characters";
import "./router-object-augmentation";
import { Campaigns } from "@/campaigns";
import { Places } from "@/places";
import { Resources } from "@/resources";

export const narratorRouter = createBrowserRouter([
  {
    path: "/",
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
