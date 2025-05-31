listaDeLivros = [] 

livro ={'ISBN'     : '978-7522-718-3',
         'Titulo'  : 'Programação Python',
         'Autor'   : 'Nilo Ney Coutinho Menezes',
         'Editora' : 'Novatec',
         'Paginas' : 328,
         'Ano'     : 2019,
         'Genero'  : 'Técnico'
        }

listaDeLivros.append(livro)

livro ={'ISBN'     : '978-7522-718-3',
         'Titulo'  : 'Aonde a gente vai, papai?',
         'Autor'   : 'Jean-Louis Fournier',
         'Editora' : 'Intrinseca',
         'Paginas' : 158,
         'Ano'     : 2009,
         'Genero'  : 'Drama'
        }

listaDeLivros.append(livro)

print(listaDeLivros[0]['Titulo'])
print(listaDeLivros[1]['Titulo'])

