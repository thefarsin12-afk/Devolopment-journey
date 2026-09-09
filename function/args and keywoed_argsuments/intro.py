# *=> tuple,using to function and method,()
def add(*args):

    return sum(args)

print(add(10,20,30,40))
print(add(10,20,30))


#**kwargs
# **=> is dictionary method using to function and method

def person(**kwargs):

    print(kwargs)

person(eid=101,name="alex",dep="hr",salary=30000,job_laction="kochi",place="thrishur")    