import streamlit as st
from urllib.parse import urlparse
from URLShortener import URLShortener

# python -m streamlit run WebUI.py --theme.base=dark

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
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
        st.link_button(
            label="Click here if you are not being redirected automatically.",
            url=url,
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
                st.success("https://kb-url.streamlit.app/?key=" + obj.shorten_url(url))
