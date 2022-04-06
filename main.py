import git
from flask import Flask
from git import Repo

app = Flask(__name__)

repo = Repo('./')


@app.route('/')
def main():
    filename = input("ficheiro a editar: ")
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
