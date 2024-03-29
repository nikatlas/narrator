import Fetcher, { FetcherState } from "@/redux/fetcher";
import NarratorAPI from "@/api/NarratorAPI";
import { Resource } from "@/resources/types";

const api = new NarratorAPI();

export const ResourcesFetcher = new Fetcher("resources/list", async () => {
  return api.getResources();
});

export const ResourcesCreateFetcher = new Fetcher(
  "resources/create",
  async (values: any) => {
    return api.createResource(values);
  },
  (data: any, state: FetcherState<Array<Resource>>, action) => {
    return [...(state?.data ?? []), data];
  },
);

export const ResourcesDeleteFetcher = new Fetcher(
  "resources/delete",
  async (id: number) => {
    return api.deleteResource(id);
  },
  (data: any, state: FetcherState<Array<Resource>>, action) => {
    return state.data?.filter((resource) => {
      return resource.id !== action.payload;
    });
  },
);

export const ResourcesUpdateFetcher = new Fetcher(
  "resources/update",
  async (resource: Resource) => {
    return api.updateResource(resource);
  },
  (data: any, state: FetcherState<Array<Resource>>, action) => {
    return [
      ...(state.data?.filter((resource) => {
        return resource.id !== action.payload.id;
      }) ?? []),
      data,
    ];
  },
);
