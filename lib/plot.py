import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt


SENTINEL_BANDS = { 'red': 3, 'green': 3, 'blue': 2 }


def raster_visible_bands(raster, bands_by_color = SENTINEL_BANDS):
    red   = raster.GetRasterBand(bands_by_color['red'])
    green = raster.GetRasterBand(bands_by_color['green'])
    blue  = raster.GetRasterBand(bands_by_color['blue'])
    return [red, green, blue]


def plot_raw_raster(bands):
    img = np.dstack([b.ReadAsArray() for b in bands])
    plt.imshow(img)
    plt.show()
    return img


def plot_raster(path, bands_by_color = SENTINEL_BANDS):
    raster = gdal.Open(path)
    plot_raw_raster(raster_visible_bands(raster, bands_by_color))
    plt.savefig(f'{path}.png')