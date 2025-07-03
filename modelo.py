# Probabilidades marginais e condicionais
probabilidades = {
    "HistoricoCompras": {
        "sim": 0.6,
        "nao": 0.4
    },
    "TempoNoSite": {
        "muito": 0.3,
        "pouco": 0.7
    },
    "InteracaoPromocao": {
        "sim": 0.5,
        "nao": 0.5
    },
    "Compra": {
        ("sim", "muito", "sim"): 0.9,
        ("sim", "muito", "nao"): 0.7,
        ("sim", "pouco", "sim"): 0.6,
        ("sim", "pouco", "nao"): 0.4,
        ("nao", "muito", "sim"): 0.5,
        ("nao", "muito", "nao"): 0.3,
        ("nao", "pouco", "sim"): 0.2,
        ("nao", "pouco", "nao"): 0.1
    }
}

def calcular_probabilidade_compra(evidencias):
    hist = evidencias["HistoricoCompras"]
    tempo = evidencias["TempoNoSite"]
    inter = evidencias["InteracaoPromocao"]

    p_hist = probabilidades["HistoricoCompras"][hist]
    p_tempo = probabilidades["TempoNoSite"][tempo]
    p_inter = probabilidades["InteracaoPromocao"][inter]

    p_compra_cond = probabilidades["Compra"][(hist, tempo, inter)]

    p_compra = p_hist * p_tempo * p_inter * p_compra_cond
    p_nao_compra = p_hist * p_tempo * p_inter * (1 - p_compra_cond)

    total = p_compra + p_nao_compra
    return {
        "Compra": round(p_compra / total, 4),
        "Nao_Compra": round(p_nao_compra / total, 4)
    }
