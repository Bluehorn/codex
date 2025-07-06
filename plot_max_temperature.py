import sys
from pathlib import Path
import xarray as xr
import matplotlib.pyplot as plt


def main(path, variable=None, output="max_temperature.png"):
    path = Path(path)
    ds = xr.open_dataset(path)
    if variable is None:
        variable = next(iter(ds.data_vars))
    data = ds[variable]
    # Determine dimensions other than time
    other_dims = [dim for dim in data.dims if dim != "time"]
    # Get the highest temperature across space for each day
    daily_max = data.max(dim=other_dims)
    # Convert from Kelvin if values look like Kelvin
    if daily_max.max() > 100:
        daily_max = daily_max - 273.15
    daily_max.plot()
    plt.title("Daily highest temperature")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    print(f"Plot saved to {output}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python plot_max_temperature.py <netcdf_path> [variable] [output_png]")
        sys.exit(1)
    args = sys.argv[1:]
    path = args[0]
    variable = args[1] if len(args) > 1 else None
    output = args[2] if len(args) > 2 else "max_temperature.png"
    main(path, variable, output)
