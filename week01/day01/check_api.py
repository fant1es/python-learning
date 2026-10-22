import requests
import sys

def fetch_status(url: str) -> dict:
    """Выполняет сетевой запрос.
    Возвращает HTTP-статус и тип данных ответа."""
    response = requests.get(url, timeout=5)
    
    return {
        "status_code": response.status_code, 
        "content-type": response.headers.get("content-type", "unknown")
        }

def main():
    print("Обращаюсь к https://api.github.com...", end="\n")
    
    try:
        data = fetch_status(url="http://10.255.255.1")

        print("Готово!", end="\n")
        print(f"HTTP статус: {data['status_code']}",
              f"Значение content-type: {data['content-type']}",
              sep="\n")
                
    except requests.exceptions.Timeout:
        print(f"Ошибка Timeout: время ожидания соединения истекло")
        # Теперь с выводом кода завершения (важно для других скриптов, например)
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения: не удалось установить соединение")
        sys.exit(2)
    except requests.exceptions.RequestException as exc:
        print(f"Ошибка: непредвиденная ошибка подключения, {exc}")
        sys.exit(3)
    
if __name__ == "__main__":
    main()