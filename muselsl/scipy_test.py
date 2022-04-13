
import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Setting standard filter requirements.
order = 6
fs = 30.0       
cutoff = 3.667  

b, a = butter_lowpass(cutoff, fs, order)

# Plotting the frequency response.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()


# Creating the data for filteration
T = 5.0         # value taken in seconds
n = int(T * fs) # indicates total samples
t = np.linspace(0, T, n, endpoint=False)

data = [[-968.75, 906.25, -240.234375, -968.75, 999.51171875], [-968.75, 871.09375, -246.58203125, -968.75, 999.51171875], [-968.75, 909.1796875, -335.9375, -968.75, 999.51171875], [-968.75, 916.015625, -207.03125, -968.75, 999.51171875], [-968.75, 863.28125, 56.640625, -968.75, 999.51171875], [-968.75, 773.4375, 172.8515625, -968.75, 999.51171875], [-968.75, 585.44921875, 308.59375, -968.75, 999.51171875], [-968.75, 740.234375, 748.53515625, -968.75, 999.51171875], [-968.75, 925.29296875, 850.09765625, -968.75, 998.53515625], [-968.75, 704.1015625, 668.9453125, -968.75, -999.0234375], [-968.75, 711.42578125, 679.6875, -968.75, 994.140625], [-968.75, 742.1875, 502.9296875, -968.75, 988.76953125], [-968.75, 656.73828125, 359.375, -968.75, 996.09375], [-968.75, 875.48828125, 377.44140625, -968.75, -996.58203125], [-968.75, 775.87890625, 264.6484375, -968.75, 981.93359375], [-968.75, 676.26953125, 186.03515625, -968.75, 886.23046875], [-969.23828125, 648.4375, 156.73828125, -968.75, 929.6875], [-968.75, 659.66796875, 115.234375, -968.75, -987.3046875], [-968.75, 940.91796875, 291.50390625, -968.75, 988.28125], [-968.75, 767.08984375, 286.62109375, -968.75, 897.4609375], [-968.75, 537.59765625, 314.94140625, -968.75, 917.96875], [-968.75, 602.5390625, 713.37890625, -968.75, 991.2109375], [-968.75, 541.9921875, 641.6015625, -968.75, -968.26171875], [-968.75, 759.765625, 708.49609375, -968.75, 842.7734375], [-969.23828125, 861.328125, -968.75, -968.75, 599.12109375], [-968.75, 555.6640625, 819.3359375, -968.75, 892.578125], [-968.75, 401.85546875, 759.765625, -968.75, -968.75], [-968.75, 436.03515625, 961.9140625, -968.75, 763.671875], [-968.75, 457.03125, 864.2578125, -968.75, 526.3671875], [-968.75, 422.8515625, 641.11328125, -968.75, 707.03125], [-968.75, 532.2265625, 614.2578125, -968.75, 904.78515625], [-968.75, 631.34765625, 604.98046875, -968.75, 649.4140625], [-968.75, 592.7734375, 465.33203125, -968.75, 300.78125], [-968.75, 406.25, 472.65625, -968.75, 372.55859375], [-968.75, 311.03515625, 565.4296875, -968.75, 623.046875], [-968.75, 382.32421875, 399.90234375, -968.75, 575.68359375], [-968.75, 487.3046875, 234.375, -968.75, 214.35546875], [-968.75, 602.05078125, 103.515625, -968.75, 103.515625], [-968.75, 424.31640625, 143.06640625, -968.75, 452.63671875], [-968.75, 307.6171875, 187.01171875, -968.75, 512.6953125], [-968.75, 412.109375, -36.1328125, -968.75, 111.81640625], [-968.75, 399.4140625, 18.06640625, -968.75, -76.171875], [-968.75, 320.3125, 308.10546875, -968.75, 133.7890625], [-968.75, 332.03125, 347.16796875, -968.75, 227.05078125], [-968.75, 229.98046875, 313.96484375, -968.75, -20.5078125], [-968.75, 398.92578125, 336.9140625, -968.75, -313.96484375], [-968.75, 495.1171875, 360.83984375, -968.75, -159.1796875], [-968.75, 421.38671875, 212.890625, -968.75, 166.015625], [-968.75, 315.91796875, 118.1640625, -968.75, 26.3671875], [-968.75, 251.46484375, 213.37890625, -968.75, -271.484375], [-968.75, 309.5703125, 149.4140625, -968.75, -194.82421875], [-968.75, 319.3359375, 268.5546875, -968.75, 111.81640625], [-968.75, 385.7421875, 216.30859375, -968.75, 131.8359375], [-968.75, 310.05859375, -76.66015625, -968.75, -336.9140625], [-968.75, 229.4921875, -205.078125, -968.75, -555.6640625], [-968.75, 271.484375, -153.80859375, -968.75, -189.94140625], [-968.75, 300.29296875, -88.8671875, -968.75, -34.1796875], [-968.75, 288.0859375, -149.90234375, -968.75, -382.32421875], [-968.75, 173.828125, -245.60546875, -968.75, -641.6015625], [-968.75, 180.6640625, -285.64453125, -968.75, -358.88671875]]
e1, e2, e3, e4, e5 = [], [], [], [], []
for x in range(0,len(data)):
    e1.append(data[x][0])
    e2.append(data[x][1])
    e3.append(data[x][2])
    e4.append(data[x][3])
    e5.append(data[x][4])

# Filtering and plotting
y = butter_lowpass_filter(e3, cutoff, fs, order)

plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()