#!/bin/bash

# Import Pywal colors
. "$HOME/.cache/wal/colors.sh"

# Options
shutdown="󰐥 SHUTDOWN"
reboot="󰜉 REBOOT"
lock="󰌾 LOCK"
suspend="󰤄 SUSPEND"
logout="󰍃 LOGOUT"

# Rofi Command
run_rofi() {
	echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi -dmenu \
		-p "󰣇 SYSTEM" \
		-mesg "Wallpaper: $(cat $HOME/.cache/wal/wal | xargs basename)" \
		-theme-str "window { width: 350px; border: 2px; border-color: $color3; background-color: #000000; }" \
		-theme-str "listview { lines: 5; }" \
		-theme-str "element selected { background-color: $color3; text-color: #000000; }"
}

# Execute based on selection
case "$(run_rofi)" in
	$shutdown) systemctl poweroff ;;
	$reboot) systemctl reboot ;;
	$lock) hyprlock ;; # Or your preferred locker
	$suspend) systemctl suspend ;;
	$logout) hyprctl dispatch exit ;;
esac
