def celsius_para_fahrenheit(celsius):
   
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)
 