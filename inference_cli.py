import argparse
from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from utils.prompt_making import make_prompt

preload_models()

def synthesize(args):

    save_path = args.output_dir
    make_prompt(name="tmp", audio_prompt_path=args.ref_audio, transcript=args.prompt_text)

    audio_array = generate_audio(args.text, prompt="tmp")

    # Save the generated audio
    write_wav(save_path, SAMPLE_RATE, audio_array)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VALL-E-X CLI")
    parser.add_argument("--ref_audio", type=str, required=True, help="Reference audio file")
    parser.add_argument("--text", type=str, required=True, help="Text to synthesize")
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory")
    parser.add_argument("--prompt_text", type=str, required=True, help="Prompt text")

    args = parser.parse_args()

    synthesize(args)
