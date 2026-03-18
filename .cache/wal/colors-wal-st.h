const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#101019", /* black   */
  [1] = "#C0717F", /* red     */
  [2] = "#B7836B", /* green   */
  [3] = "#EEA47D", /* yellow  */
  [4] = "#C57787", /* blue    */
  [5] = "#689099", /* magenta */
  [6] = "#EC8796", /* cyan    */
  [7] = "#eac8bd", /* white   */

  /* 8 bright colors */
  [8]  = "#a38c84",  /* black   */
  [9]  = "#C0717F",  /* red     */
  [10] = "#B7836B", /* green   */
  [11] = "#EEA47D", /* yellow  */
  [12] = "#C57787", /* blue    */
  [13] = "#689099", /* magenta */
  [14] = "#EC8796", /* cyan    */
  [15] = "#eac8bd", /* white   */

  /* special colors */
  [256] = "#101019", /* background */
  [257] = "#eac8bd", /* foreground */
  [258] = "#eac8bd",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
