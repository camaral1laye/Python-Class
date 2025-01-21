class TipCalculator:
    def __init__(self, bill_amount):
        self.bill_amount = bill_amount

    def get_tip_rate(self):
        if self.bill_amount > 150:
            return 0.20
        elif self.bill_amount > 50:
            return 0.15
        else:
            return 0.10

    def calculate_tip(self):
        tip_rate = self.get_tip_rate()
        tip = self.bill_amount * tip_rate
        return round(tip, 2)

    def total_amount(self):
        tip_rate = self.get_tip_rate()
        total = self.bill_amount + (self.bill_amount * tip_rate)
        return round(total, 2)