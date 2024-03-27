import cv2
import numpy as np
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Dividir imágenes TIFF en segmentos")
parser.add_argument("orthophoto", help="Ruta al archivo TIFF")
args = parser.parse_args()

orthophoto_path = Path(args.orthophoto)
base_name = orthophoto_path.stem

output_folder = orthophoto_path.parent / f"{base_name}_tiles"
output_folder.mkdir(exist_ok=True)

def dividir_imagen(img_path, tile_size, output_dir):
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)  
    if img is None:
        print(f"No se pudo cargar la imagen de {img_path}")
        return

    img_height, img_width = img.shape[:2]

    for y in range(0, img_height, tile_size[1]):
        for x in range(0, img_width, tile_size[0]):
            tile = img[y:y+tile_size[1], x:x+tile_size[0]]
            
            # Verificar si la imagen segmentada está vacia
            if not np.any(tile):  # Para todos los pixeles
                print(f"Segmento en {x}, {y} descartado por estar totalmente vacia la imagen.")
                continue  # Saltar el guardado de esta imagen segmentada
            
            tile_filename = output_dir / f"{base_name}_tile_{x:04d}_{y:04d}.png"
            cv2.imwrite(str(tile_filename), tile)
            print(f"Segmento guardado: {tile_filename}")

dividir_imagen(str(orthophoto_path), (640, 640), output_folder)
