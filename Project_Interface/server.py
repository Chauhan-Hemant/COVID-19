import pandas as pd
from flask import Flask, render_template, request
import sentiment
import feature_extract as fe
import opinion_mining as opm

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("/dashboard.html")


@app.route("/dashboard/data_visualization")
def data_visualization():
    return render_template("/data_visualization.html")


@app.route("/dashboard/sentiment_result", methods=['POST'])
def sentiment_analysis():
    site = request.form['site1']
    category = request.form['category1']
    product = request.form['product1']
    df = pd.read_csv("static/CSV/" + site + "/" + category + "/" + product + ".csv")
    result = sentiment.sent_any(df)
    for i in range(len(result)):
        result[i] = round(result[i], 2)
    return render_template("/senti_result.html", product=product, result=result)


@app.route("/dashboard/feature", methods=['POST'])
def feature():
    site = request.form['site2']
    category = request.form['category2']
    product = request.form['product2']
    csv1 = pd.read_csv("static/CSV/" + site + "/" + category + "/" + "fe/feature.csv")
    csv2 = pd.read_csv("static/CSV/" + site + "/" + category + "/" + product + ".csv")
    result = fe.feature_main(csv1, csv2)

    # for key in result:
    #     print(key, "==>", "{:.2f}".format(result[key] * 10))

    return render_template("/feture_result.html", product=product, result=result)


@app.route("/dashboard/opi", methods=['POST'])
def opi():
    site = request.form['site3']
    type = "Opinion Mining"
    category = request.form['category3']
    product = request.form['product3']
    csv1 = pd.read_csv("static/CSV/" + site + "/" + category + "/" + "fe/feature.csv")
    csv2 = pd.read_csv("static/CSV/" + site + "/" + category + "/" + product + ".csv")
    result = opm.opi_main(csv1, csv2)
    return render_template("/opi_result.html", type=type, result=result)


@app.route("/ag1")
def ag1():
    return render_template("/a_bluetooth_speakers.html")


@app.route("/ag2")
def ag2():
    return render_template("/a_cameras.html")


@app.route("/ag3")
def ag3():
    return render_template("/a_earphones.html")


@app.route("/ag4")
def ag4():
    return render_template("/a_hard_disks.html")


@app.route("/ag5")
def ag5():
    return render_template("/a_laptops.html")


@app.route("/ag6")
def ag6():
    return render_template("/a_mobiles.html")


@app.route("/ag7")
def ag7():
    return render_template("/a_pendrives.html")


@app.route("/ag8")
def ag8():
    return render_template("/a_power_banks.html")


@app.route("/ag9")
def ag9():
    return render_template("/a_smart_watches.html")


@app.route("/ag10")
def ag10():
    return render_template("/a_tablets.html")


@app.route("/fg1")
def fg1():
    return render_template("/f_bluetooth_speakers.html")


@app.route("/fg2")
def fg2():
    return render_template("/f_cameras.html")


@app.route("/fg3")
def fg3():
    return render_template("/f_earphones.html")


@app.route("/fg4")
def fg4():
    return render_template("/f_hard_disks.html")


@app.route("/fg5")
def fg5():
    return render_template("/f_laptops.html")


@app.route("/fg6")
def fg6():


@app.route("/fg9")
def fg9():
    return render_template("/f_smart_watches.html")


@app.route("/fg10")
def fg10():
    return render_template("/f_tablets.html")


app.run(host="0.0.0.0", port=4500, debug=True)

    return render_template("/f_mobiles.html")


@app.route("/fg7")
def fg7():
    return render_template("/f_pendrives.html")


@app.route("/fg8")
def fg8():
    return render_template("/f_power_banks.html")