import { Resource } from "@/resources/types";

export interface Place {
  id: number;
  name: string;
  description?: string;
  resources?: Array<number>;
}

export type NewPlace = Omit<Place, "id">;
