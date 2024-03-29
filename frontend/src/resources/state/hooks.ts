import { useAppDispatch, useAppSelector } from "@/redux/hooks";
import { useCallback } from "react";
import {
  ResourcesCreateFetcher,
  ResourcesDeleteFetcher,
  ResourcesFetcher,
} from "@/resources/state/thunk";
import { NewResource } from "@/resources/types";

export const selectResources = (state: any) => {
  return state.resources;
};

export const useResources = () => {
  return useAppSelector(selectResources);
};

export const useCreateResource = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    (payload: NewResource) => {
      dispatch(ResourcesCreateFetcher.action(payload));
    },
    [dispatch],
  );
};

export const useDeleteResource = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    (id: number) => {
      dispatch(ResourcesDeleteFetcher.action(id));
    },
    [dispatch],
  );
};

export const useFetchResources = () => {
  const dispatch = useAppDispatch();
  const { loading } = useResources();
  return useCallback(() => {
    if (!loading) {
      dispatch(ResourcesFetcher.action());
    }
  }, [dispatch, loading]);
};
