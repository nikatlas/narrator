import { styled, TextareaAutosize, TextareaAutosizeProps } from "@mui/material";
import React from "react";
import { FormikProps } from "formik";

const StyledTextareaAutosize = styled(TextareaAutosize)<TextareaAutosizeProps>(
  ({ theme }) => ({
    maxWidth: "100%",
    maxHeight: "60vh",
    width: "100%",
    fontSize: "0.875rem",
    fontWeight: 400,
    lineHeight: 1.5,
    padding: 12,
    backgroundColor: theme.palette.background.default,
    color: theme.palette.grey[900],
    border: `1px solid ${theme.palette.grey[200]}`,
    borderColor: theme.palette.grey[400],
    boxShadow: `0px 2px 2px ${theme.palette.grey[50]}`,
    borderRadius: 4,
    "&:hover": {
      borderColor: "#172b4d",
    },
    "&:focus": {
      borderColor: "#172b4d",
    },
    "&:focus-visible": {
      outline: 0,
    },
  }),
);

type TextareaAutosizeFormProps<T> = {
  form: FormikProps<T>;
  id: string;
} & Omit<TextareaAutosizeProps, "id" | "form">;

const TextareaAutosizeForm = <T,>({
  form,
  id,
  name,
  placeholder,
  ...rest
}: TextareaAutosizeFormProps<T>) => (
  <StyledTextareaAutosize
    id={id}
    name={name}
    placeholder={placeholder}
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

export default TextareaAutosizeForm;
