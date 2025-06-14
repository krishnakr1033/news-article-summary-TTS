# import backend
# from packages import *
import streamlit as st
import math
import json

def mainContent(df):
    if df.empty:
        st.warning("No data available to display.")
        return

    # Settings
    ITEMS_PER_PAGE = 9
    COLUMNS = 1

    total_pages = math.ceil(len(df) / ITEMS_PER_PAGE)
    st.session_state.page = min(st.session_state.get("page", 1), total_pages)

    # Pagination controls
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅ Prev") and st.session_state.page > 1:
            st.session_state.page -= 1
    with col3:
        if st.button("Next ➡") and st.session_state.page < total_pages:
            st.session_state.page += 1

    # Show current page
    st.markdown(f"### Page {st.session_state.page} of {total_pages}")

    # Compute current page slice
    start_idx = (st.session_state.page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    page_data = df.iloc[start_idx:end_idx]

    # Render each row
    for _, row in page_data.iterrows():
        cols = st.columns(COLUMNS)
        for col in cols:
            with col:
                st.markdown(f"### {row.get('title', 'No Title')}")
                st.write(f"**Description:** {row.get('description', 'N/A')}")
                # st.write(f"**URL:** {row.get('url', 'N/A')}")
                st.link_button("**URL**",row.get('url', 'N/A'))
                st.write(f"**Category:** {row.get('category', 'N/A')}")
                st.write(f"**Language:** {row.get('language', 'N/A')}")
                st.write(f"**Published At:** {row.get('published_at', 'N/A')}")
                st.write(f"**Domain Address:** {row.get('domain_address', 'N/A')}")

                with st.expander("🔍 More Info / Extended Study"):
                    st.write(row.get("extra_info", "No additional information available."))

                st.markdown("---")