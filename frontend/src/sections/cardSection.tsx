import Card, { CardProps } from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import Divider from "@mui/material/Divider";

import SectionTitleTooltip from "@/tooltip/sectionTitleTooltip";

export interface CardSectionProps extends Omit<CardProps, "title"> {
  title: React.ReactNode;
  actions?: React.ReactNode;
  children: React.ReactNode;
  withDivider?: boolean;
  tooltipText?: string;
  showTooltipIcon?: boolean;
}
const CardSection = ({
  title,
  actions,
  children,
  withDivider = true,
  tooltipText = "",
  showTooltipIcon = false,
  ...rest
}: CardSectionProps) => (
  <Card sx={{ mb: 2 }} {...rest}>
    <CardHeader
      title={
        <SectionTitleTooltip
          withIcon={showTooltipIcon}
          tooltipText={tooltipText}
        >
          {title}
        </SectionTitleTooltip>
      }
      action={actions}
    />
    {withDivider && <Divider />}
    <CardContent>{children}</CardContent>
  </Card>
);

export default CardSection;
