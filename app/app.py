from flask import Flask
from models import sd_model, gpt_model
from preprocess import gpt_preprocess
from configs import gpt_config

pipeline, generator = sd_model.generate_model()
gpt = gpt_model.Prompt(gpt_config.GPT_MODEL)
story = "주인공:(재훈: 검정 머리, 검정색 티셔츠를 입은 20살 남자)\n등장인물:(친구들: 한국인 남자 3명)\n이야기: 오늘은 미국 여행을 가는 날이다. 새벽 4시였지만 너무 설레는 마음으로 인천공항으로 향했다. 이번 여행은 혼자가지 않고 친구 3명과 함께 갔다. 우리는 11시간이라는 긴 비행 끝에 미국 Phoenix Sky Harbor International Airport에 도착하였다. 호텔에 가서 짐을 놓고 우리는 바로 The Grand Canyon을 보러 출발하였다. 역시 The Grand Canyon은 정말 웅장했다. 우리는 더운 와중에도 The Grand Canyon을 배경으로 사진을 엄청 많이 찍었다. 그리고 우리는 저녁을 먹으러 갔다. 저녁으로는 피자에 맥주를 마셨다. 더위가 싹 다 사라지는 기분이이였다."

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080")  
    
    protagonist, characters, story = gpt_preprocess.input_preprocess(story)
    
    inputStory = protagonist + ',' + characters + '\n' + story
    print("inputStory = ")
    print(inputStory)

    answer = gpt.generate_prompt(inputStory)
    print("answer = ")
    print(answer)
    prompts = gpt_preprocess.prompt_preprocess(answer)
    print("prompts = ")
    print(prompts) 
    
# def register_router(flask_app: Flask):
#     from router.auths.auths_router import auths_router

#     from router.diary.diary_router import diary_router
#     from router.stats.stats_router import report_router

#     flask_app.register_blueprint(auths_router)
#     flask_app.register_blueprint(diary_router)
#     flask_app.register_blueprint(report_router)


# def create_app():
#     app = Flask(__name__)
#     register_router(app)

#     return app