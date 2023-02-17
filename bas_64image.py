import base64

  
with open("i.jpg", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())
print(type(converted_string))


# decodeit = open('hello_level.jpeg', 'wb')
# decodeit.write(base64.b64decode((converted_string)))
# decodeit.close()