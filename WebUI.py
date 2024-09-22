# python -m streamlit run WebUI.py --theme.base=dark

import validators
import streamlit as st
from URLShortener import URLShortener
import streamlit.components.v1 as components

WEBSITE_URL = "https://kb-url.streamlit.app/"
# WEBSITE_URL = "http://localhost:8501/" # For testing purposes.

def is_url(url):
    try:
        return validators.url(url)
    except validators.ValidationError:
        return False

if __name__ == "__main__":
    obj = URLShortener()

    st.set_page_config(
        page_icon=":desktop_computer:",
        page_title="URL Shortener",
    )

    query_params = st.query_params
    if "key" in query_params.keys():
        url = obj.give_url_from_key(query_params["key"])
        
        if url != "Your link has expired.":
            st.write(f"Redirecting to {url}...")
            components.html(f"""
                <script>
                    window.location.href = "{url}";
                </script>
                <a href="{url}" target="_blank">Click here if you are not redirected automatically.</a>
                """, height=0
            )
            st.markdown(f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True)
            st.link_button(
                label="Click here if you are not being redirected automatically.",
                url=url,
                use_container_width=True
            )
        else:
            st.error("Your Link Has Expired!", icon=":material/error:")
            st.markdown(
                f'<meta http-equiv="refresh" content="0; url={WEBSITE_URL}">',
                unsafe_allow_html=True
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
                st.success(WEBSITE_URL + "?key=" + obj.shorten_url(url))
