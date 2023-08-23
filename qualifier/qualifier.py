from PIL import Image
#Enter paths using //
input_path=input("Enter input path=")
output_path=input("Enter output path=")
im=Image.open(input_path)
w,h=im.size
#Enter Orderlist
order=[]
a=[]
b=[]
tw=int(input("Enter tile width="))
th=int(input("Enter tile height"))
div1=w/tw
div2=h/th
n=div1*div2

def valid_input(image_size=(w,h), tile_size=(tw,th), ordering=order):
    div1=w/tw
    div2=h/th
    if div1%int(div1)==0 and div2%int(div2)==0:
        return True
    else:
        return False
        
def rearrange_tiles(image_path=input_path, tile_size=(tw,th), ordering=order, out_path=output_path): 
    if len(ordering)!=len(set(ordering)):
        raise ValueError("The tile size or ordering are not valid for the given image")
    else:
        for i in range(0,int(div2)):
            for j in range(0,int(div1)):
                pic=im.crop(box=(0+j*(w/div1),0+i*(w/div1),0+(j+1)*(w/div1),0+(i+1)*(w/div1)))
                loc=[0+j*(w/div1),0+i*(w/div1),0+(j+1)*(w/div1),0+(i+1)*(w/div1)]
                a.append(pic)
                b.append(loc)
        
        for i in a:
            i=i.resize((tw,th))
        
        new_img=Image.new("RGBA",(w,h))
        for i in range(int(n)):
            new_img.paste(a[order[i]],(int(b[i][0]),int(b[i][1])))
            
        new_img.save(output_path+"\\ARRANGED.png")

condition=valid_input()
if condition==True:
    rearrange_tiles()
else:
    print("Quitting")
