#include "mpi.h"
#include "python2.7/Python.h"

int main(int argc, char* argv[]) {
	int nRank, nProcs;
	char procName[MPI_MAX_PROCESSOR_NAME];
	int nNameLen;

	//	FILE* pi02, pi03, pi04;
	PyObject* pInt;
	Py_Initialize();
	FILE* pi02, pi03, pi04;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &nRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProcs);

	MPI_Get_processor_name(procName, &nNameLen);
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path");


	if(nRank==3){
		PyRun_SimpleString("sys.path.append('/home/pi/myProject')");
		PyRun_SimpleString("import img_preprocess as i\n"
				"i.img_pre()");
	}

	if(nRank==2){
		PyRun_SimpleString("sys.path.append('/home/pi/myProject')");

		PyRun_SimpleString("import tesseract as t\n"
				"t.tesseract()");

	}

	if(nRank==1){

		PyRun_SimpleString("sys.path.append('/home/pi/myProject')");
		PyRun_SimpleString("import han_spell as h\n"
				"h.han_task()");
	}

	printf("Process name=%s, nRank=%d, nProcs=%d\n", procName, nRank, nProcs);

	Py_Finalize();
	MPI_Finalize();
	return 0;
}

