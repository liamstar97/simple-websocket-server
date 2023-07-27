"""Package configuration."""
from setuptools import find_packages, setup
setup(
    name="websocket-server",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'fastapi',
        'uvicorn[standard]'
    ],
    ## Entry point for command line and function to be executed
    entry_points={
        'console_scripts': ['websocket-server-start=main:main']
    }
)
