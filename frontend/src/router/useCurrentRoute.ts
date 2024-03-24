import { matchRoutes, useLocation } from "react-router-dom";
import { narratorRouter } from "@/router/narratorRouter";

const useCurrentRoute = () => {
  const location = useLocation();
  const matchedRoutes = matchRoutes(narratorRouter.routes, location);
  if (!matchedRoutes) {
    return null;
  }

  return matchedRoutes[matchedRoutes.length - 1].route;
};

export default useCurrentRoute;
