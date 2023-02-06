from schema import Bookmark
from schema import db

db.drop_tables([Bookmark])
db.create_tables([Bookmark])

Bookmark(name = 'Google', link = 'https://www.google.com/').save()
Bookmark(name = 'Linkedin', link = 'https://www.linkedin.com/').save()
Bookmark(name = 'Github', link = 'https://github.com/').save()
Bookmark(name = 'Reddit', link = 'https://www.reddit.com/').save()
Bookmark(name = 'Discord', link = 'https://discord.com/').save()
Bookmark(name = 'Leetcode', link = 'https://leetcode.com/').save()
Bookmark(name = 'Facebook', link = 'https://www.facebook.com/').save()
Bookmark(name = 'The Odin Project', link = 'https://www.theodinproject.com/').save()
