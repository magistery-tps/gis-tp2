import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt


SENTINEL_BANDS = { 'red': 3, 'green': 3, 'blue': 2 }


def raster_visible_bands(raster, bands_by_color = SENTINEL_BANDS):
    bands =  []
    if 'red' in bands_by_color:
        bands.append(raster.GetRasterBand(bands_by_color['red']))
        
    if 'green' in bands_by_color:
        bands.append(raster.GetRasterBand(bands_by_color['green']))
    
    if 'blue' in bands_by_color:
        bands.append(raster.GetRasterBand(bands_by_color['blue']))

    return bands


def plot_raw_raster(bands, figsize):
    img = np.dstack([b.ReadAsArray() for b in bands])    
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(img, interpolation='nearest')
    plt.show()
    return img


def plot_raster(path, bands_by_color = SENTINEL_BANDS, figsize=(15, 10)):
    raster = gdal.Open(path)
    plot_raw_raster(raster_visible_bands(raster, bands_by_color), figsize)
    plt.savefig(f'{path}.png')