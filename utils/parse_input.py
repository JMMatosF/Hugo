import os
from cria_post import cria_post


def parse_input(i1, repo, origin):
    if i1 == 'sim':
        i2 = input("Pretende criar um novo post?: ")
        post_dictonary = cria_post()
        if i2 == 'sim':
            # title = input("Escolha titulo do post: ")
            title = post_dictonary['title']
            name = title.replace(" ", "_")
            name1 = name.lower()
            path = os.path.join("content", "posts", name1)
            file = open(path + '.md', 'a+')
            file.write("---")
            file.write("\n")
            file.write("title: " + "\"" + title + "\"")
            file.write("\n")
            file.write("draft: false")
            file.write("\n")
            file.write("---")
            file.write("\n")
            # text = input("Escreva o que desejar:  ")
            text = post_dictonary['text']
            if text == ".":
                file.close()
                path = os.path.join("content", "posts", name1)
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
                file.write("\n")
                file.write(text)
                file.write("\n")
        elif i2 == 'nao':
            os.system("hugo")
            os.system('xdg-open  https://JMMatosF.github.io/Hugo/')
        elif i2 == 'apagar':
            i3 = input("post a apagar: ")
            i3i = i3.replace(" ", "_")
            os.remove('content/posts/' + i3i + '.md')
            os.remove('docs/posts/' + i3i + '/index.html')
            os.rmdir('docs/posts/' + i3i)
            os.system('hugo')
            repo.git.add(all=True)
            repo.git.commit('-m', 'apagado ' + i3i)
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
