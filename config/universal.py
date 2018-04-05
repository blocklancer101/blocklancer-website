import urllib

import constants

BASE_URL = 'https://' + constants.HOST if constants.HTTPS else 'http://' + constants.HOST

BUSINESS_NAME = 'Blocklancer'
CONTACT_EMAIL = 'blocklancer101@gmail.com'

PRODUCT_BRIEF_URL = BASE_URL + '/product-brief'
WHITEPAPER_URL = BASE_URL + '/whitepaper'

DEMO_DAPP_URL = 'http://localhost:3000'

GITHUB_URL = 'https://github.com/blocklancer101'
SLACK_URL = '#'
DISCORD_URL = 'https://discord.gg'
CHATBOT_URL = 'https://m.me/ChatbotCommerce'
TWITTER_URL = 'https://twitter.com'
FACEBOOK_URL = 'https://www.facebook.com/blocklancer101/'

DEFAULT_SHARE_MSG = urllib.quote_plus('Check out ' + BUSINESS_NAME + ', an exciting blockchain project that will decentralize the sharing economy.')
