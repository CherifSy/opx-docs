import   cps
import   cps_utils

def cps_attr_get(cps_data, attr):
        return cps_utils.cps_attr_types_map.from_data(attr, cps_data[attr])

#  Example   GET  request 
cps_get_response   =  []
cps.get([cps.key_from_name('observed','base-pas/chassis')], cps_get_response) 

chassis_vendor_name   =  cps_attr_get(cps_get_response[0]['data'],'base-pas/chassis/vendor-name')
