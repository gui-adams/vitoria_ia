#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------------------------
# Script: update_main.sh
# Objetivo: 
#   1) Forçar o Git local a ficar idêntico a origin/main, descartando quaisquer 
#      mudanças locais (tracked ou untracked).
#   2) Aplicar eventuais novas migrações do Django.
#   3) Reiniciar os serviços Nginx e Gunicorn.
#
# Como usar:
#   1) Coloque este arquivo na raiz do seu repositório (onde há .git e manage.py).
#   2) Certifique-se de que o virtualenv esteja ativado (se for necessário para o Django).
#   3) Execute:
#        chmod +x update_main.sh
#        ./update_main.sh
#
#   Isso fará, em ordem:
#     • export USE_POSTGRES=TRUE                    (garante que o Django use Postgres via settings.py)
#     • git fetch origin
#     • git checkout main
#     • git reset --hard origin/main
#     • git clean -fd
#     • python3 manage.py makemigrations
#     • python3 manage.py migrate
#     • sudo systemctl restart nginx
#     • sudo systemctl restart gunicorn
# ------------------------------------------------------------------------------

# 0) (Opcional) Exporta variável para usar Postgres se configurado no settings.py
export USE_POSTGRES=TRUE

# 1) Verifica se estamos dentro de um diretório Git
if [ ! -d ".git" ]; then
  echo "❌ ERRO: Este script precisa ser executado a partir da raiz de um repositório Git (onde há .git)."
  exit 1
fi

# 2) Atualiza referências remotas
echo "→ Fazendo git fetch origin..."
git fetch origin

# 3) Garante estar na branch 'main'
#    Se a sua branch principal for 'master' ou outro nome, ajuste abaixo.
BRANCH="main"
CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
  echo "→ Mudando para branch '$BRANCH' (estava em '$CURRENT_BRANCH')..."
  git checkout "$BRANCH"
else
  echo "→ Já estamos na branch '$BRANCH'."
fi

# 4) Reseta o conteúdo local para coincidir exatamente com origin/main
echo "→ Executando git reset --hard origin/$BRANCH..."
git reset --hard "origin/$BRANCH"

# 5) Remove quaisquer arquivos não rastreados (untracked) e diretórios vazios
echo "→ Limpando arquivos não rastreados com git clean -fd..."
git clean -fd

echo "✅ Seu repositório local agora está sincronizado e espelha origin/$BRANCH."

# 6) Aplicar migrações do Django (caso existam)
echo "→ Aplicando migrações do Django..."
python3 manage.py makemigrations
python3 manage.py migrate

# 7) Reiniciar serviços para carregar novo código
echo "→ Reiniciando o Nginx..."
sudo systemctl restart nginx

echo "→ Reiniciando o Gunicorn..."
sudo systemctl restart gunicorn

echo "✅ Atualização concluída e serviços reiniciados com sucesso."
