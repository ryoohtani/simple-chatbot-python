from distutils.core import setup

setup(name='python_setup',
      version='1.0',
      description='Python package',
      author='ryoohtani',
      author_email='test@gmail.com',
      url='',
      packages=['backend.pyfile.csv_module'],
     )

"""
実行コマンド
python setup.py sdist
"""