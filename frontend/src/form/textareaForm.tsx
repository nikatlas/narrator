import {
  styled,
  TextareaAutosize,
  TextareaAutosizeProps,
  TextField,
  TextFieldProps,
} from "@mui/material";
import React from "react";
import { useFormikContext } from "formik";
import TextFieldForm, { TextFieldFormProps } from "@/form/textFieldForm";

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

type TextareaFormProps<T> = TextareaAutosizeProps & TextFieldFormProps<T>;

const TextareaForm = <T,>({
  id,
  name,
  placeholder,
  minRows,
  maxRows,
  ...rest
}: TextareaFormProps<T>) => {
  return (
    <TextFieldForm
      id={id}
      name={name}
      placeholder={placeholder}
      {...rest}
      InputProps={{
        inputComponent: TextareaAutosize,
        inputProps: { minRows, maxRows },
      }}
    />
  );
};

export default TextareaForm;
