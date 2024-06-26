from flask import Flask
import models.flat_2d_animerge 
import models.gpt_model

pipeline, generator = models.flat_2d_animerge.generate_model()
gpt = models.gpt_model.Prompt()

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080")    

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