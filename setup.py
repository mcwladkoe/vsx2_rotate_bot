from setuptools import setup, find_packages

requires = [
    'flask',
    'flask_bootstrap',
    'waitress',
    'python-telegram-bot',
]

setup(
    name='vsx2_rotate_text_bot',
    version='1.0.0',
    description='Rotate text telegram bot',
    author='Vladyslav Samotoy',
    author_email='svevladislav@gmail.com',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requires,
    entry_points="""\
        [console_scripts]
        rotate_text_bot = rotate_text.bot:main
    """,
    dependency_links=[
        "git+https://github.com/mcwladkoe/vsx2_rotate",
    ]
)
