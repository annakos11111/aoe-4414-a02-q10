# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts from llh coordinate frame to ecef
# Parameters:
#  lat_deg: latitude in degrees
#  lon_deg: longitude in dgrees
#  hae_km:  height above ellipsoid in km
# Output:
#  r_x_km: x component of radius in km
#  r_y_km: y component of radius in km
#  r_z_km: z component of radius in km
#
# Written by Anna Kosnic

import math as m
import sys 

# constants:
R_E_KM = 6378.1363
E_E    = 0.081819221456

# helper functions
## calculating the denominator of c_e and s_e functions
def calc_denom(ecc,lat_rad):
    return m.sqrt(1-ecc**2 *(m.sin(lat_rad))**2)

# initialize script arguments
lat_deg = float('nan') 
lon_deg = float('nan') 
hae_km = float('nan')

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km  = float(sys.argv[3])
  ...
else:
  print(\
   'Usage: '\
   'python3 python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
  )
  exit()


## script
lat_rad = lat_deg * m.pi / 180
lon_rad = lon_deg * m.pi / 180

denom = calc_denom(E_E, lat_rad)

c_e = R_E_KM/denom
s_e = R_E_KM*(1 - E_E**2)/denom

r_x_km = (c_e + hae_km)*m.cos(lat_rad)*m.cos(lon_rad)
r_y_km = (c_e + hae_km)*m.cos(lat_rad)*m.sin(lon_rad)
r_z_km = (s_e + hae_km)*m.sin(lat_rad)

print('r_x: ' + str(r_x_km) + ', r_y: ' + str(r_y_km) + ', r_z: ' + str(r_z_km))