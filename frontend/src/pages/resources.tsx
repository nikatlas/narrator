import { useCreateResource, useResources } from "@/resources/state/hooks";
import { Resources } from "@/resources";

const ResourcesPage = () => {
  const { data: resources, error } = useResources();

  return (
    <Resources
      title={"Resources"}
      resources={resources}
      error={error}
      withCreateButton
    />
  );
};

export default ResourcesPage;
