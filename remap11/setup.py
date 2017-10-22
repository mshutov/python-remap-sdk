from setuptools import setup

install_reqs = [
    'requests >= 2.16.2'
]

setup(name='remap11',
      version='0.0.1',
      description='SDK for Remap API 1.1 of http://moysklad.ru',
      url='https://github.com/mshutov/python-remap-sdk',
      author='Mikhail Shutov',
      author_email='mikhail.shutov+pyremap11@gmail.com',
      license='MIT',
      packages=['remap11'],
      install_reqs=install_reqs,
      zip_safe=False)
