# inja city function ra test mikonim
from city_functions import esme_kamel

def test_city_country() :
    full_name = esme_kamel('jamal','kazem')
    
    assert full_name == 'jamal kazem'


