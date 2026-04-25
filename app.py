import streamlit as st
import time

st.set_page_config(page_title="Licznik spalania pieniędzy", layout="centered", page_icon="🔥")

st.title("🔥 Licznik spalania budżetu miesięcznego")

monthly = st.number_input("Twoja kwota miesięczna (zł)",
                          min_value=100.0,
                          value=10000.0,
                          step=100.0,
                          format="%.0f")

if st.button("🚀 Uruchom licznik", type="primary"):
    seconds_in_month = 365.25 / 12 * 24 * 3600
    rate_per_second = monthly / seconds_in_month

    placeholder = st.empty()
    start_time = time.time()

    while True:
        try:
            elapsed = time.time() - start_time
            spent = elapsed * rate_per_second
            remaining = monthly - spent

            with placeholder.container():
                st.markdown(f"### Czas: **{elapsed:.1f} sekund**")
                st.markdown(f"### Spalone: **{spent:,.2f} zł**")
                st.markdown(f"### Pozostało: **{remaining:,.2f} zł**")
                st.progress(remaining / monthly)

            time.sleep(0.05)
        except:
            st.stop()