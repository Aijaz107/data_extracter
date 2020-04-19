from flask import Flask,render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("mainsheet").sheet1
data= sheet.get_all_records()
row = sheet.row_values(3)
col = sheet.col_values(3)
cell = sheet.cell(1,2).value

app  = Flask(__name__)
@app.route('/')
def assignment():
       return render_template('assignment.html',data=data)

if __name__=="__main__":
    app.run(debug=True)     

