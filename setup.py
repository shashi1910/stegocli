from setuptools import setup, find_packages

setup(
    name="stegocli",
    version="1.0.0",
    author="Shashi P",
    description="A CLI tool for image steganography",
    packages=find_packages(),
    install_requires=[
        "click",
        "pillow"
    ],
    entry_points={
        'console_scripts': [
            'stegocli=stegocli.cli:cli',
        ],
    },
    python_requires='>=3.6',
)
