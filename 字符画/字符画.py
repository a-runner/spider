from PIL import Image


'''
    三原色
    红 绿 蓝
    RGB :[0,256)
'''

'''
    RGB转化为灰度图像
    .convert('L').show()
    包括 黑白两种颜色
    处理方便
'''


# 打开图片
im = Image.open('dlam.jpg')   # type:Image.Image
# im.show()  展示图片

# 打印图片的格式
print(im.mode)

# 打印像素点  im.getpixel((0,0))
# 将图片转化为灰度图片
# 灰度 gray

# 算数方法   L = R * 299/1000 + G * 587/1000 + B * 114/1000
gray_img = im.convert("L")
# px = gray_img.getpixel((0,0))
# 颜色越浅  字符越散
# 颜色越深  字符越密

# 就是用不同的字符转换成像素点 进行填充
# 这里我们通过比例进行转换
ascii_list = "$$$$BBB8888EEEHHHHDDDDUUUUUYYYYYY1111111LLLLLLLL>>>>>-----.....__        "    # 字符集


# 位置  按比例计算
# index = px/256 * len(ascii_list)
# 获取字符  ascii_list[index]

# 获取行数  列数

'''
    创建一个txt文件
    再将数据写入到文件
'''
'''
对图片进行缩小 原地
resize()方法可以缩小也可以放大，而thumbnail()方法只能缩小；

resize()方法不会改变对象的大小，只会返回一个新的Image对象，而thumbnail()方法会直接改变对象的大小，返回值为none；
# gray_img.thumbnail((gray_img.size[0]//3, gray_img.size[1]//3))
'''

width, height = gray_img.size

with open('多来爱梦.txt', 'w') as f:
    # 写入数据
    for column in range(height):
        for row in range(width):
            px = gray_img.getpixel((row, column))
            index = px/256 * len(ascii_list)
            s = ascii_list[int(index)]
            f.write(s)
        # 写入换行符
        f.write('\n')