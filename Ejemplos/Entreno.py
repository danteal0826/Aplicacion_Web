from db import db

class Entreno(db.Model):
    
    #Nombre de tabla
    __tablename__="entreno"
    
    
    #Conjunto de atributos que van a ser los campos de la tabla
    #Llave primaria
    id=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.String(10))
    tipo=db.Column(db.String(30))
    duracion=db.Column(db.String(15))
    calorias=db.Column(db.String(10))
    
    
    #Método constructor para mapear datos a los campos definidos
    
    def __init__(self, fecha, tipo, duracion, calorias):
        
        self.fehca=fecha
        self.tipo=tipo
        self.duracion=duracion
        self.calorias=calorias
    