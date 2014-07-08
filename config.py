import os
import mailserversettings
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '1BluePonyDome'

OPENID_PROVIDERS = [
	{ 
		'name': 'Google', 
		'url': 'https://www.google.com/accounts/o8/id' 
	}
]
    
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# administrator list
ADMINS = ['dyspop@gmail.com']
RECIPIENTS = ['dyspop@gmail.com']

# pagination
POSTS_PER_PAGE = 10

# whoosh database for indexing and performing searches
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50