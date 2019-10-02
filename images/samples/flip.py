from PIL import Image
img = Image.open("flipped.jpg")
img = img.resize((2016, 1504))
img.save("flipped.jpg", "JPEG", optimize=True)