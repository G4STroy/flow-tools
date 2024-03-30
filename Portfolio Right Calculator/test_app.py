import os
import unittest
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download-template')
def download_template():
    path_to_file = "/Users/troy.lightfoot/Github Projects/flow-tools/Portfolio Right Calculator/resources/Portfolio Right Size Template.xlsx"
    return send_file(path_to_file, as_attachment=True)

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_download_template(self):
        response = self.app.get('/download-template')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('attachment' in response.headers.get('Content-Disposition'))

if __name__ == '__main__':
    unittest.main()
