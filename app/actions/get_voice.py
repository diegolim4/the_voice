import pyaudio
import wave

def catch_audio(duration=3, rate=48000, chunk=1024, format=pyaudio.paInt16, canais=1):
    try:
        pyaudio_obj = pyaudio.PyAudio()
        stream = pyaudio_obj.open(
            format=format, channels=canais, rate=rate, input=True, frames_per_buffer=chunk)

        print("Gravando...")
        
        frames = []

        for i in range(int(rate / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)

        print("Gravação concluída.")

        stream.stop_stream()
        stream.close()
        pyaudio_obj.terminate()

        def save_audio(file_name, frames, rate):
            wf = wave.open(file_name, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
            wf.close()

        save_audio('app/audios/audio_gravado.wav', frames, rate)    
    except Exception as e:
        msg_error = f'Error ao gravar audio:{e}'
        print(msg_error)
        return msg_error
