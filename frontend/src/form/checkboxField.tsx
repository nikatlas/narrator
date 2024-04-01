import { Field, useFormikContext } from "formik";
import React from "react";

import { Checkbox, CheckboxProps, FormControlLabel } from "@mui/material";

interface CheckboxFieldProps extends CheckboxProps {
  label: React.ReactNode;
  id: string;
}

const CheckboxField: React.FC<CheckboxFieldProps> = ({
  label,
  id,
  ...rest
}) => {
  const { values, handleChange, handleBlur, touched, errors } =
    useFormikContext();
  return (
    <FormControlLabel
      label={label}
      control={
        <Field
          component={(fieldProps: any) => (
            <Checkbox {...fieldProps} type="checkbox" />
          )}
          id={id}
          name={id}
          label={label}
          // @ts-ignore
          checked={values[id]}
          onChange={handleChange}
          onBlur={handleBlur}
          // @ts-ignore
          error={touched[id] && Boolean(errors[id])}
          // @ts-ignore
          helperText={touched[id] && errors[id]}
          {...rest}
        />
      }
    />
  );
};

export default CheckboxField;
