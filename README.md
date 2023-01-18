# neo4j
_____________________________REQUETE CYPHER______________________________

// 1- Pour créer nœud vélo :

	CREATE (v:Velo {id: 1, name: "Vélo de montagne", model: "Roadster", size: "M"});
	CREATE (v:Velo {id: 2, name: "Vélo de route", model: "Hamaya", size: "S"});
	CREATE (v:Velo {id: 3, name: "Vélo électrique", model: "Hamaya", size: "M"});
	CREATE (v:Velo {id: 4, name: "Vélo de montagne", model: "Hamaya", size: "M"});
	CREATE (v:Velo {id: 5, name: "Vélo de montagne", model: "Roadster", size: "S"});
	CREATE (v:Velo {id: 6, name: "Vélo électrique", model: "Roadster", size: "S"});
	CREATE (v:Velo {id: 7, name: "Vélo de montagne", model: "Roadster", size: "M"});
	CREATE (v:Velo {id: 8, name: "Vélo de montagne", model: "Hamaya", size: "S"});
	CREATE (v:Velo {id: 9, name: "Vélo électrique", model: "Hamaya", size: "M"});
	CREATE (v:Velo {id: 10, name: "Vélo de montagne", model: "Roadster", size: "S"});
	CREATE (v:Velo {id: 11, name: "Vélo électrique", model: "Roadster", size: "M"});
	CREATE (v:Velo {id: 12, name: "Vélo de montagne", model: "Hamaya", size: "S"});
	CREATE (v:Velo {id: 13, name: "Vélo électrique", model: "Hamaya", size: "M"});
	CREATE (v:Velo {id: 14, name: "Vélo de montagne", model: "Roadster", size: "M"});
	CREATE (v:Velo {id: 15, name: "Vélo de route", model: "Roadster", size: "M"});
	CREATE (v:Velo {id: 16, name: "Vélo de route", model: "Roadster", size: "S"});
	CREATE (v:Velo {id: 17, name: "Vélo de montagne", model: "Hamaya", size: "S"});
	CREATE (v:Velo {id: 18, name: "Vélo de montagne", model: "Roadster", size: "M"});
	CREATE (v:Velo {id: 19, name: "Vélo électrique", model: "Roadster", size: "M"});
	CREATE (v:Velo {id: 20, name: "Vélo électrique", model: "Hamaya", size: "M"});

// 2- Pour créer nœud emplacement de location :
	
	CREATE (s:Station {id: 1, name: "Eiffel Tower Station", address: "Champ de Mars, 5 Avenue Anatole France, 75007 Paris" , ville: "Paris"});
	CREATE (s:Station {id: 2, name: "Fmille Dagra Station", address: "133 boulevard de la Croix Rousse, 69004 Lyon" , ville: "Lyon"});
	CREATE (s:Station {id: 3, name: "UTT MS EBDE Station", address: "Place Alexandre-Israël, 10000 TROYES" , ville: "Troyes"});
	CREATE (s:Station {id: 4, name: "Timaelle Maelle Keke Station", address: "31 Rue Gambetta, 78200 Mantes la jolie" , ville: "Mantes la jolie"});
	

// 3- Pour créer nœud client :

	CREATE (c:Client {id: 1, name: "Dagra Robert", email: "dagra@gmail.com"});
    CREATE (c:Client {id: 2, name: "John Doe", email: "john@example.com"});
    CREATE (c:Client {id: 3, name: "Dark Mir", email: "dark@example.com"});
    CREATE (c:Client {id: 4, name: "Dagra Sonia", email: "dagra@example.com"});
    CREATE (c:Client {id: 5, name: "Christelle Gboblahi", email: "christelle@example.com"});
    CREATE (c:Client {id: 6, name: "Rick N'Dri", email: "rick@example.com"});
    CREATE (c:Client {id: 7, name: "Elysee N'goran", email: "elysee@example.com"});
    CREATE (c:Client {id: 8, name: "Koua Yabi", email: "koua@example.com"});
    CREATE (c:Client {id: 9, name: "N'da Victoire", email: "victoire@example.com"});
    CREATE (c:Client {id: 10, name: "Mario Jad", email: "mario@example.com"});
    CREATE (c:Client {id: 11, name: "Amea David", email: "amea@example.com"});
    CREATE (c:Client {id: 12, name: "Hilair Kouassi", email: "hilair@example.com"});

// 4- Pour créer une relation entre un vélo et un emplacement pour indiquer que le vélo se trouve actuellement à cet emplacement :

	MATCH (v:Velo {id: 1}), (s:Station {id: 1})
	CREATE (v)-[:LOCATION_A]->(s)

// 5- Pour créer une relation entre un client et un vélo pour indiquer que le client a loué le vélo :

	MATCH (c:Client {id: 1}), (v:Velo {id: 1})
	CREATE (c)-[:LOUE {start_date: timestamp(), end_date: timestamp()}]->(v)

// 6- Pour trouver tous les vélos disponibles à un emplacement :

	MATCH (s:Station {name: "Eiffel Tower Station"})<-[:LOCATION_A]-(v:Velo)
	WHERE NOT (v)-[:LOUE]->()
	RETURN v

// 7- Pour retrouver tout s'historique de location d'un client :

	MATCH (c:Client {name: "John Doe"})-[r:LOUE]->(v:Velo)
	RETURN v, r

//8- Affichage Clients avec des Alias

	MATCH (s:Client) RETURN s.name AS name, s.email AS email

//9- Affichage Station avec des Alias

	MATCH (n:Station) RETURN n.name AS name, n.address AS address, n.ville AS ville

//10- Affichage nam Velo avec Alias
 
	MATCH (n:Velo) RETURN n.name AS name


----------BASE DE DONNEE EXPORTE AVEC TOUTES LES TABLES ET RELATION------

[
  {
    "p": {
"start": {
"identity": 0,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 1
        }
      },
"end": {
"identity": 24,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 0,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 1
            }
          },
          "relationship": {
"identity": 0,
"start": 0,
"end": 24,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 24,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 28,
"labels": [
          "Client"
        ],
"properties": {
"name": "Dagra Robert",
"id": 1,
"email": "dagra@gmail.com"
        }
      },
"end": {
"identity": 0,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 28,
"labels": [
              "Client"
            ],
"properties": {
"name": "Dagra Robert",
"id": 1,
"email": "dagra@gmail.com"
            }
          },
          "relationship": {
"identity": 1,
"start": 28,
"end": 0,
"type": "LOUE",
"properties": {
"end_date": 1673819509163,
"start_date": 1673819509163
            }
          },
          "end": {
"identity": 0,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 1,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de route",
"model": "Hamaya",
"id": 2
        }
      },
"end": {
"identity": 24,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 1,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de route",
"model": "Hamaya",
"id": 2
            }
          },
          "relationship": {
"identity": 2,
"start": 1,
"end": 24,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 24,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 2,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 3
        }
      },
"end": {
"identity": 24,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 2,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 3
            }
          },
          "relationship": {
"identity": 3,
"start": 2,
"end": 24,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 24,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 3,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 4
        }
      },
"end": {
"identity": 24,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 3,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 4
            }
          },
          "relationship": {
"identity": 4,
"start": 3,
"end": 24,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 24,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 4,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 5
        }
      },
"end": {
"identity": 24,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 4,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 5
            }
          },
          "relationship": {
"identity": 5,
"start": 4,
"end": 24,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 24,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 5,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo électrique",
"model": "Roadster",
"id": 6
        }
      },
"end": {
"identity": 24,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 5,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo électrique",
"model": "Roadster",
"id": 6
            }
          },
          "relationship": {
"identity": 6,
"start": 5,
"end": 24,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 24,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 6,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 7
        }
      },
"end": {
"identity": 24,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 6,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 7
            }
          },
          "relationship": {
"identity": 7,
"start": 6,
"end": 24,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 24,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Paris",
"address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
"name": "Eiffel Tower Station",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 7,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 8
        }
      },
"end": {
"identity": 25,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Lyon",
"address": "133 boulevard de la Croix Rousse, 69004 Lyon",
"name": "Fmille Dagra Station",
"id": 2
        }
      },
"segments": [
        {
          "start": {
"identity": 7,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 8
            }
          },
          "relationship": {
"identity": 8,
"start": 7,
"end": 25,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 25,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Lyon",
"address": "133 boulevard de la Croix Rousse, 69004 Lyon",
"name": "Fmille Dagra Station",
"id": 2
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 8,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 9
        }
      },
"end": {
"identity": 25,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Lyon",
"address": "133 boulevard de la Croix Rousse, 69004 Lyon",
"name": "Fmille Dagra Station",
"id": 2
        }
      },
"segments": [
        {
          "start": {
"identity": 8,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 9
            }
          },
          "relationship": {
"identity": 9,
"start": 8,
"end": 25,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 25,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Lyon",
"address": "133 boulevard de la Croix Rousse, 69004 Lyon",
"name": "Fmille Dagra Station",
"id": 2
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 9,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 10
        }
      },
"end": {
"identity": 25,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Lyon",
"address": "133 boulevard de la Croix Rousse, 69004 Lyon",
"name": "Fmille Dagra Station",
"id": 2
        }
      },
"segments": [
        {
          "start": {
"identity": 9,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 10
            }
          },
          "relationship": {
"identity": 10,
"start": 9,
"end": 25,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 25,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Lyon",
"address": "133 boulevard de la Croix Rousse, 69004 Lyon",
"name": "Fmille Dagra Station",
"id": 2
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 10,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Roadster",
"id": 11
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 10,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Roadster",
"id": 11
            }
          },
          "relationship": {
"identity": 11,
"start": 10,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 11,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 12
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 11,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 12
            }
          },
          "relationship": {
"identity": 12,
"start": 11,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 12,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 13
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 12,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 13
            }
          },
          "relationship": {
"identity": 13,
"start": 12,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 13,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 14
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 13,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 14
            }
          },
          "relationship": {
"identity": 14,
"start": 13,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 14,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de route",
"model": "Roadster",
"id": 15
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 14,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de route",
"model": "Roadster",
"id": 15
            }
          },
          "relationship": {
"identity": 15,
"start": 14,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 15,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de route",
"model": "Roadster",
"id": 16
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 15,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de route",
"model": "Roadster",
"id": 16
            }
          },
          "relationship": {
"identity": 16,
"start": 15,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 16,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 17
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 16,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de montagne",
"model": "Hamaya",
"id": 17
            }
          },
          "relationship": {
"identity": 17,
"start": 16,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 17,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 18
        }
      },
"end": {
"identity": 26,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 17,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 18
            }
          },
          "relationship": {
"identity": 18,
"start": 17,
"end": 26,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 26,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Troyes",
"address": "Place Alexandre-Israël, 10000 TROYES",
"name": "UTT MS EBDE Station",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 18,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Roadster",
"id": 19
        }
      },
"end": {
"identity": 27,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Mantes la jolie",
"address": "31 Rue Gambetta, 78200 Mantes la jolie",
"name": "Timaelle Maelle Keke Station",
"id": 4
        }
      },
"segments": [
        {
          "start": {
"identity": 18,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Roadster",
"id": 19
            }
          },
          "relationship": {
"identity": 19,
"start": 18,
"end": 27,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 27,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Mantes la jolie",
"address": "31 Rue Gambetta, 78200 Mantes la jolie",
"name": "Timaelle Maelle Keke Station",
"id": 4
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 19,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 20
        }
      },
"end": {
"identity": 27,
"labels": [
          "Station"
        ],
"properties": {
"ville": "Mantes la jolie",
"address": "31 Rue Gambetta, 78200 Mantes la jolie",
"name": "Timaelle Maelle Keke Station",
"id": 4
        }
      },
"segments": [
        {
          "start": {
"identity": 19,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 20
            }
          },
          "relationship": {
"identity": 20,
"start": 19,
"end": 27,
"type": "LOCATION_A",
"properties": {

            }
          },
          "end": {
"identity": 27,
"labels": [
              "Station"
            ],
"properties": {
"ville": "Mantes la jolie",
"address": "31 Rue Gambetta, 78200 Mantes la jolie",
"name": "Timaelle Maelle Keke Station",
"id": 4
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 29,
"labels": [
          "Client"
        ],
"properties": {
"name": "John Doe",
"id": 2,
"email": "john@example.com"
        }
      },
"end": {
"identity": 1,
"labels": [
          "Velo"
        ],
"properties": {
"size": "S",
"name": "Vélo de route",
"model": "Hamaya",
"id": 2
        }
      },
"segments": [
        {
          "start": {
"identity": 29,
"labels": [
              "Client"
            ],
"properties": {
"name": "John Doe",
"id": 2,
"email": "john@example.com"
            }
          },
          "relationship": {
"identity": 21,
"start": 29,
"end": 1,
"type": "LOUE",
"properties": {
"end_date": 1673823132121,
"start_date": 1673823132121
            }
          },
          "end": {
"identity": 1,
"labels": [
              "Velo"
            ],
"properties": {
"size": "S",
"name": "Vélo de route",
"model": "Hamaya",
"id": 2
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 31,
"labels": [
          "Client"
        ],
"properties": {
"name": "Dagra Sonia",
"id": 4,
"email": "dagra@example.com"
        }
      },
"end": {
"identity": 2,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 3
        }
      },
"segments": [
        {
          "start": {
"identity": 31,
"labels": [
              "Client"
            ],
"properties": {
"name": "Dagra Sonia",
"id": 4,
"email": "dagra@example.com"
            }
          },
          "relationship": {
"identity": 22,
"start": 31,
"end": 2,
"type": "LOUE",
"properties": {
"end_date": 1673823132265,
"start_date": 1673823132265
            }
          },
          "end": {
"identity": 2,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 3
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 34,
"labels": [
          "Client"
        ],
"properties": {
"name": "Elysee N'goran",
"id": 7,
"email": "elysee@example.com"
        }
      },
"end": {
"identity": 19,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 20
        }
      },
"segments": [
        {
          "start": {
"identity": 34,
"labels": [
              "Client"
            ],
"properties": {
"name": "Elysee N'goran",
"id": 7,
"email": "elysee@example.com"
            }
          },
          "relationship": {
"identity": 23,
"start": 34,
"end": 19,
"type": "LOUE",
"properties": {
"end_date": 1673823132397,
"start_date": 1673823132397
            }
          },
          "end": {
"identity": 19,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo électrique",
"model": "Hamaya",
"id": 20
            }
          }
        }
      ],
"length": 1.0
    }
  },
  {
    "p": {
"start": {
"identity": 38,
"labels": [
          "Client"
        ],
"properties": {
"name": "Amea David",
"id": 11,
"email": "amea@example.com"
        }
      },
"end": {
"identity": 0,
"labels": [
          "Velo"
        ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 1
        }
      },
"segments": [
        {
          "start": {
"identity": 38,
"labels": [
              "Client"
            ],
"properties": {
"name": "Amea David",
"id": 11,
"email": "amea@example.com"
            }
          },
          "relationship": {
"identity": 24,
"start": 38,
"end": 0,
"type": "LOUE",
"properties": {
"end_date": 1673823449736,
"start_date": 1673823449736
            }
          },
          "end": {
"identity": 0,
"labels": [
              "Velo"
            ],
"properties": {
"size": "M",
"name": "Vélo de montagne",
"model": "Roadster",
"id": 1
            }
          }
        }
      ],
"length": 1.0
    }
  }
]

_______________________SCRIPT APPLICATION STREAMLIT PYTHON-------------

#espace ADMIN

import streamlit as st
from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "utt"), database="locationvelo", encrypted=False)
session = driver.session()


# Create a Streamlit app
def app():
    # Exécution de la requête
    query = "MATCH (n:Station) RETURN n.name AS name, n.address AS address, n.ville AS ville"
    query1 = "MATCH (s:Client) RETURN s.name AS name, s.email AS email"
    query2 = "MATCH (s:Station {name: 'Eiffel Tower Station'})<-[:LOCATION_A]-(v:Velo) WHERE NOT (v)-[:LOUE]->() RETURN v.name as name, v.model as model"


    result = session.run(query)

    result1 = session.run(query1)

    result2 = session.run(query2)

    st.title("ESPACE ADMINISTRATEUR VISUALISATION ETAT")

    st.header("LES DIFFERENTES STATIONS DE VELO")
    # Récupération des résultats
    data = []
    data.append(["STATION", "ADRESSE", "VILLESSS"])
    for record in result:
        data.append([record["name"], record["address"], record["ville"]])

    # Affichage des résultats dans un tableau Streamlit
    st.table(data)

    st.header("LES CLIENTS")
    # Récupération des résultats
    data1 = []
    data1.append(["CLIENT", "EMAIL"])
    for record1 in result1:
        data1.append([record1["name"], record1["email"]])

    # Affichage des résultats dans un tableau Streamlit
    st.table(data1)

    st.header("LES VELOS LOUE à Eiffel Tower Station")
    # Récupération des résultats
    data2 = []
    data2.append(["Station","TYPE VELO", "MODEL"])
    for record2 in result2:
        data2.append(["Eiffel Tower Station", record2["name"], record2["model"]])

    # Affichage des résultats dans un tableau Streamlit
    st.table(data2)


if __name__=="__main__":
    app()



#ESPACE CLIENT

import streamlit as st
from neo4j import GraphDatabase

#from neo4j.v1 import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "utt"), database="locationvelo", encrypted=False)
session = driver.session()

# Create a function to run Cypher queries
def run_query(tx, query):
    result = tx.run(query)
    return result

# Create a function to return the name and ville of all bike rental stations
def get_stations():
    with driver.session() as session:
        result = session.read_transaction(run_query, "MATCH (s:Station) RETURN s.name, s.ville")
        return result

# Create the Streamlit app
def app():
    st.title("ESPACE CLIENT")
    st.header("Recherchez une station dans une ville")

    # Get the user's current ville
    ville = st.text_input("Entrez la ville: Ex: Paris, Lyon (Respectez la class, s'affiche les informations  disponible)")

    # Find the nearest bike rental station
    if ville:
        #query = f"MATCH (s:Station) WHERE s.ville = '{ville}' RETURN s.name, s.ville"
        query = f"MATCH (s:Station) WHERE s.ville = '{ville}' RETURN s.name as name, s.ville as ville, s.address as address"
        with driver.session() as session:
            result = session.run(query)
            data = []
            data.append(["STATION", "ADRESSE", "VILLE"])
            for record in result:
                data.append([record["name"], record["address"], record["ville"]])

            result = session.read_transaction(run_query, query)
            st.table(data)

            # st.success(f"la station est {data}")
    else:
        st.warning("Entrez une ville dans la base s'il vous plait. Ex: Paris, Lyon")

if __name__=="__main__":
    app()
