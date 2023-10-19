import os
from rembg import remove
from PIL import Image

def process_image(input_path, output_path):
    print(f'Processing: {input_path} -> {output_path}')
    input_img = Image.open(input_path)
    output_img = remove(input_img)
    output_img = output_img.convert('RGB')  # Convert RGBA to RGB before saving
    output_img.save(output_path)
    print(f'Saved: {output_path}')

def crawl_directory(directory):
    for root, dirs, files in os.walk(directory):
        print(f'Entering directory: {root}')
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'webp')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(root, f'{os.path.splitext(file)[0]}_noback{os.path.splitext(file)[1]}')
                process_image(input_path, output_path)



if __name__ == '__main__':
    print('Script is running')
    directory = '' # updated path
    crawl_directory(directory)

