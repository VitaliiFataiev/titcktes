import datetime
import streamlit as st

class Ticket:
    def __init__(self, event_name, event_date, price, location):
        self.event_name = event_name
        self.event_date = event_date
        self.price = price
        self.location = location

tickets = []

tickets.append(Ticket("Концерт гурту Imagine Dragons", datetime.datetime(2024, 7, 10), 1200, "НСК \"Олімпійський\", Київ"))
tickets.append(Ticket("Фестиваль Atlas Weekend", datetime.datetime(2024, 6, 27), 2500, "ВДНГ, Київ"))
tickets.append(Ticket("Опера \"Кармен\" в Одеському театрі", datetime.datetime(2024, 8, 15), 800, "Одеський національний академічний театр опери та балету"))
tickets.append(Ticket("Виступ Cirque du Soleil", datetime.datetime(2024, 9, 5), 1500, "Палац спорту, Київ"))
tickets.append(Ticket("Концерт Монатика", datetime.datetime(2024, 5, 25), 700, "Арена Львів, Львів"))

def display_tickets():
    st.subheader("Список квитків")
    for i, ticket in enumerate(tickets):
        st.write(f"{i + 1}. **Назва події:** {ticket.event_name}")
        st.write(f"   **Дата:** {ticket.event_date.strftime('%d.%m.%Y')}")
        st.write(f"   **Ціна:** ₴{ticket.price:.2f}")
        st.write(f"   **Місце:** {ticket.location}")
    st.write(f"Загальна кількість квитків: {len(tickets)}")

def add_ticket():
    st.subheader("Додавання нового квитка")
    event_name = st.text_input("Назва події")
    event_date = st.date_input("Дата події", min_value=datetime.date.today())
    price = st.number_input("Ціна квитка", min_value=0.0)
    location = st.text_input("Місце проведення")
    if st.button("Додати квиток"):
        tickets.append(Ticket(event_name, event_date, price, location))
        st.success("Квиток успішно додано!")

def delete_ticket():
    st.subheader("Видалення квитка")
    if tickets:
        ticket_options = [f"{i + 1}. {ticket.event_name}" for i, ticket in enumerate(tickets)]
        ticket_to_delete = st.selectbox("Оберіть квиток для видалення", ticket_options)
        if st.button("Видалити"):
            index = ticket_options.index(ticket_to_delete)
            del tickets[index]
            st.success("Квиток успішно видалено!")
    else:
        st.warning("Немає квитків для видалення.")

st.title("Платформа продажу музичних квитків")

while True:
    choice = st.sidebar.selectbox("Оберіть дію", ["Показати список квитків", "Додати новий квиток", "Видалити квиток", "Вийти"])

    if choice == "Показати список квитків":
        display_tickets()
    elif choice == "Додати новий квиток":
        add_ticket()
    elif choice == "Видалити квиток":
        delete_ticket()
    elif choice == "Вийти":
        st.write("Дякуємо за використання нашої платформи!")
        break
