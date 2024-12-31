from setuptools import setup, find_packages

setup(
    name="pma",  # Nombre del paquete en PyPI
    version="0.0.4",  # Versión del paquete
    author="Facundo Efimenco",  # Tu nombre como autor
    author_email="facu22251@gmail.com",  # Tu correo
    description="usa esta librería para inyectar codigo en archivos, interceptar la ejecución de funciones y mas",  # Breve descripción
    long_description=open("README.md").read(),  # Descripción larga (README.md)
    long_description_content_type="text/markdown",  # Indica que usas Markdown
    url="https://github.com/facu-programer/pma-python-modify-api-/tree/v0.0.4",  # URL del proyecto (GitHub, etc.)
    packages=find_packages(),  # Encuentra automáticamente los subpaquetes
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: Other/Proprietary License",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",  # Versión mínima de Python
    install_requires=[
        # Lista de dependencias, ej.: "requests>=2.25.1"
    ],
)