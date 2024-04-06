import { Alert, Grid, Typography } from "@mui/material";
import { Place as IPlace } from "@/places/types";
import React from "react";
import { Bucket } from "@/sections/bucketSection";
import { BucketContainer } from "@/sections/bucketSection";
import { Form, Formik } from "formik";
import TextFieldForm from "@/form/textFieldForm";
import CheckboxField from "@/form/checkboxField";
import Button from "@mui/material/Button";
import { placeFormInitialValues, placeFormValidationSchema } from "./form";
import TextareaForm from "@/form/textareaForm";

interface PlaceProps {
  place: IPlace;
  onSubmit: (values: IPlace) => void;
}

const Place = ({ place, onSubmit }: PlaceProps) => {
  return (
    <BucketContainer isVertical={true}>
      <Bucket>
        <Formik
          validationSchema={placeFormValidationSchema}
          initialValues={place ?? placeFormInitialValues}
          onSubmit={onSubmit}
        >
          <Form>
            <TextFieldForm id={"name"} label={"Name"} fullWidth />
            <TextareaForm
              id={"description"}
              label={"Description"}
              fullWidth
              minRows={8}
            />
            <Grid container justifyContent={"end"} mt={2}>
              <Grid item>
                <Button type={"submit"} variant={"contained"}>
                  Save
                </Button>
              </Grid>
            </Grid>
          </Form>
        </Formik>
      </Bucket>
    </BucketContainer>
  );
};

export default Place;
