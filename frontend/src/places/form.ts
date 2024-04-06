import * as yup from "yup";

export const placeFormValidationSchema = yup.object({
  name: yup.string().required("Name is required"),
  description: yup.string().required("Description is required"),
});

export const placeFormInitialValues = {
  name: "",
  description: "",
};
