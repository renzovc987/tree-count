import cv2

# Cargar la imagen
image = cv2.imread('imagen_satelital.tif')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para detectar áreas verdes (puedes necesitar ajustar estos valores)
_, thresholded = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Encontrar contornos en la imagen umbralizada
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Contar el número de contornos encontrados (que podrían representar árboles)
num_trees = len(contours)

# Dibujar los contornos en la imagen original (solo para visualización)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Crear una ventana redimensionable
cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)

# Mostrar la imagen con los contornos detectados
cv2.imshow('Contours', image)

# Esperar hasta que se presione una tecla y luego cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imprimir el número de árboles detectados
print("Número de árboles detectados:", num_trees)

