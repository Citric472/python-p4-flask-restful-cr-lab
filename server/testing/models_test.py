from datetime import date

from app import app
from models import db, Plant

class TestPlant:
    '''Plant model in models.py'''

    
    
    def test_can_instantiate(self):
        '''Test if Plant can be instantiated with required attributes.'''
        p = Plant(name="Douglas Fir", image="example_image.jpg", price=10.00)
        assert p.name == "Douglas Fir"
        assert p.image == "example_image.jpg"
        assert p.price == 10.00

    def test_can_be_created(self):
        '''Test if Plant records can be created and committed to the database.'''
        with app.app_context():
            p = Plant(name="Douglas Fir", image="example_image.jpg", price=10.00)
            db.session.add(p)
            db.session.commit()
            assert p.id is not None

    def test_can_be_serialized(self):
        '''Test if Plant records can be serialized to a dictionary.'''
        with app.app_context():
            p = Plant(name="Douglas Fir", image="example_image.jpg", price=10.00)
            db.session.add(p)
            db.session.commit()
            serialized_plant = p.serialize()
            assert serialized_plant['name'] == "Douglas Fir"
            assert serialized_plant['image'] == "example_image.jpg"
            assert serialized_plant['price'] == 10.00