import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt 
import urllib2 
import numpy as np

response = urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav') 
print(response.info()) 

WAV_FILE = 'smashingbaby.wav' 
filehandle = open(WAV_FILE, 'w') 
filehandle.write(response.read()) 
filehandle.close() 

sample_rate, data = scipy.io.wavfile.read(WAV_FILE) 
print("Data type", data.dtype, "Shape", data.shape)
# ('Data type', dtype('uint8'), 'Shape', (43584L,))

plt.subplot(2, 1, 1)
plt.title("Original") 
plt.plot(data)

b,a = scipy.signal.iirdesign(wp=0.2, ws=0.1, gstop=60, gpass=1, ftype='butter')

filtered = scipy.signal.lfilter(b, a, data)

plt.subplot(2, 1, 2) 
plt.title("Filtered") 
plt.plot(filtered)

scipy.io.wavfile.write('filtered.wav', sample_rate, filtered. astype(data.dtype))
plt.show()
