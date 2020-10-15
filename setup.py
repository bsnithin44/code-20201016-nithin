import setuptools

setuptools.setup(
    name="bmi",
    version="0.0.1",
    author="Nithin",
    author_email="bsnithin44@gmail.com",
    description="BMI calculator",
    url="https://www.github.com/bsnithin44/code-20201016-nithin",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)