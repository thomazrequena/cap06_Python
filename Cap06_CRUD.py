import os
import subprocess
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
    5 - Cadastrar Parâmetros Atuais
    6 - Sair
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
            cursor.execute("SELECT ID, NOME, DURACAO_ESTIMADA, ILUMINACAO_HRS FROM FASES_CULTIVO")
            fases = cursor.fetchall()
            print("\n--- Fases Cadastradas ---")
            for f in fases:
                print(f"ID: {f[0]} | Nome: {f[1]} | Duração: {f[2]} dias | Luz: {f[3]}h")
        except Exception as e:
            print("Erro ao listar fases:", e)
        input("\nPressione ENTER para continuar...")

    elif opcao == 3:
        try:
            id_fase = int(input("ID da fase a alterar: "))

            print("\n--- Dados novos ---")
            novo_nome = input("Novo nome.........................: ")
            nova_descricao = input("Nova descrição....................: ")
            nova_duracao = int(input("Nova duração estimada (dias).....: "))
            nova_iluminacao = int(input("Nova iluminação (horas/dia)......: "))
            nova_umid_min = float(input("Nova umidade mínima (%)..........: "))
            nova_umid_max = float(input("Nova umidade máxima (%)..........: "))
            nova_temp_min = float(input("Nova temperatura mínima (°C).....: "))
            nova_temp_max = float(input("Nova temperatura máxima (°C).....: "))
            novo_n = input("Novo Nitrogênio (alto/médio/baixo): ")
            novo_p = input("Novo Fósforo   (alto/médio/baixo): ")
            novo_k = input("Novo Potássio  (alto/médio/baixo): ")

            cursor.setinputsizes(descricao=oracledb.CLOB)

            cursor.execute("""
                UPDATE FASES_CULTIVO 
                SET NOME = :nome, DESCRICAO = :descricao, DURACAO_ESTIMADA = :duracao, 
                    ILUMINACAO_HRS = :iluminacao, UMIDADE_MIN = :umid_min, UMIDADE_MAX = :umid_max,
                    TEMP_MIN = :temp_min, TEMP_MAX = :temp_max, NITROGENIO = :n,
                    FOSFORO = :p, POTASSIO = :k
                WHERE ID = :id
            """, {
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

    elif opcao == 5:  # Cadastro de Parâmetros Atuais
        try:
            print("\n--- Cadastrar Parâmetros Atuais ---")
            id_fase = int(input("ID da Fase de Cultivo: "))
            umidade_atual = float(input("Umidade Atual (%): "))
            temperatura_atual = float(input("Temperatura Atual (°C): "))
            iluminacao_atual = int(input("Horas de Iluminação Atual: "))
            nitrogenio_atual = input("Nitrogênio Atual (alto/médio/baixo): ")
            fosforo_atual = input("Fósforo Atual (alto/médio/baixo): ")
            potassio_atual = input("Potássio Atual (alto/médio/baixo): ")

            sql = """
                INSERT INTO MONITORAMENTO_PARAMETROS 
                (ID_FASE_CULTIVO, UMIDADE_ATUAL, TEMPERATURA_ATUAL, 
                 ILUMINACAO_ATUAL, NITROGENIO_ATUAL, FOSFORO_ATUAL, POTASSIO_ATUAL)
                VALUES (:id_fase, :umidade_atual, :temperatura_atual, 
                        :iluminacao_atual, :nitrogenio_atual, :fosforo_atual, :potassio_atual)
            """

            cursor.execute(sql, {
                "id_fase": id_fase,
                "umidade_atual": umidade_atual,
                "temperatura_atual": temperatura_atual,
                "iluminacao_atual": iluminacao_atual,
                "nitrogenio_atual": nitrogenio_atual,
                "fosforo_atual": fosforo_atual,
                "potassio_atual": potassio_atual
            })

            conn.commit()
            print("\n✔️ Parâmetros atuais cadastrados com sucesso!")

            # Verificar divergência com FASES_CULTIVO
            cursor.execute("""
                SELECT UMIDADE_MIN, UMIDADE_MAX, TEMP_MIN, TEMP_MAX, 
                       ILUMINACAO_HRS, NITROGENIO, FOSFORO, POTASSIO
                FROM FASES_CULTIVO WHERE ID = :id
            """, {"id": id_fase})
            ideal = cursor.fetchone()

            divergente = False
            if ideal:
                umid_min, umid_max, temp_min, temp_max, luz_ideal, n_ideal, p_ideal, k_ideal = ideal

                if not (umid_min <= umidade_atual <= umid_max):
                    divergente = True
                elif not (temp_min <= temperatura_atual <= temp_max):
                    divergente = True
                elif iluminacao_atual != luz_ideal:
                    divergente = True
                elif nitrogenio_atual.lower() != n_ideal.lower():
                    divergente = True
                elif fosforo_atual.lower() != p_ideal.lower():
                    divergente = True
                elif potassio_atual.lower() != k_ideal.lower():
                    divergente = True

                if divergente:
                    print("\n⚠️ Divergência detectada! Executando checklist...")
                    subprocess.run(["python", "Cap06_Checklist.py"])
                else:
                    print("\n✅ Parâmetros dentro da faixa ideal.")
            else:
                print("⚠️ Fase de cultivo não encontrada.")

        except Exception as e:
            print("Erro ao cadastrar parâmetros atuais:", e)
        input("\nPressione ENTER para continuar...")

    elif opcao == 6:
        print("Saindo do sistema...")
        break

    else:
        print("\n⚠️ Opção inválida!")
        input("Pressione ENTER para continuar...")
