#!/bin/bash
TARGET="root@192.168.1.26"
PORT="2222"
REMOTE_DIR="/config/custom_components/music_browser"

echo "Deploying Music Browser integration to Home Assistant..."

# Remove existing directory
ssh -p $PORT $TARGET "rm -rf $REMOTE_DIR"

# Create parent directory
ssh -p $PORT $TARGET "mkdir -p /config/custom_components"

# Copy the new version
scp -P $PORT -r custom_components/music_browser $TARGET:$REMOTE_DIR

echo "Music Browser integration deployed to $REMOTE_DIR"
echo "Remember to restart Home Assistant!"
