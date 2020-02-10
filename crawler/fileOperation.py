import glob, os

def rename(newname,filetype):
    ftype = ('*.%s'%filetype)
    allfiles = glob.glob(ftype)
    for afile in allfiles:
      os.rename(afile, 't_'+ afile)
     
    allfiles = glob.glob(ftype)
    count=1
    for afile in allfiles:
      new_filename = newname + str(count) + ftype.strip('*')
      print(new_filename,'done')
      os.rename(afile, new_filename)
      count += 1
    print("All Done")

def list_all():
    return list_files() + list_dir()

def list_files():
    listall = []
    all_file = glob.glob('*')
    for i in all_file:
        directory = './%s'%i
        if os.path.isdir(directory)==True:
            pass
        else:
            listall.append(i)
    return listall

def list_dir():
    listall=[]
    all_file = glob.glob('*')
    for i in all_file:
        directory = './%s'%i
        if os.path.isdir(directory)==True:
            listall.append(i)
        else:
            pass
    return listall

def mkdir(dirName):
    newdir = './%s'%dirName
    try:
        os.makedirs(newdir)
        print("%s 已建立。"%dirName)
    except FileExistsError:
        print("%s 已存在。"%dirName)
