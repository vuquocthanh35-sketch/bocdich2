from flask import Flask, request, jsonify, render_template
from engine_dich import lap_que_tang_san

app = Flask(__name__)
cau_hoi_gan_nhat = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    global cau_hoi_gan_nhat
    question = request.json.get('question', '').strip()
    
    # Nếu người dùng nhắn câu thúc giục ngắn khi vừa đợi 15s, tự động dùng lại mong cầu trước đó
    tu_tiep_noi = ["xin kết quả", "xem lại", "tiếp tục", "giải lại", "trả lời đi", "qua 15 giây"]
    if any(w in question.lower() for w in tu_tiep_noi) and cau_hoi_gan_nhat:
        question = cau_hoi_gan_nhat
    else:
        cau_hoi_gan_nhat = question

    bang_que, luan_giai = lap_que_tang_san(question)
    return jsonify({'bang_que': bang_que, 'luan_giai': luan_giai})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
