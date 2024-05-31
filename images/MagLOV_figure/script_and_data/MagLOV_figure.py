import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker
from tifffile import imread, imwrite

plt.rcParams["font.family"] = "monospace"

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

encoded_timestamps = imread('timestamps.tif')
timestamps = 1e-6*decode_timestamps(
    encoded_timestamps)['microseconds'].astype('float64')
timestamps = timestamps - timestamps[0]


def smooth_curve(t,
                 a0=None, a1=None, a2=None,
                 T0=None, T1=None, T2=None,
                 c0=None, c1=None, c2=None,):
    return (a0 * 2**(-t/T0) + a1 * 2**(-t/T1) + a2 * 2**(-t/T2)
            + c0 + c1*t + c2*t**2)

def lower_bound_fit(t, y, t_desired):
    popt, pcov = curve_fit(
                    smooth_curve, t, y,
                    [(y.max()-y.min()) / 8, # a0 initial guess
                     (y.max()-y.min()) / 4, # a1 initial guess
                     (y.max()-y.min()) / 2, # a2 initial guess
                     0.01, 0.1, 1,          # T0, T1, T2 initial guess
                     y.min(), 0., 0.])      # c0, c1, c2 initial guess
##    print("\na0: ", popt[0],
##          "\na1: ", popt[1],
##          "\na2: ", popt[2],
##          "\nT0: ", popt[3],
##          "\nT1: ", popt[4],
##          "\nT2: ", popt[5],
##          "\nc0: ", popt[6],
##          "\nc1: ", popt[7],
##          "\nc2: ", popt[8])
    return smooth_curve(t_desired, *popt)


titles = [
'                [Unused]                                 ',
'                Background                               ',
'                AsLOV2                                   ',
'Round 0 winner: AsLOV2 C450A                             ',
'Round 1 winner: AsLOV2 C450A D540M                       ',
'Round 2 winner: AsLOV2 C450A D540M Q513A                 ',
'Round 3 winner: AsLOV2 C450A D540M Q513A L496V           ',
'Round 4 winner: AsLOV2 C450P D540M Q513A L496V           ',
'Round 5 winner: AsLOV2 C450P D540M Q513K L496V           ',
'Round 6 winner: AsLOV2 C450P D540M Q513K L496V G528K     ',
]

for p in range(1, 10):
    data = np.genfromtxt('%i.csv'%(p), delimiter = ',',
                         skip_header=1, usecols=1)
    field_turns_off_s = np.arange(3.66, 76, 9.98)
    field_turns_on_s =  np.arange(8.69, 76, 9.98)
    field_turns_on_s =  np.concatenate(((0,), field_turns_on_s)) # Field on @t=0
    field_turns_off_idx = np.searchsorted(timestamps, field_turns_off_s)
    field_turns_on_idx  = np.searchsorted(timestamps, field_turns_on_s)

    idx = np.concatenate((np.arange(24), field_turns_off_idx))
    lower_fit = lower_bound_fit(timestamps[idx], data[idx], timestamps)
    residuals = data - lower_fit
    
    plt.clf()
    f, (ax, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 0.6]})

    # Show the raw data, and a lower-bound fit
    ax.plot(timestamps, data, '-', label = 'F  (Raw data)' )
    ax.plot(timestamps, lower_fit, alpha=0.5, color='gray',
            label=r'$F_{fit}$ (Smooth lower-bound fit)')
    plt.text( # y-label
        -0.12, 0.5, 'Fluorescence (counts/pixel)',
        rotation='vertical',
        horizontalalignment='center',
        verticalalignment='center',
        transform = ax.transAxes)
    ax.set_title(titles[p])
    ax.set_xlim(0, 75)
    ax.set_ylim(0, 4*lower_fit.min())
    ax.annotate('Data', (0.84, 0.01), xycoords='axes fraction')
    ax.set_xticklabels([])
    ax.legend(loc=(0.05, 0.05), fontsize=6, framealpha=0.95)

    # Inset to zoom in on a single cycle
    s = slice(220, 290)
    axins = ax.inset_axes(
        [0.65, 0.63, 0.33, 0.35],
        xlim=(timestamps[s][0], timestamps[s][-1]),
        ylim=(data[s].min()-100, data[s].max()+100),
        transform=ax.transAxes)
    ax.indicate_inset_zoom(axins)
    axins.plot(timestamps, data, '.')
    axins.plot(timestamps, lower_fit, alpha=0.5, color='gray')

    # Show the oscillatory residuals
    ax2.annotate('Residuals', (0.84, 0.01), xycoords='axes fraction')
    ax2.plot(timestamps, 100*residuals / lower_fit)
    ax2.set_xlabel('time (seconds)')
    ax2.set_ylabel(r'$( F-F_{fit} ) / F_{fit}$')
    ax2.set_xlim(0, 75)
    ax2.set_ylim(-10, 80)
    ax2.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(100))
    ax2.set_yticks((0, 25, 50, 75))
    ax2.axhline(0, linestyle='--', color='gray')
    ax2.grid('on', alpha=0.1)

    # Show when the field is on and off
    for t_on, t_off in zip(field_turns_on_s, field_turns_off_s):
        for axes in (ax, ax2): #(ax, axins, ax2):
            axes.axvspan(t_on, t_off, facecolor='black', alpha=0.05)

    plt.savefig('%i.png'%(p))

##plt.show()
