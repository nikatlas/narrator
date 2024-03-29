import * as React from "react";
import {
  Modal as MuiModal,
  Box,
  Grid,
  Button,
  IconButton,
  Typography,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import { Simulate } from "react-dom/test-utils";
import submit = Simulate.submit;

const defaultStyle = {
  position: "fixed",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 600,
  bgcolor: "background.paper",
  border: "1px solid #ccc",
  boxShadow: "0 4px 8px 0 rgba(0, 0, 0, 0.2)",
  p: 4,
};

export interface TriggerButtonProps {
  handleOpen: () => void;
  triggerButtonText: string;
}

export interface ModalProps {
  title?: string;
  children?: React.ReactNode;
  onOpen?: () => void;
  onClose?: () => void;
  beforeClose?: () => void;
  style?: React.CSSProperties;
  triggerButtonText?: string;
  triggerButtonComponent?: React.ComponentType<{
    handleOpen: () => void;
    triggerButtonText: string;
  }>;
  externalControl?: boolean; // prop for external control
  isOpen?: boolean; // Prop for external control of modal visibility
  showTriggerButton?: boolean; // show/hide the trigger button
  rest?: any;
}

const DefaultTriggerButton = ({
  handleOpen,
  triggerButtonText,
}: TriggerButtonProps) => (
  <Button onClick={handleOpen}>{triggerButtonText}</Button>
);

const Modal = ({
  title,
  children,
  onOpen,
  onClose,
  beforeClose,
  isOpen,
  externalControl,
  showTriggerButton = true,
  triggerButtonComponent: TriggerButton = DefaultTriggerButton,
  triggerButtonText = "Open Modal",
  ...rest
}: ModalProps) => {
  const [open, setOpen] = React.useState(externalControl ? !!isOpen : false);

  React.useEffect(() => {
    if (externalControl) {
      setOpen(!!isOpen);
    }
  }, [externalControl, isOpen]);

  const handleOpen = () => {
    setOpen(true);
    if (onOpen) {
      onOpen();
    }
  };

  const handleClose = () => {
    if (externalControl) return;

    if (beforeClose) {
      beforeClose();
    }
    setOpen(false);
  };

  const mergedStyle = {
    ...defaultStyle,
  };
  return (
    <>
      {showTriggerButton && (
        <TriggerButton
          handleOpen={handleOpen}
          triggerButtonText={triggerButtonText}
        />
      )}
      <MuiModal
        open={open}
        disableAutoFocus
        onClose={onClose || handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
        {...rest}
      >
        <Box sx={mergedStyle}>
          <Grid container>
            <Grid item xs>
              <Typography variant={"h5"}>{title}</Typography>
            </Grid>
            <Grid item xs textAlign={"right"}>
              <IconButton onClick={onClose || handleClose}>
                <CloseIcon />
              </IconButton>
            </Grid>
          </Grid>
          <Grid>{children}</Grid>
        </Box>
      </MuiModal>
    </>
  );
};

export default Modal;
