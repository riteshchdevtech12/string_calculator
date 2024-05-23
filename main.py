from string_calculator import StringCalculator

def main():
    calc = StringCalculator()

    inputs = [
        "",
        "1",
        "1,5",
        "1,2,3,4,5",
        "1\n2,3",
        "//;\n1;2"
    ]

    for input_str in inputs:
        try:
            result = calc.add(input_str)
            print(f'input: {input_str}, output: {result}')
        except ValueError as e:
            print(f"Exception {e}")

if __name__ == "__main__":
    main()