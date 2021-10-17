import os
import cairosvg
import time

def main():

    iconExportPathOf80 = "/export/path//icon@80/"
    iconExportPathOf60 = "/export/path//icon@60/"
    iconExportPathOf160 = "/export/path//icon@160/"
    iconExportPathOf240 = "/export/path/icon@240/"

    filename = os.listdir("/path/to/svg/file")

    print(filename)

    for i in filename:

        if i[-3:] == "svg":

            iconPath = "/path/to/svg/file"+i

            print(iconPath)
            print(iconExportPathOf80+i.replace("svg", "png"))

            cairosvg.svg2png(
                url=iconPath, write_to=iconExportPathOf80+i.replace("svg", "png"), output_width=80)
            cairosvg.svg2png(
                url=iconPath, write_to=iconExportPathOf160+i.replace("svg", "png"), output_width=160)
            cairosvg.svg2png(
                url=iconPath, write_to=iconExportPathOf240+i.replace("svg", "png"), output_width=240)
            cairosvg.svg2png(
                url=iconPath, write_to=iconExportPathOf60+i.replace("svg", "png"), output_width=60)

            filename.remove(i)

            print(filename)


if __name__ == "__main__":
    main()
