import oracledb

# Conexão com o Oracle
try:
    conn = oracledb.connect(user="rm563956", password="240981", dsn="oracle.fiap.com.br:1521/ORCL")
    cursor = conn.cursor()
except Exception as e:
    print("Erro ao conectar no banco:", e)
    exit()

print("\n--- CHECKLIST DE MONITORAMENTO AMBIENTAL ---\n")

# Consulta os dados de monitoramento e os ideais da fase correspondente
sql = """
SELECT 
    mp.ID,
    fc.NOME,
    mp.DATA_HORA,
    mp.UMIDADE_ATUAL, fc.UMIDADE_MIN, fc.UMIDADE_MAX,
    mp.TEMPERATURA_ATUAL, fc.TEMP_MIN, fc.TEMP_MAX,
    mp.ILUMINACAO_ATUAL, fc.ILUMINACAO_HRS,
    mp.NITROGENIO_ATUAL, fc.NITROGENIO,
    mp.FOSFORO_ATUAL, fc.FOSFORO,
    mp.POTASSIO_ATUAL, fc.POTASSIO
FROM MONITORAMENTO_PARAMETROS mp
JOIN FASES_CULTIVO fc ON mp.ID_FASE_CULTIVO = fc.ID
ORDER BY mp.DATA_HORA DESC
"""

cursor.execute(sql)
registros = cursor.fetchall()

# Análise dos registros
for reg in registros:
    (
        id_reg, fase_nome, data_hora,
        umid_atual, umid_min, umid_max,
        temp_atual, temp_min, temp_max,
        luz_atual, luz_ideal,
        n_atual, n_ideal,
        p_atual, p_ideal,
        k_atual, k_ideal
    ) = reg

    print(f"\n📅 Registro ID: {id_reg} | Fase: {fase_nome} | {data_hora}")
    print("------------------------------------------------------")

    # Umidade
    if not umid_min <= umid_atual <= umid_max:
        print(f"🔧 Umidade fora do ideal ({umid_atual}%). Ideal: {umid_min}–{umid_max}%.")
        if umid_atual < umid_min:
            print("➡️ Aumentar a umidade com um umidificador.")
        else:
            print("➡️ Reduzir a umidade com um desumidificador ou ventilação.")
    else:
        print("✅ Umidade OK.")

    # Temperatura
    if not temp_min <= temp_atual <= temp_max:
        print(f"🔧 Temperatura fora do ideal ({temp_atual}°C). Ideal: {temp_min}–{temp_max}°C.")
        if temp_atual < temp_min:
            print("➡️ Aumentar temperatura com aquecedor.")
        else:
            print("➡️ Reduzir temperatura com ar-condicionado ou exaustão.")
    else:
        print("✅ Temperatura OK.")

    # Iluminação
    if luz_atual != luz_ideal:
        print(f"🔧 Iluminação fora do ideal ({luz_atual}h). Ideal: {luz_ideal}h.")
        print("➡️ Ajustar temporizador das lâmpadas.")
    else:
        print("✅ Iluminação OK.")

    # Nutrientes
    def compara_nutriente(nome, atual, ideal):
        if atual.lower() != ideal.lower():
            print(f"🔧 {nome} fora do ideal (Atual: {atual}, Ideal: {ideal}).")
            print(f"➡️ Ajustar a dosagem de {nome.lower()} nos fertilizantes.")
        else:
            print(f"✅ {nome} OK.")

    compara_nutriente("Nitrogênio", n_atual, n_ideal)
    compara_nutriente("Fósforo", p_atual, p_ideal)
    compara_nutriente("Potássio", k_atual, k_ideal)

print("\n✅ Checklist finalizado!\n")
cursor.close()
conn.close()
