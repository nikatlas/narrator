import { TextField, TextFieldProps } from "@mui/material";
import React from "react";
import { FormikProps } from "formik";

type TextFieldFormProps<T> = {
  form: FormikProps<T>;
  id: string;
} & Omit<TextFieldProps, "id">;

const TextFieldForm = <T,>({
  form,
  id,
  name,
  label,
  ...rest
}: TextFieldFormProps<T>) => (
  <TextField
    id={id}
    name={name}
    label={label}
    // @ts-ignore
    value={form.values[id]}
    onChange={form.handleChange}
    onBlur={form.handleBlur}
    // @ts-ignore
    error={form.touched[id] && Boolean(form.errors[id])}
    // @ts-ignore
    helperText={form.touched[id] && form.errors[id]}
    {...rest}
  />
);

export default TextFieldForm;
