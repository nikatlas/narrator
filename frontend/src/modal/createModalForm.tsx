import { Button } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import Modal, { ModalProps } from "@/modal/modal";
import React, {
  FormEventHandler,
  ReactElement,
  ReactNode,
  useCallback,
} from "react";
import { Form, Formik, useFormik } from "formik";

interface CreateModalProps extends ModalProps {
  loading: boolean;
  initialValues: any;
  onSubmit: (values: any) => void;
  validationSchema: any;
  triggerButtonText?: string;
  children?: ReactNode;
}

const CreateModalForm = ({
  loading,
  initialValues,
  onSubmit,
  validationSchema,
  children,
  triggerButtonText,
  ...rest
}: CreateModalProps) => {
  const [isOpen, setIsOpen] = React.useState(false);

  const defaultTriggerButtonComponent = useCallback(
    () => (
      <Button
        variant="outlined"
        startIcon={<AddIcon />}
        disabled={loading}
        onClick={() => setIsOpen(true)}
      >
        {triggerButtonText ?? "Add"}
      </Button>
    ),
    [loading, triggerButtonText],
  );

  return (
    <Modal
      isOpen={isOpen}
      onClose={() => setIsOpen(false)}
      externalControl
      triggerButtonComponent={defaultTriggerButtonComponent}
      triggerButtonText={triggerButtonText}
      {...rest}
    >
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={(values, { resetForm }) => {
          onSubmit?.(values);
          setIsOpen(false);
          resetForm();
        }}
      >
        <Form>{children}</Form>
      </Formik>
    </Modal>
  );
};

export default CreateModalForm;
