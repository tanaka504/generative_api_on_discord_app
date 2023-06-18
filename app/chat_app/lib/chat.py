import copy
from rwkv.model import RWKV
from rwkv.utils import PIPELINE, PIPELINE_ARGS


class RWKVChat:
    TOKENIZER_PATH = "data/20B_tokenizer.json"
    MODEL_PATH = "data/RWKV-4-Raven-7B-v6-EngChnJpn-20230401-ctx4096.pth"
    STRATEGY = "cuda fp16"
    ARGS = PIPELINE_ARGS(
        temperature=1.0,
        top_p=0.8,
        top_k=100,
        alpha_frequency=0.25,
        alpha_presence=0.25,
        token_ban=[],
        token_stop=[0],
        chunk_len=256
    )
    CHUNK_LEN = 256

    def __init__(self) -> None:
        self.model = RWKV(model=self.MODEL_PATH, strategy=self.STRATEGY)
        self.pipeline = PIPELINE(self.model, self.TOKENIZER_PATH)

    def get_answer(self, message, user: str='') -> str:
        prompt = self.__get_prompt(message)
        answer = self.pipeline.generate(prompt, token_count=self.CHUNK_LEN, args=self.ARGS)
        return answer
    
    def __get_prompt(self, instruction):
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

# Instruction:
{instruction}

# Response:
"""

