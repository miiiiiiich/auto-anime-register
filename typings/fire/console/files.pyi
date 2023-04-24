"""
This type stub file was generated by pyright.
"""

"""Some general file utilities used that can be used by the Cloud SDK."""
def FindExecutableOnPath(executable, path=..., pathext=..., allow_extensions=...): # -> str | None:
  """Searches for `executable` in the directories listed in `path` or $PATH.

  Executable must not contain a directory or an extension.

  Args:
    executable: The name of the executable to find.
    path: A list of directories to search separated by 'os.pathsep'.  If None
      then the system PATH is used.
    pathext: An iterable of file name extensions to use.  If None then
      platform specific extensions are used.
    allow_extensions: A boolean flag indicating whether extensions in the
      executable are allowed.

  Returns:
    The path of 'executable' (possibly with a platform-specific extension) if
    found and executable, None if not found.

  Raises:
    ValueError: if executable has a path or an extension, and extensions are
      not allowed, or if there's an internal error.
  """
  ...
