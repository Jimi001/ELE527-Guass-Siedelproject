import math


def round_to_significant_figures(number, num_significant_figures):
    if number == 0:
        return 0

    magnitude = math.floor(math.log10(abs(number)))  # Determine the magnitude of the value
    scale = 10 ** (
            num_significant_figures - 1 - magnitude)  # Calculate the scale to round to the specified significant figures

    rounded_value = round(number * scale) / scale  # Multiply by scale, round, and divide by scale to achieve rounding

    return rounded_value
