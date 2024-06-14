
# LIBRARY MANAGEMENT    
A library management odoo module    
    

REQUIREMENTS
 ------------- 
 Before all make sûr you installed `postgresql` and `odoo 17` in your environment    
    
DEPENCIES 
------- 
After cloned the project and opened it with your IDE, execute the command `pip install -r requirements.txt` to install all needs dependencies    
    
MODULE IMPORT AND ODOO CONFIGURATION 
-------------------- 
- Copy the module in the path odoo_installation_path\server\odoo\addons\    
    
> **Note:** Replace **odoo_installation_path** by the path where odoo is installed.    
  
- Make sure to create a postgresql user based on the odoo configuration file (`odoo_installation_path\server\odoo.conf`). The username is in the attribute **db_user** and the password in **db_password**.   
 
- Install the module in the odoo graphique interface on [localhost:8069](http:\\localhost:8069)  
  
- Run the fastapi with the command `uvicorn fastapi_app:app --reload`