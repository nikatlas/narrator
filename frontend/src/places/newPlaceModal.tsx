import { Button } from "@mui/material";
import React from "react";
import * as yup from "yup";
import TextFieldForm from "@/form/textFieldForm";
import TextareaForm from "@/form/textareaForm";
import { useCreatePlace, usePlaces } from "@/places/state/hooks";
import CreateModalForm, { CreateModalFormProps } from "@/modal/createModalForm";
import { Place } from "@/places/types";

export interface NewPlaceModalProps
  extends Omit<
    CreateModalFormProps,
    "loading" | "initialValues" | "onSubmit" | "validationSchema"
  > {
  loading?: boolean;
  initialValues?: any;
  onSubmit?: (values: any) => void;
  validationSchema?: any;
  submitButtonText?: string;
  onNewPlace?: (place: Place) => void;
}

const validationSchema = yup.object({
  name: yup.string().required("Name is required"),
  description: yup.string().required("Description is required"),
});

const initialValues = { name: "", description: "" };

const NewPlaceModal = ({
  onNewPlace,
  submitButtonText,
  ...rest
}: NewPlaceModalProps) => {
  const createPlace = useCreatePlace();
  const { loading } = usePlaces();

  return (
    <CreateModalForm
      title={`New place`}
      triggerButtonText={"New place"}
      loading={loading}
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={async (place) => {
        const newPlace = createPlace(place);
        if (onNewPlace) {
          onNewPlace((await newPlace).payload.data as Place);
        }
      }}
      {...rest}
    >
      <TextFieldForm id={"name"} name={"name"} label={"Name"} fullWidth />
      <TextareaForm
        id={"description"}
        name={"description"}
        placeholder={"Description"}
        fullWidth
        minRows={5}
      />
      <Button type={"submit"}>{submitButtonText ?? "Create"}</Button>
    </CreateModalForm>
  );
};

export default NewPlaceModal;
