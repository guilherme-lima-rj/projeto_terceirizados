# Importando bibliotecas
import pandas as pd
import os 
import glob
from datetime import datetime

# Parametros utilizados no código
date_time_file = datetime.now
input_files = '..\\dados'
output_dir = '..\\dados\\agrupados'
output_file = 'terceirizados_agrupados.csv'
output_file_dir = f'{output_dir}\\{output_file}'

# Listando arquivos xlsx
#excel_files = glob.glob(os.path.join(folder_files,'*.xlsx'))
#excel_files = glob.glob('..\\data\\*.xlsx')
#print(excel_files)

# Caso existam arquivos XLS, converte para CSV
#if not excel_files:
#    print('Nenhum arquivo XLSX para processamento.')
#else:
#    for excel_file in excel_files:
#        temp_file = pd.read_excel(excel_file)
#        temp_file.to_csv(folder_files)

# Listando TODOS os arquivos CSV, inclusive os convertidos de XLSX
csv_files = glob.glob(os.path.join(input_files,'*.csv'))

# Cria contador de arquivos
file_counter=0

# Verifica se há arquivos para processar
if not csv_files:
    print('Nenhum arquivo CSV para processamento.')
else:
    # Dataframe vazio que armazenara os dados dos arquivos
    df_result = []

    # Loop para processar os arquivos encontrados
    for csv_file in csv_files:
        try:
            # Adiciona 1 ao contador
            file_counter += 1

            # Lê o arquivo do array e carrega os dados num dataframe temporario
            df_temp = pd.read_csv(csv_file, sep=';')
                                  
            # Captura somente o nome do arquivo
            #file_name = os.path.basename(csv_file)

            # Criacao da coluna source que contem o nome do  arquivo de origem do registro
            #df_temp['source'] = file_name
           
            # Criacao de coluna com data e hora do processamento do arquivo
            #df_temp['datahora'] = datetime.now

            # Adiciona os dados processados ao dataframe principal
            df_result.append(df_temp)
                        
        except Exception as e:
            print(f'Erro ao ler o arquivo {csv_file} : {e}')
        
    # Verifica se o df_result contem dados
    if df_result:    
        # Concatena todos os dataframes salvosem um único dataframe
        df_result = pd.concat(df_result, ignore_index= True)

        # Cria o diretório de saída com permissão de escrita e leitura, caso não exista
        os.makedirs(output_dir, exist_ok=True)
        os.chmod(output_dir, 0o777)
        
        # Cria arquivo CSV com os dados do df_result
        df_result.to_csv(output_file_dir, index=False)

    else:
        print('Nenhum dado para ser salvo.')

# Quantidade de arquivos processados
print(f'Arquivos processados:{file_counter}')