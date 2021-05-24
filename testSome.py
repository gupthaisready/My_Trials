import sys
import os
import copy
import oci
from oci.config import from_file

config_file = "D:\Workspace\oci_cli_sdk\config"

config = from_file(file_location=config_file, profile_name="DEFAULT")

lbc = oci.load_balancer.LoadBalancerClient(config)

lb_data = lbc.get_load_balancer('ocid1.loadbalancer.oc1.ap-mumbai-1.aaaaaaaagsbkau3f4ecy62muj452axqozdgolthfiviwzlo2oxkrf7k3r7sa')

lb_details = lb_data.data

print(lb_details)

my_lb = copy.deepcopy(lb_data.data.__dict__)

del my_lb['swagger_types']
del my_lb['attribute_map']
print(my_lb)