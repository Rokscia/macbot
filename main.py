from flask import Flask, request, render_template
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mac_address = request.form['text']
        mac_address = re.sub(r'[^0-9a-fA-F]', '', mac_address)
        if len(mac_address) != 12:
            return render_template('index.html', mac_address='Invalid MAC address!')
        first_answer = mac_address[10:12] + mac_address[8:10] + mac_address[6:8] + mac_address[4:6]
        second_answer = 'FFFF' + mac_address[2:4] + mac_address[0:2]
        return render_template('index.html', mac_address=mac_address, first_answer=first_answer, second_answer=second_answer)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
