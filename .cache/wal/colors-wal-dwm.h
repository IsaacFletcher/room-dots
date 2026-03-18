static const char norm_fg[] = "#eac8bd";
static const char norm_bg[] = "#101019";
static const char norm_border[] = "#a38c84";

static const char sel_fg[] = "#eac8bd";
static const char sel_bg[] = "#B7836B";
static const char sel_border[] = "#eac8bd";

static const char urg_fg[] = "#eac8bd";
static const char urg_bg[] = "#C0717F";
static const char urg_border[] = "#C0717F";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
