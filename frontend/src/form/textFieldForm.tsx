import { TextField, TextFieldProps } from "@mui/material";
import React from "react";
import { FormikProps, useFormik, useFormikContext } from "formik";

export type TextFieldFormProps<T> = {
  id?: string;
} & Omit<TextFieldProps, "id">;

const TextFieldForm = <T,>({
  id,
  name,
  label,
  ...rest
}: TextFieldFormProps<T>) => {
  const { values, handleChange, handleBlur, touched, errors } =
    useFormikContext();

  return (
    <TextField
      sx={{ mt: 2 }}
      id={id}
      name={name ?? id}
      label={label}
      // @ts-ignore
      value={values[id]}
      onChange={handleChange}
      onBlur={handleBlur}
      // @ts-ignore
      error={touched[id] && Boolean(errors[id])}
      // @ts-ignore
      helperText={touched[id] && errors[id]}
      {...rest}
    />
  );
};

export default TextFieldForm;
