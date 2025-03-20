from app import app
from app.configuration import Param
from peewee import * 
    
db = MySQLDatabase(
    Param.DB_NAME,
    user=Param.DB_USER,
    password=Param.DB_PASSWORD,
    host=Param.DB_HOST,
    port=Param.DB_PORT
)

class BaseModel(Model):
    class Meta:
        database = db  # Utilisation de la base de données définie au début

class recette(BaseModel):
    id_recette = AutoField()
    nom_recette = CharField(null=True)
    class Meta:
        table_name = 'recettes'

class role(BaseModel):
    id_role = AutoField()
    nom_role = CharField(max_length=50)
    class Meta:
        table_name = 'roles'

class utilisateur(BaseModel):
    id_utilisateur = AutoField()
    nom_utilisateur = CharField(max_length=100, null=True)
    mdp_utilisateur = CharField(max_length=255, null=True)
    id_roles = ForeignKeyField(role, backref='utilisateurs',column_name="id_role")
    class Meta:
        table_name = 'utilisateurs'

class piece(BaseModel):
    id_piece = AutoField()
    indice_piece = SmallIntegerField(null=True)
    qt_piece = SmallIntegerField(null=True)
    id_recette = ForeignKeyField(recette, backref='pieces', column_name="id_recette")
    class Meta:
        table_name = 'pieces'

class plan(BaseModel):
    id_Plan = AutoField()
    indice_plan = SmallIntegerField(null=True)
    plan_actif = BooleanField(null=True)
    id_piece = ForeignKeyField(piece, backref='plans',column_name="id_piece")
    class Meta:
        table_name = 'plans'

class cote(BaseModel):
    ID_Cote = AutoField()
    indice_cote = SmallIntegerField(null=True)
    cote = DoubleField(null=True)
    id_Plan = ForeignKeyField(plan, backref='cotes',column_name="id_plan")
    class Meta:
        table_name = 'cotes'