from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
import time

class ImageGenerator:
    # MODEL_NAME = './data/derrida'
    # MODEL_NAME = 'naclbit/trinart_derrida_characters_v2_stable_diffusion'
    MODEL_NAME = 'gsdf/Counterfeit-V2.5'
    DEVICE = 'cuda'
    DEFAULT_PROMPT = '((masterpiece,best quality))'
    DEFAULT_NEGATIVE_PROMPT = 'EasyNegative, badhandv4'
    STEPS = 25
    SEEDS = [42, 12345]

    def __init__(self) -> None:
        self.pipeline = StableDiffusionPipeline.from_pretrained(self.MODEL_NAME, torch_dtype=torch.float16).to(self.DEVICE)
        self.pipeline.scheduler = EulerDiscreteScheduler.from_config(self.pipeline.scheduler.config)
        # self.generator = torch.Generator(self.DEVICE).manual_seed(0)

    def generate(self, prompt, negative_prompt=''):
        filenames = []
        for seed in self.SEEDS:
            torch.manual_seed(seed=seed)
            image = self.pipeline(
                prompt=f'{self.DEFAULT_PROMPT} {prompt}',
                negative_prompt=f"{self.DEFAULT_NEGATIVE_PROMPT} {negative_prompt}",
                guidance_scale=7.5, 
                width=640,
                height=960,
                num_inference_steps=self.STEPS
            ).images[0]
            filename = f'generated_image.{seed}.{time.time()}.png'
            image.save(f'tmp/{filename}')
            filenames.append(filename)
        return filenames
