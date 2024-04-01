import NewResourceModal, {
  NewResourceModalProps,
} from "@/resources/newResourceModal";
import { useUpdateResources } from "@/resources/state/hooks";
import { Resource } from "@/resources/types";
import NewPlaceModal from "./newPlaceModal";
import { Place } from "@/places/types";
import { useUpdatePlace } from "@/places/state/hooks";

interface EditPlaceModalProps extends NewResourceModalProps {
  place: Place;
}

const EditPlaceModal = ({
  place,
  showTriggerButton,
  ...rest
}: EditPlaceModalProps) => {
  const editPlace = useUpdatePlace();

  const handleSubmit = (values: any) => {
    editPlace({ ...place, ...values });
    rest?.onClose?.();
  };

  return (
    <NewPlaceModal
      isOpen={showTriggerButton ? undefined : true}
      showTriggerButton={showTriggerButton ?? false}
      loading={false}
      initialValues={{
        name: place.name,
        description: place.description,
      }}
      onSubmit={handleSubmit}
      title={"Edit place"}
      triggerButtonText={"Edit place"}
      submitButtonText={"Edit"}
      {...rest}
    />
  );
};

export default EditPlaceModal;
