from setuptools import setup, find_packages

setup(
    name='pdf-color-remover',
    version='0.2',
    description='A tool to remove specified colors from PDF files using K-means clustering.',
    author='Your Name',
    author_email='andreas.konga@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'Pillow',
        'pdf2image',
        'scikit-learn',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'pdf-color-remover=pdf_color_remover.main:main_entry',
        ],
    },
)
