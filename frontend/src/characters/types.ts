export interface Character {
  id: number;
  firstName: string;
  lastName: string;
  voice: string;
  isPlayer: boolean;
  resources?: Array<number>;
}

export type NewCharacter = Omit<Character, "id">;
