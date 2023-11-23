from random import randint
# # def new(*args):
# #     num = int(0)
# #     for n in args:
# #         num += n
# #     print(num)
# #
# #
# # new(4, 5, 6, 7, 8, 9, 0)
from flask import Flask
app = Flask(__name__)
# if __name__ == "__main__":
#      app.run()
# # def bold(function):
# #     def make_bold():
# #
# #         return f"<b> {function()} </b>"
# #     return make_bold
# # def emphasis(function):
# #     def emphasised():
# #         return "<em>" + function() + "</em>"
# #     return emphasised
# # def make_bold(function):
# #     def bold():
# #        return "<b>" + function() + "</b>"
# #     return bold
# #
# # def make_underlined(function):
# #     def underline():
# #         return "<u>" + function() + "</u>"
# #     return underline
# #
# # @app.route("/")
# #
# # @bold("/")
# # @emphasis("/")
# # @make_underlined("/")
# # def home_page():
# #     print("what is your name")
# #
# #
# # @app.route("/username/<name>")
# # def hello_world(name):
# #     return f"hello {name}"
# #
# # @app.route("/")
# # 
# #
#


@app.route("/")
def home():
    return "<h1> guess a number between 0 and 9 </h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


random_number = randint(0, 9)


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True, )
