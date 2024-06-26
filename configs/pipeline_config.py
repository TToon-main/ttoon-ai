import random

CHECKPOINTS = [
    'runwayml/stable-diffusion-v1-5',
    'stablediffusionapi/flat-2d-animerge', 
    # 'frankjoshua/toonyou_beta6', 
    # 'HeWhoRemixes/seekyou-alpha1-fp16', 
    # 'stablediffusionapi/deliberate-v2'
    ]

EMBEDDINGS = [
    '/Users/jaehunchoi/Desktop/JAE/HONGIK/졸업프로젝트/ttoon-ai/embeddings/badhandv4.pt',
    '/Users/jaehunchoi/Desktop/JAE/HONGIK/졸업프로젝트/ttoon-ai/embeddings/EasyNegative.pt'
    ]

FIXED_PROMPT = ",((Best quality,Extremely detailed,Masterpiece)),(facial expression),(different hair color and style of Characters:1.7),(((All Characters exist in image)))"

NEGATIVE_PROMPT = "easynegative,badhandv4,(((same character))),poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, overexposed, bad art, distorted face,text,((extra hand)),((extra arm)),NSFW"

SAVE_DIR = "/Users/jaehunchoi/Desktop/JAE/HONGIK/졸업프로젝트/ttoon-ai/test_outputs/"

TEST_IMAGE_TITLE = "TEST_IMAGE"

seed = random.randint(0,1024)

print(seed)