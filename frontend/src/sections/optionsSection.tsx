import React from 'react';

import { Grid } from '@mui/material';

import { InternalSection, InternalSectionProps } from './section';

interface SectionProps extends InternalSectionProps {}

const OptionsSection: React.FC<SectionProps> = ({ children, ...restProps }: SectionProps) => (
    <InternalSection {...restProps}>
        {children &&
            React.Children.toArray(children).map((child, index) => (
                // eslint-disable-next-line react/no-array-index-key
                <Grid item key={index}>
                    {child}
                </Grid>
            ))}
    </InternalSection>
);

export default OptionsSection;
