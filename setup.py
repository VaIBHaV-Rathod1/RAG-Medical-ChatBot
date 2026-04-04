from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RAG Medcal ChatBot",
    version="0.1",
    author="Vaibhav",
    packages=find_packages(),
    install_requires = requirements,
)