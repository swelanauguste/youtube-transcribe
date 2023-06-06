import uuid

import whisper
from celery import shared_task
from .models import AudioTranscription


@shared_task
def process_transcription(job_id):
    job = AudioTranscription.objects.get(id=job_id)
    audio_path = job.audio_file.path

    try:
        model = whisper.load_model("base")
        response = model.transcribe(audio_path, fp16=False)
        job.status = "processing"
        job.save()
        job.transcript = response["text"]
        job.status = "complete"
        job.save()
    except Exception as e:
        print(str(e))
        job.status = "failed"
        job.save()
    return f'{job.status}'
