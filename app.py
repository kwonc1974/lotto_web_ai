from flask import Flask, render_template, request, jsonify
from hybrid_generator import generate_hybrid_numbers
from smart_generator import generate_weighted_numbers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    hybrid_count = int(request.args.get('hybrid', 0))
    smart_count = int(request.args.get('smart', 0))
    total = hybrid_count + smart_count

    if total > 10:
        return jsonify({'error': '총 추천 수는 최대 10게임까지만 가능합니다.'}), 400

    hybrid = generate_hybrid_numbers(hybrid_count)
    smart = generate_weighted_numbers(smart_count)
    result = hybrid + smart
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)




