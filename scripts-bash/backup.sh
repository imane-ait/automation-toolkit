#!/bin/bash

SOURCE_DIR="$1"
BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_${DATE}.tar.gz"

# Vérifier qu'un argument est fourni
if [ -z "$SOURCE_DIR" ]; then
    echo "ERROR: provide a source directory"
    echo "Usage: ./backup.sh /path/to/folder"
    exit 1
fi

# Vérifier que le dossier source existe
if [ ! -d "$SOURCE_DIR" ]; then
    echo "ERROR: source directory does not exist"
    exit 1
fi

# Créer le dossier backup s'il n'existe pas
mkdir -p "$BACKUP_DIR"

# Créer l'archive
echo "Creating backup..."
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

# Vérifier si ça a marché
if [ $? -eq 0 ]; then
    echo "SUCCESS: $BACKUP_NAME created"
else
    echo "ERROR: backup failed"
    exit 1
fi

# Garder seulement les 5 derniers backups
ls -t "$BACKUP_DIR"/backup_*.tar.gz | tail -n +6 | xargs -r rm

echo "Done. Backups kept: $(ls "$BACKUP_DIR" | wc -l)"
