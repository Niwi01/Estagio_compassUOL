CREATE TABLE refinando AS
SELECT 
bkjson.tituloprincipal AS tituloprincipal_json,
CASE WHEN bkjson.anolancamento = '\N' THEN NULL ELSE CAST(bkjson.anolancamento AS INT) END AS anolancamento_json,
bkjson.id AS id_json,
bkjson.notamedia AS notamedia_json,
bkjson.numerovotos AS numerovotos_json,
bkcsv.id AS id_csv,
bkcsv.titulopincipal AS tituloprincipal_csv,
CASE WHEN bkcsv.anolancamento = '\N' THEN NULL ELSE CAST(bkcsv.anolancamento AS INT) END AS anolancamento_csv,
CASE WHEN bkcsv.tempominutos = '\N' THEN NULL ELSE CAST(bkcsv.tempominutos AS INT) END AS tempominutos_csv,
bkcsv.genero AS generos,
CASE WHEN bkcsv.notamedia = '\N' THEN NULL ELSE CAST(bkcsv.notamedia AS DOUBLE) END AS notamedia_csv,
CASE WHEN bkcsv.numerovotos = '\N' THEN NULL ELSE CAST(bkcsv.numerovotos AS INT) END AS numerovotos_csv,
bkcsv.personagem AS personagem_csv,
bkcsv.nomeartista AS nomeartista_csv, 
CASE WHEN bkcsv.anonascimento = '\N' THEN NULL ELSE CAST(bkcsv.anonascimento AS INT) END AS anonascimento_csv,
CASE WHEN bkcsv.anofalecimento = '\N' THEN NULL ELSE CAST(bkcsv.anofalecimento AS INT) END AS anofalecimento_csv,
bkcsv.profissao AS profissao_csv
FROM "12" as bkjson join movies as bkcsv on bkcsv.id = bkjson.id