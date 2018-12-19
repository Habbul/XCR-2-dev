import pyaudio
import wave
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, frames_per_buffer=CHUNK)
print("Mic :: Recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
stream.stop_stream()
stream.close()
p.terminate()
print("Mic :: Done recording.")

wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

CHUNK = 128 

wf = wave.open('output.wav', 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
window = np.blackman(CHUNK)

list_for_freq_plot = []
data = wf.readframes(CHUNK)
while len(data) == CHUNK*swidth:
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),data))*window
    fftData=abs(np.fft.rfft(indata))**2
    which = fftData[1:].argmax() + 1
    x1 = 0
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
    thefreq = (which+x1)*RATE/CHUNK
    if thefreq > 256:
        if CHUNK < 129:
            CHUNK = 16 * 1024
            window = np.blackman(CHUNK)
        else:
            print "The freq is %f Hz." % (thefreq)
            list_for_freq_plot.append(thefreq)
    data = wf.readframes(CHUNK)
wf.close()
#histogram by 200 hz in time chunks 
print(''.join(map(str, map(lambda x: (int)((x-100) / 200), list_for_freq_plot))))
