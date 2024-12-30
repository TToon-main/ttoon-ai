from flask import Flask
import sys, os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from datetime import datetime
from models import sd_model, gpt_model, s3_model
from preprocess import gpt_preprocess
from configs import gpt_config, pipeline_config, s3_config

s3 = s3_model.s3_connection()

app = Flask(__name__)

@app.route('/get_images', methods=['GET'])
def get_images():
    protagonist, characters, story = gpt_preprocess.input_preprocess(story)
    
    inputStory = protagonist + ',' + characters + '\n' + story
    print("inputStory = ")
    print(inputStory)
    
    gpt = gpt_model.Prompt()
    answer = gpt.generate_prompt(inputStory)
    print("answer = ")
    print(answer)
    
    prompts = gpt_preprocess.prompt_preprocess(answer)
    print("prompts = ")
    print(prompts) 
    
    for i in range(len(prompts)):
        images = sd_model.generate_image(prompts[i])

        for j in range(len(images)):
            s3.upload_file(
                Filename = images[j],
                Bucket = s3_config.S3_BUCKET,
                Key = pipeline_config.SAVE_DIR+datetime.today().strftime("%Y%m%d")+'-'+str(i)+f'-{j}'+'.png',
                ExtraArgs = {"ContentType": "image/png", "ACL": "public-read"},
                )
        
    s3_model.s3.upload_file(
        Filename=os.path.join(ROOT_DIR, 'test_image.png'),
        Bucket=s3_config.S3_BUCKET,
        Key='test_image',
        ExtraArgs={"ContentType": "image/png", "ACL": "public-read"},
    )
    return "Image uploaded successfully"
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
