from flask import Flask, render_template, request, jsonify, url_for, redirect,flash
from captcha.image import ImageCaptcha
import random
import time

captcha_length = 5
allowed_string = "०१२३४५६७८९अइउएकखगघचछजझटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ"
# vijaychopade"अआइईउऊएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ०१२३४५६७८९"

app = Flask(__name__)

# import ipdb;
# ipdb.set_trace()

def generate_marathi_captcha():
    captcha_code = "".join(
        (random.choice(allowed_string) for i in range(captcha_length))
    )
    current_timestamp = time.strftime("%Y%m%d-%H%M%S")
    image_object = ImageCaptcha(
        fonts=["C:/Users/OM/Desktop/captchaProject/Lohit-Devanagari.ttf"]
    )
    image_object.write(captcha_code, f"./static/{current_timestamp}.png")
    return captcha_code + "+", current_timestamp


@app.route("/welcome")
def welcome():
    return render_template("./welcome.html")


@app.route("/refresh", methods=["GET", "POST"])
def refresh():
    global num3
    if request.method == "GET":
        num3, current_timestamp = generate_marathi_captcha()
        return jsonify(current_timestamp)


@app.route("/")
def login_page():
    global num3
    if request.method == "GET":
        num3, current_timestamp = generate_marathi_captcha()
        return render_template("./loginMarathi.html", file_name=current_timestamp)


@app.route("/captcha/validation", methods=["GET", "POST"])
def captcha_validation():
    if request.method == "GET":
        return redirect(url_for(".login_page"))
    try:
        if request.method == "POST":
            captchaValue = request.form["pi"]
            # userid = request.form["name"]
            # userpass = request.form["pass"]
            # print("userName: "+userid+"\nuserpassword: "+userpass)
            l1 = str(captchaValue)
            l2 = str(num3)
            print(l1, l2)
            l = len(l2) - 1
            l3 = l2[0:l]
            if l1 == l3:
                # if userid == "vijay chopade":
                #     if userpass == 2000:
                        return redirect(url_for(".welcome"))
                #     else:
                #         return "Password Not Match!"
                # else:
                #     return "User ID Not Match!"
            else:
                return render_template("./error.html")

    except:
        return render_template("./error.html")
    


if __name__ == "__main__":
    app.run()
    # app.debug = True
    #vijay chopade
