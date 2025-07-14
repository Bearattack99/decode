from flask import Flask, render_template, request

app = Flask(__name__)

ENCODING_MAP = {
    'a': 'a', 'b': 'c', 'c': 'e', 'd': 'f', 'e': 'h',
    'f': 'j', 'g': 'l', 'h': 'm', 'i': 'o', 'j': 'q',
    'k': 's', 'l': 't', 'm': 'v', 'n': 'x', 'o': 'y',
    'p': 'b', 'q': 'd', 'r': 'g', 's': 'i', 't': 'k',
    'u': 'n', 'v': 'p', 'w': 'r', 'x': 'u', 'y': 'w',
    'z': 'z',
    'A': 'A', 'B': 'C', 'C': 'E', 'D': 'F', 'E': 'H',
    'F': 'J', 'G': 'L', 'H': 'M', 'I': 'O', 'J': 'Q',
    'K': 'S', 'L': 'T', 'M': 'V', 'N': 'X', 'O': 'Y',
    'P': 'B', 'Q': 'D', 'R': 'G', 'S': 'I', 'T': 'K',
    'U': 'N', 'V': 'P', 'W': 'R', 'X': 'U', 'Y': 'W',
    'Z': 'Z'
}

DECODING_MAP = {v: k for k, v in ENCODING_MAP.items()}

def transform_text(text, mapping):
    return ''.join([mapping.get(char, char) for char in text])

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['input_text']
        if 'encode' in request.form:
            result = transform_text(text, ENCODING_MAP)
        elif 'decode' in request.form:
            result = transform_text(text, DECODING_MAP)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()