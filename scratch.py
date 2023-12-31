from sys import argv
from os import listdir, path

def main(path_user):
    try:
        print(path_user)
        if not path.exists(path_user):
            raise Exception
        print(listdir(path_user))            
    except:
        print("Wahala")
    
if __name__ == '__main__':
    main(argv[1])
    