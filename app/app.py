from flask import Flask
import sys, os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from datetime import datetime
from models import sd_model, gpt_model, s3_model
from preprocess import gpt_preprocess
from configs import gpt_config, pipeline_config, s3_config

s3 = s3_model.s3_connection()

story = "주인공:(혜원: 검정 긴머리, 흰색 반팔 티셔츠에 빨간색 가디건을 입은 20살 여자)\n등장인물:(친구들: 한국인 여자 3명))\n이야기: 오늘은 오랜만에 학과 동기들과 컨퍼런스를 들으러 가는 날이었다. 오전에 동기 3명과 만나서 서울 코엑스의 전시홀로 향했다. 오전 세션을 듣고, 점심을 먹으러 피자 맛집을 갔는데 정말 맛있었다. 그러고 여러가지 부스를 돌아다니며 게임과 이벤트에 참여했다. 그러고 나머지 저녁세션을 듣고, 집을 갔다. 집에 갈 때 퇴근시간이어서 지하철에 사람이 정말 많아서 힘들었다. 2시간동안 지하철 속 많은 사람들에 껴서 집으로 왔다. 그래도 알찬 하루였다."

app = Flask(__name__)

@app.route('/get_images', methods=['GET'])
def get_images():
    # protagonist, characters, story = gpt_preprocess.input_preprocess(story)
    
    # inputStory = protagonist + ',' + characters + '\n' + story
    # print("inputStory = ")
    # print(inputStory)
    
    # gpt = gpt_model.Prompt()
    # answer = gpt.generate_prompt(inputStory)
    # print("answer = ")
    # print(answer)
    
    # prompts = gpt_preprocess.prompt_preprocess(answer)
    # print("prompts = ")
    # print(prompts) 
    
    # for i in range(len(prompts)):
    #     images = sd_model.generate_image(prompts[i])

    #     for j in range(len(images)):
    #         s3.upload_file(
    #             Filename = images[j],
    #             Bucket = s3_config.S3_BUCKET,
    #             Key = pipeline_config.SAVE_DIR+datetime.today().strftime("%Y%m%d")+'-'+str(i)+f'-{j}'+'.png',
    #             ExtraArgs = {"ContentType": "image/png", "ACL": "public-read"},
    #             )
        
    # s3_model.s3.upload_file(
    #     Filename=os.path.join(ROOT_DIR, 'test_image.png'),
    #     Bucket=s3_config.S3_BUCKET,
    #     Key='test_image',
    #     ExtraArgs={"ContentType": "image/png", "ACL": "public-read"},
    # )
    # return "Image uploaded successfully"
    

    file_path = os.path.join(ROOT_DIR, 'app')
    file_path = os.path.join(ROOT_DIR, 'test_image.png')

    s3_model.s3.upload_file(
            Filename = file_path,
            Bucket = s3_config.S3_BUCKET,
            Key = 'test_image',
            ExtraArgs = {"ContentType": "image/png"},
        )

    return True

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
