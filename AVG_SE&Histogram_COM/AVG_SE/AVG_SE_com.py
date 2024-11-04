import os
import matplotlib.pyplot as plt
from PIL import Image

def load_image(image_path):
    """Load an image from the given path."""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def plot_images_in_subplots(image_info, save_path):
    """Plot images from each specified path into a 1x3 subplot and save the figure."""
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))  # Adjusted size for better fit

    for i, (image_path, annotation) in enumerate(image_info):
        img = load_image(image_path)
        
        if img:
            axes[i].imshow(img)
            axes[i].axis('off')  # Turn off axis
            axes[i].set_title(annotation, fontsize=20)  # Set annotation as title
        else:
            axes[i].text(0.5, 0.5, 'No Image', fontsize=20, ha='center')
            axes[i].axis('off')

    plt.tight_layout()
    plt.savefig(save_path)  # Save the figure to the specified path
    plt.show()

base_directory = r"."

image_info = [
    (os.path.join(base_directory, 'LAVG_SE_plot.png'), '(a) Linear chain(10)'),
    (os.path.join(base_directory, 'ZAVG_SE_plot.png'), '(b) Zigzag chain(14)'),
    (os.path.join(base_directory, 'HAVG_SE_plot.png'), '(c) Single helix(17)')
]

save_path = os.path.join(base_directory, 'c60cntpng_com.pdf')

plot_images_in_subplots(image_info, save_path)
