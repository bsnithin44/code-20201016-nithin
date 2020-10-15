from flask import Flask
from bmi import BmiCalculator
from flask import request
from flask import jsonify
app = Flask(__name__)

bmi_calculator = BmiCalculator()

@app.route('/')
def index():
    return "BMI Calculator"

@app.route('/bmi', methods = ['POST'])
def postJsonHandler():
    bmi_category = request.args.get("bmi_category")
    data = request.get_json()
    data_len = len(data)
    category = []

    for i in data:
        bmi, bmi_category, risk = bmi_calculator.bmi(height = i['height'], weight = i['weight'])
        i.update(
            {
                'bmi':bmi,
                "bmi_category":bmi_category,
                "risk":risk
                }
        )
        if bmi_category == bmi_category:
            category.append(i['gender'])

    new_data = {}
    new_data['records'] = data
    new_data['additional_info'] = {
        "type":bmi_category,
        "male_percentage":round(100*category.count('male')/data_len,2),
        "female_percentage":round(100*category.count('female')/data_len,2)
    }
    return jsonify(new_data)
  

if __name__ == '__main__':
    app.run(host='localhost', port= 8000 ,debug=True)