import numpy as np
import matplotlib.pyplot as plt
from tifffile import imread, imwrite
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes,mark_inset, InsetPosition

def decode_timestamps(image_stack):
    """Decode PCO image timestamps from binary-coded decimal.

    See github.com/AndrewGYork/tools/blob/master/pco.py for the full version
    """
    timestamps = image_stack[:, 0, :14]
    timestamps = (timestamps & 0x0F) + (timestamps >> 4) * 10
    ts = {}
    ts['microseconds'] = np.sum(
        timestamps[:, 8:14] * np.array((3600e6, 60e6, 1e6, 1e4, 1e2, 1)),
        axis=1, dtype='uint64')
    return ts



time_values = imread('timestamps.tif')
timestamps = 1e-6*decode_timestamps(time_values
            )['microseconds'].astype('float64')
timestamps= timestamps-timestamps[0]

data_names = [
           # '100green_10Reds',
            '100Green_20Red',
         #   '100Green_40Red',
         #   '100Green_100Red',
            ]

#488
data = np.zeros((15000))
ax = plt.subplot(111) #whole path

data[:] = np.genfromtxt('{}.csv'.format(data_names[0]),
                                            delimiter = ',',
                                            skip_header=1,
                                            usecols=1)
ax.plot(timestamps, data)
plt.ylabel('Fluorescence')
plt.xlabel('time (seconds)')
ax.set_title('mScarlet + FMN - 35 mW/cm$^2$ 560 nm excitation')
ax.set_xlim(0,500)
ax.set_ylim(5000,13000)
plt.axvspan(0, 75, facecolor='cyan', alpha=0.1)
plt.axvspan(75, 500, facecolor='greenyellow', alpha=0.1)

axins = zoomed_inset_axes(ax,2,loc='lower right')
axins.plot(timestamps, data)
##
x1,x2,y1,y2 = 75,250,10225,10300
axins.set_xlim(x1,x2)
axins.set_ylim(y1,y2)
ip = InsetPosition(axins, [0.19, 0.06, 0.78, 0.75])#left edge, bottom edge, width, height
axins.set_axes_locator(ip)
##
mark_inset(ax,axins,loc1=1,loc2=3)#1,3
plt.savefig('/Users/ingaramo/Desktop/magnetofluorescence-main/images/Scarlet_protein/red_power/Figure_scarlet_FMN_20RedPower.png')
plt.show()




