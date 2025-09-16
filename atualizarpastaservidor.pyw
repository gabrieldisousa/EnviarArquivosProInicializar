import os
import shutil
from pathlib import Path

# Caminho da pasta compartilhada (outra máquina)
PASTA_REDE = r"\\pastacompartilhada\teste$"

# Caminho da pasta Inicializar do usuário atual
PASTA_INICIALIZAR = Path(os.getenv("APPDATA")) / r"Microsoft\Windows\Start Menu\Programs\Startup"

def copiar_arquivos():
    if not os.path.exists(PASTA_REDE):
        print("[ERRO] Pasta remota inacessível, saindo...")
        return

    for arquivo in os.listdir(PASTA_REDE):
        caminho_origem = os.path.join(PASTA_REDE, arquivo)

        # Copiar apenas arquivos (ignora subpastas)
        if os.path.isfile(caminho_origem):
            caminho_destino = os.path.join(PASTA_INICIALIZAR, arquivo)

            # Só copia se o arquivo da rede for mais novo ou não existir no destino
            if (not os.path.exists(caminho_destino) or
                os.path.getmtime(caminho_origem) > os.path.getmtime(caminho_destino)):
                try:
                    shutil.copy2(caminho_origem, caminho_destino)
                    print(f"[OK] Copiado: {arquivo} -> {PASTA_INICIALIZAR}")
                except Exception as e:
                    print(f"[ERRO] Falha ao copiar {arquivo} para {PASTA_INICIALIZAR}: {e}")

if __name__ == "__main__":
    copiar_arquivos()
