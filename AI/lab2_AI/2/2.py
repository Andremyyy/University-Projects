import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import os
import cv2

folder_path = "C:/Users/ema_a/Desktop/AI/images_lab2"

# lista fișierelor din folder
image_files = os.listdir(folder_path)



# a) sa se vizualizeze una din imagini

#de ex: prima imagine
image_path = os.path.join(folder_path, image_files[0])

# incarcarea si afisarea imaginii
image = Image.open(image_path)

plt.imshow(image)
#ascund axele de coordonate
plt.axis('off')
plt.show()



# b)daca imaginile nu aceeasi dimensiune,
# sa se redimensioneze toate la 128 x 128 pixeli
# si sa se vizualizeze imaginile intr-un cadru tabelar.

# dimensiunea dorită (128x128 pixeli)
new_size = (128, 128)

#  figură pentru vizualizarea imaginilor într-un grid
n_images = len(image_files)  # numarul de imagini
n_cols = 4  # câte imagini pe orizontală
n_rows = (n_images // n_cols) + (1 if n_images % n_cols != 0 else 0)  # cate randuri ne trebuie

# cadru tabelar pentru imagini
fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 5 * n_rows))

# aplatizez lista de axuri pentru a o face mai ușor de iterat
axes = axes.flatten()

for i, image_file in enumerate(image_files):

    image_path = os.path.join(folder_path, image_file)

    image = Image.open(image_path)

    image_resized = image.resize(new_size)

    # afisez imaginea în tabel
    axes[i].imshow(image_resized)
    axes[i].axis('off')

# dacă sunt mai multe imagini decât rânduri x coloane, ascund coordonatele goale
for j in range(i + 1, len(axes)):
    axes[j].axis('off')

# ajustez spațierea între subgrafice
plt.tight_layout()

plt.show()



#c) sa se transforme imaginile in format gray-levels si sa se vizualizeze

# cadru tabelar pentru imagini
n_images = len(image_files)  # nr total de imagini
n_cols = 5  # câte imagini pe orizontală
n_rows = (n_images // n_cols) + (1 if n_images % n_cols != 0 else 0)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 5 * n_rows))
axes = axes.flatten()

for i, image_file in enumerate(image_files):
    image_path = os.path.join(folder_path, image_file)

    image = Image.open(image_path)

    # transform imaginea în scala de gri folosind 'L' pt grayscale
    image_gray = image.convert('L')

    # afisez imaginea în tabel folosind  cmap='gray' pentru grayscale
    axes[i].imshow(image_gray, cmap='gray')
    axes[i].axis('off')

for j in range(i + 1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()

plt.show()



# d) sa se blureze o imagine si sa se afiseze in format "before-after"

# de ex imaginea 6
image_path = os.path.join(folder_path, image_files[5])

image = Image.open(image_path)

# aplic un efect de blur Gaussian ( cu cate este mai mare radius-ul cu atat este mai blurata imaginea )
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=10))

# figura pentru a aranja cele două imagini într-un format "inainte-dupa"
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# imaginea originală pe primul subgrafic
axes[0].imshow(image)
axes[0].set_title("Inainte - Original")
axes[0].axis('off')

# imaginea blurată pe al doilea subgrafic
axes[1].imshow(blurred_image)
axes[1].set_title("Dupa - Blurat")
axes[1].axis('off')

plt.tight_layout()

plt.show()


#e) sa se identifice muchiile intr-o imagine si sa se afiseze in format "before-after"

#de ex: imaginea 12
image_path = os.path.join(folder_path, image_files[11])

# incarc imaginea cu OpenCV
image = cv2.imread(image_path)

# convertesc imaginea în scala de gri
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# aplic detecția muchiilor folosind Canny
edges = cv2.Canny(gray_image, threshold1=150, threshold2=200)  # ajust pragurile pentru a controla sensibilitatea

#figura pentru a aranja cele două imagini într-un format "before-after"
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

#imaginea originală pe primul subgrafic
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Conversia din BGR(Blue-Green-Red) din OpenCv în RGB(Red-Green-Blue) din matplotlib
axes[0].set_title("Inainte - Original")
axes[0].axis('off')

#imaginea cu muchii detectate pe al doilea subgrafic
axes[1].imshow(edges, cmap='gray')  #  imaginea cu muchii în scala de gri
axes[1].set_title("Dupa - Muchii detectate")
axes[1].axis('off')

plt.tight_layout()

plt.show()