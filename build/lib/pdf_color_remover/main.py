import argparse
import numpy as np
from pdf2image import convert_from_path
from sklearn.cluster import KMeans
from PIL import Image
import matplotlib.pyplot as plt
import sys

def pdf_to_images(pdf_path, dpi):
    images = convert_from_path(pdf_path,dpi=dpi)
    return images

def image_to_clusters(images, n_clusters):
    combined_pixels = []
    
    for img in images:
        img_array = np.array(img)
        img_array = img_array.reshape(-1, 3)
        combined_pixels.append(img_array)
    
    combined_pixels = np.vstack(combined_pixels)
    
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(combined_pixels)
    
    return kmeans

def display_color_palette(kmeans):
    colors = kmeans.cluster_centers_.astype(int)
    plt.figure(figsize=(10, 2))
    plt.imshow([colors])
    plt.xticks(ticks=np.arange(len(colors)), labels=np.arange(len(colors)), fontsize=12)
    plt.title('Cluster Color Palette (Select Indices to Change)', fontsize=14)
    # plt.axis('off')
    plt.show()

def change_color(image, labels, target_clusters):
    img_array = np.array(image)
    img_array_reshaped = img_array.reshape(-1, 3)
    
    for cluster in target_clusters:
        img_array_reshaped[labels == cluster] = [255, 255, 255]
    
    return img_array_reshaped.reshape(img_array.shape)

def main(input_pdf, output_pdf, n_clusters=5, dpi=100, quality=95):
    images = pdf_to_images(input_pdf, dpi)
    kmeans = image_to_clusters(images, n_clusters)
    display_color_palette(kmeans)

    all_labels = []
    for img in images:
        img_array = np.array(img).reshape(-1, 3)
        labels = kmeans.predict(img_array)
        all_labels.append(labels)

    while True:
        try:
            target_clusters = input('Enter two cluster indices to change to white (e.g., 0,1): ')
            target_clusters = list(map(int, target_clusters.split(',')))
            if len(target_clusters) != 2 or any(c < 0 or c >= n_clusters for c in target_clusters):
                raise ValueError("Invalid cluster indices.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter two valid cluster indices separated by a comma.")
    
    output_images = []
    
    for i, img in enumerate(images):
        new_image_array = change_color(img, all_labels[i], target_clusters)
        new_image = Image.fromarray(new_image_array)
        output_images.append(new_image)
    
    output_images[0].save(output_pdf, save_all=True, append_images=output_images[1:], optimize=True, quality=quality)

def main_entry():
    parser = argparse.ArgumentParser(description="Remove colors from PDF.")
    parser.add_argument('-f', '--file', required=True, help="Input PDF file path.")
    parser.add_argument('-o', '--output', default='output.pdf', help="Output PDF file path.")
    parser.add_argument('--clusters', type=int, default=5, help="Number of clusters for k-means.")
    parser.add_argument('--dpi', type=int, default=100, help="DPI image quality for each page")
    parser.add_argument('--quality', type=int, default=100, help="Image quality")
    args = parser.parse_args()
    sys.exit(main(args.file, args.output, args.clusters, args.dpi))


if __name__ == "__main__":
    main_entry()