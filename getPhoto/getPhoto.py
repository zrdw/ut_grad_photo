import urllib
import os

# replace **** to real numbers

def get_photo(varo, varf, vara):

    path = "../gradPhoto/"
    if not os.path.exists(path):
        os.mkdir(path)

    indexes = list(range(*,*))
    
    for index in indexes:
        dest = path+"****"+str(index)+"/"
        if not os.path.exists(dest):
            os.mkdir(dest)

        x = 55
        y = 55
        idx = 0
        while y<575+110:
            while x<425+110:
                """
                Open the link of f****photography, click on one photo preview, it pops up and small window, and provides a small zoom in view
                Copy the link zoom in view(or open in a new tab and copy the link), it should be something like the below one.
                """
                url = "http://images1.f****photography.com/Magnifier/MagnifyRender.ashx?X="+str(x)+"&Y="+str(y)+"&O="+varo+"&R=****"+str(index)+"&F="+varf+"&A="+vara
                print url
                urllib.urlretrieve(url, dest+"/"+str(idx)+".jpg")
                x += 110
                idx += 1
            x = 55            
            y += 110


if __name__=="__main__":
    get_photo("********", "****", "*****")
