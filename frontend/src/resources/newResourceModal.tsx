import { Button } from "@mui/material";
import React from "react";
import * as yup from "yup";
import TextFieldForm from "@/form/textFieldForm";
import TextareaForm from "@/form/textareaForm";
import { useCreateResource, useResources } from "@/resources/state/hooks";
import CreateModalForm, { CreateModalFormProps } from "@/modal/createModalForm";

export interface NewResourceModalProps
  extends Omit<
    CreateModalFormProps,
    "loading" | "initialValues" | "onSubmit" | "validationSchema"
  > {
  loading?: boolean;
  initialValues?: any;
  onSubmit?: (values: any) => void;
  validationSchema?: any;
  submitButtonText?: string;
}

const validationSchema = yup.object({
  name: yup.string().required("Name is required"),
  text: yup.string().required("Text is required"),
});

const initialValues = { name: "", text: "" };

const NewResourceModal = ({
  submitButtonText,
  ...rest
}: NewResourceModalProps) => {
  const { loading } = useResources();
  const createResource = useCreateResource();

  return (
    <CreateModalForm
      title={`New resource`}
      loading={loading}
      initialValues={initialValues}
      onSubmit={createResource}
      validationSchema={validationSchema}
      triggerButtonText={"New resource"}
      {...rest}
    >
      <TextFieldForm id={"name"} name={"name"} label={"Name"} fullWidth />
      <TextareaForm
        id={"text"}
        name={"text"}
        placeholder={"Text"}
        fullWidth
        minRows={5}
      />
      <Button type={"submit"}>{submitButtonText ?? "Create"}</Button>
    </CreateModalForm>
  );
};

export default NewResourceModal;
