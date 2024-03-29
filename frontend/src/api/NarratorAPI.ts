import HttpAPI from "./HttpAPI";
import { NewPlace, Place } from "@/places/types";
import { NewResource, Resource } from "@/resources/types";

class NarratorAPI extends HttpAPI {
  constructor() {
    super("/api/", {
      "Content-Type": "application/json",
    });
  }

  getCampaigns() {
    return this.get("campaign/");
  }

  getPlaces(): Promise<Array<Place>> {
    return this.get("place/");
  }
  createPlace({ name, description }: NewPlace): Promise<Place> {
    return this.post("place/", {
      name,
      description,
    });
  }

  deletePlace(id: number): any {
    return this.delete(`place/${id}/`);
  }

  getCharacters() {
    return this.get("character/");
  }

  getInteractions(playerId: string, npcId: string) {
    return this.get(`character-interaction/conversation/${playerId}/${npcId}/`);
  }

  sendMessage(playerId: string, npcId: string, message: string) {
    return this.post(`character-interaction/interact/${playerId}/${npcId}/`, {
      message,
    });
  }

  getCharacter(npcId: string) {
    return this.get(`character/${npcId}/`);
  }

  clearThread(playerId: string, npcId: string) {
    return this.delete(
      `character-interaction/interact/${playerId}/${npcId}/clear/`,
    );
  }

  getResources(): Promise<Array<Resource>> {
    return this.get("resource/");
  }

  createResource(values: any): Promise<Resource> {
    return this.post("resource/", values);
  }

  deleteResource(id: number) {
    return this.delete(`resource/${id}/`);
  }

  updateResource(resource: Resource) {
    return this.put(`resource/${resource.id}/`, resource);
  }
}

export default NarratorAPI;
