class Product:
    def __init__(self, name, price, url, image) -> None:
        self.name = name
        self.price = price
        self.url = url
        self.image = image

    def toHtmlRow(self):
        row = "<tr>"
        row += f"<td><img src=\"{self.image}\"></td>"
        row += f"<td><a href=\"{self.url}\">{self.name}</td>"
        row += f"<td>{self.price}</td>"
        row += "</tr>"
        return row