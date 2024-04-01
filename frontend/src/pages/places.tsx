import { Places } from "@/places";
import { usePlaces } from "@/places/state/hooks";

const PlacesPage = () => {
  const { data: places, error } = usePlaces();

  return <Places places={places} error={error} />;
};

export default PlacesPage;
