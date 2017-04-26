#include <stdio.h>
#include <stdlib.h>

int main(void) {

  FILE *pp;
  pp = popen("python test.py", "r");
  double x,y;
  int i;
  if (pp != NULL) {
    i = 0;
    while (1) {
      char *line;
      char buf[1000];
      line = fgets(buf, sizeof buf, pp);
      if (line == NULL) break;
      if (i==0) {
	x=atof(line);
	printf("x=%f\n", x); /* line includes '\n' */
      } 
      if (i==1) {
	y=atof(line);
	printf("y=%f\n", y); /* line includes '\n' */
      } 
      i++;
    }
    pclose(pp);
  }
  return 0;
}
