#!/bin/bash

sudo pacman -S git base-devel hyprland alacritty xdg-desktop-portal-hyprland waybar swaync rofi qt6ct qt5ct dolphin kvantum cliphist

if pacman -Qi "paru" > /dev/null; then
  echo "Creating Directories"
else
  echo "PARU package manager is not installed installing."
  git clone https://aur.archlinux.org/paru.git /tmp/paru
  cd /tmp/paru
  makepkg -si
  echo "PARU installed, Creating Directories"
fi

# Create Directories

mkdir -p ~/.local/share/bin

mkdir -p ~/.local/bin

mkdir -p ~/Pictures/Wallpapers/

mkdir -p ~/room-dots/backup/.local/bin/

mkdir -p ~/room-dots/backup/.local/share/bin/

mkdir -p ~/room-dots/backup/.config/

mkdir -p ~/room-dots/backup/Pictures/Wallpapers/

# Backup existing data

cp -r ~/.local/share/bin ~/room-dots/backup/.local/share/bin

cp -r ~/.local/bin ~/room-dots/backup/.local/bin

cp -r ~/.config ~/room-dots/backup/.config

cp -r ~/Pictures/Wallpapers ~/room-dots/backup/Pictures/Wallpapers

# Copy new configuration to directories

cp -r ~/room-dots/.config/ ~/.config

cp -r ~/room-dots/.local/share/bin ~/.local/share/bin

cp -r ~/room-dots/.local/bin ~/.local/bin


echo "Installing optional packages..."
sudo pacman -S keepassxc nvim

echo "Installing Zen Browser"
paru zen-browser

echo "Installing NVChad"
git clone https://github.com/NvChad/starter ~/.config/nvim

echo "Run nvim and then do :MasonInstallAll and :TSInstallAll"
echo "Delete the .git directory from .config/nvim"
