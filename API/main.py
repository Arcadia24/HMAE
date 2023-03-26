from fastapi import FastAPI, File
import librosa
import io
import soundfile as sf
import os
from PIL import Image
import API.utils as utils
import datetime
import uvicorn

args = {"signal_length" : 5, 
        "hop_length" : 512, 
        "num_mels" : 128, 
        "fmin" : 20, 
        "fmax" : 16000}

audio_path = 'dataset/audio_module/'
spectrogram_path = 'dataset/spectrogram_module/'

def last_name(path : str) -> int:
    # find last audio name
    file_name = os.listdir(path)
    if len(file_name) == 0:
        return 0
    file_name = sorted(file_name, key=lambda x: int(x.split('.')[0]))
    return int(file_name[-1].split('.')[0])

def save_spectrogram(audio, sr, number, path, args):
    # Split signal into five second chunks
    specs = utils.get_spectrogram(audio, sr, args)
    for mel_spec in specs:
        im = Image.fromarray(mel_spec * 255.0).convert("L")
        im.save(path + f'{number}.png')

app = FastAPI()

@app.post("/module/{module_id}")
async def get_audio(module_id: int, file : bytes = File(...)):
    audio, sr = librosa.load(io.BytesIO(file))
    print(audio.shape, sr, audio.shape[0]/sr)
    number = last_name(audio_path + f'/module{module_id}/') + 1
    sf.write(audio_path + f'/module{module_id}/{number}.wav', audio, sr, subtype='PCM_24')
    with open(f'{module_id}.txt', 'w') as f:
        f.write(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    save_spectrogram(audio, sr, number, spectrogram_path + f'/module{module_id}/', args)
    return 200

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8000)