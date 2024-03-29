import { useAppDispatch, useAppSelector } from "@/redux/hooks";
import { useCallback } from "react";
import {
  ResourcesCreateFetcher,
  ResourcesDeleteFetcher,
  ResourcesFetcher,
  ResourcesUpdateFetcher,
} from "@/resources/state/thunk";
import { NewResource, Resource } from "@/resources/types";

export const selectResources = (state: any) => {
  return state.resources;
};

export const useResources = () => {
  const { data, ...rest } = useAppSelector(selectResources);
  return {
    data: [...data].sort((a: Resource, b: Resource) => b.id - a.id),
    ...rest,
  };
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

export const useUpdateResources = () => {
  const dispatch = useAppDispatch();
  const { loading } = useResources();
  return useCallback(
    (resource: Resource) => {
      const { file, ...rest } = resource;
      if (!loading) {
        dispatch(ResourcesUpdateFetcher.action(rest));
      }
    },
    [dispatch, loading],
  );
};
