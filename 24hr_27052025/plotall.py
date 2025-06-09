import numpy as np
import matplotlib.pyplot as plt
import glob


skip = 40

for file in glob.glob('*.txt'):
    if 'Background' in file: x, I_background = np.loadtxt(file,skiprows=skip,usecols=(0,1),unpack=True)
    if 'Reference' in file: x, I_ref = np.loadtxt(file,skiprows=skip,usecols=(0,1),unpack=True)

count = 0

for file in glob.glob('*.txt'):
    if 'Reference' not in file and 'Background' not in file: 
        x, I = np.loadtxt(file,skiprows=skip,usecols=(0,1),unpack=True)
        abs = -np.log10((I - I_background)/(I_ref - I_background))
        plt.plot(x,abs,'b-',lw=0.6)
        count += 1

x, I = np.loadtxt('24HourExp_27052025_FLMS018081_10-08-22-355.txt',usecols=(0,1),skiprows=skip,unpack=True)
abs = -np.log10((I - I_background)/(I_ref - I_background))
plt.plot(x, abs, 'k-')

x, I = np.loadtxt('24HourExp_27052025_FLMS018081_10-48-22-285.txt',usecols=(0,1),skiprows=skip,unpack=True)
abs = -np.log10((I - I_background)/(I_ref - I_background))
plt.plot(x, abs, 'r-')

print(count)
    
plt.xlim(200.0,400.0)
plt.show()
