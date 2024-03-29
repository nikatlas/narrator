export interface Resource {
  id: number;
  name: string;
  text?: string;
}

export type NewResource = Omit<Resource, "id">;
