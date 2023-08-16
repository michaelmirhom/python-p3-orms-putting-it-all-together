import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__(self,name,breed):
        self.id =None
        self.name =name
        self.breed =breed
    @classmethod
    def   create_table(cls):
        sql = """ 
         CREATE TABLE IF NOT EXISTS dogs(
         id INTEGER PRIMARY KEY,
         name TEXT,
         breed TEXT
         )
         """
        CURSOR.execute(sql)
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS dogs
            """
        CURSOR.execute(sql)

    def  save(self):
        sql = """
        INSERT INTO dogs(name,breed) VALUES(?,?)
        """
        CURSOR.execute(sql,(self.name,self.breed))
        self.id = CURSOR.lastrowid
        CONN.commit()
    
    @classmethod
    def create(cls, name, breed) :
        new_dog = cls(name,breed)
        new_dog.save()
        return new_dog
    @classmethod
    def new_from_db(cls,row):
        id,name,breed =row
        dog =cls(name,breed)
        dog.id =id
        return dog
    @classmethod
    def get_all(cls):
        sql = """
         SELECT * FROM dogs

         """
        rows = CURSOR.execute(sql).fetchall()
        return[cls.new_from_db(row) for row in rows]
    @classmethod
    def find_by_name(cls, name):
     sql = """
         SELECT * FROM dogs
         WHERE name = ?
      """
     row = CURSOR.execute(sql, (name,)).fetchone() 
     if row:
                   return cls.new_from_db(row) 
     else:
           return None
    @classmethod
    def find_by_id(cls, id):
        sql = """
           SELECT * FROM dogs WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        if row :
             return cls.new_from_db(row)
        else:
             None
    @classmethod         
    def  find_or_create_by(cls,name,breed):
        sql = """
         SELECT * FROM dogs WHERE name = ? AND breed = ?
         """
        row = CURSOR.execute(sql,(name,breed)) .fetchone()
        if row:
             return cls.new_from_db(row)
        else :
         new_dog = cls(name,breed)
         new_dog.save()
         return new_dog
    def update(self):
        if self.id is None:
          raise ValueError("this dod is not vexists")
        else :
            sql= """
              UPDATE dogs  SET id= ? , name = ? , breed= ?

             """
            CURSOR.execute(sql,(self.id,self.name,self.breed))
            CONN.commit()
            
            
        
           
         
        
        
    
         

           



    
   



        


            
            
 
        
