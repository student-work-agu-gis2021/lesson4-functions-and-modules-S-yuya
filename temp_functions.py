"""A function that converts force temperature from Fahrenheit to Celsius."""
def fahr_to_celsius(temp_fahrenheit):
  converted_temp = (temp_fahrenheit-32)/1.8 
  return converted_temp
  
"""A function that classifies temperature into four different classes."""
def temp_classifier(temp_celsius):
  if temp_celsius < -2:
    return 0
  elif temp_celsius < 2:
    return 1
  elif temp_celsius < 15:
    return 2
  elif temp_celsius >= 15:
    return 3