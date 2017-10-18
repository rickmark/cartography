from distutils.core import setup

setup(
    name='cartography',
    version='1.0.0',
    packages=['geocoder'],
    url='https://github.com/rickmark/cartography',
    license='MIT',
    author='rickmark',
    author_email='rickmark@outlook.com',
    description='Example Geo-coding Service',
    install_requires=[
        'flask',
        'flask-restful',
        'redis',
        'python-consul',
        'googlemaps'
    ],
    setup_requires=[],
    tests_requrie=[]
)



## Test for consul, redis, that they are started, register redis in consul