try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('sample.png')))
st = pytesseract.image_to_string(Image.open('otsu.jpg'), config="-psm 6")
print('st = ', st)