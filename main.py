from bmi import BmiCalculator
import json


if __name__ == '__main__':

    with open('data.json','r') as f:
        data = json.load(f)

    data_len = len(data)

    bmi_calculator = BmiCalculator()

    category = []
    bmiCategory = 'Overweight'
    for i in data:
        bmi, bmi_category, risk = bmi_calculator.bmi(height = i['height'], weight = i['weight'])
        i.update(
            {
                'bmi':bmi,
                "bmi_category":bmi_category,
                "risk":risk
                }
        )

        if bmi_category == bmiCategory:
            category.append(i['gender'])

    print(f"Statistics: category - {bmiCategory}")
    print(f"male_percentage: {round(100*category.count('male')/data_len,2)}")
    print(f"female_percentage: {round(100*category.count('female')/data_len,2)}")