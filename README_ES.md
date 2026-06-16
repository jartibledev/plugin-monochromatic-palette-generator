# [:uk:](README.md) [:de:](README_DE.md) [:fr:](README_FR.md) 
# Generador de Paletas Monocromáticas

Una herramienta independiente que genera paletas de colores monocromáticas y las exporta para su uso en software de diseño de código abierto como GIMP, Krita e Inkscape.

## 🌟 Características
| | | |
|:---:| :---: | :---: | 
| ![Texto alternativo](./media/gif_1.gif) | ![Texto alternativo](./media/gif_2.gif) | ![Texto alternativo](./media/gif_3.gif) |
| * **Cantidad de Colores Personalizada:** Selecciona fácilmente el número exacto de colores que deseas en tu paleta monocromática. | * **Exportación Universal .GPL:** Exporta automáticamente las paletas generadas en el formato estándar `.gpl` (Paleta de GIMP), haciéndolas compatibles al instante con GIMP, Krita e Inkscape. | * **Aplicación Independiente (Standalone):** No requiere una instalación compleja. Simplemente ejecuta el archivo ejecutable y comienza a generar paletas. |

## 📋 Requisitos Previos

* **SO:** Windows (para ejecutar el archivo `.exe`).
* **Software de Destino:** GIMP, Krita o Inkscape (para usar los archivos `.gpl` generados).

## 🚀 Instalación y Uso

1. Descarga o clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/jartibledev/plugin-monochromatic-palette-generator.git](https://github.com/jartibledev/plugin-monochromatic-palette-generator.git)
2. Navega al directorio dist.
3. Haz doble clic en el archivo .exe para iniciar el programa.
4. (Recomendado): Para un acceso más fácil, haz clic derecho sobre el archivo .exe, selecciona Crear acceso directo, y luego arrastra el acceso directo a tu Escritorio.
## 🎨 Cómo importar tus palettas.GPL 

Una vez que hayas generado tu archivo .gpl usando este programa, puedes importarlo fácilmente en tu software de diseño favorito:

### En GIMP
1. Abre Gimp y ve a **Editar > Preferencias**.
2. Desplázate hacia abajo en el menú de la izquierda, expande **Carpetas**, y haz clic en **Paletas**.
3.Verás una lista de rutas de carpetas. Haz clic en la que está dentro de tu directorio de usuario (generalmente la de arriba) para resaltarla, luego haz clic en el botón **"Mostrar la ubicación del archivo en el gestor de archivos"** (el icono de archivador en la parte superior derecha).
4. Copia tu archivo `.gpl` generado en esa carpeta.
5. En GIMP, abre tu diálogo de Paletas (**Ventanas > Diálogos empotrables > Paletas**) y haz clic en el icono de **Configurar esta pestaña** (el pequeño triángulo), luego selecciona **Menú de paletas > Actualizar paletas**.

### En Krita
1. Abre Krita y ve a **Preferencias > Gestionar recursos**.
2. Haz clic en **Abrir carpeta de recursos**.
3. Abre la carpeta `palettes` y copia tu archivo `.gpl` dentro.
4. Reinicia Krita, o abre el panel de Paletas (**Preferencias > Paneles > Paleta**), haz clic en el icono de carpeta en la parte inferior izquierda del panel, y selecciona tu nueva paleta de la lista.

### En Inkscape
1. Abre tu Explorador de archivos.
2. Navega hasta la carpeta de paletas personalizadas de Inkscape. Generalmente se encuentra en:
   * **Windows:** `%appdata%\inkscape\palettes`
3. Pega tu archivo `.gpl` generado en esta carpeta.
4. Reinicia Inkscape. Tu nueva paleta estará ahora disponible haciendo clic en la pequeña flecha en el extremo derecho de la barra de paleta de colores en la parte inferior de la pantalla.
