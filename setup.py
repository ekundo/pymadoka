from setuptools import setup, find_packages

setup(
    name='pymadoka',
    version='0.2.13-ekundo',
    py_modules=['pymadoka'],
    author = "ekundo",
    author_email = "ekundo@gmail.com",
    description = ("A library to control Daikin BRC1H (Madoka) thermostats"),
    license = "MIT",
    url = "https://github.com/ekundo/pymadoka",
    keywords = "thermostat homeautomation bluetooth",
    packages=find_packages()+ find_packages(where="./features"),
    install_requires=[
        'click',
        'bleak',
        'pyyaml',
        'asyncio-mqtt'
    ],
    entry_points='''
        [console_scripts]
        pymadoka=pymadoka.cli:cli
        pymadoka-mqtt=pymadoka.mqtt:run
    ''',
)
