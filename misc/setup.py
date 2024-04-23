import pathlib
import setuptools

setuptools.setup(
    name="ghostwindow",
    version="1.0.0",
    author="rk767",
    author_email="/",
    description="A small package with some useful window utility functions",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/rk767/ghost-window",
    license="Apache 2.0",
    project_urls={
        "Documentation": "https://github.com/rk767/ghost-window",
        "Source": "https://github.com/rk767/ghost-window",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    include_package_data=True,
)