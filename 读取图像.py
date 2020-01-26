from PIL import Image
import csv

im = Image.open('字符画/amcharts.pixelMap_ABCD.png')    # type:Image.Image

gray_image = im.convert('L')

width, height = gray_image.size

re_image = gray_image.resize((round(width/6), round(height/6)))

width, height = re_image.size
print(width, height)

with open('障碍坐标.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for column in range(height):
        for row in range(width):
            # 获取对应像素值
            px = re_image.getpixel((row, column))
            px = round(px)
            if px == 90:  # 89.458
                writer.writerow((column, row))



print('结束')

exit()
with open('障碍坐标测试表格.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for column in range(height):
        for row in range(width):
            # 获取对应像素值
            px = re_image.getpixel((row, column))
            px = round(px)
            if px == 90:
                print(column)
                writer.writerow((column, row))



print('结束')


exit()

for column in range(height):
    for row in range(width):
        # 获取对应像素值
        px = re_image.getpixel((row, column))
        if px == 0:
            i = i + 1
            print(column, row)

print(i)

exit()
re_image.save('调整后的彩色图像.png')


with open('障碍坐标.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for column in range(height):
        for row in range(width):
            # 获取对应像素值
            px = re_image.getpixel((row, column))
            px = round(px)
            if px == 89:  # 89.458
                writer.writerow((column, row))



print('结束')










exit()
im = Image.open('字符画/amcharts.pixelMap_ABCD.png')   # type:Image.Image
# im.show()  展示图片

#im = Image.open('')   # type:Image.Image
# im.show()  展示图片

# 打印图片的格式
print(im.mode)

# 打印像素点  im.getpixel((0,0))
# 将图片转化为灰度图片
# 灰度 gray

# 算数方法   L = R * 299/1000 + G * 587/1000 + B * 114/1000
gray_img = im.convert("L")
#
width, height = gray_img.size
# print(width, height)
#
# imame_re = gray_img.resize((round(width/6), round(height/6)))
# #
# imame_re.save('调整的图像.png')
#
# width, height = imame_re.size
# print(width, height)

i = 0
for column in range(height):
    for row in range(width):
        # 获取对应像素值
        px = gray_img.getpixel((row, column))
        if px == 129:
            i = i + 1
            print(column, row)


print('结束')
print(i)

'''
    像素范围：
    844 - 854
    855 - 865
'''