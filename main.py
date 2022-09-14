import sounddevice
from scipy.io.wavfile import write

#sample_rate
fs=44100

second = int(input("Saisissez le temps d'enregistrement en secondes : "))
print("Enregistrement en cours.....\n")

record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=1)
sounddevice.wait()

write("enregistrement.wav", fs, record_voice)

print("L'enregistrement est prêt, consulter le répertoire.")
