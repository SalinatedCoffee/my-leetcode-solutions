class Solution:
  def simplifyPath(self, path: str) -> str:
    # stack

    dirs = []
    for t in path.split('/'):
      if not t or t == '.':
        continue
      if t == '..':
        if dirs:
          dirs.pop()
      else:
        dirs.append(t)
      
    return "/" + "/".join(dirs)

