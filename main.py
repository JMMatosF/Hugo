import os
# import time
import git
import cria_post
# import shutil
# from flask import Flask
from git import Repo

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
def main():
    i1 = 'sim'

    if i1 == 'sim':
        # nDir = input("nome do site: ")
        # os.chdir(nDir)
        # repo.git.add(nDir)
        # repo.git.commit('-m','ola')
        # origin.push()
        i2 = input("Pretende criar um novo post?: ")
        if i2 == 'sim':
            title = input("Escolha titulo do post: ")
            name = title.replace(" ", "_")
            path = os.path.join("content", "posts", name)
            file = open(path + '.md', 'a+')
            file.write("---")
            file.write("\n")
            file.write("title: " + "\"" + title + "\"")
            file.write("\n")
            file.write("draft: false")
            file.write("\n")
            file.write("---")
            file.write("\n")
            while True:
                text = input("Escreva o que desejar:  ")
                file.write("\n")
                file.write(text)
                file.write("\n")
                if text == ".":
                    file.close()
                    path = os.path.join("content", "posts", name)
                    os.system("hugo")
                    repo.git.add(path + '.md')
                    repo.git.add(os.path.join("docs"))
                    repo.git.add(update=True)
                    repo.git.add(all=True)
                    repo.git.commit('-m', 'ola')
                    origin.push()
                    os.system('xdg-open https://github.com/JMMatosF/Hugo/actions')
                    # os.system('xdg-open  https://JMMatosF.github.io/Hugo/')

                if text == "delete":
                    file.truncate(0)

        elif i2 == 'nao':
            os.system("hugo")
            os.system('xdg-open  https://JMMatosF.github.io/Hugo/')
        elif i2 == 'apagar':
            i3 = input("post a apagar: ")
            os.remove('content/posts/' + i3 + '.md')
            os.remove('docs/posts/' + i3 + '/index.html')
            os.rmdir('docs/posts/' + i3)
            os.system('hugo')
            repo.git.add(all=True)
            repo.git.commit('-m', 'apagado ' + i3)
            origin.push()

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
        # os.system("hugo server -D")


main()
