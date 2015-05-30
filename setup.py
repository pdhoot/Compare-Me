from distutils.core import setup
setup(
  name = 'compareMe',
  packages = ['compareMe' , 'compareMe.bin'], 
  version = '1.0',
  description = 'A comparison library',
  author = 'Punit Dhoot',
  author_email = 'punitdhoot1@gmail.com',
  url = 'https://github.com/pdhoot/Compare-Me', 
  download_url = 'https://github.com/pdhoot/Compare-Me/tarball/1.0',
  keywords = ['compare' , 'users' , 'spoj' ,'codechef' , 'github'], # arbitrary keywords
  classifiers = [],
  scripts = ['compareMe/bin/compareMe'],
  install_requires = ['beautifulsoup4'],
  license = 'MIT'
)
