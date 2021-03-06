from setuptools import setup, find_packages
from django_th import __version__ as version

install_requires = [
    'djangorestframework==3.5.3',
    'Django==1.8.17',
    'django-formtools==1.0',
    'arrow==0.10.0',
    'django-js-reverse==0.7.2',
    'django-redis==4.6.0',
    'requests-oauthlib==0.7.0',
    'pypandoc==1.3.3',
    'flake8==3.2.1',
]

extras_require_evernote = [
    'evernote3',
    'pytidylib==0.3.2',
]
extras_require_github = [
    'github3.py==1.0.0a4',
]
extras_require_instapush = [
    'instapush==0.1.2'
]
extras_require_pelican = [
    'awesome-slugify==1.6.5',
]
extras_require_pocket = [
    'pocket==0.3.6',
]
extras_require_pushbullet = [
    'pushbullet.py==0.10.0'
]
extras_require_rss = [
    'feedparser==5.2.1',
]
extras_require_taiga = [
    'python-taiga==0.8.6',
]
extras_require_todoist = [
    'todoist-python==7.0.13',
]
extras_require_trello = [
    'py-trello==0.7.0',
    'pytz==2016.7',
]
extras_require_twitter = [
    'twython==3.4.0',
]
extras_require_wallabag = [
    'wallabag_api==1.1.0',
]


extras_require_all = \
    extras_require_evernote\
    + extras_require_github\
    + extras_require_instapush\
    + extras_require_pelican\
    + extras_require_pocket\
    + extras_require_pushbullet\
    + extras_require_rss\
    + extras_require_taiga\
    + extras_require_todoist\
    + extras_require_trello\
    + extras_require_twitter\
    + extras_require_wallabag


setup(
    name='django_th',
    version=version,
    description='Trigger Happy - take the control of your data '
                'with this bridge between your internet services',
    author='FoxMaSk',
    maintainer='FoxMaSk',
    author_email='foxmask@trigger-happy.eu',
    maintainer_email='foxmask@trigger-happy.eu',
    url='https://github.com/foxmask/django-th',
    download_url="https://github.com/foxmask/django-th/"
                 "archive/trigger-happy-" + version + ".zip",
    packages=find_packages(exclude=['django_th/local_settings']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Database',
    ],
    install_requires=install_requires,
    extras_require={
        'all': extras_require_all,
        'evernote': extras_require_evernote,
        'github': extras_require_github,
        'instapush': extras_require_instapush,
        'pelican': extras_require_pelican,
        'pocket': extras_require_pocket,
        'pushbullet': extras_require_pushbullet,
        'rss': extras_require_rss,
        'taiga': extras_require_taiga,
        'todoist': extras_require_todoist,
        'trello': extras_require_trello,
        'twitter': extras_require_twitter,
        'wallabag': extras_require_wallabag,
    },
    include_package_data=True,
)
