#include <FoxFS.h>

#include <cstdlib>
#include <cstring>

#if defined(_WIN32) || defined(_WIN64) || defined(WIN32) || defined(WIN64)
	#include <windows.h>
#else
	#include <limits.h>
#endif

#include "FileSystem.h"

extern "C"
{
	
	PCCC CCC_EXPORT CCC_API CCC_Create() { return reinterpret_cast<PCCC>(new FoxFS::FileSystem()); }
	void CCC_EXPORT CCC_API CCC_Destroy(PCCC manager) { delete reinterpret_cast<FoxFS::FileSystem*>(manager); }
	
	int CCC_EXPORT CCC_API CCC_SetKeyServerA(PCCC manager, const char* hostname, unsigned short port) { return reinterpret_cast<FoxFS::FileSystem*>(manager)->setKeyServer(hostname, port); }
	int CCC_EXPORT CCC_API CCC_SetKeyServerW(PCCC manager, const wchar_t* hostname, unsigned short port)
	{
		char host[
#if defined(_WIN32) || defined(_WIN64) || defined(WIN32) || defined(WIN64)
					MAX_PATH + 1
#else
					PATH_MAX + 1
#endif
				] = {0};
		wcstombs(host, hostname, wcslen(hostname));
		return CCC_SetKeyServerA(manager, host, port);
	}
	int CCC_EXPORT CCC_API CCC_LoadW(PCCC manager, const wchar_t* filename) { return reinterpret_cast<FoxFS::FileSystem*>(manager)->load(filename); }
	int CCC_EXPORT CCC_API CCC_LoadA(PCCC manager, const char* filename)
	{
		wchar_t file[
#if defined(_WIN32) || defined(_WIN64) || defined(WIN32) || defined(WIN64)
						MAX_PATH + 1
#else
						PATH_MAX + 1
#endif
					] = {0};
		mbstowcs(file, filename, strlen(filename));
		return CCC_LoadW(manager, file);
	}
	int CCC_EXPORT CCC_API CCC_UnloadA(PCCC manager, const char* filename)
	{
		wchar_t file[
#if defined(_WIN32) || defined(_WIN64) || defined(WIN32) || defined(WIN64)
						MAX_PATH + 1
#else
						PATH_MAX + 1
#endif
						] = {0};
		mbstowcs(file, filename, strlen(filename));
		return CCC_LoadW(manager, file);
	}
	int CCC_EXPORT CCC_API CCC_UnloadW(PCCC manager, const wchar_t* filename) { return reinterpret_cast<FoxFS::FileSystem*>(manager)->unload(filename); }
	
	unsigned int CCC_EXPORT CCC_API CCC_SizeA(PCCC manager, const char* filename) { return reinterpret_cast<FoxFS::FileSystem*>(manager)->size(filename); }
	unsigned int CCC_EXPORT CCC_API CCC_SizeW(PCCC manager, const wchar_t* filename)
	{
		char file[
#if defined(_WIN32) || defined(_WIN64) || defined(WIN32) || defined(WIN64)
					MAX_PATH + 1
#else
					PATH_MAX + 1
#endif
					] = {0};
		wcstombs(file, filename, wcslen(filename));
		return CCC_SizeA(manager, file);
	}
	int CCC_EXPORT CCC_API CCC_ExistsA(PCCC manager, const char* filename) { return reinterpret_cast<FoxFS::FileSystem*>(manager)->exists(filename); }
	int CCC_EXPORT CCC_API CCC_ExistsW(PCCC manager, const wchar_t* filename)
	{
		char file[
#if defined(_WIN32) || defined(_WIN64) || defined(WIN32) || defined(WIN64)
					MAX_PATH + 1
#else
					PATH_MAX + 1
#endif
					] = {0};
		wcstombs(file, filename, wcslen(filename));
		return CCC_ExistsA(manager, file);
	}
	int CCC_EXPORT CCC_API CCC_GetA(PCCC manager, const char* filename, void* buffer, unsigned int maxsize, unsigned int* outsize) { return reinterpret_cast<FoxFS::FileSystem*>(manager)->get(filename, buffer, maxsize, outsize); }
	int CCC_EXPORT CCC_API CCC_GetW(PCCC manager, const wchar_t* filename, void* buffer, unsigned int maxsize, unsigned int* outsize)
	{
		char file[
#if defined(_WIN32) || defined(_WIN64) || defined(WIN32) || defined(WIN64)
					MAX_PATH + 1
#else
					PATH_MAX + 1
#endif
					] = {0};
		wcstombs(file, filename, wcslen(filename));
		return CCC_GetA(manager, file, buffer, maxsize, outsize);
	}

}