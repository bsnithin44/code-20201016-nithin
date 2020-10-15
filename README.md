## BMI Calculator
This repository is of simple python package to calculate bmi.


### How to use
1. SDK : Install the package using the below code and run in your enironment by refereing to below code.

   ```
   pip install git+https://www.github.com/bsnithin44/code-20201016-nithin/
   ```
   ```
   from bmi import BmiCalculator

   bmi_calculator = BmiCalculator()

   bmi, bmi_category, risk = bmi_calculator.bmi(height = 170, weight = 60)
   ```

2. API : Install the requirements in requirements.txt and the run the below commands.


   ```
   python app.py
   ```

   ```
   curl --location --request POST 'http://localhost:8000/bmi?bmi_category=Overweight' \
   --header 'Content-Type: application/json' \
   --data-raw '[
       {
           "gender":"male",
           "height":157,
           "weight":55
       },
       {
           "gender":"female",
           "height":180,
           "weight":90
       }
   ]'
   ```

### Run tests
```
python bmi_test.py
```

### Additional info
```
The BMI categories are :
   "Normal weight"
   "Overweight"
   "Underweight"
   "Moderately obese"
   "Severely obese"
   "Very severely obese"
```