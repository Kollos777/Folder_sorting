from setuptools import setup

setup(
   name='clean_folder',
   version='1.0',
   description='A useful module',
   url="https://github.com/Kollos777/Folder_sorting.git",
   author='Kostiantyn Litvinov',
   author_email='Kolloslit@gmail.com',
   license='MIT',
   packages=['clean_folder'],
   install_requires=[],
   entry_points={
       'console_scripts': [
           'clean_folder=clean_folder.clean:main'
       ]
   }
)
