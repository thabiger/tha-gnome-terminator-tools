from setuptools import setup

setup(name='tha-gnome-terminator-tools',
      version='0.1',
      description='Automation scripts for the Gnome Terminator',
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
      zip_safe=False)
