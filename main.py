from audio_processing import preprocess_and_extract_speech_segment
from cross_correlation import compare_signals
from config import AUDIO_FILES, SIMILARITY_THRESHOLD

def main():
    base_file_path = AUDIO_FILES['base']
    for file_path in AUDIO_FILES['to_compare']:
        print(f"Comparing {base_file_path} with {file_path}")
        if compare_audio_files(base_file_path, file_path, SIMILARITY_THRESHOLD):
            print(f"Pre-recorded message detected in {file_path}")
        else:
            print(f"Live speech or non-pre-recorded message detected in {file_path}")

def compare_audio_files(file_path_1, file_path_2, threshold):
    segment1, _ = preprocess_and_extract_speech_segment(file_path_1)
    segment2, _ = preprocess_and_extract_speech_segment(file_path_2)
    return compare_signals(segment1, segment2, threshold)

if __name__ == "__main__":
    main()