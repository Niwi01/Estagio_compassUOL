select count(livro.edicao) as "quantidade", editora.nome, endereco.estado, endereco.cidade
from editora join endereco on editora.endereco = codendereco
			join livro on editora.codeditora = livro.editora
group by editora.nome, editora.endereco
order by quantidade desc 
limit 5