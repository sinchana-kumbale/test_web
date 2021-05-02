import matplotlib.pyplot as plt
import base64
from io import BytesIO
def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    buffer.close()
    return graph
def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('State-Wise Case Distribution')
    plt.bar(x,y,color=['red','green','blue','yellow','pink'])
    plt.xlabel('States')
    plt.ylabel('Active Cases')
    plt.savefig(r'C:\Users\sinch\AppData\Local\Programs\Python\Python39\Scripts\test_web\test_app.jpg')
    
