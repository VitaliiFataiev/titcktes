import streamlit as st
import datetime
import json
import os

class Ticket:
    def __init__(self, event_name, event_date, price, location):
        self.event_name = event_name
        self.event_date = event_date
        self.price = price
        self.location = location

tickets = []

def display_tickets():
    st.write("## Список квитків")
    for i, ticket in enumerate(tickets):
        st.write(f"**{i + 1}. Назва події:** {ticket.event_name}")
        st.write(f"   **Дата:** {ticket.event_date.strftime('%d.%m.%Y')}")
        st.write(f"   **Ціна:** ₴{ticket.price * 28.1:.2f}")
        st.write(f"   **Місце:** {ticket.location}")
        st.write("---")
    st.write(f"**Загальна кількість квитків:** {len(tickets)}")

def add_ticket():
    st.write("## Додавання нового квитка")
    event_name = st.text_input("Назва події:")
    event_date = st.date_input("Дата події:", datetime.date.today())
    price = st.number_input("Ціна квитка (в гривнях):", value=0.0)
    location = st.text_input("Місце проведення:")

    if st.button("Додати квиток"):
        if not event_name or not location:
            st.warning("Будь ласка, введіть назву події та місце проведення.")
            return
        tickets.append(Ticket(event_name, event_date, price / 28.1, location))
        st.success("Квиток успішно додано!")

def delete_ticket():
    st.write("## Видалення квитка")
    if not tickets:
        st.warning("Список квитків порожній.")
        return

    st.write("### Оберіть квиток для видалення:")
    ticket_options = [ticket.event_name for ticket in tickets]
    selected_ticket = st.selectbox("", ticket_options)

    if st.button("Видалити квиток"):
        index_to_delete = ticket_options.index(selected_ticket)
        del tickets[index_to_delete]
        st.success("Квиток успішно видалено!")

def save_to_file():
    filename = "tickets.json"
    data = []
    for ticket in tickets:
        data.append({
            "event_name": ticket.event_name,
            "event_date": ticket.event_date.strftime("%d.%м.%Y"),
            "price": ticket.price,
            "location": ticket.location
        })
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    st.success(f"Дані було успішно збережено у файл {filename}")

def load_from_file():
    filename = "tickets.json"
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                tickets.clear()
                for ticket_data in data:
                    event_name = ticket_data["event_name"]
                    event_date = datetime.datetime.strptime(ticket_data["event_date"], "%d.%м.%Y")
                    price = float(ticket_data["price"])
                    location = ticket_data["location"]
                    tickets.append(Ticket(event_name, event_date, price, location))
            st.success(f"Дані було успішно завантажено з файлу {filename}")
        except Exception as e:
            st.error(f"Помилка завантаження даних з файлу {filename}: {e}")
    else:
        st.warning(f"Файл {filename} не знайдено. Немає даних для завантаження.")

st.title("Платформа продажу музичних квитків")

load_from_file()

menu = ["Показати список квитків", "Додати новий квиток", "Видалити квиток", "Зберегти дані у файл", "Вийти"]
choice = st.sidebar.selectbox("Оберіть дію:", menu)

if choice == "Показати список квитків":
    display_tickets()
elif choice == "Додати новий квиток":
    add_ticket()
elif choice == "Видалити квиток":
    delete_ticket()
elif choice == "Зберегти дані у файл":
    save_to_file()
elif choice == "Вийти":
    save_to_file()  # Збереження перед виходом
    st.write("Дякуємо за використання нашої платформи!")
