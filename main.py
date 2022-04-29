import os
import time

import git
import shutil
from flask import Flask
from git import Repo

repo = Repo('./')

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
def main():

    i1 = input("tem um site ou nao?: ")
    if i1 == 'sim':
        nDir = input("nome do site: ")
        os.chdir(nDir)
        os.system("hugo --minify")
        # repo.git.add(nDir)
        # repo.git.commit('-m','ola')
        # origin = repo.remote(name='origin')
        # origin.push()
        i2 = input("Pretende criar um novo post?: ")
        if i2 == 'sim':
            nficheiro = input("Escolha nome do ficheiro: ")
            titulo = input("Escolha titulo do post: ")
            path = os.path.join("content", "posts", nficheiro)
            file = open(path + '.md', 'a+')
            file.write("---")
            file.write("\n")
            file.write("title: " + "\"" + titulo + "\"")
            file.write("\n")
            file.write("draft: false")
            file.write("\n")
            file.write("---")
            file.write("\n")
            while True:
                text = input("Escreva o que desejar:  ")
                if text == ".":
                    file.close()
                    path = os.path.join("exemple", "content", "posts", nficheiro)
                    print(os.getcwd())
                    repo.git.add(path + '.md')
                    repo.git.add(os.path.join("exemple", "docs"))
                    repo.git.commit('-m', 'ola')
                    origin = repo.remote(name='origin')
                    origin.push()
                    os.system('xdg-open  https://JMMatosF.github.io/Hugo/')
                    os.system("hugo server -D")
                    # repo.git.add("main.py")
                    # repo.git.add(filename)
                    # commit = input("Mensagem de commit: ")
                    # repo.git.commit('-m', commit)
                    # origin = repo.remote(name='origin')
                    # origin.push()

                if text == "delete":
                    file.truncate(0)

                file.write(text)
                file.write("\n")

        if i2 == 'nao':
            os.system('xdg-open  http://localhost:1313/Hugo')
            os.system("hugo server -D")

    if i1 == 'nao':
        a = input("nome do diretorio: ")
        os.system("hugo new site " + a + " --force")
        os.chdir(a)
        sitename = input("Nome do site: ")
        os.system("git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke")
        file = open('config.toml', 'a')
        file.truncate(0)
        file.write("baseURL = \'http://example.org/\'")
        file.write("\n")
        file.write("languageCode = \'en-us\'")
        file.write("\n")
        file.write("title = " + "\'" + sitename + "\'")
        file.write("\n")
        file.write("theme = 'ananke'")
        file.write("\n")
        # file.write("publishDir = \"docs\"")
        file.close()
        os.system("hugo new posts/my-first-post.md")
        # repo.git.add(a)
        # repo.git.commit('-m', 'ola')
        # origin = repo.remote(name='origin')
        # origin.push()
        # original = r'Hugo\gh-pages.yml'
        # target = r'' + a
        # shutil.copyfile(original, target)
        os.system('xdg-open  http://localhost:1313/')
        os.system("hugo server -D")


main()
