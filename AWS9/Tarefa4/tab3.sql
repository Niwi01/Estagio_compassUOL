create table filmes as
SELECT --pode colocar distinct
CONCAT(id_json, ',', id_csv) AS filme_id,
tituloprincipal_json,
anolancamento_json,
generos,
tituloprincipal_csv,
anolancamento_csv,
tempominutos_csv

FROM refinando;
