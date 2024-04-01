import React from 'react';

import { Grid, GridProps } from '@mui/material';

interface SpacingContainerProps extends GridProps {}

const SpacingContainer = ({ children, ...restProps }: SpacingContainerProps) => (
    <Grid container spacing={2} {...restProps}>
        {children &&
            React.Children.toArray(children).map((child, index) => (
                // eslint-disable-next-line react/no-array-index-key
                <Grid item key={index}>
                    {child}
                </Grid>
            ))}
    </Grid>
);

export default SpacingContainer;
