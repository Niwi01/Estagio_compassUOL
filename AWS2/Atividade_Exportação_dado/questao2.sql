select editora.codeditora as 'CodEditora',
		editora.nome as 'NomeEditora',
		count(livro.titulo) as 'QuantidadeLivros'
from livro right join editora on livro.editora = editora.codeditora  
group by editora.nome
order by QuantidadeLivros desc
limit 5