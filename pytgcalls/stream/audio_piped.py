from pytgcalls.types import StreamType
from pytgcalls.types.input_stream import InputAudioStream

class AudioPiped(InputAudioStream):
    def __init__(self, file_path: str):
        super().__init__(file_path=file_path, stream_type=StreamType().local_stream)
