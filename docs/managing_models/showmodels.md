 When working with bigger application sometimes, you get lost sometimes, a lot...


### Manage FastAPI's **`showmodels`** goes to your **core/models** folder and creates a schema of your models.


#### Let's say we have 4 folders under my **core/models**

- `item.py`
- `token.py`
- `msg.py`
- `user.py`

```
manage-fastapi showmodels
```

With this command we are getting a fancy output of our models.

```
╔════════════════════════════════╗
║ item.py                        ║
║ -------                        ║
║ ItemBase                       ║
║ ItemCreate                     ║
║ ItemUpdate                     ║
║ ItemInDBBase                   ║
║ Item                           ║
║ ItemInDB                       ║
╚════════════════════════════════╝
╔════════════════════════════════╗
║ token.py                       ║
║ --------                       ║
║ Token                          ║
║ TokenPayload                   ║
╚════════════════════════════════╝
╔════════════════════════════════╗
║ msg.py                         ║
║ ------                         ║
║ Msg                            ║
╚════════════════════════════════╝
╔════════════════════════════════╗
║ user.py                        ║
║ -------                        ║
║ UserBase                       ║
║ UserCreate                     ║
║ UserUpdate                     ║
║ UserInDBBase                   ║
║ User                           ║
║ UserInDB                       ║
╚════════════════════════════════╝
```
