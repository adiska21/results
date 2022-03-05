from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    pass


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Результаты</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                
                </head>
                <body style="font-size:40px">
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <div class="alert alert-success" role="alert">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div>
                        Составляет {rating}
                    </div>
                    <div class="alert alert-warning" role="alert">
                        Желаем удачи!
                    </div>
                </body>
                </html>'''


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
