import librosa
import numpy as np


def get_spectrogram(audio : np.array, sr:int, args : dict) -> list[np.array]:
    """Create mel-spectrogram from audio

    Args:
        audio (np.array): audio to create mel-spectrogram from
        sr (int): sample rate
        args (dict): arguments

    Returns:
        list[np.array]: list of mel-spectrograms
    """
    # Split signal into five second chunks
    sig_splits = []
    for i in range(0, len(audio), int(args["signal_length"] * sr)):
        split = audio[i:i + int(args["signal_length"] * sr)]

        # End of signal?
        if len(split) < int(args["signal_length"] * sr):
            break
        
        sig_splits.append(split)
        
    # Extract mel spectrograms for each audio chunk
    specs = []
    for chunk in sig_splits:
        
        mel_spec = librosa.feature.melspectrogram(y=chunk, 
                                                  sr=sr, 
                                                  n_fft=1024, 
                                                  hop_length=args["hop_length"], 
                                                  n_mels=args["num_mels"], 
                                                  fmin=args["fmin"], 
                                                  fmax=args["fmax"])
    
        mel_spec = librosa.power_to_db(mel_spec, ref=np.max) 
        
        # Normalize
        
        mel_spec -= mel_spec.mean()
        mel_spec /= mel_spec.std()
        
        specs.append(mel_spec)
        
    return specs