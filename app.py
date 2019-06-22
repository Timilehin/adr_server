import flask 
import iranlowo
import requests

app = flask.Flask(__name__)

YORUBA_TTS_LINK_BASE = "http://ttsyoruba.com"


@app.route("/")
def hello():
    form = """<h1> Welome to the Yoruba Diacritizer</h1> <br>
      <form action="/predict" method="POST">
        Undiacritized Yoruba:<br>
        <input type="text" name="text"><br>
        <input type="submit" value="Submit">
      </form>"""
    return form


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    user_input = flask.request.form.get("text")
    result = iranlowo.adr.diacritize_text(user_input)
    yoruba_tts_link = YORUBA_TTS_LINK_BASE + "/?q="+result
    return "<h1> Welome to the Yoruba Diacritizer</h1> <br> Undiacritized: " + user_input + "<br> <br> Diacritized: " + result + "<br> <br> <a href='" + yoruba_tts_link + "'>Hear it </a> <br> <br> <a href='/'>Diacritize more</a>"
    
if __name__ == '__main__':
    print("Flask starting server ...")
    app.run()
