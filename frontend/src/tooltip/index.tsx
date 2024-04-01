import * as React from 'react';

import InfoIcon from '@mui/icons-material/Info';
import {
    Box,
    TooltipProps as MuiToolTipProps,
    Tooltip as MuiTooltip,
    tooltipClasses,
} from '@mui/material';
import { styled } from '@mui/material/styles';

import RichTooltip from './richTooltip';

const defaultSX = {
    bgcolor: 'none',
};

interface TooltipProps {
    children?: React.ReactNode;
    sx?: Object;
    title?: string;
    placement?:
        | 'bottom-end'
        | 'bottom-start'
        | 'bottom'
        | 'left-end'
        | 'left-start'
        | 'left'
        | 'right-end'
        | 'right-start'
        | 'right'
        | 'top-end'
        | 'top-start'
        | 'top';
}
const InfoButton = () => <InfoIcon fontSize="small" color="secondary" />;

const PrimaryTooltip = styled(({ className, ...props }: MuiToolTipProps) => (
    <MuiTooltip {...props} classes={{ popper: className }} />
))(({ theme }) => ({
    [`& .${tooltipClasses.tooltip}`]: {
        backgroundColor: theme.palette.primary.main,
        color: theme.palette.common.white,
        boxShadow: theme.shadows[1],
        fontSize: 12,
        padding: '8px',
        textAlign: 'justify',
    },
    [`& .${tooltipClasses.arrow}`]: {
        color: theme.palette.primary.main,
    },
}));

const Tooltip = ({
    children = <InfoButton />,
    sx = defaultSX,
    title = '',
    placement = 'top',
}: TooltipProps) => (
    <PrimaryTooltip sx={{ bgcolor: 'primary' }} title={title} placement={placement || 'top'} arrow>
        <Box sx={sx}>{children}</Box>
    </PrimaryTooltip>
);

export default Tooltip;

export { RichTooltip };
