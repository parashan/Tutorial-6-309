# Tutorial-6-309

### Task 1 - Use  Django REST Framework to  make a GET, POST endpoint at localhost:8000/items/
You are given the following Serializers, and Model objects:
- ItemSerializer
- Item 

GET Requirements
- Return the serialized Item list as JSON
- pictures should be a path to the image
- Test with curl_get_list.sh
POST Requirements
- Should allow for uploading an optional image with field 'picture'. 
- All other fields are mandatory
- You can test this with the curl request in `curl_post.sh`

Implement your answer in the `items_list` function in views.py.

### Task 2 - Use  Django REST Framework to  make a GET, PUT, DELETE, PATCH endpoint at localhost:8000/items/<int:pk>
You are given the following Serializers, and Model objects:
- ItemSerializer
- Item 

GET Requirements
- Return the serialized Item as JSON
- picture should be a path to the image

PUT Requirements
- Should allow for updating all fields except for image, You must update all fields except image
- return the newly updated field

PATCH Requirements
- Should allow for updating some fields except for image
- return the newly updated field

DELETE Requirements
- delete the item with the designated primary key in request
- return status 204
Implement your answer in the `item_detail` function in views.py.

Notes:
- You should use Django REST Framework's `Response` object instead of `HTTPResponse` or `JSONResponse`
- Item contains an `ImageField`, can Django REST API handle an image upload with only `JSONParser`?
- You can view the endpoint on the browser at `localhost:8000/items`
- You can view images at `localhost:8000/Images/<int:pk>` where `pk` is the id of the item with the image
- If you wish, you may use Class based views to implement the question
