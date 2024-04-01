import * as yup from "yup";

export const characterFormValidationSchema = yup.object({
  firstName: yup.string().required("First name is required"),
  lastName: yup.string().required("Last name is required"),
  voice: yup.string().nullable(),
  isPlayer: yup.boolean().required("Is player is required"),
});

export const characterFormInitialValues = {
  firstName: "",
  lastName: "",
  voice: "",
  isPlayer: false,
};
