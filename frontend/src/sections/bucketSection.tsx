import React from 'react';

import Divider from '@mui/material/Divider';
import Grid, { GridProps } from '@mui/material/Grid';

import CardSection, { CardSectionProps } from './cardSection';

export interface BucketSectionProps extends CardSectionProps {
    isVertical?: boolean;
}

interface BucketProps extends GridProps {
    withDivider?: boolean;
    isVertical?: boolean;
}

/*
 * Bucket is a component that is used to display multiple sections inside a BucketContainer or a BucketSection.
 * It is used to display multiple sections in a row or in a column.
 * It adds a divider between each section by default, but can be disabled by setting withDivider to false.
 *
 * @param {boolean} isVertical - Defaults to false.
 *    If true, the sections will be displayed in a column. If false, the sections will be displayed in a row.
 *    Notice that in case of vertical arrangement, the xs, sm, md, lg and xl props should not be set, otherwise they will restrict the Bucket from extending fullWidth.
 *
 * @param {boolean} withDivider - Defaults to false.
 *    If true, a divider will be displayed between each section. If false, no divider will be displayed.
 *    Notice, inside a BucketContainer the default value is `true` for all but last Buckets
 *
 * @param {GridProps} rest - Any other props that should be passed to the root Grid component.
 */
export const Bucket = ({
    isVertical = false,
    withDivider = false,
    xs,
    sm,
    md,
    lg,
    xl,
    ...rest
}: BucketProps) => (
    <Grid item xs={xs ?? 12} sm={sm} md={md} lg={lg} xl={xl} {...rest}>
        <Grid
            container
            flexDirection={isVertical ? 'column' : 'row'}
            justifyContent="space-between"
            wrap="nowrap"
            height="100%"
        >
            <Grid item xs>
                {rest.children}
            </Grid>
            <Grid>
                {withDivider && (
                    <Divider
                        orientation={isVertical ? 'horizontal' : 'vertical'}
                        flexItem
                        sx={{
                            height: '100%',
                            display: {
                                xs: xs === 12 || !xs ? 'none' : 'block',
                                sm: sm === 12 ? 'none' : 'block',
                                md: md === 12 ? 'none' : 'block',
                                lg: lg === 12 ? 'none' : 'block',
                                xl: xl === 12 ? 'none' : 'block',
                            },
                            pl: 2,
                            pt: 2,
                        }}
                    />
                )}
            </Grid>
        </Grid>
    </Grid>
);
Bucket.isBucket = true;

export const BucketContainer = ({
    isVertical = false,
    children,
}: {
    isVertical: boolean;
    children: React.ReactNode;
}) => {
    const childArray = React.Children.toArray(children);

    return (
        <Grid
            container
            spacing={2}
            alignItems="stretch"
            flexDirection={isVertical ? 'column' : 'row'}
        >
            {childArray.map((child, index) => {
                if (React.isValidElement(child) && (child.type as any)?.isBucket) {
                    return (
                        // eslint-disable-next-line react/no-array-index-key
                        <React.Fragment key={index}>
                            {React.cloneElement(child, {
                                withDivider: index < childArray.length - 1,
                                isVertical,
                                ...child.props,
                            })}
                        </React.Fragment>
                    );
                }
                return null;
            })}
        </Grid>
    );
};
BucketContainer.isBucket = true;

const BucketSection = ({ isVertical = false, children, ...rest }: BucketSectionProps) => (
    <CardSection {...rest}>
        <BucketContainer isVertical={isVertical}>{children}</BucketContainer>
    </CardSection>
);

export default BucketSection;
