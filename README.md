# Meteo 473 Threat Index — Group 1

## Project Description
<b>Hail Threat Index (HTI): Project Description</b> <br>
This project is entitled the "Hail Threat Index." Specifically, the threat is designed to determine the probability that a specific location will see hail. We did this by first analyzing HRRR model data from the severe weather outbreak that occurred on March 10th, 2026. This outbreak produced particularly large hail across the upper Midwest. Using the HRRR data, we extracted multiple variables that are scientifically and experimentally proven to have varying levels of a strong correlation with hail probability. We then curated individual indices for the four variables (Vertically Integrated Liquid (VIL) Density, Vertical Velocity, Reflectivity, CAPE) based on the correlation of various values with hail probability. Then, we generated a mathematical equation that weights each of the four variables, producing a HTI ranging from 0-100, with 100 indicating the highest likelihood of hail. 

Hail Threat Index (HTI): Audience and Purpose <br>
The target audience for the HTI are both meteorologists and the general public. Meteorologists can use this index program in order to better identify where hail is and isn't likely depending on location. The target audience then will become the general public, as meteorologists will be able to more efficiently and reliably forecast and relay information about hail risks. This is the purpose/value of the HTI - it allows meteorologists to better understand the where, when, and why behind hail formation in order to do the best job possible keeping the general public safe from hail events than can at times be destructive or deadly.

## Group Members
- Manuel Amdur
- Myles McKell
- Jonathan Murray

## How to Run
1. Download data by running `download_data.py`
2. Generate plots by running `threat_index.py`

## License
MIT
