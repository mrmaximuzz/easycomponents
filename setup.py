import setuptools

setuptools.setup(
    name="easycomponents",
    version="0.1.0",
    author="Maxim Petrov",
    author_email="mmrmaximuzz@gmail.com",
    description="Utility for architects to manage components in projects",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
)
