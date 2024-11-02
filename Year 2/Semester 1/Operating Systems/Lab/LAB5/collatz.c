#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>

void collatz(int n, char result[]) {
  while (n > 1) {
    char aux[11] = "";
    snprintf(aux, sizeof(aux), "%d", n);
    strcat(result, aux);
    strcat(result, " ");
    
    if (n & 1)
      n = n * 3 + 1;
    else
      n >>= 1;
  }
  strcat(result, "1.");
}

int main(int argc, char** argv) {
  pid_t firstParent = getppid();
  pid_t secondParent = getpid();
  printf("Starting parent %d\n", secondParent);

  char shm_name[] = "myshm";
  int shm_fd = shm_open(shm_name, O_CREAT|O_RDWR, S_IRUSR|S_IWUSR);
  if (shm_fd < 0) {
    perror(NULL);
    return errno;
  }
  
  size_t shm_size = getpagesize();
  if (ftruncate(shm_fd, shm_size) == -1) {
    perror(NULL);
    shm_unlink(shm_name);
    return errno;
  }
  
  char* shm_ptr = mmap(0, shm_size, PROT_READ, MAP_SHARED, shm_fd, 0);
  if (shm_ptr == MAP_FAILED) {
    perror(NULL);
    shm_unlink(shm_name);
    return errno;
  }
  
  for (int i = 1; i < argc; ++i) {
    pid_t pid = fork();
    if (pid < 0)
      return errno;
    else if (pid == 0) {
      pid_t childPID = getpid();
      char t[100] = "";
      
      strcat(t, argv[i]);
      strcat(t, ": ");
      collatz(atoi(argv[i]), t);
      
      char* shm_ptr_child = mmap(shm_ptr + 100 * (i - 1), 100, PROT_WRITE, MAP_SHARED, shm_fd, 0);
      if (shm_ptr_child == MAP_FAILED) {
        perror(NULL);
        shm_unlink(shm_name);
        return errno;
      }
      
      write(shm_fd, t, 100);
      munmap(shm_ptr_child, 100);
      
      printf("Done Parent %d Me %d\n", secondParent, childPID);
      exit(childPID);
      perror(NULL);
    }
    else {
      wait(NULL);
    }
  }

  for (int i = 1; i < argc; ++i)
    printf("%s\n", shm_ptr + 100 * (i - 1));
    
  munmap(shm_ptr, shm_size);
  shm_unlink(shm_name);
  printf("Done Parent %d Me %d\n", firstParent, secondParent);
  return 0;
}
