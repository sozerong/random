from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/random', methods=['POST'])
def generate_random_value():
    # 요청에서 코드를 가져옴
    data = request.get_json()
    code = data.get("code")
    
    # 코드를 실행한 결과에 따라 랜덤 값 생성
    if code:
        random_value = random.randint(1, 100)  # 1~100 사이의 랜덤 값 생성
        return jsonify({"input_code": code, "random_value": random_value})
    else:
        return jsonify({"error": "코드를 입력해주세요."}), 400

if __name__ == '__main__':
    app.run(debug=True)
