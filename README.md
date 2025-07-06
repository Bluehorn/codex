# Codex

This repository demonstrates a simple script to visualize maximum
temperatures from a NetCDF data set. Install the project dependencies
and run the plotting script.

## Setup

```bash
pip install -e .
```

The script `plot_max_temperature.py` requires a local NetCDF file as
input. Due to network restrictions this repository does not fetch data
from the internet. Download a NetCDF file manually from
https://opendata.dwd.de/ and pass the path to the script.

## Example

```bash
python plot_max_temperature.py /path/to/air_temperature_max.nc
```

Optionally specify the variable name and output image filename:

```bash
python plot_max_temperature.py /path/to/file.nc tasmax output.png
```
