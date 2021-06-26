#!/usr/bin/env python3

import os
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

'''
This script keeps the last number of files as specified
'''
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
PATH = os.environ.get('DROPBOX_PATH')
NUMBER_OF_FILES = int(os.environ.get('NUMBER_OF_FILES'))

with dropbox.Dropbox(ACCESS_TOKEN) as dbx:
    dbx.users_get_current_account()
    print("Successfully set up client!")
print(len(dbx.files_list_folder(PATH).entries))
to_delete = dbx.files_list_folder(PATH).entries[:((len(dbx.files_list_folder(PATH).entries))-NUMBER_OF_FILES)]
for entry in to_delete:
    dbx.files_delete_v2(entry.id)
print(len(dbx.files_list_folder(PATH).entries))
