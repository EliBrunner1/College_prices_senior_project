def get_search_url(keywords):
  search_engine = "https://www.google.com/search?q="
  return search_engine + keywords.replace(" ", "+")


keywords = "Oregon state university"
search_url = get_search_url(keywords)
print(search_url)
