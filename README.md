# Temperature Conversions

# Temperature Converter

This is a simple temperature converter program written in Python. It can convert temperatures between Celsius, Fahrenheit, and Kelvin.

## Conversion Functions

### Celsius to Fahrenheit

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
```
### Fahrenheit to Celsius

```python
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
```
### Kelvin to Celsius

```python
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius
```
### Celsius to Kelvin

```python
def celsius_to_kelvin(fahrenheit):
    kelvin = celsius + 273.15
    return kelvin
```
### Kelvin to Fahrenheit

```python
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit
```
### Fahrenheit to Kelvin

```python
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin
```

## Usage

1. Run the program.
2. Choose a conversion option from the available options.
3. Enter the temperature value to be converted.
4. The program will perform the chosen temperature conversion and display the result

## Available Options

1. Celsius to Kelvin
2. Kelvin to Celsius
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kelvin to Fahrenheit
6. Fahrenheit to Kelvin

## Notes

The program accepts user input and allows rounding the result to the nearest whole number.
