import { useState } from "react";

import { Box, Card, Popper, PopperProps } from "@mui/material";

interface RichTooltipProps extends Omit<PopperProps, "open" | "content"> {
  children: React.ReactNode;
  content?: React.ReactNode;
  closeDelay?: number;
}
const RichTooltip = ({
  children,
  content,
  closeDelay = 200,
  ...restProps
}: RichTooltipProps) => {
  const [anchor, setAnchor] = useState<(EventTarget & HTMLElement) | null>(
    null,
  );
  const [timer, setTimer] = useState<NodeJS.Timeout | null>(null);
  const handleEnterAnchor = (event: React.MouseEvent<HTMLElement>) => {
    if (timer) {
      clearTimeout(timer);
    }
    setAnchor(event.currentTarget);
  };
  const handleEnterPopper = () => {
    if (timer) {
      clearTimeout(timer);
    }
  };

  const handlePopperClose = () => {
    const t = setTimeout(() => {
      setAnchor(null);
    }, closeDelay);
    setTimer(t);
  };

  return (
    <Box display="inline-block">
      <Box onMouseEnter={handleEnterAnchor} onMouseLeave={handlePopperClose}>
        {children}
      </Box>
      <Popper open={!!anchor} anchorEl={anchor} {...restProps}>
        <Card
          onMouseEnter={handleEnterPopper}
          onMouseLeave={handlePopperClose}
          onClick={(e) => e.stopPropagation()}
        >
          {content}
        </Card>
      </Popper>
    </Box>
  );
};
export default RichTooltip;
