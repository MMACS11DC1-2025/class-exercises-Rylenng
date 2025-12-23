# Dead Grass Detection Using Image Processing

## Project Overview

**Theme:** Grass inspector, to see amount of dead grass\
**Image Set:** 10 lawn images (`lawn1.jpg` -- `lawn10.jpg`)

This project analyzes a collection of lawn images to detect and measure
the amount of dead grass in each image. The program processes every
pixel in each image, identifies pixels that likely represent dead grass
based on color values, and calculates a Dead Grass Feature Density Score
for comparison.

------------------------------------------------------------------------

## Feature Description

**Detected Feature:** Dead grass pixels

A pixel is classified as dead grass if its RGB values is a
yellow coloration commonly associated with dry or unhealthy grass.

### Feature Definition Logic

-   Red \> 120\
-   Green \> 90\
-   Blue \< 90

------------------------------------------------------------------------

## Image Processing and Feature Extraction (Unit 5)

-   Uses a function `is_dead_grass(pixel)`
-   Nested loops iterate through every pixel in all 10 images
-   Calculates a Feature Density Score for each image
-   Results are stored in a master list

------------------------------------------------------------------------

## Code Profiling

The `time` module is used to measure execution time for pixel
processing.\
Execution time is printed to three decimal places.

------------------------------------------------------------------------

## Algorithms and Efficiency (Unit 6)

### Selection Sort

A custom Selection Sort algorithm sorts images by dead grass density
from highest to lowest.

### Binary Search

A Binary Search algorithm allows the user to search for a target grass
percentage.

------------------------------------------------------------------------

## Testing and Robustness

-   Program tested on all images
-   Sorting and searching validated
-   User input handling tested

------------------------------------------------------------------------

## Performance Analysis

Pixel-by-pixel image scanning takes the most processing time.\
Sorting and searching have minimal impact on performance.

------------------------------------------------------------------------

## Challenges Faced

-   Figuring out how to implement selection sort
-   Getting binary search to work

------------------------------------------------------------------------

## Real-World Use Case

Applications include: - Lawn care - Environmental
monitoring - Agricultural analysis

------------------------------------------------------------------------

## Files Included

-   main.py
-   README.md
-   10 lawn images

------------------------------------------------------------------------

## Summary

Overall this was a pretty challenging project. Overcame many challenges over time. Used pixel scanning and functions. Successfully takes deadgrass pixels and achieves the goal.
