# PDF Color Remover

A tool to remove specified colors from multi-page PDF files using K-means clustering. Chosen clusters are shown as colors and indexes. Close the graphical window and choose two clusters based on the color that were shown in color palette, that are then changed to white pixel colors (255,255,255).

## Installation

Clone the repository and install:

```bash
git clone https://github.com/AndyMcCode/pdf-color-remover.git
cd pdf-color-remover
pip install .
```

## Usage 
pdf-color-remover -f path/to/your/file.pdf -o output.pdf --clusters 8 --dpi 140

Choose the color clusters e.g. for cluster in index 0 and 5

input "0,5", to choose color 0 and 5 to be changed.

## You will also need
sudo apt install poppler-utils
python > 3.8


## OS
Works on my machine (Debian 12)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
