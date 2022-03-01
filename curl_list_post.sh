curl --location --request POST 'http://127.0.0.1:8000/items/' \
--form 'name="TestItem"' \
--form 'stock_count="5"' \
--form 'price="9.99"' \
--form 'picture=@"house.jpg"' # Replace this with any other jpg or pngs you want.