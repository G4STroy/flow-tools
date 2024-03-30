from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure this file exists in the 'templates' directory

@app.route('/download-template')
def download_template():
    path_to_file = "resources/template.xlsx"  # Update the path to where your actual template file is
    return send_file(path_to_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
