export interface Place {
  id: number;
  name: string;
  description?: string;
}

export type NewPlace = Omit<Place, "id">;
