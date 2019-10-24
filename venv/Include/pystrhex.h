#ifndef Py_STRHEX_H
#define Py_STRHEX_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef Py_LIMITED_API
/* Returns a str() containing the hex representation of argbuf. */
PyAPI_FUNC(PyObject*) _Py_strhex(const char* argbuf, const Py_ssize_t arglen);
/* Returns a bytes() containing the ASCII hex representation of argbuf. */
PyAPI_FUNC(PyObject*) _Py_strhex_bytes(const char* argbuf, const Py_ssize_t arglen);
<<<<<<< HEAD
=======
/* These variants include support for a separator between every N bytes: */
PyAPI_FUNC(PyObject*) _Py_strhex_with_sep(const char* argbuf, const Py_ssize_t arglen, const PyObject* sep, const int bytes_per_group);
PyAPI_FUNC(PyObject*) _Py_strhex_bytes_with_sep(const char* argbuf, const Py_ssize_t arglen, const PyObject* sep, const int bytes_per_group);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
#endif /* !Py_LIMITED_API */

#ifdef __cplusplus
}
#endif

#endif /* !Py_STRHEX_H */
