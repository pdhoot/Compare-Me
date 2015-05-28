from distutils.core import setup
setup(
  name = 'compareMe',
  packages = ['compareMe'], 
  version = '0.1',
  description = 'A comparison library',
  author = 'Punit Dhoot',
  author_email = 'punitdhoot1@gmail.com',
  url = 'https://github.com/pdhoot/Compare-Me', 
  download_url = 'https://github.com/pdhoot/Compare-Me/tarball/0.1',
  keywords = ['compare' , 'users' , 'spoj' ,'codechef' , 'github'], # arbitrary keywords
  classifiers = [],
  entry_points={
        'console_scripts': ['compareMe --spoj = compareMe.spoj']
    }
)
