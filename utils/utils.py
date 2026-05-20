
def formatar_valor(valor):
    if valor >= 1_000_000_000:
        return f"R$ {valor/1_000_000_000:.1f} BI"
    elif valor >= 1_000_000:
        return f"R$ {valor/1_000_000:.1f} MI"
    else:
        return f"R$ {valor:,.2f}"
