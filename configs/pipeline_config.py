import random
import sys, os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
import embeddings

CHECKPOINTS = [
    'runwayml/stable-diffusion-v1-5',
    'stablediffusionapi/flat-2d-animerge', 
    # 'frankjoshua/toonyou_beta6', 
    # 'HeWhoRemixes/seekyou-alpha1-fp16', 
    # 'stablediffusionapi/deliberate-v2'
    ]

EMBEDDINGS_DIR = os.path.join(ROOT_DIR, 'embeddings')
EMBEDDINGS = os.listdir(EMBEDDINGS_DIR)

FIXED_PROMPT = ",((Best quality,Extremely detailed,Masterpiece)),(facial expression),(different hair color and style of Characters:1.7),(((All Characters exist in image)))"

NEGATIVE_PROMPT = "easynegative,badhandv4,(((same character))),poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, overexposed, bad art, distorted face,text,((extra hand)),((extra arm)),NSFW"

# SAVE_DIR = sys.append(ROOT_DIR, image)

TEST_IMAGE_TITLE = "TEST_IMAGE"

seed = random.randint(0,1024)

print(seed)