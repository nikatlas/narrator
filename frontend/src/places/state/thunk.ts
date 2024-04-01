import Fetcher, { FetcherState } from "@/redux/fetcher";
import NarratorAPI from "@/api/NarratorAPI";
import { Place } from "@/places/types";
import { Resource } from "@/resources/types";

const api = new NarratorAPI();

export const PlacesFetcher = new Fetcher("places/list", async () => {
  return api.getPlaces();
});

export const PlacesCreateFetcher = new Fetcher(
  "places/create",
  async (values: any) => {
    return api.createPlace(values);
  },
  (data: any, state: FetcherState<Array<Place>>, action) => {
    return [...(state?.data ?? []), data];
  },
);

export const PlacesDeleteFetcher = new Fetcher(
  "places/delete",
  async (id: number) => {
    return api.deletePlace(id);
  },
  (data: any, state: FetcherState<Array<Place>>, action) => {
    return state.data?.filter((place) => {
      return place.id !== action.payload;
    });
  },
);

export const PlacesUpdateFetcher = new Fetcher(
  "places/update",
  async (place: Place) => {
    return api.updatePlace(place);
  },
  (data: any, state: FetcherState<Array<Place>>, action) => {
    return [
      ...(state.data?.filter((place) => {
        return place.id !== action.payload.id;
      }) ?? []),
      data,
    ];
  },
);
