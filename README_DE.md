# [:uk:](README.md) [:es:](README_ES.md) [:fr:](README_FR.md) 
# Monochromatischer Paletten-Generator

Ein eigenständiges Tool, das monochromatische Farbpaletten generiert und sie zur Verwendung in Open-Source-Designsoftware wie GIMP, Krita und Inkscape exportiert.

## 🌟 Funktionen
| | | |
|:---:| :---: | :---: | 
| ![Texto alternativo](./media/gif_1.gif) | ![Texto alternativo](./media/gif_2.gif) | ![Texto alternativo](./media/gif_3.gif) |
| * **Benutzerdefinierte Farbanzahl:** Wählen Sie ganz einfach die genaue Anzahl der Farben für Ihre monochromatische Palette aus. | * **Universeller .GPL-Export:** Exportiert Ihre generierten Paletten automatisch im Standardformat `.gpl` (GIMP-Palette), sodass sie sofort mit GIMP, Krita und Inkscape kompatibel sind. | * **Eigenständige Anwendung (Standalone):** Keine komplexe Installation erforderlich. Führen Sie einfach die ausführbare Datei aus und beginnen Sie mit der Generierung von Paletten. |

## 📋 Voraussetzungen

* **Betriebssystem:** Windows (um die `.exe`-Datei auszuführen).
* **Zielsoftware:** GIMP, Krita oder Inkscape (um die generierten `.gpl`-Dateien zu verwenden).

## 🚀 Installation & Nutzung

1. Laden Sie dieses Repository herunter oder klonen Sie es auf Ihren lokalen Computer:
   ```bash
   git clone [https://github.com/jartibledev/plugin-monochromatic-palette-generator.git](https://github.com/jartibledev/plugin-monochromatic-palette-generator.git)
2. Navigieren Sie in das Verzeichnis `dist`.
3. Doppelklicken Sie auf die `.exe`-Datei, um das Programm zu starten.
4. **(Empfohlen)**: Für einen einfacheren Zugriff klicken Sie mit der rechten Maustaste auf die `.exe`-Datei, wählen Sie Verknüpfung erstellen und ziehen Sie die Verknüpfung dann auf Ihren Desktop.

## 🎨 So importieren Sie Ihre .GPL-Paletten
Sobald Sie Ihre `.gpl`-Datei mit diesem Programm generiert haben, können Sie sie ganz einfach in Ihre bevorzugte Designsoftware importieren:
### In GIMP
1. Öffnen Sie GIMP und gehen Sie zu **Bearbeiten > Einstellungen**.
2. Scrollen Sie im linken Menü nach unten, erweitern Sie **Ordner** und klicken Sie auf **Paletten**.
3. Sie sehen eine Liste von Ordnerpfaden. Klicken Sie auf denjenigen, der sich in Ihrem Benutzerverzeichnis befindet (normalerweise der oberste), um ihn zu markieren, und klicken Sie dann auf die Schaltfläche **"Dateispeicherort im Dateimanager anzeigen"** (das Aktenschrank-Symbol oben rechts).
4. Kopieren Sie Ihre generierte `.gpl`-Datei in diesen Ordner.
5. Öffnen Sie in GIMP Ihren Paletten-Dialog (**Fenster > Andockbare Dialoge > Paletten**) und klicken Sie auf das Symbol **Diesen Reiter konfigurieren** (das kleine Dreieck), dann wählen Sie **Palettenmenü > Paletten aktualisieren**.

### In Krita
1. Öffnen Sie Krita und gehen Sie zu **Einstellungen > Ressourcen verwalten**.
2. Klicken Sie auf **Ressourcenordner öffnen**.
3. Öffnen Sie den Ordner `palettes` und kopieren Sie Ihre `.gpl`-Datei hinein.
4. Starten Sie Krita neu oder öffnen Sie das Paletten-Andockfenster (**Einstellungen > Andockbereiche > Palette**), klicken Sie auf das Ordnersymbol unten links im Andockfenster und wählen Sie Ihre neue Palette aus der Liste.

### In Inkscape
1. Öffnen Sie Ihren Datei-Explorer.
2. Navigieren Sie zum Ordner für benutzerdefinierte Paletten in Inkscape. Dieser befindet sich typischerweise unter:
   * **Windows:** `%appdata%\inkscape\palettes`
3. Fügen Sie Ihre generierte `.gpl`-Datei in diesen Ordner ein.
4. Starten Sie Inkscape neu. Ihre neue Palette ist nun verfügbar, indem Sie auf den kleinen Pfeil ganz rechts in der Farbpalettenleiste am unteren Bildschirmrand klicken.
