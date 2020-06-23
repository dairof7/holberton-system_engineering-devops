#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - infinite loop
 * Return: O on success
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
 * main - create a five zombie process
 * Return: O on success
 */
int main(void)
{
	int i = 0;
	pid_t zombie_id;

	while (i < 5)
	{
		zombie_id = fork();
		if (zombie_id > 0)
			printf("Zombie process created, PID: %d\n", zombie_id);
		else
			exit(0);
		i++;
	}
	infinite_while();
	return (0);
}
