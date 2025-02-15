import pandas as pd
from flask import Flask, render_template

# Pandas
# csv_data = pd.read_csv('Python-projects-beginner-to-advanced/Sales_analysis/supermarket_sales - Sheet1.csv')
# for x in range(1):
#     a = csv_data.iloc[range(60),16]
#     # print(a)
#     f = open('Python-projects-beginner-to-advanced/Sales_analysis/Rating.csv','a')
#     f.write(str(a))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

app.run(debug=True)