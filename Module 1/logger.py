def logger(message, *args, **kwargs):

    print("=== LOG START ===")
    print(f"Message: {message}")

 
    if args:
        print("Args:", ", ".join(map(str, args)))

 
    if kwargs:
        print("Kwargs:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

    print("=== LOG END ===\n")



logger("Test", 1, 2, user="admin")
logger("Ошибка подключения", "Сервер недоступен", code=500, retry=True)
