import minify_html

with open("Robotics.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# We gebruiken alleen minify_js, de rest doet de tool automatisch naar de nieuwste standaarden
minified = minify_html.minify(html_content, minify_js=True)

with open("Robotics1.html", "w", encoding="utf-8") as f:
    f.write(minified)
