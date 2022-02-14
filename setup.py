from distutils.core import setup
setup(
  name = 'mnnllzz',
  packages = ['mnnllzz'],
  version = '1.0',
  license='MIT',
  description = 'Create randomized tests',
  author = 'Andrea Tomadin',
  author_email = 'andrea.tomadin@unipi.it',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['TEST', 'EXAM'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)