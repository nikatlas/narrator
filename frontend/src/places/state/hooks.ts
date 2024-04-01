import { useAppDispatch, useAppSelector } from "@/redux/hooks";
import { useCallback } from "react";
import {
  PlacesCreateFetcher,
  PlacesDeleteFetcher,
  PlacesFetcher,
  PlacesUpdateFetcher,
} from "@/places/state/thunk";
import { NewPlace, Place } from "@/places/types";
import { createSelector } from "@reduxjs/toolkit";
import { selectResources, selectResourcesByIds } from "@/resources/state/hooks";
import { Resource } from "@/resources/types";

export const selectPlaces = (state: any) => state.places;

export const selectPlace = createSelector(
  (state: any) => selectPlaces(state).data,
  (_: any, placeId: number) => placeId,
  (places: Array<Place>, placeId: number) =>
    places?.find((place: Place) => place.id === placeId),
);

export const usePlaces = () => {
  return useAppSelector(selectPlaces);
};

export const usePlace = (placeId: number) => {
  return useAppSelector((state) => selectPlace(state, placeId));
};

export const usePlaceResources = (place: Place) => {
  return useAppSelector((state) =>
    selectResourcesByIds(state, place.resources ?? []),
  );
};

export const useCreatePlace = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    async (payload: NewPlace) => dispatch(PlacesCreateFetcher.action(payload)),
    [dispatch],
  );
};

export const useDeletePlace = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    (id: number) => {
      dispatch(PlacesDeleteFetcher.action(id));
    },
    [dispatch],
  );
};

export const useFetchPlaces = () => {
  const dispatch = useAppDispatch();
  const { loading } = usePlaces();
  return useCallback(() => {
    if (!loading) {
      dispatch(PlacesFetcher.action());
    }
  }, [dispatch, loading]);
};

export const useUpdatePlace = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    (payload: Place) => {
      dispatch(PlacesUpdateFetcher.action(payload));
    },
    [dispatch],
  );
};
