#include <stdio.h>
#include <unistd.h>

int main()
{
  const char text[14] = "Hello, World!\n";
  syscall(1, STDOUT_FILENO, text, 14);
  return 0;
}
