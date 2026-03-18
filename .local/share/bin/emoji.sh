rofi -dmenu -i -p "Emoji" -config ~/.config/rofi/config-fuzz.rasi < ~/.config/rofi/emojis.txt \
| awk '{print $1}' \
| tr -d '\n' \
| wl-copy
