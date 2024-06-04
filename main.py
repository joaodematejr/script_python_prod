import pandas as pd

# Leitura do arquivo CSV com delimitador ';'
csv_file_path = 'Basesocios_29-05-24.csv'
df = pd.read_csv(csv_file_path, delimiter=';')

# Conversão para JSON como uma lista de objetos
json_data = df.to_json(orient='records', force_ascii=False, indent=4)

# Salvando o JSON em um arquivo
json_file_path = 'arquivo.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print(f'Arquivo JSON salvo em: {json_file_path}')

# Gerar comandos SQL INSERT INTO
insert_statements = []

for index, row in df.iterrows():
    insert_statement = f"INSERT INTO tb_member (name, cpf, plano) VALUES ('{row['nome']}', '{row['cpf']}', '{row['plano']}');"
    insert_statements.append(insert_statement)

# Salvar os comandos SQL em um arquivo
sql_file_path = 'inserts.sql'
with open(sql_file_path, 'w', encoding='utf-8') as sql_file:
    for statement in insert_statements:
        sql_file.write(statement + '\n')

print(f'Arquivo SQL salvo em: {sql_file_path}')
