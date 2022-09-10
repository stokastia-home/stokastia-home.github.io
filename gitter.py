from jft.text_colours.bright.cyan import f as cy
from jft.text_colours.bright.magenta import f as mag
# from jft.system.git.log_oneline import f
# print(f('.').stdout.decode().split('\n')[0])
from subprocess import run as sprun
def f_M(_): return f_X(_, 'Updated', ask=True)
def f_A(_): return f_X(_, 'Added', ask=True)
def f_D(_): return f_X(_, 'Removed', ask=False)
def f_X(a, b, ask=True):
  sprun(args=['code', a])
  __=mag(a)
  response=input(cy(f"Proceed with '")+a+cy(f"'? (Q/Y/N):")) if ask else 'Y'
  if response=='Y':
    result=sprun(args=['git', 'add', a], capture_output=True, cwd='.')
    print(cy("Executing 'git add'"))
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
    print(cy("Executing 'git commit'"))
    result=sprun(
      args=['git', 'commit', '-m', f'{b} {a}.'], capture_output=True, cwd='.'
    )
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
    print(cy("Executing 'git push'"))
    result=sprun(args=['git', 'push'], capture_output=True, cwd='.')
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
  elif response=='Q': exit()
  else: print('Cancelled.')
def main():
  print(cy("Executing 'git pull'"))
  result=sprun(args=['git', 'pull'], capture_output=True, cwd='.')
  print(cy('result.stdout.decode():')+f' {result.stdout.decode()}')
  print(cy("Executing 'git status -s'"))
  result=sprun(args=['git', 'status', '-s'], capture_output=True, cwd='.')
  q=[_ for _ in result.stdout.decode().split("\n") if _]
  print(len(q))
  d={}
  for j in q:
    z=3
    k, v=j[:z-1], j[z:]
    if k not in d: d[k]=set()
    d[k].add(v)
  __={'??': 'Added', ' D': 'Removed', ' M': 'Updated'}
  if ' M' in d: _=sorted(d[' M'])[0]; f_M(_)
  if '??' in d: _=sorted(d['??'])[0]; f_A(_)
  if ' D' in d: _=sorted(d[' D'])[0]; f_D(_)
  if any([_ in d for _ in [' M', '??', ' D']]): main()
if __name__=='__main__':
  main()
