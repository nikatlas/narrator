import { useAppDispatch, useAppSelector } from "@/redux/hooks";
import { useCallback } from "react";
import {
  PlacesCreateFetcher,
  PlacesDeleteFetcher,
  PlacesFetcher,
} from "@/places/state/thunk";
import { NewPlace } from "@/places/types";

export const selectPlaces = (state: any) => state.places;

export const usePlaces = () => {
  return useAppSelector(selectPlaces);
};

export const useCreatePlace = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    (payload: NewPlace) => {
      dispatch(PlacesCreateFetcher.action(payload));
    },
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
