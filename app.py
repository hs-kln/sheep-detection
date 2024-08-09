from flask import Flask, render_template, request, redirect, url_for, flash, Response
from detect import detect_objects, detect_objects_model2, detect_objects_model3
import io

app = Flask(__name__)
app.secret_key = 'Rr1223'

# Database connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def sheep_input():
    return render_template('form.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/model1')
def model1():
    return render_template('model1.html')

@app.route('/model2')
def model2():
    return render_template('model2.html')

@app.route('/model3')
def model3():
    return render_template('model3.html')

@app.route('/upload_model1', methods=['POST'])
def upload_file_model1():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        img_bytes, categories_str = detect_objects(file.read())
        
        # Create a response with both the image and categories
        response = Response(img_bytes, mimetype='image/jpeg')
        response.headers['X-Detected-Categories'] = categories_str
        
        return response

@app.route('/upload_model2', methods=['POST'])
def upload_file_model2():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        img_bytes, categories_str = detect_objects_model2(file.read())
        
        # Create a response with both the image and categories
        response = Response(img_bytes, mimetype='image/jpeg')
        response.headers['X-Detected-Categories'] = categories_str
        
        return response

@app.route('/upload_model3', methods=['POST'])
def upload_file_model3():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        img_bytes, categories_str = detect_objects_model3(file.read())
        
        # Create a response with both the image and categories
        response = Response(img_bytes, mimetype='image/jpeg')
        response.headers['X-Detected-Categories'] = categories_str
        
        return response

@app.route('/submit_service', methods=['POST'])
def submit_service():
    # Handle form submission here
    # e.g., saving data to the database
    return redirect(url_for('index.html'))
if __name__ == '__main__':
    app.run(debug=True)












    
