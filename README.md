# Proyecto: Reconocimiento Facial con Registro Automático en Python

---

## 📋 Descripción

Este proyecto permite:

- Capturar imágenes de personas a través de la cámara web.
- Registrar su nombre la primera vez que son detectadas.
- Guardar varias imágenes de cada persona para mejorar la precisión del reconocimiento.
- Mostrar en pantalla el nombre de la persona junto con un contador de cuántas veces ha sido vista.
- Reproducir un sonido de alerta cuando se detecta una persona nueva.

---

## 📦 Funcionalidades

- 🎥 **Captura en vivo** desde la cámara web.
- 🆕 **Registro automático** de nuevas personas.
- 🖼️ **Captura múltiple** de imágenes (configurable, por defecto 5).
- 📈 **Contador de detecciones**: muestra “Nombre (N)” encima del rostro.
- 🔊 **Alerta sonora** para nuevas personas.
- 🗃️ **Almacena imágenes** en carpetas `known_faces/<nombre>/`.
- 💾 **Base de datos de codificaciones** en `encodings.pickle`, actualizable sin reiniciar.

---

## 🛠️ Requisitos del sistema

- Python 3.7 o superior  
- Cámara web conectada  
- Windows / macOS / Linux  

---

## 🧩 Instalación

1. **Clonar o copiar el repositorio**  
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio



**(Opcional) Crear y activar entorno virtual**

 ```bash
Copiar
Editar
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
Instalar dependencias

 ```bash
Copiar
Editar
pip install -r requirements.txt
Descargar sonido de alerta

Coloca un archivo new_person.mp3 en la raíz del proyecto.

Puede ser un “beep” o cualquier alerta corta.


📝 requirements.txt
text
Copiar
Editar
opencv-python
face_recognition
dlib
numpy
playsound==1.2.2

🏗️ Estructura del proyecto

```bash
Copiar
Editar
mi_proyecto/
│
├── app.py                # Código principal
├── requirements.txt      # Dependencias
├── README.md             # Documentación
├── new_person.mp3        # Sonido para nueva persona
├── known_faces/          # Carpeta con subcarpetas por persona
│   └── <Nombre>/
│       ├── <Nombre>_0.jpg
│       ├── <Nombre>_1.jpg
│       └── ...
└── encodings.pickle      # Codificaciones faciales
🚀 Uso
Ejecuta:

bash
Copiar
Editar
python app.py
Aparecerá la consola:

nginx
Copiar
Editar
Presiona 's' para capturar una imagen o 'q' para salir.
‘s’: captura y, si es persona nueva, pide nombre y toma 5 fotos.

‘q’: cierra la ventana y termina el programa.

Durante la ejecución, verás en pantalla tu rostro y, si ya estás registrado, tu nombre más el contador de detecciones.

## 📈 Detalles técnicos

| Función                   | Cómo funciona                                                            |
|---------------------------|---------------------------------------------------------------------------|
| Captura varias imágenes   | Captura 5 fotos cada vez que detecta una persona nueva.                  |
| Registro automático       | Agrega el rostro al archivo `encodings.pickle` sin reiniciar.             |
| Contador de detecciones   | Muestra “Nombre (N)” encima del rectángulo que rodea el rostro.           |
| Sonido de detección       | Reproduce `new_person.mp3` para personas no registradas.                  |
| Carpeta organizada        | Crea `known_faces/<Nombre>/` con todas las imágenes capturadas.           |
| Mejora del reconocimiento | Más imágenes = mayor precisión al identificar en el futuro.               |

---

## 🛠️ Solución de problemas

| Problema                         | Solución                                                                                             |
|----------------------------------|------------------------------------------------------------------------------------------------------|
| `cv2` no encontrado              | Ejecuta `pip install opencv-python`.                                                                  |
| `playsound` no encontrado        | Ejecuta `pip install playsound==1.2.2`.                                                               |
| `face_recognition` o `dlib` falla| Instala los `.whl` precompilados de dlib y face_recognition desde [Gohlke](https://www.lfd.uci.edu/~gohlke/pythonlibs/). |
| Ventana no aparece               | Usa CMD o PowerShell estándar (no terminal integrada). Asegúrate de que `cv2.imshow()` esté dentro del bucle principal. |
| Cámara ocupada/no detectada      | Cierra otras apps que usen la cámara o cambia el índice en `VideoCapture(0)` a `1`, etc.              |

📜 Licencia
Este proyecto es de código abierto.
Puedes usarlo, modificarlo y distribuirlo libremente para fines educativos o personales.
Para uso comercial, se recomienda dar crédito al autor original.

🤝 Agradecimientos
face_recognition

OpenCV
