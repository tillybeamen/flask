from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    num_boxes = 3
    color = 'blue'
    return render_template('index.html', num_boxes=num_boxes, color=color)

@app.route('/play/<int:num_boxes>')
def play_num_boxes(num_boxes):
    color = 'blue'
    return render_template('index.html', num_boxes=num_boxes, color=color)

@app.route('/play/<int:num_boxes>/<color>')
def play_num_boxes_color(num_boxes, color):
    return render_template('index.html', num_boxes=num_boxes, color=color)

if __name__ == '__main__':
    app.run(debug=True)
