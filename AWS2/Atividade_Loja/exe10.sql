SELECT DISTINCT tbvendedor.nmvdd as 'vendedor', 
		sum(tbvendas.qtd*tbvendas.vrunt) as 'valor_total_vendas',
		ROUND(SUM(tbvendas.qtd*tbvendas.vrunt)*tbvendedor.perccomissao/100,2) as 'comissao'
FROM tbvendas LEFT JOIN tbvendedor on tbvendas.cdvdd = tbvendedor.cdvdd 
WHERE tbvendas.status = 'Concluído'
group by tbvendedor.nmvdd
order by comissao desc