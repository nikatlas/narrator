import { ReactElement } from 'react';

import { Tooltip as MuiTooltip } from '@mui/material';

import Tooltip from '.';

interface SectionTitleTooltipProps {
    withIcon?: boolean;
    tooltipText?: string;
    children: React.ReactNode;
}

const SectionTitleTooltip = ({ withIcon, tooltipText, children }: SectionTitleTooltipProps) => {
    if (withIcon) {
        return tooltipText ? <Tooltip sx={{ ml: 1 }} title={tooltipText} /> : <>{children}</>;
    }

    if (tooltipText) {
        return (
            <MuiTooltip title={tooltipText} placement="top">
                <span>{children}</span>
            </MuiTooltip>
        );
    }

    return children as ReactElement;
};

export default SectionTitleTooltip;
