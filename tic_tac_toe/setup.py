from setuptools import setup, find_packages

setup(
    name="tic_tac_toe",
    version="1.0.0",
    author="Felipe Rey",
    author_email="reymiguelez.br@gmail;com",
    description="Um simples jogo da velha em Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Reymiguelez/Tic_Tac_Toe/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'tic-tac-toe=tic_tac_toe.game:jogar',
        ],
    },
)
