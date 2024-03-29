export interface Resource {
  id: number;
  name: string;
  text?: string;
  file?: string;
}

export type NewResource = Omit<Resource, "id">;
