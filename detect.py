import sounddevice as sd
import vosk
import queue 
import json
wake_word="shadow"
model_path ="vosk-model-small-en-us-0.15"
q=queue.Queue()
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model,16000)
def callback(indata,frames,time_,state):
    q.put(bytes(indata))
def detect_wake_word(timeout=5):
    with sd.RawInputStream(samplerate=16000,blocksize=8000,dtype='int16',channels=1,callback=callback):
        sd.sleep(timeout*1000)
        while not q.empty():
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text","").lower()
                if wake_word in text:
                    print("shadow is active")
                    return True
    return False