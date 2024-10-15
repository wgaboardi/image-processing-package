from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="imagem_processing_wlg",
    version="1.0.0",
    author="Wellington",
    author_email="wgaboardi@gmailll.com",
    description="Functions for image processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wgaboardi/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
