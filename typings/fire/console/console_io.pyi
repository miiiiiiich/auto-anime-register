"""
This type stub file was generated by pyright.
"""

"""General console printing utilities used by the Cloud SDK."""
def IsInteractive(output=..., error=..., heuristic=...): # -> bool:
  """Determines if the current terminal session is interactive.

  sys.stdin must be a terminal input stream.

  Args:
    output: If True then sys.stdout must also be a terminal output stream.
    error: If True then sys.stderr must also be a terminal output stream.
    heuristic: If True then we also do some additional heuristics to check if
               we are in an interactive context. Checking home path for example.

  Returns:
    True if the current terminal session is interactive.
  """
  ...

def More(contents, out, prompt=..., check_pager=...): # -> None:
  """Run a user specified pager or fall back to the internal pager.

  Args:
    contents: The entire contents of the text lines to page.
    out: The output stream.
    prompt: The page break prompt.
    check_pager: Checks the PAGER env var and uses it if True.
  """
  ...

