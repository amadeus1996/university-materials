#include <stdio.h>
#include <pthread.h> // threads
#include <errno.h>   // errno
#include <stdlib.h>  // malloc
#include <string.h>  // strlen

void* reverse(void *v) {
  char* aux = (char*)v;
  int n = strlen(aux);
  char* result = (char*)malloc(n);
  
  for (int i = n - 1; i >= 0; --i)
    result[n - 1 - i] = aux[i];
    
  result[n] = '\0';
  return result;    
}

int main(int argc, char** argv) {
  if (argc == 1) {
    printf("Invalid input\n");
    return 0;
  }
  
  char sir[256] = "";
  for (int i = 1; i <= argc - 2; ++i) {
    strcat(sir, argv[i]);
    strcat(sir, " ");
  }
  strcat(sir, argv[argc - 1]);

  pthread_t thr;
  if (pthread_create(&thr, NULL, reverse, sir)) {
    perror(NULL);
    return errno;
  }
  
  void* result;
  if (pthread_join(thr, &result)) {
    perror(NULL);
    return errno;
  }
  
  printf("%s\n", (char*)result);
  free(result);
  return 0;
}
