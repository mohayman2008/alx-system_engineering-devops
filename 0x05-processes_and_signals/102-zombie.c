#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>

/**
 * infinite_while - enters into infinite loop
 *
 * Return: (0) if returned which will not happen automatically
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create zombie processes
 *
 * @ac: number of arguments
 * @av: arguments vector
 * Return: Always (0)
 */
int main(int ac, char **av)
{
	pid_t pid, parent;
	int i = 0;

	pid = parent = getpid();

	for (; i < 5 ; i++)
	{
		if (pid < 0)
		{
			perror("Fatal Error: ");
			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
			break;

		pid = fork();
		if (getpid() == parent)
			printf("Zombie process created, PID: %d\n", pid);
	}

	if (getpid() == parent) /* The parent process */
		infinite_while();

	return (0);
}
