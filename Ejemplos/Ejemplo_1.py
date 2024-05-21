from flask import Flask, render_template, request, redirect, url_for
from db import db
from Entreno import Entreno


class Programa:
    
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///entrenos.sqlite3"
        
        #Agregar la db a nuestra aplicacion
        db.init_app(self.app)
        self.app.add_url_rule('/', view_func=self.buscarTodos)    
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])
        
        #Iniciar el servidor
        with self.app.app_context():
            db.create_all()
            self.app.run(debug=True)
            
            
    def buscarTodos(self):
        
        return render_template('mostrarDatos.html', entrenos=Entreno.query.all())
    
        
    def agregar(self):
        
        #Verificar si debe enviar el formulario o procesar los datos
        
        if request.method=="POST":
            
            #Crear un objeto de la clase estudiante con los valores del formulario
            fecha=request.form['fecha']
            tipo=request.form['tipo']
            duracion=request.form['duracion']
            calorias=request.form['calorias']
            miEntreno=Entreno(fecha, tipo, duracion, calorias)
            
            #Guardar el objeto en la db
            db.session.add(miEntreno)
            db.session.commit()
            
            return redirect(url_for('buscarTodos'))
        
        return render_template('seguimientoEjercicio.html')
    
miPrograma=Programa()