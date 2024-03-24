import "react-router";

declare module "react-router" {
  interface IndexRouteObject {
    name?: string;
  }
  interface NonIndexRouteObject {
    name?: string;
  }
}
