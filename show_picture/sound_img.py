import scipy.io.wavfile 
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

plt.subplot(2, 1, 2)
repeated = np.tile(data, 3)
plt.title("Repeated") 
plt.plot(repeated) 

scipy.io.wavfile.write("repeated_yababy.wav", sample_rate, repeated)
plt.show()
