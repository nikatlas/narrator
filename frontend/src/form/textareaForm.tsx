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
      sx={{ mt: 2 }}
      id={id ?? name}
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
