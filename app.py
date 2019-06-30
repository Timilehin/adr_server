import flask 
import iranlowo
import requests

app = flask.Flask(__name__)

YORUBA_TTS_LINK_BASE = "http://ttsyoruba.com"


@app.route("/")
def index():
    render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    user_input = flask.request.form.get("text")
    result = iranlowo.adr.diacritize_text(user_input)
    yoruba_tts_link = YORUBA_TTS_LINK_BASE + "/?q="+result
    render_template('result.html', user_input=user_input, result=result, yoruba_tts_link=yoruba_tts_link)
    #return ""
    
if __name__ == '__main__':
    print("Flask starting server ...")
    app.run()
