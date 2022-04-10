import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimplifyPython",
    version="0.0.3",
    author="Isaac",
    author_email="necrownyx@outlook.com",
    description="Simplifys aspects of python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Necrownyx/SimplifyPython",
    project_urls={
        "Bug Tracker": "https://github.com/Necrownyx/SimplifyPython/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'json',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
