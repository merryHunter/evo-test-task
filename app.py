from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run()