from PIL import Image
import pytesseract
def shibie(imagepath):
    img = Image.open(imagepath)
    # 转化为灰度图片
    img = img.convert('L')
    # 二值化处理
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = img.point(table, '1')
    # out.show()
    img = img.convert('RGB')
    # img.show()
    return pytesseract.image_to_string(img)
