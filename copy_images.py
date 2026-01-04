import os
import re
import shutil


def run(filename: str, src: str, dst: str):
    with open(filename, "r") as f:
        md = f.read()
    # find all the image tags ![](path_to_image.jpg)
    # and strip out the filename just including the date/filename - iel /other/path/2021/07/filename.jpg
    # just remove the 2021/07/filename.jpg
    images = re.findall(r"!\[[^\]]*\]\([^\)]*([0-9]{4}/[^\)]*)\)", md)
    for image in images:
        sourcefile = os.path.join(src, image)
        dstfile = os.path.join(dst, image)
        if os.path.exists(sourcefile):
            # print(f"copying {sourcefile} to {dstfile}")
            os.makedirs(os.path.dirname(dstfile), exist_ok=True)
            shutil.copyfile(sourcefile, dstfile)
        else:
            print(f"error: missing source file: {sourcefile}")


if __name__ == "__main__":
    run("_posts/2020-11-17-setting-up-an-stm32f4-as-an-spi-device-with-freertos-and-stm32mxcube.md", "../static", "img")
