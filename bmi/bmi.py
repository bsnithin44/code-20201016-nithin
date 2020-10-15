class BmiCalculator():
    def __init__(self):
        self.memo = {}

    def bmi(self, height : int, weight : int)-> tuple:
        """
        Input
        height : int
        float : int

        Returns tuple
        """
        height = (height)
        if (height, weight) not in self.memo:
            bmi = (10**4) *weight / ( height **2)
            bmi_category, risk = self.get_bmi_category_and_risk(bmi)
            
            self.memo[(height, weight)] = (round(bmi,2), bmi_category, risk)
        
        return self.memo[(height, weight)]
    
    def get_bmi_category_and_risk(self, bmi:float)-> tuple:
        """
        bmi : float
        """
        if bmi >=30:
            if bmi >= 35:
                if bmi >=40:
                    val = "Very severely obese","Very high risk"
                else:
                    val = "Severely obese","High risk"
            else:
                val = "Moderately obese","Medium risk"
        else:
            if bmi <= 24.9:
                if bmi <= 18.5:
                    if bmi <= 18.4:
                        val = "Underweight","Malnutrition risk"
                    else:
                        val = "Normal weight","Low risk"
                else:
                    val = "Normal weight","Low risk"
            else:
                val = "Overweight","Enhanced risk"
        return val