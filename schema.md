
# Sparkify Relational Data Schema
**FACT: Songplays**  
|Column| Data Type| Contraints|
|-|-|-|
|songplay_id| SERIAL| PRIMARY KEY|
|start_time| TIME(6)| FOREIGN KEY|
|user_id| INT| FOREIGN KEY|
|level| VARCHAR | |
|song_id| VARCHAR| FOREIGN KEY|
|artist_id| VARCHAR | FOREIGN KEY|
|session_id| INT | |
|location| VARCHAR| |
|user_agent| VARCHAR| |  

---

**DIMENSION: Users**  
|Column| Data Type| Contraints|
|-|-|-|
|user_id| INT| PRIMARY KEY|
|first_name|VARCHAR| |
|last_name|VARCHAR| |
|gender| VARCHAR ||
|level| VARCHAR||

---

**DIMENSION: Songs**  
|Column| Data Type| Contraints|
|-|-|-|
|song_id| VARCHAR| PRIMARY KEY|
|title| VARCHAR| |
|artist_id| VARCHAR| |
|year| INT| |
|duration| FLOAT| |

---

**DIMENSION: Artists**  
|Column| Data Type| Contraints|
|-|-|-|
|artist_id| VARCHAR| PRIMARY KEY|
|name| VARCHAR | |
|location| VARCHAR | |
|latitude| FLOAT ||
|longitude| FLOAT||

---

**DIMENSION: Time**  
|Column| Data Type| Contraints|
|-|-|-|
|start_time| TIME(6)| PRIMARY KEY|
|hour| INT| |
|day| INT | |
|week| INT | |
|month| INT| |
|year| INT | |
|weekday| VARCHAR||