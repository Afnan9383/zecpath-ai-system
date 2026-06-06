from screening_ai.transcript_normalizer import clean_transcript_text


def mock_speech_to_text(audio_file_path):
    """
    Mock STT function for project demonstration.
    In production, this will connect to a real STT service.
    """
    sample_outputs = {
        "sample_intro.wav": "Um my name is Afnan and I am interested in AI and data science",
        "sample_experience.wav": "Uh I have three years experience in Python and Django",
        "sample_silence.wav": "",
        "sample_partial.wav": "I think maybe I can join next month"
    }

    file_name = audio_file_path.split("/")[-1].split("\\")[-1]

    return sample_outputs.get(file_name, "I have experience related to this role")


def process_audio_transcript(audio_file_path, question_id, candidate_id, job_id):
    raw_text = mock_speech_to_text(audio_file_path)
    cleaned_result = clean_transcript_text(raw_text)

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "question_id": question_id,
        "audio_file": audio_file_path,
        "raw_transcript": raw_text,
        "cleaned_transcript": cleaned_result["cleaned_text"],
        "status": cleaned_result["status"],
        "flags": cleaned_result["flags"]
    }