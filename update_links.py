import os
import re
import shutil


def run(filename: str, src: str, dst: str):
    with open(filename, "r") as f:
        md = f.readlines()

    updated = []

    print('updating links and figures')
    for line in md:
        # update links from absolute to relative paths
        if '](http://dangerfromdeer.com/wp-content/uploads/' in line:
            old_line = line
            line.replace('](http://dangerfromdeer.com/wp-content/uploads/', '](/img/')
            print(f"Updating image link: \n  {old_line}\n  {line}")

            #remove width query param
            if '?w=' in line:
                old_line = line
                line = re.sub(r'\?w=[0-9]*\)', ')', line)
                print(f"removed query param: \n  {old_line}\n  {line}")

        # update captions
        m = re.match(fr'(.*)<figure>!\[\]\((.*)\)<figcaption.*>(.*)</figcaption></figure>(.*)', line)
        if m:
            old_line = line
            line = f'{m.group(1)}![{m.group(3)}]({m.group(2)}){m.group(4)}\n'
            print(f"Updating image format: \n  {old_line}\n  {line}")

        updated.append(line)


    print("Saving updated md file")
    with open(filename, 'w') as f:
        f.writelines(updated)

    print("Copying images")
    # find all the image tags ![](path_to_image.jpg)
    # and strip out the filename just including the date/filename - iel /other/path/2021/07/filename.jpg
    # just remove the 2021/07/filename.jpg
    images = re.findall(r"!\[[^\]]*\]\([^\)]*([0-9]{4}/[^\)]*)\)", '\n'.join(updated))
    for image in images:
        sourcefile = os.path.join(src, image)
        dstfile = os.path.join(dst, image)
        if os.path.exists(sourcefile):
            print(f"  copying {sourcefile} to {dstfile}")
            os.makedirs(os.path.dirname(dstfile), exist_ok=True)
            shutil.copyfile(sourcefile, dstfile)
        else:
            print(f"error: missing source file: {sourcefile}")


if __name__ == "__main__":
    run("_posts/2020-06-03-more-fences-and-a-new-arrival.md", "../static", "img")
