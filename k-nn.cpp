#include <vector>
#include <algorithm>
#include <string>
#include <ostream>

struct Element
{
	int id;
	std::string nae;
}

struct Compare{
	Compare(int dim) : dim(dim) {}
	bool operator(const Element &e1, const Element &e2) {
		return e1.pos[dim] < e2.pos[dim];
	}
	const int dim;
}

std::ostream &operator<<(std::ostream &os, const Element &e) {
	return "(" << e.id << ", " << e.name << ")";
}

thread_local int dim;

int main()
{
	std::vector<Element> v{{3, "Jane"}, {1, "Alice"}, {5, "Kyle"}};
	
	//int dim = 1;
	//std::sort(v.begin(), v.end(),[=](const Element &e1, const Element %e2) {return e1.id < e2.id;});
	
	for(int i = 0; i < nDims; i++)
	{
		Compare cmp(i);
		std::sort(v.begin(), v.end(), cmp);
		for(const auto &e : v)
		{
			std::cout << e << std::edl;
		}
	}
	
	/*
	Compare cmp(3);
	std::sort(v.begin(), v.end(), cmp);
	for(const auto &e : v)
	{
		std::cout << e << std::edl;
	}
	*/
}


#include <stdio.h>
#include <stdlib.h>


//parallelize queries
/*
	split into groups and let each thread go at it
*/

//parallelize trees - 
/*
	C++11 use threads
	inside tree builing function ->
	do_split...;
	if(!hit_thread_limit)
	{
		pthread_create(&tid, nullptr, do_node, ...);
	}
	else
	{
		do_node(...);
	}
*/

/*
	start with set of points
	find approximate median
	create first node in split
	
	
	specifics of parallelization - make it go fast
	pull 100 threads, pick a median, then do a partition
	assign each thread half the points to partition?
	
	speedup in tree building
	
	*Mmap the results file makes it super simple*
	each thread will know exactly where it needs to look in result file
*/

void doit(int n_rows, int n_col, float (*a)[n_rows][n_cols])
{
	//const int n_rows = 4;
	//const int n_cols = 4;
	//float **a = (float** )malloc(n_rows*sizeof(float *));
	
	/*
	for(int i = 0; i < n_rows; i++)
	{
		a[i] = (float*) malloc(n_cols*sizeof(float));
	}
	*/
	
	for(int i = 0; i < n_rows; i++)
	{
		for(int j = 0; j < n_cols; j++)
		{
			a[i][j]= 3.14*i*j;
		}
	}
	
	for(int i = 0; i < n_rows; i++)
	{
		for(int j = 0; j < n_cols; j++)
		{
			printf("%f, ", a[i][j]);
		}
		printf("\n");
	}
}