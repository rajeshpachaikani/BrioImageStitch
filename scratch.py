import shutil

def get_remaining_space():
    total, used, free = shutil.disk_usage("/")
    t = "Total: %d GiB" % (total // (2**30))
    u = "Used: %d GiB" % (used // (2**30))
    f = "Free: %d GiB" % (free // (2**30))
    return t, u, f

print(get_remaining_space())