import os
import re
import shutil


def copy_header_images(filename: str, src: str, dst: str):
    
    updated = []
    with open(filename, "r") as f:
        for line in f:

            # copy header images
            if line.startswith("image: /img/"):
                image = line[12:]
                print(f"Copying image: {image}")
                sourcefile = os.path.join(src, image)
                dstfile = os.path.join(dst, image)
                if os.path.exists(sourcefile):
                    print(f"  copying {sourcefile} to {dstfile}")
                    os.makedirs(os.path.dirname(dstfile), exist_ok=True)
                    shutil.copyfile(sourcefile, dstfile)
                else:
                    print(f"  error: missing source file: {sourcefile}")

            # translate images to have captions
            line = re.sub(
                r'!\[(.*)\]\((.*)\)', 
                '{% include image.html url="\\2" description="\\1" %}',
                line
            )
            updated.append(line)

    with open(filename, 'w') as f:
        f.writelines(updated)


if __name__ == "__main__":
    for filename in os.listdir('_posts'):
        if filename.endswith('.md'):
            copy_header_images(os.path.join('_posts', filename), "../static", "img")
