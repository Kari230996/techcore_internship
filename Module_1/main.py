from app.utils import greet_user

def main():
    name = input("Введите имя: ")
    message = greet_user(name)
    print(message)

if __name__ == "__main__":
    main()