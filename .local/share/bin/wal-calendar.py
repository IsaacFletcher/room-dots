#!/usr/bin/env python3
"""
wal-calendar — pywal-colored GTK4 calendar popup anchored below waybar.
Requires: gtk4-layer-shell  (pacman -S gtk4-layer-shell)
Usage:    bind to waybar clock on-click
          clicking outside or Escape closes it
"""

import gi
import os
import sys

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
gi.require_version("Gtk4LayerShell", "1.0")
from gi.repository import Gtk, Gdk, GLib, Gtk4LayerShell as LayerShell

# ── Pywal colors ───────────────────────────────────────────────────────────────
WAL_COLORS = os.path.expanduser("~/.cache/wal/colors")

def load_wal_colors():
    colors = {}
    try:
        with open(WAL_COLORS) as f:
            for i, line in enumerate(f):
                colors[f"color{i}"] = line.strip()
    except FileNotFoundError:
        pass
    colors.setdefault("color0", "#000000")
    colors.setdefault("color3", "#ffffff")
    colors.setdefault("color4", "#aaaaaa")
    colors.setdefault("color5", "#888888")
    return colors

# ── CSS ────────────────────────────────────────────────────────────────────────
def build_css(c):
    return f"""
window {{
    background-color: #000000;
    border: 2px solid {c['color3']};
    border-radius: 6px;
}}

box.calendar-root {{
    padding: 8px;
}}

calendar {{
    background-color: #000000;
    color: #ffffff;
    border-radius: 4px;
    font-family: 'JetBrainsMono Nerd Font', 'CaskaydiaMono Nerd Font', monospace;
    font-size: 12px;
    font-weight: 900;
}}

calendar > header {{
    background-color: #000000;
    padding: 2px 0 6px 0;
}}

calendar > header > label {{
    color: {c['color4']};
    font-weight: 900;
    font-size: 13px;
    font-family: 'JetBrainsMono Nerd Font', monospace;
}}

calendar > header > button {{
    background-color: transparent;
    color: {c['color4']};
    border: none;
    border-radius: 4px;
    padding: 2px 6px;
    min-width: 0;
    font-weight: 900;
}}

calendar > header > button:hover {{
    background-color: rgba(255,255,255,0.1);
}}

calendar > grid > label.header {{
    color: rgba(255,255,255,0.4);
    font-size: 11px;
    font-weight: 900;
    padding-bottom: 4px;
}}

calendar > grid > label {{
    color: rgba(255,255,255,0.85);
    font-size: 12px;
    border-radius: 4px;
    padding: 10px 16px;
}}

calendar > grid > label:hover {{
    background-color: rgba(255,255,255,0.08);
}}

calendar > grid > label.today {{
    color: {c['color3']};
    font-weight: 900;
}}

calendar > grid > label:selected,
calendar > grid > label.selected {{
    background-color: {c['color3']};
    color: #000000;
    font-weight: 900;
    border-radius: 4px;
}}

calendar > grid > label.other-month {{
    color: rgba(255,255,255,0.2);
}}
"""

# ── App ────────────────────────────────────────────────────────────────────────
class CalendarApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.wal.calendar")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        colors = load_wal_colors()

        css = Gtk.CssProvider()
        css.load_from_data(build_css(colors).encode())
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

        win = Gtk.Window(application=app)
        win.set_decorated(False)
        win.set_resizable(False)
        win.set_title("wal-calendar")

        # ── Layer shell: anchor just below the waybar ──────────────────────────
        LayerShell.init_for_window(win)
        LayerShell.set_layer(win, LayerShell.Layer.OVERLAY)

        # Pin to top edge only — window floats horizontally centered
        LayerShell.set_anchor(win, LayerShell.Edge.TOP,    True)
        LayerShell.set_anchor(win, LayerShell.Edge.LEFT,   False)
        LayerShell.set_anchor(win, LayerShell.Edge.RIGHT,  False)
        LayerShell.set_anchor(win, LayerShell.Edge.BOTTOM, False)

        # margin-top = waybar height (38) + waybar margin-top (8) + gap (6) = 52
        # Adjust this value if the popup doesn't clear your bar
        LayerShell.set_margin(win, LayerShell.Edge.TOP, 52)

        # -1 = don't reserve space / don't push anything
        LayerShell.set_exclusive_zone(win, -1)
        LayerShell.set_keyboard_mode(win, LayerShell.KeyboardMode.EXCLUSIVE)

        # ── Calendar widget ────────────────────────────────────────────────────
        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        root.add_css_class("calendar-root")
        win.set_child(root)

        cal = Gtk.Calendar()
        root.append(cal)

        # ── Close on Escape ────────────────────────────────────────────────────
        key_ctrl = Gtk.EventControllerKey()
        key_ctrl.connect(
            "key-pressed",
            lambda ctrl, val, code, state:
                app.quit() if val == Gdk.KEY_Escape else None
        )
        win.add_controller(key_ctrl)

        # ── Close on focus loss ────────────────────────────────────────────────
        win.connect(
            "notify::is-active",
            lambda w, _: GLib.timeout_add(
                100, lambda: app.quit() if not win.is_active() else None
            )
        )

        win.present()


if __name__ == "__main__":
    app = CalendarApp()
    sys.exit(app.run(sys.argv))
