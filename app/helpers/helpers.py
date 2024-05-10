from pathlib import Path

def path_audio(name_audio):
    try:
        dir_path_audios = Path(__file__).resolve().parent.parent

        path_audios = dir_path_audios / 'audios'

        if not path_audios.exists():
            path_audios.mkdir()

        
        full_path_audio = path_audios / name_audio

        return full_path_audio

    except Exception as e:
        msg_error = e
        print('Error - path_audio: ', msg_error)
        return msg_error