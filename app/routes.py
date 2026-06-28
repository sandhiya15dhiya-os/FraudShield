from flask import Blueprint, request, jsonify, render_template
from app.detector import detect_anomaly
from app.models import add_transaction, get_history

main = Blueprint('main', __name__)

@main.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "FraudShield is running 🛡️"}), 200
@main.route('/', methods=['GET'])
def dashboard():
    return render_template('index.html')

@main.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    required = ["txn_id", "amount", "hour", "country", "account_id", "timestamp"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    history = get_history()
    result = detect_anomaly(data, history)
    add_transaction(data)

    return jsonify(result), 200

@main.route('/history', methods=['GET'])
def history():
    return jsonify(get_history()), 200

@main.route('/history/clear', methods=['DELETE'])
def clear():
    from app.models import clear_history
    clear_history()
    return jsonify({"message": "History cleared"}), 200