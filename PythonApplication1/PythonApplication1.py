import cv2
import os

def convert_png_to_jpeg(png_folder, jpeg_folder):
    for filename in os.listdir(png_folder):
        if filename.endswith(".png"):
            png_file = os.path.join(png_folder, filename)
            jpeg_file = os.path.join(jpeg_folder, os.path.splitext(filename)[0] + ".jpeg")

            img = cv2.imread(png_file)
            cv2.imwrite(jpeg_file, img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

if __name__ == "__main__":
    png_folder = r"C:\png_folder"
    jpeg_folder = r"C:\jpeg_folder"

    convert_png_to_jpeg(png_folder, jpeg_folder)

