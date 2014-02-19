# -*- coding: utf-8 -*-
try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    import setuptools

setuptools.setup(
    name='phoenix',
    version='0.1',
    description='',
    author='',
    author_email='',
    install_requires=[
        "pecan",
    ],
    test_suite='phoenix',
    zip_safe=False,
    include_package_data=True,
    packages=setuptools.find_packages(exclude=['ez_setup'])
)
