# Post at least one item
curl --location --request POST 'http://127.0.0.1:8000/items/' \
--form 'name="TestItem"' \
--form 'stock_count="5"' \
--form 'price="9.99"' \
--form 'picture=@"house.jpg"' # Replace this with any other jpg or pngs you want.

curl --location --request GET 'http://127.0.0.1:8000/items/1' #replace 1 wiuth any other pk you want to query