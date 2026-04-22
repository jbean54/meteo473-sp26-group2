# Meteo 473 Threat Index — Group 1

## Project Description
The "Hail Threat Index" is designed to determine the probability of a hail at a specific location. The index was created by utilizing HRRR model data to extract multiple variables that are proven to have a correlation with hail probability. These variables include vertical velocity, convective available potential energy (CAPE), reflectivity, and vertically integrated liquid (VIL) density. After comparing the variables to recorded hail reports from March 10, 2026, we designed a formula for a hail probability index based on the prescence of these variables. Using this formula, we can generate hail probability risks given model data for any location and any event. 

## Group Members
- Manuel Amdur
- Myles McKell
- Jonathan Murray

## How to Run
1. Download data by running `download_data.py`
2. Generate plots by running `threat_index.py`

## License
MIT
