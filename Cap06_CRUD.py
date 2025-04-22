import os
import oracledb

# Conexão com Oracle
try:
    conn = oracledb.connect(user='rm563956', password="240981", dsn='oracle.fiap.com.br:1521/ORCL')
    cursor = conn.cursor()
except Exception as e:
    print("Erro ao conectar com o banco de dados:", e)
    exit()

# Loop principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---- CRUD - FASES DE CULTIVO ----")
    print("""
    1 - Cadastrar Fase
    2 - Listar Fases
    3 - Alterar Fase
    4 - Excluir Fase
    5 - Sair
    """)

    try:
        opcao = int(input("Escolha -> "))
    except ValueError:
        print("\n⚠️ Digite um número válido!")
        input("Pressione ENTER para continuar...")
        continue

    if opcao == 1:
        try:
            print("\n--- Cadastrar Nova Fase de Cultivo ---")
            nome = input("Nome da fase.........................: ")
            descricao = input("Descrição............................: ")
            duracao = int(input("Duração estimada (dias)..............: "))
            iluminacao = int(input("Horas de iluminação por dia..........: "))
            umid_min = float(input("Umidade mínima (%)...................: "))
            umid_max = float(input("Umidade máxima (%)...................: "))
            temp_min = float(input("Temperatura mínima (°C)..............: "))
            temp_max = float(input("Temperatura máxima (°C)..............: "))
            n = input("Nitrogênio (ex: alto/médio/baixo)....: ")
            p = input("Fósforo   (ex: alto/médio/baixo).....: ")
            k = input("Potássio  (ex: alto/médio/baixo).....: ")

            sql = """
                INSERT INTO FASES_CULTIVO 
                (NOME, DESCRICAO, DURACAO_ESTIMADA, ILUMINACAO_HRS, 
                 UMIDADE_MIN, UMIDADE_MAX, TEMP_MIN, TEMP_MAX, 
                 NITROGENIO, FOSFORO, POTASSIO)
                VALUES (:nome, :descricao, :duracao, :iluminacao, 
                        :umid_min, :umid_max, :temp_min, :temp_max, 
                        :n, :p, :k)
            """

            cursor.setinputsizes(descricao=oracledb.CLOB)

            cursor.execute(sql, {
                "nome": nome,
                "descricao": descricao,
                "duracao": duracao,
                "iluminacao": iluminacao,
                "umid_min": umid_min,
                "umid_max": umid_max,
                "temp_min": temp_min,
                "temp_max": temp_max,
                "n": n,
                "p": p,
                "k": k
            })

            conn.commit()
            print("\n✔️ Fase cadastrada com sucesso!")
        except Exception as e:
            print("Erro ao cadastrar fase:", e)
        input("\nPressione ENTER para continuar...")

    elif opcao == 2:
        try:
            cursor.execute("SELECT ID, NOME, DURACAO_ESTIMADA FROM FASES_CULTIVO")
            fases = cursor.fetchall()
            print("\n--- Fases Cadastradas ---")
            for f in fases:
                print(f"ID: {f[0]} | Nome: {f[1]} | Duração: {f[2]} dias")
        except Exception as e:
            print("Erro ao listar fases:", e)
        input("\nPressione ENTER para continuar...")

    elif opcao == 3:
        try:
            id_fase = int(input("ID da fase a alterar: "))

            # Buscar dados atuais
            cursor.execute("SELECT * FROM FASES_CULTIVO WHERE ID = :id", {"id": id_fase})
            fase = cursor.fetchone()

            if not fase:
                print("⚠️ Fase não encontrada!")
                input("Pressione ENTER para continuar...")
                continue

            descricao_texto = fase[2].read() if fase[2] else ""

            print("\n--- Dados Atuais da Fase ---")
            print(f"Nome................: {fase[1]}")
            print(f"Descrição...........: {descricao_texto[:100]}{'...' if len(descricao_texto) > 100 else ''}")
            print(f"Duração Estimada....: {fase[3]} dias")
            print(f"Iluminação..........: {fase[4]} horas/dia")
            print(f"Umidade Mínima......: {fase[5]}%")
            print(f"Umidade Máxima......: {fase[6]}%")
            print(f"Temperatura Mínima..: {fase[7]}°C")
            print(f"Temperatura Máxima..: {fase[8]}°C")
            print(f"Nitrogênio..........: {fase[9]}")
            print(f"Fósforo.............: {fase[10]}")
            print(f"Potássio............: {fase[11]}")

            print("\n--- Informe os novos valores ---")
            novo_nome = input("Novo nome..............................: ")
            nova_descricao = input("Nova descrição.........................: ")
            nova_duracao = int(input("Nova duração estimada (dias)..........: "))
            nova_iluminacao = int(input("Nova iluminação (horas/dia)...........: "))
            nova_umid_min = float(input("Nova umidade mínima (%)...............: "))
            nova_umid_max = float(input("Nova umidade máxima (%)...............: "))
            nova_temp_min = float(input("Nova temperatura mínima (°C)..........: "))
            nova_temp_max = float(input("Nova temperatura máxima (°C)..........: "))
            novo_n = input("Novo nível de nitrogênio..............: ")
            novo_p = input("Novo nível de fósforo.................: ")
            novo_k = input("Novo nível de potássio................: ")

            sql = """
                UPDATE FASES_CULTIVO 
                SET NOME = :nome,
                    DESCRICAO = :descricao,
                    DURACAO_ESTIMADA = :duracao,
                    ILUMINACAO_HRS = :iluminacao,
                    UMIDADE_MIN = :umid_min,
                    UMIDADE_MAX = :umid_max,
                    TEMP_MIN = :temp_min,
                    TEMP_MAX = :temp_max,
                    NITROGENIO = :n,
                    FOSFORO = :p,
                    POTASSIO = :k
                WHERE ID = :id
            """

            cursor.setinputsizes(descricao=oracledb.CLOB)

            cursor.execute(sql, {
                "nome": novo_nome,
                "descricao": nova_descricao,
                "duracao": nova_duracao,
                "iluminacao": nova_iluminacao,
                "umid_min": nova_umid_min,
                "umid_max": nova_umid_max,
                "temp_min": nova_temp_min,
                "temp_max": nova_temp_max,
                "n": novo_n,
                "p": novo_p,
                "k": novo_k,
                "id": id_fase
            })

            conn.commit()
            print("\n✔️ Fase alterada com sucesso!")

        except Exception as e:
            print("Erro ao alterar fase:", e)
        input("\nPressione ENTER para continuar...")

    elif opcao == 4:
        try:
            id_excluir = int(input("ID da fase a excluir: "))
            cursor.execute("DELETE FROM FASES_CULTIVO WHERE ID = :id", {"id": id_excluir})
            conn.commit()
            print("\n✔️ Fase excluída com sucesso!")
        except Exception as e:
            print("Erro ao excluir fase:", e)
        input("\nPressione ENTER para continuar...")

    elif opcao == 5:
        print("Saindo do sistema...")
        break

    else:
        print("\n⚠️ Opção inválida!")
        input("Pressione ENTER para continuar...")
