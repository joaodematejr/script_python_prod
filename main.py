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
