#search for files with SUID
find / -perm -u=s -type f 2>/dev/null
