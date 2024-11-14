#include <stdio.h>
#include <sys/types.h>
#include <pthread.h>
#include <errno.h>
#include <stdlib.h>

#define MAX_RESOURCES 5
int available_resources = MAX_RESOURCES;
pthread_mutex_t mtx;

struct args {
  int value;
};

void* decrease_count(void* resources) {
  struct args* arg = resources;
  int* result = malloc(sizeof(int));
  
  pthread_mutex_lock(&mtx);
  if (available_resources < arg->value) {
    *result = -1;
    return result;
  }
  available_resources -= arg->value;
  //*result = 0;
  printf("Got %d resources %d remaining\n", arg->value, available_resources);
  pthread_mutex_unlock(&mtx);
  //return result;
  return NULL;
}

void* increase_count(void* resources) {
  struct args* arg = resources;
  pthread_mutex_lock(&mtx);
  available_resources += arg->value;
  printf("Released %d resources %d remaining\n", arg->value, available_resources);
  pthread_mutex_unlock(&mtx);
  return NULL;
}

int main() {
  if (pthread_mutex_init(&mtx, NULL)) {
    perror(NULL);
    return errno;
  }
  
  struct args arg = {0};
  struct args resources[] = {2, 2, 1, 3, 2};
  pthread_t *threads = malloc(5 * sizeof(pthread_t));
  for (int i = 0; i < 5; ++i) {
    arg = resources[i];
    if (pthread_create(&threads[i], NULL, decrease_count, &arg)) {
      perror(NULL);
      return errno;
    }
    if (pthread_join(threads[i], NULL)) {
      perror(NULL);
      return errno;
    }
    if (pthread_create(&threads[i], NULL, increase_count, &arg)) {
      perror(NULL);
      return errno;
    }
    if (pthread_join(threads[i], NULL)) {
      perror(NULL);
      return errno;
    }
  }
  pthread_mutex_destroy(&mtx);
  return 0;
}
