from setuptools import setup

setup(name='{{cookiecutter.project_name}}',
      version='{{cookiecutter.version}}',
      description='{{cookiecutter.project_short_description}}',
      url='http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}',
      author='{{cookiecutter.full_name}}',
      author_email='{{cookiecutter.email}}',
      license='MIT',
      packages=['{{cookiecutter.project_name}}'],
      zip_safe=False)
