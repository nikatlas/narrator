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
import toast from "react-hot-toast";
import { CharactersCreateFetcher } from "@/characters/state/thunk";

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

export const usePlaceResources = (place: Place, search?: string) => {
  return useAppSelector((state) =>
    selectResourcesByIds(state, place.resources ?? [], search),
  );
};

export const useCreatePlace = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    async (payload: NewPlace) => {
      const action = dispatch(PlacesCreateFetcher.action(payload));
      toast.promise(action, {
        loading: "Saving...",
        success: <b>Place created!</b>,
        error: <b>{"Could not save place :("}</b>,
      });
      return action;
    },
    [dispatch],
  );
};

export const useDeletePlace = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    async (id: number) => {
      const action = dispatch(PlacesDeleteFetcher.action(id));
      toast.promise(action, {
        loading: "Deleting...",
        success: <b>Place deleted!</b>,
        error: <b>{"Could not delete place :("}</b>,
      });
      return action;
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
    async (payload: Place) => {
      const action = dispatch(PlacesUpdateFetcher.action(payload));
      toast.promise(action, {
        loading: "Saving...",
        success: <b>Place saved!</b>,
        error: <b>{"Could not save place :("}</b>,
      });
      return action;
    },
    [dispatch],
  );
};
