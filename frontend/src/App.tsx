import { narratorRouter } from "@/router";
import { RouterProvider } from "react-router-dom";
import React from "react";
import { Provider as ReduxProvider } from "react-redux";
import { store } from "@/redux/store";

const App = () => {
  return (
    <ReduxProvider store={store}>
      <RouterProvider router={narratorRouter} />
    </ReduxProvider>
  );
};

export default App;
