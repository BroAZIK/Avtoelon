from parsing.cobalt import cobalt
from parsing.damas import damas
from parsing.equinox import equinox
from parsing.gentra import gentra
from parsing.labo import labo
from parsing.lacetti import lacetti
from parsing.malibu import malibu
from parsing.malibu2 import malibu2
from parsing.matiz import matiz
from parsing.monza import monza
from parsing.nexia import nexia
from parsing.onix import onix
from parsing.spark import spark
from parsing.tracker import tracker
from parsing.ip_changer import change_ip_random

def max_parse():
    # cobalt()
    # damas()
    # change_ip_random()

    # equinox()
    # gentra()
    # change_ip_random()
    
    
    labo()
    lacetti()
    change_ip_random()
    
    
    malibu()
    malibu2()
    change_ip_random()
    
    
    matiz()
    monza()
    change_ip_random()
    
    
    nexia()
    onix()
    change_ip_random()
    
    
    spark()
    tracker()

max_parse()

