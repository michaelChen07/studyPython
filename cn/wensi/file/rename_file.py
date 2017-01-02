#encoding=utf-8
#14.遍历某个目录下的所有图片，并在图片名称后面增加_xx
import os
def rename_file(path):

    if os.path.exists(path):
        os.chdir(path)
        files = os.listdir(path)

        for file in files:
            picname = os.path.splitext(file)
            if picname[1] in [".bmp",".dib", ".gif", ".jfif",".jpe",".jpeg", ".jpg",".png", ".tif",".tiff", ".ico"]:
                os.rename(file,picname[0]+"_XX"+picname[1])
        return "done"

print rename_file(r"d:\test\test2")