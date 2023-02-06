from schema import Bookmark

rows = Bookmark.select()

def see_bookmarks():
    for row in rows:
      print ("name: {}\nlink: {}\n------------------------".format(row.name, row.link))

see_bookmarks()