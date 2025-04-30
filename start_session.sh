
#!/bin/bash
# Exit on error
set -e

echo "[+] Starting AI Assistant session setup..."

# Activate the Python virtual environment
echo "[+] Activating Python virtual environment..."
source ~/ai_assistant_env/bin/activate

# Define backup location on Google Drive
GDRIVE_BACKUP_PATH="$HOME/Google Drive/vatsalbach@gmail.com/0AIPOis-4Lsp5Uk9PVA/1XX5MRtuvxXc7ZIJKEL7bTW0QicNJ8zJt/1mmDA4huDKcbKaAcCU_HeuNyarkilV2YN"

# Restore the latest backup for essential folders
echo "[+] Syncing essential folders from Google Drive backup..."
for folder in config data models; do
    if [ -d "$GDRIVE_BACKUP_PATH/$folder" ]; then
        echo "[+] Syncing $folder..."
        rsync -av --delete "$GDRIVE_BACKUP_PATH/$folder/" ./$folder/
    else
        echo "[!] Folder $folder not found in backup."
    fi
done

# Pull the latest changes from GitHub
echo "[+] Pulling latest updates from GitHub..."
git -C ~/ai_assistant_env pull origin main

echo "[✓] Environment ready. You're good to go!"
