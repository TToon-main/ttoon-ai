import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from configs import pipeline_config
from diffusers import StableDiffusionPipeline,DPMSolverSinglestepScheduler
import transformers
import torch
import warnings
# from datetime import datetime
warnings.filterwarnings('ignore')

def generate_model():
    clip_skip = 2
    text_encoder = transformers.CLIPTextModel.from_pretrained(
        pipeline_config.CHECKPOINTS[0],
        subfolder = "text_encoder",
        torch_dtype = torch.float16,
        num_hidden_layers = 12 - (clip_skip - 1))

    scheduler = DPMSolverSinglestepScheduler.from_pretrained(
        pipeline_config.CHECKPOINTS[0]
        ,subfolder="scheduler")

    pipeline = StableDiffusionPipeline.from_pretrained(
        pipeline_config.CHECKPOINTS[0]
        ,torch_dtype = torch.float16
        ,safety_checker = None
        ,requires_safety_checker = False
        ,scheduler=scheduler
        ,text_encoder = text_encoder)

    pipeline.load_textual_inversion(pipeline_config.EMBEDDINGS[0])
    pipeline.load_textual_inversion(pipeline_config.EMBEDDINGS[1])

    pipeline.to("cuda")

    generator = torch.Generator("cuda").manual_seed(pipeline_config.seed)
    
    return pipeline, generator

def generate_image(pipeline, generator, prompt):
    image = pipeline(prompt + pipeline_config.FIXED_PROMPT,
                    negative_prompt = pipeline_config.NEGATIVE_PROMPT,
                    generator = generator,
                    num_inference_steps = 23,
                    guidance_scale = 8,
                    width = 512,
                    height = 512,
                    num_images_per_prompt = 3
                    ).images

    return image

# def save_image1(image, image_no):
#         for i in range(len(image)):
#             image[i].save(SAVE_DIR[1]+datetime.today().strftime("%Y%m%d")+'-'+TEST_IMAGE_TITLE+image_no+f'-{i}'+'.png')