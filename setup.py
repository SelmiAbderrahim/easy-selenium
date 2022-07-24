import setuptools

__version__ = "0.1.4"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='easy py selenium',
    version=__version__,
    author='Selmi Abderrahim',
    author_email='contact@selmi.tech',
    description='A tool that makes working with selenium easier.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SelmiAbderrahim/easy-selenium',
    project_urls = {
        "Bug Tracker": "https://github.com/SelmiAbderrahim/easy-selenium/issues"
    },
    include_package_data=True,
    package_data={
        "easy_selenium.executable": ["*.json"],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='python automation tools with selenium',
    license='MIT',
    packages=setuptools.find_packages(include=["easy_selenium", "easy_selenium.*"], exclude=["easy_selenium.tests", "easy_selenium.tests.*"]),
    install_requires=['lucd==0.1.7', 'beautifulsoup4==4.11.1', 'black==22.6.0', 'python-decouple==3.6', 'loguru==0.6.0'],
)
