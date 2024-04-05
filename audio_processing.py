import librosa

def preprocess_and_extract_speech_segment(file_path, top_db=20):
    audio, sr = librosa.load(file_path, sr=None, mono=True)
    # Trim silence
    speech_segment, _ = librosa.effects.trim(audio, top_db=top_db)
    return speech_segment, sr
