"""
Dummy file for testing some ideas
"""

from src.main.main import Templite
import webbrowser

PAGE_HTML = """
<p>Welcome, {name}!</p>
<p>Products:</p>
<ul>
{products}
</ul>
"""

PRODUCT_HTML = "<li>{product_name}: {price} cedis</li>\n"


# testing a simple idea


def make_page(name: str, products: list[dict[str, str]], template: str):
    #
    product_list = ""
    for product in products:
        product_list += PRODUCT_HTML.format(
            product_name=product["product_name"], price=product["price"]
        )
    processed_template = PAGE_HTML.format(name=name, products=product_list)
    index_html = open("index.html", "w")
    index_html.write(processed_template)
    return processed_template


data = make_page(
    name="mike dean",
    products=[
        {"product_name": "orange", "price": 12.23},
        {"product_name": "apple", "price": 4.23},
        {"product_name": "pear", "price": 7.23},
        {"product_name": "pawpaw", "price": 11.3},
    ],
    template="",
)

print(data)


# Make a Templite object.
templite = Templite(
    """
    <h1>Hello {{name|upper}}!</h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
    {% endfor %}
    """,
    {"upper": str.upper},
)

# Later, use it to render some data.
text = templite.render(
    {
        "name": "Ned",
        "topics": ["Python", "Geometry", "Juggling"],
    }
)
