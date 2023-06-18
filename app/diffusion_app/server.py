from flask import Flask, request, jsonify

# import base64
# from io import BytesIO
from lib.generator import ImageGenerator


app = Flask(__name__)

image_generator = ImageGenerator()

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.values.get('prompt', '')
    negative_prompt = request.values.get('negative', '')

    filenames = image_generator.generate(prompt=prompt, negative_prompt=negative_prompt)
    # jpeg_data = BytesIO()
    # image.save(jpeg_data, format='JPEG')
    # image_bytes = jpeg_data.getvalue()
    # base64_string = base64.b64encode(image_bytes).decode('utf-8')
    res = {
        'status': 'ok',
        'filenames': filenames
    }

    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
