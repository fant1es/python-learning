import requests

def fetch_status(url: str) -> dict:
    """Выполняет сетевой запрос.
    Возвращает HTTP-статус и тип данных ответа."""
    response = requests.get(url, timeout=5)
    response.raise_for_status() # Вызовет ошибку при HTTP статусе 4xx/5xx       
    
    return {
        "status_code": response.status_code, 
        "content-type": response.headers.get("content-type", "unknown")
        }

def main():
    print("Обращаюсь к https://api.github.com...", end="\n")
    
    try:
        data = fetch_status(url="https://api.github.com")

        print("Готово!", end="\n")
        print(f"HTTP статус: {data['status_code']}",
              f"Значение content-type: {data['content-type']}",
              sep="\n")
                
    except requests.exceptions.Timeout:
        print(f"Ошибка Timeout: время ожидания соединения истекло")
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения: не удалось установить соединение")
    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка HTTP: HTTP статус ответа - {http_err.response.status_code}")
    except requests.exceptions.RequestException:
        print(f"Ошибка: непредвиденная ошибка подключения")
    
if __name__ == "__main__":
    main()