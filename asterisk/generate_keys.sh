#!/bin/bash

set -e

echo " Carregando variáveis do .env..."
set -a
source './.env'
set +a

SOURCE_DIR="./"
TARGET_DIR="/etc/asterisk"



find "$SOURCE_DIR" -type f -name "*.conf" | while read file; do
    # Mantém estrutura de pastas
    relative_path="${file#$SOURCE_DIR/}"
    target_file="$TARGET_DIR/$relative_path"

    mkdir -p "$(dirname "$target_file")"

    # Substitui variáveis e copia
    envsubst < "$file" > "$target_file"

done

echo "Configurações copiadas e processadas com sucesso!"

KEY_DIR="/etc/asterisk/keys"

echo "Gerando certificado..."

sudo mkdir -p $KEY_DIR

sudo openssl req -x509 -newkey rsa:2048 \
-keyout $KEY_DIR/asterisk.key \
-out $KEY_DIR/asterisk.crt \
-days 365 \
-nodes \
-subj "/CN=$SERVER_HOST/O=VoIP App"

sudo cat $KEY_DIR/asterisk.key $KEY_DIR/asterisk.crt > $KEY_DIR/asterisk.pem

echo "Certificado gerado!"