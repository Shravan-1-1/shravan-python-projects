import os
from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "shravan_super_secret_key_2026"

# Smart Bank Data (tere Day3 code se)
BANK_DATA = "bank_data.json"

def load_bank_data():
    if os.path.exists(BANK_DATA):
        with open(BANK_DATA, 'r') as f:
            return json.load(f)
    return {"balance": 5000, "transactions": []}

def save_bank_data(data):
    with open(BANK_DATA, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    data = load_bank_data()
    return render_template('dashboard.html', 
                         balance=data['balance'], 
                         transactions=data['transactions'][-5:])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username == 'shravan':  # Simple auth
            session['user'] = username
            return redirect(url_for('home'))
    return '''
    <!doctype html>
    <title>Smart Bank - Login</title>
    <h1>🔥 Shravan Smart Bank</h1>
    <form method=post>
        Username: <input type=text name=username value="shravan"><br>
        <input type=submit value=Login>
    </form>
    '''

@app.route('/deposit', methods=['POST'])
def deposit():
    data = load_bank_data()
    amount = float(request.form['amount'])
    data['balance'] += amount
    data['transactions'].append({
        'type': 'Deposit', 
        'amount': amount, 
        'time': '2026-02-28'
    })
    save_bank_data(data)
    return redirect(url_for('home'))

@app.route('/withdraw', methods=['POST'])  
def withdraw():
    data = load_bank_data()
    amount = float(request.form['amount'])
    if data['balance'] >= amount:
        data['balance'] -= amount
        data['transactions'].append({
            'type': 'Withdraw', 
            'amount': -amount, 
            'time': '2026-02-28'
        })
        save_bank_data(data)
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)