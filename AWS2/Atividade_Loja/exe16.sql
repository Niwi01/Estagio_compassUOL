SELECT tbvendas.estado, tbvendas.nmpro,	round(avg(tbvendas.qtd),4) as 'quantidade_media'
FROM tbvendas
where tbvendas.status = 'Concluído'
group by tbvendas.nmpro, tbvendas.estado
order by tbvendas.estado
