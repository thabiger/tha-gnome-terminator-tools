from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='tha-gnome-terminator-tools',
      version='0.1',
      description='Automation scripts for Gnome Terminator',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/thabiger/tha-gnome-terminator-tools',
      author='Tomasz Habiger',
      author_email='tomasz.habiger@gmail.com',
      license='MIT',
      packages=['tha-gnome-terminator-tools'],
      install_requires=[
        'boto3',
        'jinja2',
        'objectpath'
      ],
      scripts=['tha-gnome-terminator-tools/bin/terminator-ec2-ssh'],
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3.8',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent"
      ],
)
