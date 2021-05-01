from flask import Flask, render_template, request
import config
from colormap import rgb2hex
import statistics

app = Flask(__name__)

# define all HTTP endpoints that we wish to serve
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/mixcolors", methods=('GET', 'POST'))
def mix_two_colors():
    if request.method == 'POST':
        color1 = request.form['color1']
        color2 = request.form['color2']
        #hex_color = '#0000FF'
        hex_color = get_resultant_color(color1, color2)
        return render_template("mix_colors.html", hex_color = hex_color, color1=color1, color2=color2)

    return render_template("mix_colors.html")

def get_resultant_color(color1, color2):
    #get rgb value of input colors
    rgb_color1 = config.rgb_values[color1]
    rgb_color2 = config.rgb_values[color2]

    result_rgb = []
    for i in range(0,3):
        list_high_low = []
        high = rgb_color1[i]
        low = rgb_color2[i]
        list_high_low.append(rgb_color1[i])
        list_high_low.append(rgb_color2[i])
        #result_rgb[i] = abs(high - low) / 2
        result_rgb.append(round(statistics.median(list_high_low)))

    hex_color = rgb2hex(result_rgb[0], result_rgb[1], result_rgb[2])
    return hex_color




if __name__ == "__main__":
    app.run(debug=True)