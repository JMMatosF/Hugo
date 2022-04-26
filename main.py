import os
import git
import shutil
from flask import Flask
from git import Repo

app = Flask(__name__)

i1 = input("tem um site ou nao?: ")
if i1 == 'sim':
    nDir = input("nome do site: ")
    os.chdir(nDir)
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
        file.write("draft: true")
        file.write("\n")
        file.write("---")
        file.write("\n")

        while True:
            text = input("Escreva o que desejar:  ")
            if text == ".":
                file.close()
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
        os.system("hugo server -D")


if i1 == 'nao':

    a = input("nome do diretorio: ")
    os.system("hugo new site " + a)
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
    file.close()
    os.system("hugo new posts/my-first-post.md")
    # original = r'Hugo\gh-pages.yml'
    # target = r'' + a
    # shutil.copyfile(original, target)
    os.system("hugo server -D")

filename = input("ficheiro a editar: ")
repo = Repo('./')


@app.route('/')
def main():
    while True:
        f = open(filename, "a+", encoding="utf-8")
        texto = input("Escreva o que desejar: ")
        if texto == ".":
            f.close()
            repo.git.add("main.py")
            repo.git.add(filename)
            commit = input("Mensagem de commit: ")
            repo.git.commit('-m', commit)
            origin = repo.remote(name='origin')
            origin.push()
            exit()
        f.write(texto)
        f.write("\n")
        if texto == "delete":
            f.truncate(0)


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
    print(f'Error creating remote: {error}')

if __name__ == '__main__':
    app.run()
