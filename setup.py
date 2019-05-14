"""Package setup utilities"""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

REQUIRES = ['requests']
DEVELOP_REQUIRES = [
    "pylint==2.1.1",
    "pytest==4.0.0",
    "responses==0.10.4"
]

setuptools.setup(
    name="devicepilot",
    version="1.0.1",
    author="DevicePilot",
    author_email="tom.wallace@devicepilot.com",
    description="DevicePilot SDK for IoT Analytics",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/devicepilot/devicepilot-py",
    packages=setuptools.find_packages(exclude=('tests',)),
    install_requires=REQUIRES,
    extras_require={"develop": DEVELOP_REQUIRES},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Database :: Front-Ends",
        "Topic :: Home Automation",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging"
    ],
)
