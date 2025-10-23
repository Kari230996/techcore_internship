class DatabaseConnection:
    def __enter__(self):
        """Открывает соединение (эмуляция)."""
        self.conn = "Соединение с базой данных установлено"
        print(self.conn)
        return self  

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрывает соединение, даже если произошла ошибка."""
        print("Соединение закрыто")

        if exc_type:
            print(f"Произошла ошибка: {exc_val}")

        return False



if __name__ == "__main__":
    with DatabaseConnection() as conn:
        print("Работаем с базой данных...")
       
