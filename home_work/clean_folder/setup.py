from setuptools import setup, find_namespace_packages

setup(
    name='Sort Folder',
    version='1',
    description='very useful code for folder sorting',
    url='https://github.com/paukdv/Module_7/',
    author='paukdv',
    author_email='paukdv@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:run']}
)
