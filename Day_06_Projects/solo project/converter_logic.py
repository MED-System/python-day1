class CurrencyConverter:
    def __init__(self):
        # These are the Exchange Rates (compared to 1 Dollar)
        self.rates = {
            "EUR": 0.92,
            "GBP": 0.79,
            "JPY": 150.0
        }

    def convert(self, amount, currency_type):
        if currency_type in self.rates:
            return amount * self.rates[currency_type]
        else:
            return None