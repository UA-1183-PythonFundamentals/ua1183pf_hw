import requests
from util.constants import COUNTRYAPI_KEY

class Country:
    def __init__(self, name:str):
        self.__name = name
        
    def process_dict(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.process_dict(value)
            else:
                return key, value
                
    def get_country_info(self):
        try:
            url = f'https://countryapi.io/api/name/{self.__name}?apikey={COUNTRYAPI_KEY}'
            response = requests.get(url)
            data = response.json()
            
            for country_code in data.keys():
                data = data[country_code]
                        
            official_name = data["official_name"]
            calling_code = data["callingCode"]
            capital = data["capital"]
            region = data["region"]
            subregion = data["subregion"]
            population = data["population"]
            area = data["area"]
            timezones = ', '.join(data["timezones"])
            
            currencies_data = data["currencies"]
            lang_data = data["languages"]
            
            # Currencies
            currencies = []
            for inner_dict in currencies_data.values():
                name_value = inner_dict.get('name')
                if name_value is not None:
                    currencies.append(name_value)
            
            currencies = ', '.join(currencies)
            
            # Lang
            lang_values = list(lang_data.values())
            lang_string = ', '.join(lang_values)
                    
            
            result = f"Official name: {official_name}\n Capital: {capital}\n Region: {region}\n Subregion: {subregion}\n Calling code: {calling_code}\n Population: {population}\n Area of country: {area}\n Timezone: {timezones}\n Currencies: {currencies}\n Language: {lang_string}"
            
            return result
        except Exception as e:
            return "Country not found"
