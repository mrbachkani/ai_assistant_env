#!/bin/bash

# Exit on error
set -e

# Git sync
echo "[+] Pushing to GitHub..."
git add .
git commit -m "Auto-save: $(date '+%Y-%m-%d %H:%M:%S')"
git push

# Define source and destination
SRC_DIR=$(pwd)
GDRIVE_BACKUP_PATH="$HOME/Google Drive/vatsalbach@gmail.com/0AIPOis-4Lsp5Uk9PVA/1XX5MRtuvxXc7ZIJKEL7bTW0QicNJ8zJt/1mmDA4huDKcbKaAcCU_HeuNyarkilV2YN"

echo "[+] Copying essential folders to Google Drive backup..."
for folder in config data models; do
    if [ -d "$SRC_DIR/$folder" ]; then
        rsync -av --delete "$SRC_DIR/$folder/" "$GDRIVE_BACKUP_PATH/$folder/"
    fi
done

echo "[✓] Backup completed and GitHub sync done!"
