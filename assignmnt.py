'''
Created on 08-Jun-2017

@author: Aayush
'''
import math

def dist_calculator(location1,location2):
    dist_x=(location1.lattitude)-(location2.lattitude)
    dist_y=(location1.longitude)-(location2.longitude)
    dist_sqare=math.pow(dist_x,2)+math.pow(dist_y,2)
    dist=math.sqrt(dist_sqare)
    return dist
        
def assign_cab(cust1):
    global cab_list
    if(len(cab_list)==0):
        print('no car left')
    else:
        second_cab_list=[]
        if(cust1.clrpref=='pink'):
            for j in cab_list:
                if(j.color=='pink'):
                    second_cab_list.append(j)
            list_dist=[]
            for i in range(0,len(second_cab_list)):
                dist=dist_calculator(second_cab_list[i].location,cust1.location)
                list_dist.append(dist)
            ind=list_dist.index(min(list_dist))
            popped_item=second_cab_list.pop(ind)
            cust1.cab=popped_item
            cab_list.pop(cab_list.index(popped_item))    
        else:
            list_dist=[]
            for i in range(0,len(cab_list)):
                dist=dist_calculator(cab_list[i].location,cust1.location)
                list_dist.append(dist)
            ind=list_dist.index(min(list_dist))
            cust1.cab=cab_list.pop(ind)

def calculate_bill(cust):
    dist=dist_calculator(cust.dest_loc,cust.location)
    if(cust.clrpref=='pink'):
        bill=dist*2+5+(dist//cust.cab.avgspeed)
    else:
        bill=dist*2+(dist//cust.cab.avgspeed)
    returned_cab=cust.cab
    cab_list.append(returned_cab)
    cust.cab=None
    return bill
    

class Cab(object):
    def __init__(self,location,color,speed):
        self.location=location
        self.color=color
        self.avgspeed=speed
        
class Location(object):
    def __init__(self,lattitude,longitude):
        self.lattitude=lattitude
        self.longitude=longitude
        
class Customer(object):
    def __init__(self,location,dest_loc,clrpref):
        self.location=location
        self.cab=None
        self.bill=None
        self.dest_loc=dest_loc
        self.clrpref=clrpref
        
            
loc1=Location(5,0)
loc2=Location(0,4)
loc3=Location(6,0)
loc4=Location(0,7)

c_loc1=Location(0,0)
c_loc2=Location(1,0)

c_d_loc1=Location(3,4)
c_d_loc2=Location(5,6)

cab1=Cab(loc1,'black',45)
cab2=Cab(loc2,'red',55)
cab3=Cab(loc3,'white',65)
cab4=Cab(loc4,'blue',50)
cab5=Cab(loc4,'pink',60)

cab_list=[cab1,cab2,cab3,cab4,cab5]
print(len(cab_list))
cust1=Customer(c_loc1,c_d_loc1,'pink')
assign_cab(cust1)

# es=Elitecustomer(loc4,c_d_loc2,'pink')
# assign_cab(es)
print(cust1.cab.color)
print(len(cab_list))
print(calculate_bill(cust1))
print(len(cab_list))
# print(cust1.cab.color)
# print(len(cab_list))
# print(calculate_bill(cust1))
# print(len(cab_list))
# print(cust1.cab)
#cust2=Customer(c_loc2,c_d_loc2)
#assign_cab(cust2)
#print(cust2.cab.color)
#print(len(cab_list))


#print(cust1.location.lattitude,cust1.cab.location.lattitude)
#cab_list.pop(3)
#print(cab_list)