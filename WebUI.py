# python -m streamlit run WebUI.py --theme.base=dark

import validators
import streamlit as st
from URLShortener import URLShortener

WEBSITE_URL = "https://kb-url.streamlit.app/"
# WEBSITE_URL = "http://localhost:8501/" # For testing purposes.

def is_url(url):
    try:
        return validators.url(url)
    except validators.ValidationError:
        return False

if __name__ == "__main__":
    shortener = URLShortener()

    st.set_page_config(
        page_icon=":desktop_computer:",
        page_title="URL Shortener",
    )

    query_params = st.query_params
    if "key" in query_params.keys():
        url = shortener.give_url_from_key(query_params["key"])
        
        if url != "Your link has expired.":
            st.link_button(
                label="Click here to go to your website. (Automatic redirection not possible on streamlit cloud😅)",
                url=url,
                use_container_width=True
            )
        else:
            st.error("Your Link Has Expired!", icon=":material/error:")
            st.link_button(
                label="Click here to go to the home page.",
                url=WEBSITE_URL,
                use_container_width=True
            )

    else:
        st.title("URL Shortener")
        url = st.text_input("Enter your URL")
        submit_btn = st.button("Submit", use_container_width=True)

        if submit_btn:
            if not is_url(url):
                st.error("Please enter a valid URL!")
            else:
                st.write("Shortened URL")
                st.success(WEBSITE_URL + "?key=" + shortener.shorten_url(url))
