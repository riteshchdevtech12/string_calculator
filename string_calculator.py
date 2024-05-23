import re

class StringCalculator:
    def add(self, numbers : str):
        if not numbers:
            return 0
        
        delimiter = ',|\n'

        if numbers.startswith('//'): #check if there is any custom delimiter
            parts = numbers.split('\n', 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]
        
        number_list = re.split(delimiter, numbers)

        integers = []
        negatives = []

        for num in number_list:
            if num:
                value = int(num)
                if value < 0:
                    negatives.append(value)
                else:
                    integers.append(value)

        if negatives:
            raise f"negative numbers not allowed {','.join(map(str, negatives))}"
        else:
            return sum(integers)

