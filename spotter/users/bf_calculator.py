import math

def male_bf_percent(height: float, waist_inches: float, neck_inches: float) -> float:
    new_bf_percent = 86.010 * math.log10(waist_inches / neck_inches) - 70.041 * math.log10(height) + 36.76
    return new_bf_percent

def female_bf_percent(height: float, waist_inches: float, neck_inches: float, hip_inches: float) -> float:
    new_bf_percent = 163.205 * math.log10(waist_inches + hip_inches - neck_inches) - 97.684 * math.log10(height) - 78.387
    return new_bf_percent
