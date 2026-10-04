# localhost-exposure-auditor
A beginner friendly python tool that checks TCP ports on localhost (127.0.0.1) to learn about sockets and network connections.
##  version 0.1
checks wheter a TCP connection can be established to  ports 22, 80, 443, 8000 and  8080 on 127.0.0.1

## run
Requires Python 3. no additional packages needed
```bash
python localhost_auditor.py
```
on windows u can also  use:
```powershell
py  localhost_auditor.py
```
## Limitations
- Checks localhost only
- -Does not identify processes or PIDs.
- an unsuccessful connection does not always mean a port is closed.
- an open  port does not by itself security vulnerability.

- ## what i learned :D
- creating tcp sockets in python.
- checking connection results with connect_ex()
- using loops,  timneouts and automatic socket cleanup
