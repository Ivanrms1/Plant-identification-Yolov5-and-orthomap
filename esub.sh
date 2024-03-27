#!/bin/bash

# Iterar sobre todos los archivos .mp4 en el directorio actual
for video in *.MP4; do
    # Obtener el nombre base del video sin la extensión
    base_name="${video%.*}"

    # Comando ffmpeg para extraer los subtítulos
    ffmpeg -i "$video" -map 0:s:0 "${base_name}.srt"
done

