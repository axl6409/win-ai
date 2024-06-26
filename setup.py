from setuptools import setup, find_packages

setup(
    name="my_chatgpt_app",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
        "tk",
        "customtkinter",
    ],
    entry_points={
        "console_scripts": [
            "my_chatgpt_app=src.main:main",
        ],
    },
)
