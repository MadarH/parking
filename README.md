# Service Parking
Ce projet Git est une service pour se connecter avec le systeme d'access et d'avoir une communication en ce qui concerne la gestion des parkings du smart city

#Execution
Note: A chaque etape, il faut etre dans le catkin_ws et faire sourcer le setup.
```bash
source devel/setup.bash
```
##Etapes:
1) Ouvrir le premier terminal et entrez la commande:
```bash
 roscore
```

2) Le deuxieme terminal on lance le script python.
```bash
rosrun parking parking_access_server.py
```

3) Dans le troisieme terminal, on lance le service.
```bash
rosservice call /parking_access_server
```

On obtiendra: 
```bash
"parking_id:
  data: 0
state_parking:
  data: 0" 
```
C'est sur cette partie-la qu'on pourra modifier l'etat des parkings.

4)Enfin sur la quatrieme terminal, entrez la commande: 
```bash
rostopic echo /parking_state
```

On observe l'etat des parkings:

```bash
data: "{\"parking_4\": 0, \"parking_1\": 0, \"parking_2\": 0, \"parking_3\": 0}"
---
```


