
#ifndef Py_INTRCHECK_H
#define Py_INTRCHECK_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(int) PyOS_InterruptOccurred(void);
PyAPI_FUNC(void) PyOS_InitInterrupts(void);
#ifdef HAVE_FORK
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03070000
PyAPI_FUNC(void) PyOS_BeforeFork(void);
PyAPI_FUNC(void) PyOS_AfterFork_Parent(void);
PyAPI_FUNC(void) PyOS_AfterFork_Child(void);
#endif
#endif
/* Deprecated, please use PyOS_AfterFork_Child() instead */
<<<<<<< HEAD
PyAPI_FUNC(void) PyOS_AfterFork(void) Py_DEPRECATED(3.7);
=======
Py_DEPRECATED(3.7) PyAPI_FUNC(void) PyOS_AfterFork(void);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78

#ifndef Py_LIMITED_API
PyAPI_FUNC(int) _PyOS_IsMainThread(void);
PyAPI_FUNC(void) _PySignal_AfterFork(void);

#ifdef MS_WINDOWS
/* windows.h is not included by Python.h so use void* instead of HANDLE */
PyAPI_FUNC(void*) _PyOS_SigintEvent(void);
#endif
#endif /* !Py_LIMITED_API */

#ifdef __cplusplus
}
#endif
#endif /* !Py_INTRCHECK_H */
