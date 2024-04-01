import { narratorRouter } from "@/router";
import { RouterProvider } from "react-router-dom";
import React from "react";
import { Provider as ReduxProvider } from "react-redux";
import { store } from "@/redux/store";
import { Toaster } from "react-hot-toast";

const App = () => {
  return (
    <ReduxProvider store={store}>
      <Toaster position="top-center" reverseOrder={false} />
      <RouterProvider router={narratorRouter} />
    </ReduxProvider>
  );
};

export default App;
