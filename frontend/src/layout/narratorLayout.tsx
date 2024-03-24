import { Link, Outlet } from "react-router-dom";
import React from "react";
import { NarratorDrawer } from "@/menu";

function NarratorLayout() {
  return (
    <NarratorDrawer>
      <Outlet />
    </NarratorDrawer>
  );
}

export default NarratorLayout;
