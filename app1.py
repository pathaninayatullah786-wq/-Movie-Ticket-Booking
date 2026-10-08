import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# -----------------------------
# Movie and Ticket Data
# -----------------------------
movies = {
    "Avengers: Endgame": 200,
    "Interstellar": 180,
    "RRR": 150,
    "Pushpa 2": 180,
    "Kalki 2898 AD": 200
}

ticket_types = {
    "Regular": 0,
    "Premium": 50,
    "VIP": 100
}

# -----------------------------
# Title
# -----------------------------
st.title("🎬 Movie Ticket Booking")
st.write("Book your movie tickets quickly and easily! 🍿")

st.divider()

# -----------------------------
# Booking Form
# -----------------------------
st.subheader("🎟️ Select Your Tickets")

movie = st.selectbox(
    "🎥 Choose Movie",
    list(movies.keys())
)

ticket_type = st.selectbox(
    "🎫 Ticket Category",
    list(ticket_types.keys())
)

number_of_tickets = st.number_input(
    "👥 Number of Tickets",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

# -----------------------------
# Price Calculation
# -----------------------------
base_price = movies[movie]
extra_price = ticket_types[ticket_type]

price_per_ticket = base_price + extra_price
total_price = price_per_ticket * number_of_tickets

# -----------------------------
# Price Display
# -----------------------------
st.info(
    f"💰 Price per ticket: ₹{price_per_ticket}"
)

st.success(
    f"💵 Total Price: ₹{total_price}"
)

st.divider()

# -----------------------------
# Booking Button
# -----------------------------
if st.button("🎟️ Confirm Booking", use_container_width=True):

    st.session_state.booking_confirmed = True

# -----------------------------
# Booking Summary
# -----------------------------
if st.session_state.get("booking_confirmed", False):

    st.subheader("🧾 Booking Summary")

    st.write(f"🎬 **Movie:** {movie}")
    st.write(f"🎫 **Ticket Type:** {ticket_type}")
    st.write(f"👥 **Number of Tickets:** {number_of_tickets}")
    st.write(f"💰 **Price per Ticket:** ₹{price_per_ticket}")
    st.write(f"💵 **Total Amount:** ₹{total_price}")

    st.success("✅ Booking Confirmed! Enjoy your movie! 🍿🎬")

    if st.button("🔄 New Booking", use_container_width=True):
        st.session_state.booking_confirmed = False
        st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption("🎬 Movie Ticket Booking System | Built with Python & Streamlit")