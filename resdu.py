#!/opt/imh-python/bin/python2.7
# Check disk usage of the reseller and child accounts
size_name = ("KB", "MB", "GB", "TB")
     59     i = int(math.floor(math.log(size, 1024)))
     60     p = math.pow(1024, i)
     61     s = round(size/p, 2)
     62     if (s > 0):
     63         return '%s %s' % (s, size_name[i])
     64     else:
     65         return '0B'