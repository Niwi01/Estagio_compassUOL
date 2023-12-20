SELECT tbvendas.cdpro, tbvendas.nmpro
FROM tbvendas, (SELECT nmpro, count(qtd) from tbvendas group by qtd)
WHERE tbvendas.status = 'Concluído' AND (dtven between '2014-02-03' and '2018-02-02')
order by tbvendas.qtd desc
limit 1
