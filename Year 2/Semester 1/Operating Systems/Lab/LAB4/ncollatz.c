#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>
#include <stdlib.h>

void collatz(int n) {
  printf("%d: %d", n, n);
  while (n > 1) {
      if (n & 1)
        n = 3 * n + 1;
      else
        n >>= 1;
      printf(" %d", n);
  }
  printf(".\n");
}

int main(int argc, char** argv) {
  pid_t firstParent = getppid();
  pid_t firstChild = getpid();
  printf("Starting parent %d\n", firstChild);
  for (int i = 1; i < argc; ++i) {
    pid_t pid = fork();
    if (pid < 0)
      return errno;
    else if (pid == 0) {
      collatz(atoi(argv[i]));
      printf("Done Parent %d Me %d\n", firstChild, getpid());
      exit(getpid());
    }
    else
      wait(NULL);
  }
  printf("Done Parent %d Me %d\n", firstParent, firstChild);
  return 0;
}
