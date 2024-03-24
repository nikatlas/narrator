import HttpAPI from "./HttpAPI";
import { NewPlace, Place } from "@/types";

class NarratorAPI extends HttpAPI {
  baseUrl: string = "/api/";

  constructor() {
    super("", {
      "Content-Type": "application/json",
    });
  }

  getCampaigns() {
    return this.get(this.baseUrl + "campaign/");
  }

  getPlaces(): Promise<Array<Place>> {
    return this.get(this.baseUrl + "place/");
  }
  createPlace({ name, description }: NewPlace): Promise<Place> {
    return this.post(this.baseUrl + "place/", {
      name,
      description,
    });
  }

  deletePlace(id: number): any {
    return this.delete(this.baseUrl + `place/${id}/`);
  }

  getCharacters() {
    return this.get(this.baseUrl + "character/");
  }

  getInteractions(playerId: string, npcId: string) {
    return this.get(
      this.baseUrl + `character-interaction/conversation/${playerId}/${npcId}/`,
    );
  }

  sendMessage(playerId: string, npcId: string, message: string) {
    return this.post(
      this.baseUrl + `character-interaction/interact/${playerId}/${npcId}/`,
      {
        message,
      },
    );
  }

  getCharacter(npcId: string) {
    return this.get(this.baseUrl + `character/${npcId}/`);
  }

  clearThread(playerId: string, npcId: string) {
    return this.delete(
      this.baseUrl +
        `character-interaction/interact/${playerId}/${npcId}/clear/`,
    );
  }
}

export default NarratorAPI;
