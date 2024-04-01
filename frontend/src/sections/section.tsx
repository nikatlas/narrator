import React, { ReactNode } from "react";

import { Divider, Grid, Typography } from "@mui/material";
import type { GridProps } from "@mui/material";

import SectionTitleTooltip from "@/tooltip/sectionTitleTooltip";

export interface InternalSectionProps extends Omit<GridProps, "title"> {
  children?: ReactNode;
  title?: ReactNode;
  header?: ReactNode;
  actions?: ReactNode[];
  actionsDatatestID?: string;
  description?: string;
  tooltipText?: string;
  divider?: boolean;
  showTooltipIcon?: boolean;
}

export interface SectionProps extends InternalSectionProps {}

const gridProps = {
  sx: {
    padding: {
      xs: 1,
      md: 2,
      lg: 3,
    },
    textAlign: "justify",
  },
};

const itemStyling = {
  marginBottom: 1,
};

export const InternalSection = ({
  title,
  header,
  actions,
  actionsDatatestID,
  description,
  children,
  tooltipText,
  divider = false,
  showTooltipIcon = false,
  ...restProps
}: SectionProps) => (
  <>
    <Grid container alignItems="center" spacing={1} {...restProps}>
      {title && (
        <Grid item xs>
          <SectionTitleTooltip
            withIcon={showTooltipIcon}
            tooltipText={tooltipText}
          >
            <Typography variant="h6" textAlign="left">
              {title}
            </Typography>
          </SectionTitleTooltip>
        </Grid>
      )}
      {header && (
        <Grid item display="flex" alignItems="center" flexDirection="row">
          {header}
        </Grid>
      )}
      {actions && (
        <Grid item xs>
          <Grid
            container
            justifyContent="flex-end"
            spacing={1}
            data-testid={actionsDatatestID}
          >
            {actions.filter(Boolean).map((action, index) => (
              // eslint-disable-next-line react/no-array-index-key
              <Grid item key={index}>
                {action}
              </Grid>
            ))}
          </Grid>
        </Grid>
      )}
      {description && (
        <Grid item xs={12} sx={itemStyling}>
          <Typography>{description}</Typography>
        </Grid>
      )}
      <Grid item xs={12} sx={itemStyling}>
        {children}
      </Grid>
    </Grid>
    {divider && <Divider />}
  </>
);

const Section = ({ children, ...restProps }: SectionProps) => (
  <InternalSection {...gridProps} {...restProps}>
    {children}
  </InternalSection>
);
export default Section;
