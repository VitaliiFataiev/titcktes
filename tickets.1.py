import datetime

class Ticket:
    def __init__(self, event_name, event_date, price, location):
        self.event_name = event_name
        self.event_date = event_date
        self.price = price
        self.location = location

tickets = []

tickets.append(Ticket("Концерт гурту X", datetime.datetime(2024, 4, 10), 100, "Концертний зал \"Музикальний світ\""))
tickets.append(Ticket("Фестиваль Y", datetime.datetime(2024, 5, 15), 80, "Парк \"Сонячний ліс\""))
tickets.append(Ticket("Опера Z", datetime.datetime(2024, 6, 20), 150, "Національний оперний театр"))
tickets.append(Ticket("Виступ артиста A", datetime.datetime(2024, 7, 5), 120, "Культурний центр \"АртХолл\""))
tickets.append(Ticket("Музичний форум B", datetime.datetime(2024, 8, 25), 90, "Конференц-зал \"Гармонія\""))

def display_tickets():
    available_tickets = 0
    for i, ticket in enumerate(tickets):
        print(f"{i + 1}. Назва події: {ticket.event_name}")
        print(f"   Дата: {ticket.event_date.strftime('%d.%m.%Y')}")
        print(f"   Ціна: ₴{ticket.price * 28.1:.2f}")
        print(f"   Місце: {ticket.location}\n")
        available_tickets += 1
    print(f"Загальна кількість квитків: {len(tickets)}")
    print(f"Доступно квитків: {available_tickets}")

def add_ticket():
    event_name = input("Введіть назву події: ")
    event_date = input("Введіть дату події (у форматі дд.мм.рррр): ")
    price = float(input("Введіть ціну квитка: ₴"))
    location = input("Введіть місце проведення: ")
    tickets.append(Ticket(event_name, datetime.datetime.strptime(event_date, "%d.%m.%Y"), price / 28.1, location))
    print("Квиток успішно додано!")

def delete_ticket():
    display_tickets()
    index = int(input("Введіть номер квитка, який потрібно видалити: ")) - 1
    if 0 <= index < len(tickets):
        del tickets[index]
        print("Квиток успішно видалено!")
    else:
        print("Недійсний номер квитка. Спробуйте ще раз.")

if __name__ == "__main__":
    print("Ласкаво просимо до платформи продажу музичних квитків!")
    while True:
        print("\nОберіть дію:")
        print("1. Показати список квитків")
        print("2. Додати новий квиток")
        print("3. Видалити квиток")
        print("4. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            display_tickets()
        elif choice == "2":
            add_ticket()
        elif choice == "3":
            delete_ticket()
        elif choice == "4":
            print("Дякуємо за використання нашої платформи!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
