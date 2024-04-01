import type { Character as ICharacter } from "./types";
import { Bucket, BucketContainer } from "@/sections/bucketSection";
import { Form, Formik } from "formik";
import {
  characterFormInitialValues,
  characterFormValidationSchema,
} from "@/characters/form";
import TextFieldForm from "@/form/textFieldForm";
import CheckboxField from "@/form/checkboxField";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";

interface CharacterProps {
  character: ICharacter;
  onSubmit: (values: ICharacter) => void;
}

const Character = ({ character, onSubmit }: CharacterProps) => {
  return (
    <BucketContainer isVertical={true}>
      <Bucket>
        <Formik
          validationSchema={characterFormValidationSchema}
          initialValues={character ?? characterFormInitialValues}
          onSubmit={onSubmit}
        >
          <Form>
            <TextFieldForm id={"firstName"} label={"First name"} fullWidth />
            <TextFieldForm id={"lastName"} label={"Last name"} fullWidth />
            <TextFieldForm id={"voice"} label={"Voice"} fullWidth />
            <CheckboxField id={"isPlayer"} label={"Player"} />
            <Grid container justifyContent={"end"}>
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

export default Character;
