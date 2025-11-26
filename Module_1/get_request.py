import requests

def get_request():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")
        return None

# Пример использования
result = get_request()

if result:
    print("Успешный ответ от API:")
    print(result)

else:
    print("Произошла ошибка при выполнении запроса.")