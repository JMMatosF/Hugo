import os
# import time
import git
from cria_post import cria_post
# import shutil
# from flask import Flask
from git import Repo
from utils.parse_input import parse_input

repo = Repo('./')
origin = repo.remote(name='origin')
with repo.config_writer() as git_config:
    git_config.set_value('user', 'email', 'jmatosfernandes@live.com.pt')
    git_config.set_value('user', 'name', 'JMMatosF')

with repo.config_reader() as git_config:
    print(git_config.get_value('user', 'email'))
    print(git_config.get_value('user', 'name'))

# List remotes
print('Remotes:')
for remote in repo.remotes:
    print(f'- {remote.name} {remote.url}')
try:
    remote = repo.create_remote('origin', url='git@github.com:JMMatosF/Hugo.git')
except git.exc.GitCommandError as error:
    print('')


########################################
if __name__ == '__main__':
    i1 = 'sim'

    parse_input(i1, repo, origin)