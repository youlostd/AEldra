#include "../../Binary/Extern/include/CCC.h"

/*#pragma comment( lib, "lz4_old.lib" )
#pragma comment( lib, "xxhash_old.lib" )
#pragma comment( lib, "CCC_old.lib" )
#pragma comment( lib, "LIBCMT.lib")
#pragma comment( lib, "cryptlib-5.6.1MT_old.lib")*/
#pragma comment( lib, "lz4.lib" )
#pragma comment( lib, "xxhash.lib" )
#pragma comment( lib, "CCC.lib" )
#pragma comment( lib, "LIBCMT.lib")
#pragma comment( lib, "cryptopp-static.lib")

#define export __declspec(dllexport)

extern "C"
{
	//void export setup() { FILE* x = fopen("x.txt", "a+"); fprintf(x, "XSXSX"); fclose(x);  };
	PCCC export CCC_Create2() { return CCC_Create(); };
	void export CCC_Destroy2(PCCC manager) { return CCC_Destroy(manager);  };

	int export CCC_LoadA2(PCCC manager, const char* filename) { return CCC_LoadA(manager, filename); };
	int export CCC_LoadW2(PCCC manager, const wchar_t* filename) { return CCC_LoadW(manager, filename); };
	int export CCC_UnloadA2(PCCC manager, const char* filename) { return CCC_UnloadA(manager, filename); };
	int export CCC_UnloadW2(PCCC manager, const wchar_t* filename) { return CCC_UnloadW(manager, filename); };

	unsigned int export CCC_SizeA2(PCCC manager, const char* filename) { return CCC_SizeA(manager, filename); };
	unsigned int export CCC_SizeW2(PCCC manager, const wchar_t* filename) { return CCC_SizeW(manager, filename); };
	int export CCC_ExistsA2(PCCC manager, const char* filename) { return CCC_ExistsA(manager, filename); };
	int export CCC_ExistsW2(PCCC manager, const wchar_t* filename) { return CCC_ExistsW(manager, filename); };
	int export CCC_GetA2(PCCC manager, const char* filename, void* buffer, unsigned int maxsize, unsigned int* outsize) { return CCC_GetA(manager, filename, buffer, maxsize, outsize); };
	int export CCC_GetW2(PCCC manager, const wchar_t* filename, void* buffer, unsigned int maxsize, unsigned int* outsize) { return CCC_GetW(manager, filename, buffer, maxsize, outsize); };
}
