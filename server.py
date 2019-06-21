import flask 
import iranlowo
app = flask.Flask(__name__)


@app.route("/")
def hello():
    form = """Welome to the Yoruba Diacritizer <br>
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
    return "<h1> Welome to the Yoruba Diacritizer<h1> <br> Undiacritized: " + user_input + "<br> <br> Diacritized: " + result + "<br> <br> <a href='/'>Diacritize more</a>"
    
if __name__ == '__main__':
    print("Loading PyTorch model and Flask starting server ...")
    app.run()
