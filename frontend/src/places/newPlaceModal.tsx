import { Button } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import Modal from "@/modal/modal";
import React from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import TextFieldForm from "@/form/textFieldForm";
import TextareaAutosizeForm from "@/form/textareaForm";
import NarratorAPI from "@/api/NarratorAPI";
import { useCreatePlace } from "@/places/state/hooks";

const validationSchema = yup.object({
  name: yup.string().required("Name is required"),
  description: yup.string(),
});

const api = new NarratorAPI();

const NewPlaceModal = () => {
  const [isOpen, setIsOpen] = React.useState(false);
  const createPlace = useCreatePlace();

  const formik = useFormik({
    initialValues: {
      name: "",
      description: "",
    },
    validationSchema: validationSchema,
    onSubmit: (values) => {
      createPlace(values);
      setIsOpen(false);
      formik.resetForm();
    },
  });

  return (
    <Modal
      isOpen={isOpen}
      externalControl
      title={`New place`}
      triggerButtonComponent={() => (
        <Button
          variant="outlined"
          startIcon={<AddIcon />}
          onClick={() => setIsOpen(true)}
        >
          New place
        </Button>
      )}
    >
      <form onSubmit={formik.handleSubmit}>
        <TextFieldForm
          form={formik}
          id={"name"}
          name={"name"}
          label={"Name"}
          fullWidth
        />
        <TextareaAutosizeForm
          form={formik}
          id={"description"}
          name={"description"}
          placeholder={"Description"}
          minRows={3}
        />
        <Button type={"submit"}>Create</Button>
      </form>
    </Modal>
  );
};

export default NewPlaceModal;
