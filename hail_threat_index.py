#Code for the formula to calculate the index of the 4 NWP model variables worked on by Myles, Manuel, and Jonathan
from herbie import Herbie, FastHerbie
from herbie.toolbox import EasyMap, pc
from herbie import paint
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from datetime import datetime, timedelta, time, timezone
import pandas as pd, numpy as np
import xarray as xr
import dask
from matplotlib.colors import ListedColormap


custom_cmap = [ #from notebook.community
    "white", # ND
    "white", # -30
    "mistyrose", # -25
    "darksalmon", # -20
    "orangered", # -15
    "red", # -10
    "firebrick", # -5
    "maroon", # 0
    ]

realcmap = ListedColormap(custom_cmap, name='nws_reflectivity_colors')

ds_file = xr.open_dataset("hrrr_2026031012.nc") #ds_file used to open the netcdf file in order for us to use the data to create plots
ds_file
ds_file = ds_file.rename({"unknown":"cloudtop"})

def map(): #map function used to create our base maps when needed
    fig = plt.figure(figsize=(12,9)) #figure size for us to place our base map
    ax = fig.add_subplot(111, projection=ccrs.LambertConformal()) #projection used for our base map
    ax.set_extent([-107,-79,26,44], ccrs.PlateCarree()) #set extent for our base map to zoom into our area of interest
    ax.add_feature(cfeature.COASTLINE) #coastlines added on our map 
    ax.add_feature(cfeature.STATES, linestyle=':')
    ax.add_feature(cfeature.BORDERS)
    return fig, ax

lon = ds_file['longitude'] #getting the longitude from our ds_file so we can plot our data
lat = ds_file['latitude'] #gettting the latitude from our ds_file so we can plot our data
dataproj = ccrs.PlateCarree() #making PlateCarree in our dataproj so we can add it to our pcolormesh


# Start with all contributions set to 0
vil_density =  (ds_file["veril"] /  ds_file["cloudtop"]) *100
vil_density_5hr_rolling = vil_density.rolling(valid_time=5).max()
def vil_density_index(ds_file,step): #created a function to make it easier to plot the index at different steps
# Start with all contributions set to 0
    vil_density_5hr_rolling_time =vil_density_5hr_rolling.isel(valid_time=step).values
    vil_density_contribution = np.zeros_like(vil_density_5hr_rolling_time)

    mask = (vil_density_5hr_rolling_time >= 0.25) & (vil_density_5hr_rolling_time < 1.75 )
    vil_density_contribution[mask] = (vil_density_5hr_rolling_time[mask] - 0.25) / 1.50

    mask = (vil_density_5hr_rolling_time >= 1.75) 
    vil_density_contribution[mask] = 1.0
    return vil_density_contribution



def refc_index(ds_file, step): #created a function to make it easier to plot the index at different steps
    refc_5hr_rolling = ds_file['refc'].rolling(valid_time=5).max()
    refc_5hr_rolling_time = refc_5hr_rolling.isel(valid_time=step).values
    refc_contribution = np.zeros_like(refc_5hr_rolling_time)

    # Setting the index = 0 if reflectivity is less than 45 
    mask = refc_5hr_rolling_time < 45
    refc_contribution[mask] = 0

    # Creating a linearly increasing index from 0 to 1, for reflectivity in betwene 45 and 60 (inclusive)
    mask = (refc_5hr_rolling_time >= 45) & (refc_5hr_rolling_time <= 60)
    refc_contribution[mask] = ((refc_5hr_rolling_time[mask] - 45) / 15)

    # Setting the index = 1 if reflectivty is greater than 60
    mask = refc_5hr_rolling_time > 60
    refc_contribution[mask] = 1
    return refc_contribution



def cape_index(ds_file,step): #created a function to make it easier to plot the index at different steps

    cape_5hr_rolling = ds_file['cape'].rolling(valid_time=5).max()
    cape_5hr_rolling_time = cape_5hr_rolling.isel(valid_time=step).values
    cape_contribution = np.zeros_like(cape_5hr_rolling_time)

    # Setting the index = 0 if CAPE is less than 1250
    mask = (cape_5hr_rolling_time < 1250)
    cape_contribution[mask] = 0

    # Creating a linearly increasing index from 0 to 1, for CAPE in between 1250 and 2500 (inclusive)
    mask = (cape_5hr_rolling_time >= 1250) & (cape_5hr_rolling_time <= 2500)
    cape_contribution[mask] = (cape_5hr_rolling_time[mask] - 1250) / 1250

    # Setting the index = 1 if CAPE is greater than 2500
    mask = cape_5hr_rolling_time > 2500
    cape_contribution[mask] = 1
    return cape_contribution


def vert_velo_index(ds_file,step): #created a function to make it easier to plot the index at different steps
#Vertical Velocity Parameter Index
    vert_velo_5hr_rolling = ds_file["wz"].rolling(valid_time=5).max()
    vert_velo_5hr_rolling_time = vert_velo_5hr_rolling.isel(valid_time=step).values
    vert_velo_contribution = np.zeros_like(vert_velo_5hr_rolling_time)

    mask = (vert_velo_5hr_rolling_time >= 0) & (vert_velo_5hr_rolling_time < 0.55)
    vert_velo_contribution[mask] = (vert_velo_5hr_rolling_time[mask] - 0) / 1.45

    mask = (vert_velo_5hr_rolling_time >= 0.55) & (vert_velo_5hr_rolling_time < 1.2)
    vert_velo_contribution[mask] = (vert_velo_5hr_rolling_time[mask] - 0.20) / 1

    mask = (vert_velo_5hr_rolling_time >= 1.2)
    vert_velo_contribution[mask] = 1
    return vert_velo_contribution


#Code for implementing the algorithm function worked on by Myles, Jonathan, and Manuel
# Research used to inform our weighting: 
# https://www.weather.gov/ohx/vildensityhailsize
# https://www.weather.gov/media/wrh/online_publications/TAs/TA1005.pdf
def hail_index(ds_file,step):
    cape_5hr_rolling = ds_file['cape'].rolling(valid_time=5).max()
    cape_5hr_rolling_time = cape_5hr_rolling.isel(valid_time=step).values
    cape_contribution = np.zeros_like(cape_5hr_rolling_time)

    # Setting the index = 0 if CAPE is less than 1250
    mask = (cape_5hr_rolling_time < 1250)
    cape_contribution[mask] = 0

    # Creating a linearly increasing index from 0 to 1, for CAPE in between 1250 and 2500 (inclusive)
    mask = (cape_5hr_rolling_time >= 1250) & (cape_5hr_rolling_time <= 2500)
    cape_contribution[mask] = (cape_5hr_rolling_time[mask] - 1250) / 1250

    # Setting the index = 1 if CAPE is greater than 2500
    mask = cape_5hr_rolling_time > 2500
    cape_contribution[mask] = 1

    refc_5hr_rolling = ds_file['refc'].rolling(valid_time=5).max()
    refc_5hr_rolling_time = refc_5hr_rolling.isel(valid_time=step).values
    refc_contribution = np.zeros_like(refc_5hr_rolling_time)

    # Setting the index = 0 if reflectivity is less than 45 
    mask = refc_5hr_rolling_time < 45
    refc_contribution[mask] = 0

    # Creating a linearly increasing index from 0 to 1, for reflectivity in betwene 45 and 60 (inclusive)
    mask = (refc_5hr_rolling_time >= 45) & (refc_5hr_rolling_time <= 60)
    refc_contribution[mask] = ((refc_5hr_rolling_time[mask] - 45) / 15)

    # Setting the index = 1 if reflectivty is greater than 60
    mask = refc_5hr_rolling_time > 60
    refc_contribution[mask] = 1

    vil_density_5hr_rolling_time =vil_density_5hr_rolling.isel(valid_time=step).values
    vil_density_contribution = np.zeros_like(vil_density_5hr_rolling_time)

    mask = (vil_density_5hr_rolling_time >= 0.25) & (vil_density_5hr_rolling_time < 1.75 )
    vil_density_contribution[mask] = (vil_density_5hr_rolling_time[mask] - 0.25) / 1.50

    mask = (vil_density_5hr_rolling_time >= 1.75) 
    vil_density_contribution[mask] = 1.0

    #vert velo index being created
    vert_velo_5hr_rolling = ds_file["wz"].rolling(valid_time=5).max()
    vert_velo_5hr_rolling_time = vert_velo_5hr_rolling.isel(valid_time=step).values
    vert_velo_contribution = np.zeros_like(vert_velo_5hr_rolling_time)

    mask = (vert_velo_5hr_rolling_time >= 0) & (vert_velo_5hr_rolling_time < 0.55)
    vert_velo_contribution[mask] = (vert_velo_5hr_rolling_time[mask] - 0) / 1.45

    mask = (vert_velo_5hr_rolling_time >= 0.55) & (vert_velo_5hr_rolling_time < 1.2)
    vert_velo_contribution[mask] = (vert_velo_5hr_rolling_time[mask] - 0.20) / 1

    mask = (vert_velo_5hr_rolling_time >= 1.2)
    vert_velo_contribution[mask] = 1

    hail_index_calc = (cape_contribution * 0.20 + refc_contribution * 0.225 + vil_density_contribution * 0.35 + vert_velo_contribution * 0.225) * 100
    return hail_index_calc


#Code to automate plot generation worked on by Myles
for i in [9,12,15,18,21,24]: #creating for loop over time of the 6 time steps we plotted
    fig, axes = map() #calling map function
    pcolor4 = axes.pcolormesh(lon, lat, hail_index(ds_file,i), cmap = realcmap, vmax = 100, transform = dataproj) #creating a pcolormesh map for hail index at step 9
    plt.colorbar(pcolor4, ax=axes, label = 'Hail Index', shrink = 0.7) #creating colorbar for the map
    axes.set_title(f"Hail Index\n HRRR - Initial Time: {pd.to_datetime(ds_file['valid_time'].isel(valid_time=0).values):%HZ %a %b %d %Y} | Valid Time: {pd.to_datetime(ds_file['valid_time'].isel(valid_time=i).values):%HZ %a %b %d %Y}") #title for map at step 9 with model name, valid time and initial time
    file_name = "Hail_Index_{0:03d}.png".format(i) #creating hail index file name and formatting it so it can be in terms of time
    plt.savefig(file_name) #saving hail index figs with the file name format