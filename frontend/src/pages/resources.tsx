import { useResources } from "@/resources/state/hooks";
import { Resources } from "@/resources";

const ResourcesPage = () => {
  const { data: resources, error } = useResources();

  return <Resources resources={resources} error={error} />;
};

export default ResourcesPage;
