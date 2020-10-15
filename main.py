from bmi import BmiCalculator
import json


if __name__ == '__main__':

    with open('data.json','r') as f:
        data = json.load(f)

    bmi_calculator = BmiCalculator()

    over_weight = []
    for i in data:
        bmi, bmi_category, risk = bmi_calculator.bmi(height = i['height'], weight = i['weight'])
        i.update(
            {
                'bmi':bmi,
                "bmi_category":bmi_category,
                "risk":risk
                }
        )

        if bmi_category == 'Overweight':
            over_weight.append(i['gender'])
    
    print(over_weight)