#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>

int main() {
  pid_t pid = fork();
  if (pid < 0)
    return errno;
  else if (pid == 0) {
    char *argv[] = {"ls", NULL};
    execve("/usr/bin/ls", argv, NULL);
    perror(NULL);
  }
  else {
    pid_t childpid = getpid();
    printf("My PID=%d, Child PID=%d\n", getppid(), childpid);
    wait(NULL);
    printf("Child %d finished\n", childpid);
  }
  return 0;
}
