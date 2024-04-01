import { useAppDispatch, useAppSelector } from "@/redux/hooks";
import { useCallback } from "react";
import {
  ResourcesCreateFetcher,
  ResourcesDeleteFetcher,
  ResourcesFetcher,
  ResourcesUpdateFetcher,
} from "@/resources/state/thunk";
import { NewResource, Resource } from "@/resources/types";
import { createSelector } from "@reduxjs/toolkit";
import toast from "react-hot-toast";
import { PlacesCreateFetcher } from "@/places/state/thunk";

export const selectResources = (state: any) => {
  return state.resources;
};

export const selectResourcesByIds = createSelector(
  (state: any) => selectResources(state).data,
  (_: any, resourceIds: Array<number>) => resourceIds,
  (resources: Array<Resource>, resourceIds: Array<number>) =>
    resources.filter((resource: Resource) => resourceIds.includes(resource.id)),
);

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
    async (payload: NewResource) =>
      toast.promise(dispatch(ResourcesCreateFetcher.action(payload)), {
        loading: "Saving...",
        success: <b>Resource created!</b>,
        error: <b>{"Could not save resource :("}</b>,
      }),
    [dispatch],
  );
};

export const useDeleteResource = () => {
  const dispatch = useAppDispatch();
  return useCallback(
    async (id: number) => {
      return toast.promise(dispatch(ResourcesDeleteFetcher.action(id)), {
        loading: "Deleting resource...",
        success: <b>Resource deleted!</b>,
        error: <b>{"Could not delete resource :("}</b>,
      });
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
        return toast.promise(dispatch(ResourcesUpdateFetcher.action(rest)), {
          loading: "Saving resource...",
          success: <b>Resource saved!</b>,
          error: <b>{"Could not save resource :("}</b>,
        });
      }
    },
    [dispatch, loading],
  );
};
