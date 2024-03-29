import NewResourceModal, {
  NewResourceModalProps,
} from "@/resources/newResourceModal";
import { useUpdateResources } from "@/resources/state/hooks";
import { Resource } from "@/resources/types";

interface EditResourceModalProps extends NewResourceModalProps {
  resource: Resource;
}

const EditResourceModal = ({ resource, ...rest }: EditResourceModalProps) => {
  const editResource = useUpdateResources();

  const handleSubmit = (values: any) => {
    editResource({ ...resource, ...values });
    rest?.onClose?.();
  };

  return (
    <NewResourceModal
      isOpen={true}
      showTriggerButton={false}
      loading={false}
      initialValues={{
        name: resource.name,
        text: resource.text,
      }}
      onSubmit={handleSubmit}
      title={"Edit resource"}
      triggerButtonText={"Edit resource"}
      submitButtonText={"Edit"}
      {...rest}
    />
  );
};

export default EditResourceModal;
