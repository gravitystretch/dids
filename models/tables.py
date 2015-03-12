
import datetime
import json
import os
"""
defines the table "dids" which is responsible for
holding reference info for all dids in the system.
The following information is stored:

author_id
date_created
title (optional)
likes (count of likes)
spam (count of 'marked as spam/invalid')
link (optional link to external site)
"""

db.define_table('dids',
                Field('author_id'),
                Field('date_created','datetime'),
                Field('title'),
                Field('likes','integer', default=0),
                Field('spam','integer'),
                Field('link')
                )
                
"""
defines the table holding all the contents of all the dids
in the system. this includes gifs, image id's, text bodies, and
videos (potentially)
"""

db.define_table('elements',
                Field('did_id'),
                Field('stack_num','integer'),
                Field('is_image','boolean'),
                Field('element_data')
                )

"""
defines table that will hold image locations on FS
"""
db.define_table('image',
                Field('img','upload'))

"""
defines the table holding all comments for all dids.
"""

db.define_table('comments',
                Field('did_id'),
                Field('date_created', 'datetime'),
                Field('author_id'),
                Field('reply_id'),
                Field('body','text')
                )
                
                
"""
defines the table holding all "likes"
"""
                
db.define_table('likes',
                Field('user_id'),
                Field('did_id')
                )


"""#########################################################################################
#######
#######   users table 
#######
######################################################################################### """

def get_user_name():
    s = ''
    if auth.user_id:
        s = auth.user.first_name
    else:
        s = 'John Doe'
    return s

    
"""
defines the table holding all "likes"
"""
                
db.define_table('followers',
                Field('follower_id'),
                Field('following_id')
                )
    
    
"""
defines table holding user information
"""
db.define_table('users',
                Field('user_id'),
                Field('username'),
                Field('profile_img', 'upload', default=os.path.join(request.folder, 'static', 'images', 'facebook.png')),
                Field('about'),
                Field('email'),
                Field('dids', 'reference dids'),
                Field('users_followers', 'reference users'),
                Field('users_following', 'reference users'),
                Field('feed'),
                )
db.users.username.default = get_user_name()
db.users.user_id.default = auth.user_id
db.users.about.default = ''
#db.users.email.default = auth.user.email


"""################################################################################################"""






