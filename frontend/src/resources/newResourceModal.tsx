import { Button } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import Modal from "@/modal/modal";
import React from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import TextFieldForm from "@/form/textFieldForm";
import TextareaForm from "@/form/textareaForm";
import { useCreateResource, useResources } from "@/resources/state/hooks";
import CreateModalForm from "@/modal/createModalForm";

const validationSchema = yup.object({
  name: yup.string().required("Name is required"),
  text: yup.string().required("Text is required"),
});

const initialValues = { name: "", text: "" };

const NewResourceModal = () => {
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
    >
      <TextFieldForm id={"name"} name={"name"} label={"Name"} fullWidth />
      <TextareaForm
        id={"text"}
        name={"text"}
        placeholder={"Text"}
        fullWidth
        minRows={5}
      />
      <Button type={"submit"}>Create</Button>
    </CreateModalForm>
  );
};

export default NewResourceModal;
