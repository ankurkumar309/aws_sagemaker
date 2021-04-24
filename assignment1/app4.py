from flask import Flask, render_template, request
import boto
import boto.s3
import boto3


app = Flask(__name__)
'''
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        conn = boto.s3.connect_to_region('ap-south-1')
        bucket = conn.get_bucket('1673-assignment-1')
        folders = bucket.list("","/")
        print(folders)
        l=[]
        for folder in folders:
            l.append(str(folder.name))
        folders_all= ' ,'.join(l)
    return render_template('home.html', folders_a= folders_all)

'''

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    #print("I was here 1")
    if request.method == 'POST':
        #print(request.form.get('folder name'))
        try:
            #print('in try block')
            s3 = boto3.resource('s3')
            #print('after s3')
            bucket = s3.Bucket('1673-assignment-1')
            #print('after bucket')
            folder_name = request.form['folder name']
            #print(folder_name)
            c=[]
            #print(str(folder_name))
            for obj in bucket.objects.filter(Delimiter='/', Prefix=str(folder_name)+ '/'):
                print(obj)
                c.append(obj.key)
				
            files_all=' ,'.join(c[1:len(c)])
            #print(files_all)
			
			
            
            #model_prediction = round(float(model_prediction), 2)
        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('predict.html', contents = files_all)


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8085)
