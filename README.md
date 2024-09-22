# URL Shortener

This is a simple implementation of a URL Shortener using a HashMap. It's made using `python3` and deployed on streamlit cloud [here](https://kb-url.streamlit.app/ "URL Shortener").

## Installation Guide

Just install the requirements in the `requirements.txt` file using the following command.

```powershell
pip install -r requirements.txt
```

After the installation, you can use the standard streamlit commands to run it.

```powershell
python -m streamlit run WebUI.py --theme.base=dark
```

If you are running it locally, remember to make sure that the `WEBSITE_URL` in `WebUI.py` is redirecting to your local server.

```python
WEBSITE_URL = "http://localhost:8501/"
```

## Future Updates

* [ ] Add a database using `sqlite3` with all necessary features like a trigger that deletes the entries after a given amount of time so that the website will be able to use the HashMap for frequently used URLs and store the less frequently used URLs in the database.
* [ ] Figure out a way for automatic redirection since streamlit cloud doesn't work well with JS.

## Note

I most likely won't update this. I just wanted to try out streamlit and streamlit cloud so consider this project done & dusted. I still need to learn a lot of things, especially good practices.
