#ifndef Py_FILEUTILS_H
#define Py_FILEUTILS_H
<<<<<<< HEAD

=======
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
#ifdef __cplusplus
extern "C" {
#endif

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03050000
PyAPI_FUNC(wchar_t *) Py_DecodeLocale(
    const char *arg,
    size_t *size);

PyAPI_FUNC(char*) Py_EncodeLocale(
    const wchar_t *text,
    size_t *error_pos);

PyAPI_FUNC(char*) _Py_EncodeLocaleRaw(
    const wchar_t *text,
    size_t *error_pos);
#endif

<<<<<<< HEAD
#ifdef Py_BUILD_CORE
PyAPI_FUNC(int) _Py_DecodeUTF8Ex(
    const char *arg,
    Py_ssize_t arglen,
    wchar_t **wstr,
    size_t *wlen,
    const char **reason,
    int surrogateescape);

PyAPI_FUNC(int) _Py_EncodeUTF8Ex(
    const wchar_t *text,
    char **str,
    size_t *error_pos,
    const char **reason,
    int raw_malloc,
    int surrogateescape);

PyAPI_FUNC(wchar_t*) _Py_DecodeUTF8_surrogateescape(
    const char *arg,
    Py_ssize_t arglen);
=======

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03080000
typedef enum {
    _Py_ERROR_UNKNOWN=0,
    _Py_ERROR_STRICT,
    _Py_ERROR_SURROGATEESCAPE,
    _Py_ERROR_REPLACE,
    _Py_ERROR_IGNORE,
    _Py_ERROR_BACKSLASHREPLACE,
    _Py_ERROR_SURROGATEPASS,
    _Py_ERROR_XMLCHARREFREPLACE,
    _Py_ERROR_OTHER
} _Py_error_handler;

PyAPI_FUNC(_Py_error_handler) _Py_GetErrorHandler(const char *errors);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78

PyAPI_FUNC(int) _Py_DecodeLocaleEx(
    const char *arg,
    wchar_t **wstr,
    size_t *wlen,
    const char **reason,
    int current_locale,
<<<<<<< HEAD
    int surrogateescape);
=======
    _Py_error_handler errors);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78

PyAPI_FUNC(int) _Py_EncodeLocaleEx(
    const wchar_t *text,
    char **str,
    size_t *error_pos,
    const char **reason,
    int current_locale,
<<<<<<< HEAD
    int surrogateescape);
=======
    _Py_error_handler errors);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
#endif

#ifndef Py_LIMITED_API
PyAPI_FUNC(PyObject *) _Py_device_encoding(int);

#if defined(MS_WINDOWS) || defined(__APPLE__)
    /* On Windows, the count parameter of read() is an int (bpo-9015, bpo-9611).
       On macOS 10.13, read() and write() with more than INT_MAX bytes
       fail with EINVAL (bpo-24658). */
#   define _PY_READ_MAX  INT_MAX
#   define _PY_WRITE_MAX INT_MAX
#else
    /* write() should truncate the input to PY_SSIZE_T_MAX bytes,
       but it's safer to do it ourself to have a portable behaviour */
#   define _PY_READ_MAX  PY_SSIZE_T_MAX
#   define _PY_WRITE_MAX PY_SSIZE_T_MAX
#endif

#ifdef MS_WINDOWS
struct _Py_stat_struct {
    unsigned long st_dev;
    uint64_t st_ino;
    unsigned short st_mode;
    int st_nlink;
    int st_uid;
    int st_gid;
    unsigned long st_rdev;
    __int64 st_size;
    time_t st_atime;
    int st_atime_nsec;
    time_t st_mtime;
    int st_mtime_nsec;
    time_t st_ctime;
    int st_ctime_nsec;
    unsigned long st_file_attributes;
<<<<<<< HEAD
=======
    unsigned long st_reparse_tag;
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
};
#else
#  define _Py_stat_struct stat
#endif

PyAPI_FUNC(int) _Py_fstat(
    int fd,
    struct _Py_stat_struct *status);

PyAPI_FUNC(int) _Py_fstat_noraise(
    int fd,
    struct _Py_stat_struct *status);

PyAPI_FUNC(int) _Py_stat(
    PyObject *path,
    struct stat *status);

PyAPI_FUNC(int) _Py_open(
    const char *pathname,
    int flags);

PyAPI_FUNC(int) _Py_open_noraise(
    const char *pathname,
    int flags);

PyAPI_FUNC(FILE *) _Py_wfopen(
    const wchar_t *path,
    const wchar_t *mode);

PyAPI_FUNC(FILE*) _Py_fopen(
    const char *pathname,
    const char *mode);

PyAPI_FUNC(FILE*) _Py_fopen_obj(
    PyObject *path,
    const char *mode);

PyAPI_FUNC(Py_ssize_t) _Py_read(
    int fd,
    void *buf,
    size_t count);

PyAPI_FUNC(Py_ssize_t) _Py_write(
    int fd,
    const void *buf,
    size_t count);

PyAPI_FUNC(Py_ssize_t) _Py_write_noraise(
    int fd,
    const void *buf,
    size_t count);

#ifdef HAVE_READLINK
PyAPI_FUNC(int) _Py_wreadlink(
    const wchar_t *path,
    wchar_t *buf,
<<<<<<< HEAD
    size_t bufsiz);
=======
    /* Number of characters of 'buf' buffer
       including the trailing NUL character */
    size_t buflen);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
#endif

#ifdef HAVE_REALPATH
PyAPI_FUNC(wchar_t*) _Py_wrealpath(
    const wchar_t *path,
    wchar_t *resolved_path,
<<<<<<< HEAD
    size_t resolved_path_size);
=======
    /* Number of characters of 'resolved_path' buffer
       including the trailing NUL character */
    size_t resolved_path_len);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
#endif

PyAPI_FUNC(wchar_t*) _Py_wgetcwd(
    wchar_t *buf,
<<<<<<< HEAD
    size_t size);
=======
    /* Number of characters of 'buf' buffer
       including the trailing NUL character */
    size_t buflen);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78

PyAPI_FUNC(int) _Py_get_inheritable(int fd);

PyAPI_FUNC(int) _Py_set_inheritable(int fd, int inheritable,
                                    int *atomic_flag_works);

PyAPI_FUNC(int) _Py_set_inheritable_async_safe(int fd, int inheritable,
                                               int *atomic_flag_works);

PyAPI_FUNC(int) _Py_dup(int fd);

#ifndef MS_WINDOWS
PyAPI_FUNC(int) _Py_get_blocking(int fd);

PyAPI_FUNC(int) _Py_set_blocking(int fd, int blocking);
#endif   /* !MS_WINDOWS */

<<<<<<< HEAD
PyAPI_FUNC(int) _Py_GetLocaleconvNumeric(
    PyObject **decimal_point,
    PyObject **thousands_sep,
    const char **grouping);

#endif   /* Py_LIMITED_API */

#ifdef Py_BUILD_CORE
PyAPI_FUNC(int) _Py_GetForceASCII(void);

/* Reset "force ASCII" mode (if it was initialized).

   This function should be called when Python changes the LC_CTYPE locale,
   so the "force ASCII" mode can be detected again on the new locale
   encoding. */
PyAPI_FUNC(void) _Py_ResetForceASCII(void);
#endif

#ifdef __cplusplus
}
#endif

=======
#endif   /* Py_LIMITED_API */

#ifdef __cplusplus
}
#endif
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
#endif /* !Py_FILEUTILS_H */
