class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ls = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        ls.append(kelvin)
        ls.append(fahrenheit)
        return ls
        
