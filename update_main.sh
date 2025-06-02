#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------------------------
# Script: update_main.sh
# Objetivo: Forçar o Git local a ficar idêntico a origin/main, descartando
#           quaisquer mudanças locais (tracked ou untracked).
#
# Como usar:
#   1) Coloque este arquivo na raiz do seu repositório (onde está .git e manage.py).
#   2) Execute:
#        chmod +x update_main.sh
#        ./update_main.sh
#
#   Isso fará:
#     • git fetch origin
#     • git checkout main
#     • git reset --hard origin/main
#     • git clean -fd
# ------------------------------------------------------------------------------

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
