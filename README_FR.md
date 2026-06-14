# [:es:](README_ES.md) [:de:](README_DE.md) [:uk:](README.md) 
# Générateur de Palettes Monochromatiques

Un outil indépendant qui génère des palettes de couleurs monochromatiques et les exporte pour une utilisation dans des logiciels de conception open source tels que GIMP, Krita et Inkscape.

## 🌟 Fonctionnalités

* **Nombre de Couleurs Personnalisé :** Sélectionnez facilement le nombre exact de couleurs que vous souhaitez dans votre palette monochromatique.
* **Exportation Universelle .GPL :** Exporte automatiquement vos palettes générées au format standard `.gpl` (Palette GIMP), les rendant instantanément compatibles avec GIMP, Krita et Inkscape.
* **Application Indépendante :** Aucune installation complexe n'est requise. Il suffit de lancer l'exécutable et de commencer à générer des palettes.

## 📋 Prérequis

* **OS (Système d'exploitation) :** Windows (pour exécuter le fichier `.exe`).
* **Logiciel Cible :** GIMP, Krita ou Inkscape (pour utiliser les fichiers `.gpl` générés).

## 🚀 Installation et Utilisation

1. Téléchargez ou clonez ce dépôt sur votre machine locale :
   ```bash
  git clone [https://github.com/jartibledev/plugin-monochromatic-palette-generator.git](https://github.com/jartibledev/plugin-monochromatic-palette-generator.git)
2. Accédez au répertoire `dist`.
3. Double-cliquez sur le fichier `.exe` pour lancer le programme.
4. **(Recommandé)**: Pour un accès plus facile, faites un clic droit sur le fichier `.exe` et sélectionnez Créer un raccourci, puis faites glisser le raccourci sur votre Bureau.
## 🎨 Comment Importer vos Palettes .GPL

Une fois que vous avez généré votre fichier `.gpl` à l'aide de ce programme, vous pouvez facilement l'importer dans votre logiciel de conception préféré :

### Dans GIMP
1. Ouvrez GIMP et allez dans **Édition > Préférences**.
2. Faites défiler le menu de gauche vers le bas, développez **Dossiers**, et cliquez sur **Palettes**.
3. Vous verrez une liste de chemins de dossiers. Cliquez sur celui qui se trouve dans votre répertoire utilisateur (généralement le premier) pour le mettre en surbrillance, puis cliquez sur le bouton **"Afficher l'emplacement du fichier dans le gestionnaire de fichiers"** (l'icône de classeur en haut à droite).
4. Copiez votre fichier `.gpl` généré dans ce dossier.
5. Dans GIMP, ouvrez votre fenêtre de Palettes (**Fenêtres > Fenêtres ancrables > Palettes**) et cliquez sur l'icône **Configurer cet onglet** (le petit triangle), puis sélectionnez **Menu des palettes > Actualiser les palettes**.

### Dans Krita
1. Ouvrez Krita et allez dans **Paramètres > Gérer les ressources**.
2. Cliquez sur **Ouvrir le dossier des ressources**.
3. Ouvrez le dossier `palettes` et copiez votre fichier `.gpl` à l'intérieur.
4. Redémarrez Krita, ou ouvrez le panneau Palette (**Paramètres > Panneaux > Palette**), cliquez sur l'icône de dossier en bas à gauche du panneau, et sélectionnez votre nouvelle palette dans la liste.

### Dans Inkscape
1. Ouvrez votre Explorateur de fichiers.
2. Accédez au dossier des palettes personnalisées d'Inkscape. Il est généralement situé dans :
   * **Windows :** `%appdata%\inkscape\palettes`
3. Collez votre fichier `.gpl` généré dans ce dossier.
4. Redémarrez Inkscape. Votre nouvelle palette sera désormais disponible en cliquant sur la petite flèche à l'extrême droite de la barre de palette de couleurs en bas de l'écran.